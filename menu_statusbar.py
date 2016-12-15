"""
This module contains the statusbar class

*Examples:* ::

	Enter code examples here. (optional field)

*Todo:*
	* Enter thing to do. (optional field)

*Author:*
	* Mitri Van, mitri.van@volition-inc.com, 10/3/2013 11:14:40 AM
"""

import wx

class status_bar( wx.StatusBar ):
	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.DefaultSize ):

		# Initialize base class
		wx.StatusBar.__init__( self, parent = parent, id = id, style = wx.SB_NORMAL )

		self.SetForegroundColour( wx.Colour( 10, 10, 10 ) )
		self.SetBackgroundColour( wx.Colour( 171, 171, 171 ) )

		self.SetStatusText( 'Dragonchess by Gary Gygax' )