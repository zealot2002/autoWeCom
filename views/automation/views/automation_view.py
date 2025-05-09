#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
View for the Automation page
"""

import wx
import wx.grid
from config.settings import BACKGROUND_COLOR, PRIMARY_COLOR
from views.automation.viewmodels.automation_viewmodel import AutomationViewModel

class AutomationView(wx.Panel):
    """View class for the Automation page"""
    
    def __init__(self, parent):
        """Initialize the automation view"""
        super(AutomationView, self).__init__(parent)
        
        # Set page name
        self.SetName("Automation")
        
        # Set background color
        self.SetBackgroundColour(BACKGROUND_COLOR)
        
        # Create ViewModel
        self.viewmodel = AutomationViewModel()
        
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
        
        # Create content panel
        content_panel = wx.Panel(self)
        content_panel.SetBackgroundColour(wx.WHITE)
        
        # Create content sizer
        content_sizer = wx.BoxSizer(wx.VERTICAL)
        
        # Create task grid
        self.task_grid = wx.grid.Grid(content_panel)
        self.task_grid.CreateGrid(0, 4)
        
        # Configure grid columns
        self.task_grid.SetColLabelValue(0, "Task Name")
        self.task_grid.SetColLabelValue(1, "Description")
        self.task_grid.SetColLabelValue(2, "Schedule")
        self.task_grid.SetColLabelValue(3, "Status")
        
        self.task_grid.SetColSize(0, 150)
        self.task_grid.SetColSize(1, 200)
        self.task_grid.SetColSize(2, 150)
        self.task_grid.SetColSize(3, 100)
        
        # Add grid to content sizer
        content_sizer.Add(self.task_grid, 1, wx.EXPAND | wx.ALL, 10)
        
        # Create button panel
        button_panel = wx.Panel(content_panel)
        button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        # Add buttons
        self.add_button = wx.Button(button_panel, label="Add Task")
        self.remove_button = wx.Button(button_panel, label="Remove Task")
        self.start_button = wx.Button(button_panel, label="Start Task")
        self.stop_button = wx.Button(button_panel, label="Stop Task")
        
        button_sizer.Add(self.add_button, 0, wx.RIGHT, 10)
        button_sizer.Add(self.remove_button, 0, wx.RIGHT, 10)
        button_sizer.Add(self.start_button, 0, wx.RIGHT, 10)
        button_sizer.Add(self.stop_button, 0)
        
        button_panel.SetSizer(button_sizer)
        content_sizer.Add(button_panel, 0, wx.ALL | wx.ALIGN_RIGHT, 10)
        
        # Set content panel sizer
        content_panel.SetSizer(content_sizer)
        
        # Add content panel to main sizer
        main_sizer.Add(content_panel, 1, wx.EXPAND | wx.ALL, 20)
        
        # Set sizer
        self.SetSizer(main_sizer)
        
        # Bind events
        self.add_button.Bind(wx.EVT_BUTTON, self._on_add_task)
        self.remove_button.Bind(wx.EVT_BUTTON, self._on_remove_task)
        self.start_button.Bind(wx.EVT_BUTTON, self._on_start_task)
        self.stop_button.Bind(wx.EVT_BUTTON, self._on_stop_task)
        
        # Load initial data
        self._load_tasks()
    
    def _load_tasks(self):
        """Load tasks from the ViewModel into the grid"""
        tasks = self.viewmodel.get_tasks()
        
        # Clear existing grid
        if self.task_grid.GetNumberRows() > 0:
            self.task_grid.DeleteRows(0, self.task_grid.GetNumberRows())
        
        # Add tasks to grid
        for i, task in enumerate(tasks):
            self.task_grid.AppendRows(1)
            self.task_grid.SetCellValue(i, 0, task["name"])
            self.task_grid.SetCellValue(i, 1, task["description"])
            self.task_grid.SetCellValue(i, 2, task["schedule"])
            self.task_grid.SetCellValue(i, 3, task["status"])
            
            # Color the status cell based on status
            if task["status"] == "Active":
                self.task_grid.SetCellBackgroundColour(i, 3, wx.Colour(200, 255, 200))  # Light green
            else:
                self.task_grid.SetCellBackgroundColour(i, 3, wx.Colour(255, 200, 200))  # Light red
    
    def _on_add_task(self, event):
        """Handle add task button click"""
        # In a real app, this would open a dialog to input task details
        task = {
            "name": "New Task",
            "description": "New task description",
            "schedule": "Manual",
            "status": "Inactive"
        }
        self.viewmodel.add_task(task)
        self._load_tasks()
    
    def _on_remove_task(self, event):
        """Handle remove task button click"""
        selected_row = self.task_grid.GetGridCursorRow()
        if selected_row >= 0:
            self.viewmodel.remove_task(selected_row)
            self._load_tasks()
    
    def _on_start_task(self, event):
        """Handle start task button click"""
        selected_row = self.task_grid.GetGridCursorRow()
        if selected_row >= 0:
            self.viewmodel.start_task(selected_row)
            self._load_tasks()
    
    def _on_stop_task(self, event):
        """Handle stop task button click"""
        selected_row = self.task_grid.GetGridCursorRow()
        if selected_row >= 0:
            self.viewmodel.stop_task(selected_row)
            self._load_tasks() 