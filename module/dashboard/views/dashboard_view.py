#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
View for the Dashboard page
"""

import wx
import threading
from config.settings import BACKGROUND_COLOR, PRIMARY_COLOR
from module.dashboard.viewmodels.dashboard_viewmodel import DashboardViewModel

class DashboardView(wx.Panel):
    """View class for the Dashboard page"""
    
    def __init__(self, parent):
        """Initialize the dashboard view"""
        super(DashboardView, self).__init__(parent)
        
        # Set page name
        self.SetName("Dashboard")
        
        # Set background color
        self.SetBackgroundColour(BACKGROUND_COLOR)
        
        # Create ViewModel
        self.viewmodel = DashboardViewModel()
        
        # Initialize UI
        self._init_ui()
    
    def _init_ui(self):
        """Initialize UI components"""
        # Create main sizer
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        
        # Create title
        title = wx.StaticText(self, label=self.GetName())
        title.SetFont(wx.Font(16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        main_sizer.Add(title, 0, wx.ALL | wx.CENTER, 20)
        
        # Create form panel
        form_panel = wx.Panel(self)
        form_panel.SetBackgroundColour(wx.WHITE)
        
        # Create form sizer
        form_sizer = wx.GridBagSizer(10, 10)
        
        # Add target contact input
        target_label = wx.StaticText(form_panel, label="Target Contact:")
        form_sizer.Add(target_label, pos=(0, 0), flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL, border=10)
        
        self.target_input = wx.TextCtrl(form_panel, size=(300, -1))
        # 设置默认联系人为"文件传输助手"
        self.target_input.SetValue("文件传输助手")
        form_sizer.Add(self.target_input, pos=(0, 1), span=(1, 2), flag=wx.EXPAND | wx.ALL, border=10)
        
        # Add content input
        content_label = wx.StaticText(form_panel, label="Content:")
        form_sizer.Add(content_label, pos=(1, 0), flag=wx.ALL | wx.ALIGN_TOP, border=10)
        
        self.content_input = wx.TextCtrl(form_panel, style=wx.TE_MULTILINE, size=(300, 100))
        form_sizer.Add(self.content_input, pos=(1, 1), span=(1, 2), flag=wx.EXPAND | wx.ALL, border=10)
        
        # Add send button
        self.send_button = wx.Button(form_panel, label="Send")
        self.send_button.SetBackgroundColour(PRIMARY_COLOR)
        self.send_button.SetForegroundColour(wx.WHITE)
        form_sizer.Add(self.send_button, pos=(2, 2), flag=wx.ALL | wx.ALIGN_RIGHT, border=10)
        
        # 添加状态文本
        self.status_text = wx.StaticText(form_panel, label="Ready to send message")
        form_sizer.Add(self.status_text, pos=(2, 0), span=(1, 2), flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL, border=10)
        
        # Make columns expandable
        form_sizer.AddGrowableCol(1)
        form_sizer.AddGrowableRow(1)
        
        # Set form sizer
        form_panel.SetSizer(form_sizer)
        
        # Add form panel to main sizer
        main_sizer.Add(form_panel, 1, wx.EXPAND | wx.ALL, 20)
        
        # Bind events
        self.send_button.Bind(wx.EVT_BUTTON, self._on_send)
        
        # Set sizer
        self.SetSizer(main_sizer)
    
    def _on_send(self, event):
        """Handle send button click"""
        # 禁用发送按钮，防止重复点击
        self.send_button.Disable()
        self.status_text.SetLabel("Sending message...")
        
        # 更新状态栏
        frame = self.GetTopLevelParent()
        frame.SetStatusText("Sending message, please wait...")
        
        # 获取输入值
        target = self.target_input.GetValue()
        content = self.content_input.GetValue()
        
        # 更新 ViewModel
        self.viewmodel.set_target(target)
        self.viewmodel.set_content(content)
        
        # 创建一个线程来发送消息，避免界面冻结
        thread = threading.Thread(target=self._send_message_thread)
        thread.daemon = True
        thread.start()
    
    def _send_message_thread(self):
        """在单独的线程中发送消息"""
        # 发送消息
        success, message = self.viewmodel.send_message()
        
        # 使用 CallAfter 更新 UI，确保在主线程中更新
        wx.CallAfter(self._update_ui_after_send, success, message)
    
    def _update_ui_after_send(self, success, message):
        """更新发送后的 UI 状态"""
        # 重新启用发送按钮
        self.send_button.Enable()
        
        # 更新状态文本
        if success:
            self.status_text.SetLabel("Message sent successfully")
            wx.MessageBox(message, "Success", wx.OK | wx.ICON_INFORMATION)
            
            # 清空内容输入框，为下一条消息做准备
            self.content_input.SetValue("")
        else:
            self.status_text.SetLabel("Failed to send message")
            wx.MessageBox(message, "Error", wx.OK | wx.ICON_ERROR)
        
        # 更新状态栏
        frame = self.GetTopLevelParent()
        frame.SetStatusText(message) 