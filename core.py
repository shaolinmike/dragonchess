"""
Dragonchess for Python

http://en.wikipedia.org/wiki/Dragonchess
Dragonchess is a three-dimensional fantasy chess variant created by Gary Gygax,
co-creator of the famed role-playing game Dungeons & Dragons. The game was introduced
in 1985 in issue No. 100 of Dragon Magazine.[1][2][3]

The Dragonchess gameboard consists of three vertically stacked 12×8 levels. The
upper level (blue and white) represents the air, the middle level (green and amber)
represents the land, and the lower level (red and brown) is the subterranean world (Gygax 1985:34).

The Dragonchess game pieces (42 per player) are an ensemble of characters and
monsters inspired or derived from fantasy settings in Dungeons & Dragons. Intricate
inter- and intra-level game piece capabilities are defined. As in chess, the game
is won by delivering checkmate to the enemy king.

						Upper Board
*---*---*---*---*---*---*---*---*---*---*---*---*
|   |   | G |   |   |   | R |   |   |   | G |   |
*---*---*---*---*---*---*---*---*---*---*---*---*
|   | s |   | s |   | s |   | s |   | s |   | s |
*---*---*---*---*---*---*---*---*---*---*---*---*
|   |   |   |   |   |   |   |   |   |   |   |   |
*---*---*---*---*---*---*---*---*---*---*---*---*
|   |   |   |   |   |   |   |   |   |   |   |   |
*---*---*---*---*---*---*---*---*---*---*---*---*
|   |   |   |   |   |   |   |   |   |   |   |   |
*---*---*---*---*---*---*---*---*---*---*---*---*
|   |   |   |   |   |   |   |   |   |   |   |   |
*---*---*---*---*---*---*---*---*---*---*---*---*
|   | s |   | s |   | s |   | s |   | s |   | s |
*---*---*---*---*---*---*---*---*---*---*---*---*
|   |   | G |   |   |   | R |   |   |   | G |   |
*---*---*---*---*---*---*---*---*---*---*---*---*

						Middle Board
*---*---*---*---*---*---*---*---*---*---*---*---*
| O | U | H | T | C | M | K | P | T | H | U | O |
*---*---*---*---*---*---*---*---*---*---*---*---*
| w | w | w | w | w | w | w | w | w | w | w | w |
*---*---*---*---*---*---*---*---*---*---*---*---*
|   |   |   |   |   |   |   |   |   |   |   |   |
*---*---*---*---*---*---*---*---*---*---*---*---*
|   |   |   |   |   |   |   |   |   |   |   |   |
*---*---*---*---*---*---*---*---*---*---*---*---*
|   |   |   |   |   |   |   |   |   |   |   |   |
*---*---*---*---*---*---*---*---*---*---*---*---*
|   |   |   |   |   |   |   |   |   |   |   |   |
*---*---*---*---*---*---*---*---*---*---*---*---*
| w | w | w | w | w | w | w | w | w | w | w | w |
*---*---*---*---*---*---*---*---*---*---*---*---*
| O | U | H | T | C | M | K | P | T | H | U | O |
*---*---*---*---*---*---*---*---*---*---*---*---*

						Lower Board
*---*---*---*---*---*---*---*---*---*---*---*---*
|   |   | B |   |   |   | E |   |   |   | B |   |
*---*---*---*---*---*---*---*---*---*---*---*---*
|   | d |   | d |   | d |   | d |   | d |   | d |
*---*---*--;-*---*---*---*---*---*---*---*---*---*
|   |   |   |   |   |   |   |   |   |   |   |   |
*---*---*---*---*---*---*---*---*---*---*---*---*
|   |   |   |   |   |   |   |   |   |   |   |   |
*---*---*---*---*---*---*---*---*---*---*---*---*
|   |   |   |   |   |   |   |   |   |   |   |   |
*---*---*---*---*---*---*---*---*---*---*---*---*
|   |   |   |   |   |   |   |   |   |   |   |   |
*---*---*---*---*---*---*---*---*---*---*---*---*
|   | d |   | d |   | d |   | d |   | d |   | d |
*---*---*---*---*---*---*---*---*---*---*---*---*
|   |   | B |   |   |   | E |   |   |   | B |   |
*---*---*---*---*---*---*---*---*---*---*---*---*



*Todo:*
	* Enter thing to do. (optional field)

*Author:*
	* Mitri Van, mitri.van@volition-inc.com, 9/30/2013 3:58:36 PM
"""

try:
	import wx
except ImportError:
	raise ImportError, "The wxPython module is required to run this application.  Download it from wxPython.org (http://www.wxpython.org/download.php)"

import board
import const
import input_move
import menu
import menu_statusbar

import pylint

