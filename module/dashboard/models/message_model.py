#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Message model for the Dashboard page
"""

import os
import subprocess
from config.settings import APP_NAME  # 导入设置

class MessageModel:
    """Model class for message data"""
    
    def __init__(self, target="", content=""):
        """Initialize the message model"""
        self.target = target
        self.content = content
        # 设置脚本路径
        self.script_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))), 
                                        "rpa", "send_wechat_message.sh")
    
    def validate(self):
        """Validate the message data"""
        if not self.target:
            return False, "Target contact cannot be empty"
        
        if not self.content:
            return False, "Message content cannot be empty"
        
        # 检查脚本是否存在
        if not os.path.exists(self.script_path):
            return False, f"Script not found at: {self.script_path}"
        
        # 检查脚本是否可执行
        if not os.access(self.script_path, os.X_OK):
            return False, f"Script is not executable: {self.script_path}"
            
        return True, "Valid message data"
    
    def send(self):
        """Send the message using the RPA script"""
        # 先验证数据
        valid, message = self.validate()
        if not valid:
            return False, message
        
        try:
            # 调用外部脚本
            process = subprocess.Popen(
                [self.script_path, self.target, self.content],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                cwd=os.path.dirname(self.script_path)  # 设置工作目录为脚本所在目录
            )
            
            # 获取输出
            stdout, stderr = process.communicate(timeout=60)  # 设置超时时间为60秒
            
            # 检查返回码
            if process.returncode == 0:
                return True, f"Message to '{self.target}' sent successfully via WeChat"
            else:
                return False, f"Error sending message: {stderr}"
                
        except subprocess.TimeoutExpired:
            process.kill()
            return False, "Script execution timed out"
        except Exception as e:
            return False, f"Error executing script: {str(e)}" 