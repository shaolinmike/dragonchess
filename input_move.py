"""
This module contains the input control

*Examples:* ::

	Enter code examples here. (optional field)

*Todo:*
	* Enter thing to do. (optional field)

*Author:*
	* Mitri Van, mitri.van@volition-inc.com, 10/3/2013 10:44:19 AM
"""

import wx

class Input( wx.Panel ):
	def __init__( self, parent, name, id = wx.ID_ANY, style = wx.TE_PROCESS_TAB ):

		# Initialize base class
		wx.Panel.__init__( self, parent = parent, id = wx.ID_ANY, pos =  wx.DefaultPosition, size = wx.DefaultSize,
		                  style = wx.TAB_TRAVERSAL|wx.NO_BORDER, name = name )

		self.board_textctrl = wx.TextCtrl( self, wx.ID_ANY, pos = wx.DefaultPosition, size = wx.DefaultSize, style = style)

		# Sizer
		sizer_control = wx.BoxSizer( wx.HORIZONTAL )
		sizer_control.Add( self.board_textctrl, proportion = 1, flag = wx.EXPAND | wx.ALL )

		self.SetSizer( sizer_control )
		self.Layout( )