class Dragonchess( wx.Frame ):
	def __init__( self, parent, id = wx.ID_ANY, title = ( const.TITLE + " - ver " + const.VERSION ),
					pos = wx.DefaultPosition, size = ( 1027, 345 ) ):

		# Initialize base class
		wx.Frame.__init__( self, parent = parent, id = id, title = title, pos = pos, size = size, style = wx.DEFAULT_FRAME_STYLE ^ wx.MAXIMIZE_BOX ^ wx.RESIZE_BORDER  )

		# Controls
		self.upper_board	= board.Board( self, 'Air Board' )
		self.middle_board = board.Board( self, 'Ground Board' )
		self.lower_board 	= board.Board( self, 'Under Board' )

		self.text_entry	= input_move.Input( self, 'Input Field' )

		self.status_bar 	= menu_statusbar.status_bar( self )
		self.SetStatusBar( self.status_bar )

		# Sizers
		sizer_board = wx.BoxSizer( wx.HORIZONTAL )
		sizer_board.Add( self.upper_board,	proportion = 0, flag = wx.EXPAND | wx.ALL, border = 5 )
		sizer_board.Add( self.middle_board,	proportion = 0, flag = wx.EXPAND | wx.ALL, border = 5 )
		sizer_board.Add( self.lower_board,	proportion = 0, flag = wx.EXPAND | wx.ALL, border = 5 )

		sizer_main = wx.BoxSizer( wx.VERTICAL )
		sizer_main.Add( sizer_board, proportion = 9, flag = wx.EXPAND | wx.ALL )
		sizer_main.Add( self.text_entry, proportion = 1, flag = wx.EXPAND | wx.ALL, border = 5 )

		self.SetSizer( sizer_main )
		self.Layout()

		# Data
		self.initialize_data( )

		## Event Handlers



	def initialize_data( self ):
		self.upper_board.board_textctrl.SetValue( "    A   B   C   D   E   F   G   H   I   J   K   L\
\n  *---*---*---*---*---*---*---*---*---*---*---*---*\
\n8 |   |   | G |   |   |   | R |   |   |   | G |   | 8\
\n  *---*---*---*---*---*---*---*---*---*---*---*---*\
\n7 |   | s |   | s |   | s |   | s |   | s |   | s | 7\
\n  *---*---*---*---*---*---*---*---*---*---*---*---*\
\n6 |   |   |   |   |   |   |   |   |   |   |   |   | 6\
\n  *---*---*---*---*---*---*---*---*---*---*---*---*\
\n5 |   |   |   |   |   |   |   |   |   |   |   |   | 5\
\n  *---*---*---*---*---*---*---*---*---*---*---*---*\
\n4 |   |   |   |   |   |   |   |   |   |   |   |   | 4\
\n  *---*---*---*---*---*---*---*---*---*---*---*---*\
\n3 |   |   |   |   |   |   |   |   |   |   |   |   | 3\
\n  *---*---*---*---*---*---*---*---*---*---*---*---*\
\n2 |   | s |   | s |   | s |   | s |   | s |   | s | 2\
\n  *---*---*---*---*---*---*---*---*---*---*---*---*\
\n1 |   |   | G |   |   |   | R |   |   |   | G |   | 1\
\n  *---*---*---*---*---*---*---*---*---*---*---*---*\
\n    A   B   C   D   E   F   G   H   I   J   K   L" )

		self.middle_board.board_textctrl.SetValue( "    A   B   C   D   E   F   G   H   I   J   K   L\
\n  *---*---*---*---*---*---*---*---*---*---*---*---*\
\n8 | O | U | H | T | C | M | K | P | T | H | U | O | 8\
\n  *---*---*---*---*---*---*---*---*---*---*---*---*\
\n7 | w | w | w | w | w | w | w | w | w | w | w | w | 7\
\n  *---*---*---*---*---*---*---*---*---*---*---*---*\
\n6 |   |   |   |   |   |   |   |   |   |   |   |   | 6\
\n  *---*---*---*---*---*---*---*---*---*---*---*---*\
\n5 |   |   |   |   |   |   |   |   |   |   |   |   | 5\
\n  *---*---*---*---*---*---*---*---*---*---*---*---*\
\n4 |   |   |   |   |   |   |   |   |   |   |   |   | 4\
\n  *---*---*---*---*---*---*---*---*---*---*---*---*\
\n3 |   |   |   |   |   |   |   |   |   |   |   |   | 3\
\n  *---*---*---*---*---*---*---*---*---*---*---*---*\
\n2 | w | w | w | w | w | w | w | w | w | w | w | w | 2\
\n  *---*---*---*---*---*---*---*---*---*---*---*---*\
\n1 | O | U | H | T | C | M | K | P | T | H | U | O | 1\
\n  *---*---*---*---*---*---*---*---*---*---*---*---*\
\n    A   B   C   D   E   F   G   H   I   J   K   L" )

		self.lower_board.board_textctrl.SetValue( "    A   B   C   D   E   F   G   H   I   J   K   L\
\n  *---*---*---*---*---*---*---*---*---*---*---*---*\
\n8 |   |   | B |   |   |   | E |   |   |   | B |   | 8\
\n  *---*---*---*---*---*---*---*---*---*---*---*---*\
\n7 |   | d |   | d |   | d |   | d |   | d |   | d | 7\
\n  *---*---*---*---*---*---*---*---*---*---*---*---*\
\n6 |   |   |   |   |   |   |   |   |   |   |   |   | 6\
\n  *---*---*---*---*---*---*---*---*---*---*---*---*\
\n5 |   |   |   |   |   |   |   |   |   |   |   |   | 5\
\n  *---*---*---*---*---*---*---*---*---*---*---*---*\
\n4 |   |   |   |   |   |   |   |   |   |   |   |   | 4\
\n  *---*---*---*---*---*---*---*---*---*---*---*---*\
\n3 |   |   |   |   |   |   |   |   |   |   |   |   | 3\
\n  *---*---*---*---*---*---*---*---*---*---*---*---*\
\n2 |   | d |   | d |   | d |   | d |   | d |   | d | 2\
\n  *---*---*---*---*---*---*---*---*---*---*---*---*\
\n1 |   |   | B |   |   |   | E |   |   |   | B |   | 1\
\n  *---*---*---*---*---*---*---*---*---*---*---*---*\
\n    A   B   C   D   E   F   G   H   I   J   K   L" )


#--------
#  MAIN
#--------
app = wx.App( )
frame = Dragonchess( None )
frame.Show( )
app.MainLoop( )