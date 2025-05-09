#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Message model for the Dashboard page
"""

import os
import subprocess
import logging
import time
from config.settings import APP_NAME  # 导入设置

# 配置日志
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("autowecom_debug.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("MessageModel")

class MessageModel:
    """Model class for message data"""
    
    def __init__(self, target="", content=""):
        """Initialize the message model"""
        self.target = target
        self.content = content
        self.log_messages = []
        
        # 设置脚本路径
        self.script_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))), 
                                        "rpa", "send_wechat_message.sh")
        logger.info(f"Script path: {self.script_path}")
        self.add_log(f"初始化消息模型，脚本路径: {self.script_path}")
    
    def add_log(self, message):
        """添加日志消息到列表"""
        timestamp = time.strftime("%H:%M:%S", time.localtime())
        log_entry = f"[{timestamp}] {message}"
        self.log_messages.append(log_entry)
        logger.debug(message)
        return log_entry
    
    def get_logs(self):
        """获取所有日志消息"""
        return self.log_messages
    
    def validate(self):
        """Validate the message data"""
        self.add_log(f"验证消息数据: 目标={self.target}, 内容长度={len(self.content)}")
        
        if not self.target:
            self.add_log("错误: 目标联系人不能为空")
            return False, "Target contact cannot be empty"
        
        if not self.content:
            self.add_log("错误: 消息内容不能为空")
            return False, "Message content cannot be empty"
        
        # 检查脚本是否存在
        if not os.path.exists(self.script_path):
            error_msg = f"脚本未找到: {self.script_path}"
            self.add_log(error_msg)
            return False, f"Script not found at: {self.script_path}"
        
        # 检查脚本是否可执行
        if not os.access(self.script_path, os.X_OK):
            error_msg = f"脚本不可执行: {self.script_path}"
            self.add_log(error_msg)
            return False, f"Script is not executable: {self.script_path}"
            
        self.add_log("验证通过: 消息数据有效")
        return True, "Valid message data"
    
    def send(self):
        """Send the message using the RPA script"""
        # 先验证数据
        self.add_log("开始发送消息...")
        valid, message = self.validate()
        if not valid:
            return False, message
        
        try:
            # 记录命令
            cmd = [self.script_path, self.target, self.content]
            cwd = os.path.dirname(self.script_path)
            self.add_log(f"执行命令: {' '.join(cmd)}")
            self.add_log(f"工作目录: {cwd}")
            
            # 调用外部脚本
            process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                cwd=cwd  # 设置工作目录为脚本所在目录
            )
            
            # 获取输出
            self.add_log("等待脚本执行完成...")
            stdout, stderr = process.communicate(timeout=60)  # 设置超时时间为60秒
            
            # 记录输出
            if stdout:
                self.add_log(f"脚本标准输出:\n{stdout}")
            if stderr:
                self.add_log(f"脚本错误输出:\n{stderr}")
            
            # 检查返回码
            self.add_log(f"脚本返回码: {process.returncode}")
            if process.returncode == 0:
                self.add_log(f"消息发送成功: 目标={self.target}")
                return True, f"Message to '{self.target}' sent successfully via WeChat\n\nDebug logs:\n" + "\n".join(self.log_messages[-10:])
            else:
                error_msg = f"发送消息失败，错误信息: {stderr}"
                self.add_log(error_msg)
                return False, f"Error sending message: {stderr}\n\nDebug logs:\n" + "\n".join(self.log_messages)
                
        except subprocess.TimeoutExpired:
            error_msg = "脚本执行超时"
            self.add_log(error_msg)
            process.kill()
            return False, f"Script execution timed out\n\nDebug logs:\n" + "\n".join(self.log_messages)
        except Exception as e:
            error_msg = f"执行脚本时发生错误: {str(e)}"
            self.add_log(error_msg)
            return False, f"Error executing script: {str(e)}\n\nDebug logs:\n" + "\n".join(self.log_messages) 