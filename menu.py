"""
This module defines the menu class


*Todo:*
	* Enter thing to do. (optional field)

*Author:*
	* Mitri Van, mitri.van@volition-inc.com, 10/3/2013 9:21:39 AM
"""
import wx

class Menu( wx.MenuBar ):
	def __init__( self, parent, name, id = wx.ID_ANY ):

		# Initialize base class
		wx.MenuBar.__init__( self, parent = parent, id = wx.ID_ANY, pos =  wx.DefaultPosition, size = wx.DefaultSize )

		file_menu 		= wx.Menu()
		disk_menu 		= wx.Menu()
		tree_menu 		= wx.Menu()
		view_menu 		= wx.Menu()
		options_menu 	= wx.Menu()
		security_menu 	= wx.Menu()
		window_menu 	= wx.Menu()
		help_menu 		= wx.Menu()

		drive_listbox 	= wx.Menu()
		icon01 			= wx.Menu()

		# Populate the menus
		file_menu.Append(ID_OPEN, "&Open","Opens selected item")
		file_menu.AppendSeparator()
		file_menu.Append(ID_EXIT, "E&xit","Quits Multi-Explorer")

		help_menu.AppendSeparator()
		help_menu.Append(ID_ABOUT, "&About"," Information about this program")


		# Add the menus to the menubar
		menu_bar = wx.MenuBar()
		menu_bar.Append(file_menu,"&File")
		menu_bar.Append(disk_menu,"&Disk")
		menu_bar.Append(tree_menu,"&Tree")
		menu_bar.Append(view_menu,"&View")
		menu_bar.Append(options_menu,"&Options")
		menu_bar.Append(security_menu,"&Security")
		menu_bar.Append(window_menu,"&Window")
		menu_bar.Append(help_menu,"&Help")

		menu_bar2 = wx.MenuBar()
		menu_bar2.Append(drive_listbox,"Drive Listbox")

		menu_bar3 = wx.MenuBar()
		menu_bar3.Append(icon01,"Icon01")

		# Handler events
		wx.EVT_MENU( self, ID_OPEN, self.on_open_selected)
		wx.EVT_MENU( self, ID_EXIT, self.on_exit_selected)
		wx.EVT_MENU( self, ID_ABOUT, self.on_about_selected)

		self.SetMenuBar(menu_bar)
		self.Show(True)


	def on_exit_selected(self, event):
		self.Close(True)


	def on_about_selected(self, event):
		d = wx.MessageDialog(self, "\tHello Editor\n"
											"\t       by\n\n"
											"\t  Mitri Van\n"
											"          (mitriv@gmail.com)\n\n"
											"\tJune 23, 2007","About Hello Editor          ", wx.OK)
		d.ShowModal()
		d.Destroy()


	def on_open_selected(self, event):
		self.dirname = ""
		dlg = wx.FileDialog(self, "Open a file", self.dirname, "","*.*", wx.OPEN)

		if dlg.ShowModal() == wx.ID_OK:
			self.filename 	= dlg.GetFilename()
			self.dirname 	= dlg.GetDirectory()
			f = open(os.path.join(self.dirname, self.filename), 'r')
			self.control.SetValue(f.read())
			f.close()
			dlg.Destroy()


