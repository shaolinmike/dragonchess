"""
This module defines the board class

*Examples:* ::

	Enter code examples here. (optional field)

*Todo:*
	* Enter thing to do. (optional field)

*Author:*
	* Mitri Van, mitri.van@volition-inc.com, 10/3/2013 10:43:25 AM
"""

import wx

class Board( wx.Panel ):
	def __init__( self, parent, name, id = wx.ID_ANY ):

		# Initialize base class
		wx.Panel.__init__( self, parent = parent, id = wx.ID_ANY, pos =  wx.DefaultPosition, size = ( 330, 255 ),
		                  style = wx.TAB_TRAVERSAL|wx.NO_BORDER, name = name )

		self.board_textctrl = wx.TextCtrl( self, wx.ID_ANY, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.TE_MULTILINE | wx.TE_NO_VSCROLL )

		# Sizer
		sizer_control = wx.BoxSizer( wx.HORIZONTAL )
		sizer_control.Add( self.board_textctrl, proportion = 1, flag = wx.EXPAND | wx.ALL )

		self.SetSizer( sizer_control )
		self.Layout( )
		sizer_control.Fit( self )

		# Font Settings
		typeface = wx.Font( 8, wx.MODERN, wx.NORMAL, wx.BOLD, False, u'Consolas')
		self.board_textctrl.SetFont( typeface )

		self.board_textctrl.SetForegroundColour( wx.Colour( 255, 178, 0 ) )
		self.board_textctrl.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )

		#self.board_textctrl.Enable( False )

		# Initialize data
		board_array = [ const.ILLEGAL_MOVE ]*448