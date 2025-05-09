#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
View for the Dashboard page
"""

import wx
import threading
import time
import logging
from config.settings import BACKGROUND_COLOR, PRIMARY_COLOR
from module.dashboard.viewmodels.dashboard_viewmodel import DashboardViewModel

logger = logging.getLogger("DashboardView")

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
        
        # 创建一个垂直分割的面板
        splitter = wx.SplitterWindow(self, style=wx.SP_3D | wx.SP_LIVE_UPDATE)
        splitter.SetMinimumPaneSize(100)  # 设置最小面板大小
        
        # 表单面板
        form_panel = wx.Panel(splitter)
        form_panel.SetBackgroundColour(wx.WHITE)
        
        # 日志面板
        log_panel = wx.Panel(splitter)
        log_panel.SetBackgroundColour(wx.WHITE)
        
        # 将面板添加到分割窗口
        splitter.SplitHorizontally(form_panel, log_panel)
        splitter.SetSashPosition(300)  # 设置分割位置
        
        # 添加分割窗口到主布局
        main_sizer.Add(splitter, 1, wx.EXPAND | wx.ALL, 20)
        
        # 创建表单面板布局
        self._init_form_panel(form_panel)
        
        # 创建日志面板布局
        self._init_log_panel(log_panel)
        
        # Set sizer
        self.SetSizer(main_sizer)
    
    def _init_form_panel(self, parent):
        """初始化表单面板"""
        # Create form sizer
        form_sizer = wx.GridBagSizer(10, 10)
        
        # Add target contact input
        target_label = wx.StaticText(parent, label="Target Contact:")
        form_sizer.Add(target_label, pos=(0, 0), flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL, border=10)
        
        self.target_input = wx.TextCtrl(parent, size=(300, -1))
        # 设置默认联系人为"文件传输助手"
        self.target_input.SetValue("文件传输助手")
        form_sizer.Add(self.target_input, pos=(0, 1), span=(1, 2), flag=wx.EXPAND | wx.ALL, border=10)
        
        # Add content input
        content_label = wx.StaticText(parent, label="Content:")
        form_sizer.Add(content_label, pos=(1, 0), flag=wx.ALL | wx.ALIGN_TOP, border=10)
        
        self.content_input = wx.TextCtrl(parent, style=wx.TE_MULTILINE, size=(300, 100))
        form_sizer.Add(self.content_input, pos=(1, 1), span=(1, 2), flag=wx.EXPAND | wx.ALL, border=10)
        
        # Add send button
        self.send_button = wx.Button(parent, label="Send")
        self.send_button.SetBackgroundColour(PRIMARY_COLOR)
        self.send_button.SetForegroundColour(wx.WHITE)
        form_sizer.Add(self.send_button, pos=(2, 2), flag=wx.ALL | wx.ALIGN_RIGHT, border=10)
        
        # 添加状态文本
        self.status_text = wx.StaticText(parent, label="Ready to send message")
        form_sizer.Add(self.status_text, pos=(2, 0), span=(1, 2), flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL, border=10)
        
        # Make columns expandable
        form_sizer.AddGrowableCol(1)
        form_sizer.AddGrowableRow(1)
        
        # Set form sizer
        parent.SetSizer(form_sizer)
        
        # Bind events
        self.send_button.Bind(wx.EVT_BUTTON, self._on_send)
    
    def _init_log_panel(self, parent):
        """初始化日志面板"""
        # 创建日志面板布局
        log_sizer = wx.BoxSizer(wx.VERTICAL)
        
        # 添加日志标题
        log_title = wx.StaticText(parent, label="Execution Logs:")
        log_title.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        log_sizer.Add(log_title, 0, wx.ALL, 10)
        
        # 添加日志显示区域
        self.log_ctrl = wx.TextCtrl(parent, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.HSCROLL)
        self.log_ctrl.SetFont(wx.Font(10, wx.FONTFAMILY_TELETYPE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
        log_sizer.Add(self.log_ctrl, 1, wx.EXPAND | wx.ALL, 10)
        
        # 添加按钮面板
        button_panel = wx.Panel(parent)
        button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        # 添加清除日志按钮
        self.clear_log_button = wx.Button(button_panel, label="Clear Logs")
        self.clear_log_button.Bind(wx.EVT_BUTTON, self._on_clear_logs)
        button_sizer.Add(self.clear_log_button, 0, wx.RIGHT, 10)
        
        # 添加复制日志按钮
        self.copy_log_button = wx.Button(button_panel, label="Copy Logs")
        self.copy_log_button.Bind(wx.EVT_BUTTON, self._on_copy_logs)
        button_sizer.Add(self.copy_log_button, 0)
        
        button_panel.SetSizer(button_sizer)
        log_sizer.Add(button_panel, 0, wx.ALIGN_RIGHT | wx.ALL, 10)
        
        # 设置日志面板布局
        parent.SetSizer(log_sizer)
    
    def _on_clear_logs(self, event):
        """清除日志"""
        self.log_ctrl.Clear()
        self.add_log("日志已清除")
    
    def _on_copy_logs(self, event):
        """复制日志到剪贴板"""
        if wx.TheClipboard.Open():
            wx.TheClipboard.SetData(wx.TextDataObject(self.log_ctrl.GetValue()))
            wx.TheClipboard.Close()
            wx.MessageBox("日志已复制到剪贴板", "信息", wx.OK | wx.ICON_INFORMATION)
    
    def add_log(self, message):
        """添加日志到日志控件"""
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        log_message = f"[{timestamp}] {message}"
        self.log_ctrl.AppendText(log_message + "\n")
        logger.debug(message)
        
        # 滚动到最新日志
        self.log_ctrl.ShowPosition(self.log_ctrl.GetLastPosition())
    
    def _on_send(self, event):
        """Handle send button click"""
        # 禁用发送按钮，防止重复点击
        self.send_button.Disable()
        self.status_text.SetLabel("Sending message...")
        
        # 添加日志
        self.add_log("开始发送消息流程")
        
        # 更新状态栏
        frame = self.GetTopLevelParent()
        frame.SetStatusText("Sending message, please wait...")
        
        # 获取输入值
        target = self.target_input.GetValue()
        content = self.content_input.GetValue()
        
        self.add_log(f"目标联系人: {target}")
        self.add_log(f"消息内容: {content}")
        
        # 更新 ViewModel
        self.viewmodel.set_target(target)
        self.viewmodel.set_content(content)
        
        # 创建一个线程来发送消息，避免界面冻结
        self.add_log("创建后台线程发送消息")
        thread = threading.Thread(target=self._send_message_thread)
        thread.daemon = True
        thread.start()
    
    def _send_message_thread(self):
        """在单独的线程中发送消息"""
        # 发送消息
        self.add_log("执行发送消息")
        success, message = self.viewmodel.send_message()
        
        # 获取模型中的日志
        logs = self.viewmodel.get_message_logs()
        
        # 使用 CallAfter 更新 UI，确保在主线程中更新
        wx.CallAfter(self._update_ui_after_send, success, message, logs)
    
    def _update_ui_after_send(self, success, message, logs):
        """更新发送后的 UI 状态"""
        # 显示模型中的日志
        for log in logs:
            if not log in self.log_ctrl.GetValue():  # 避免重复日志
                self.log_ctrl.AppendText(log + "\n")
        
        # 重新启用发送按钮
        self.send_button.Enable()
        
        # 更新状态文本
        if success:
            self.status_text.SetLabel("Message sent successfully")
            self.add_log("消息发送成功")
            wx.MessageBox(message, "Success", wx.OK | wx.ICON_INFORMATION)
            
            # 清空内容输入框，为下一条消息做准备
            self.content_input.SetValue("")
        else:
            self.status_text.SetLabel("Failed to send message")
            self.add_log(f"消息发送失败: {message}")
            wx.MessageBox(message, "Error", wx.OK | wx.ICON_ERROR)
        
        # 更新状态栏
        frame = self.GetTopLevelParent()
        status_msg = "Message sent successfully" if success else "Failed to send message"
        frame.SetStatusText(status_msg) 