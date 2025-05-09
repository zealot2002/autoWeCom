#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Model for the Automation page
"""

import os
import subprocess
from config.settings import PLATFORM, RPA_SCRIPTS_DIR

class AutomationModel:
    """Model class for automation data"""
    
    def __init__(self):
        """Initialize the automation model"""
        self.tasks = []
        self.active_tasks = []
        self.platform = PLATFORM
    
    def add_task(self, task):
        """Add a new automation task"""
        self.tasks.append(task)
        return True
    
    def remove_task(self, task_id):
        """Remove an automation task"""
        if task_id < len(self.tasks):
            del self.tasks[task_id]
            return True
        return False
    
    def get_tasks(self):
        """Get all tasks"""
        return self.tasks
    
    def start_task(self, task_id):
        """Start an automation task"""
        if task_id < len(self.tasks):
            task = self.tasks[task_id]
            if task not in self.active_tasks:
                self.active_tasks.append(task)
                
                # 示例：如果是发送消息任务，则执行平台特定的发送脚本
                if task.get("type") == "send_message":
                    self._execute_send_message_task(task)
                
            return True
        return False
    
    def stop_task(self, task_id):
        """Stop an automation task"""
        if task_id < len(self.tasks):
            task = self.tasks[task_id]
            if task in self.active_tasks:
                self.active_tasks.remove(task)
            return True
        return False
    
    def _execute_send_message_task(self, task):
        """Execute a send message task based on platform"""
        contact = task.get("contact", "文件传输助手")
        message = task.get("message", "Hello from autoWeCom")
        
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
        
        if self.platform == "mac":
            # 执行macOS脚本
            script_path = os.path.join(base_dir, "rpa", "send_wechat_message.sh")
            try:
                subprocess.Popen(["bash", script_path, contact, message])
                return True
            except Exception as e:
                print(f"Error executing Mac script: {e}")
                return False
        elif self.platform == "windows":
            # 执行Windows脚本
            script_path = os.path.join(base_dir, "rpa", "windows", "send_wechat_message.bat")
            try:
                # Windows下使用cmd /c启动批处理
                subprocess.Popen(["cmd", "/c", script_path, contact, message])
                return True
            except Exception as e:
                print(f"Error executing Windows script: {e}")
                return False
        return False 