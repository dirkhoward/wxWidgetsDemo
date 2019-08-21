#!/bin/python
"""
Hellow world, fleshed out
"""

import wx


class HellowFrame(wx.Frame):
    """
    A frame that says 'Hello World'
    """

    def __init__(self, *args, **kw):
        # ensure the parent __init__ is called
        super(HellowFrame, self).__init__(*args, **kw)

        # create a panel in the frame
        panel1 = wx.Panel(self)

        # put some text into the panel
        hello = wx.StaticText(panel1, label='Hello world!', pos=(25, 25))
        font = hello.GetFont()
        font.PointSize += 10
        font = font.Bold()
        hello.SetFont(font)

        # create a menu bar
        self.makeMenuBar()

        self.CreateStatusBar()
        self.SetStatusText('Welcome to wxPython!')

    def makeMenuBar(self):
        """
        A menu bar is composed of menus, which are composed of menu items.
        """

        # Make a file menu
        fileMenu = wx.Menu()
        helloItem = fileMenu.Append(-1, '&Hello...\tCtrl-H',
                                    'Help string shown in status bar for this menu item')
        fileMenu.AppendSeparator()
        exitItem = fileMenu.Append(wx.ID_EXIT)

        helpMenu = wx.Menu()
        aboutItem = helpMenu.Append(wx.ID_ABOUT)

        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, '&File')
        menuBar.Append(helpMenu, '&Help')

        self.SetMenuBar(menuBar)

        # associate a handler to each menu element
        self.Bind(wx.EVT_MENU, self.OnHello, helloItem)
        self.Bind(wx.EVT_MENU, self.OnExit, exitItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)


    def OnExit(self, event):
        ''' Close the frame and terminate the application '''
        self.Close(True)


    def OnHello(self, event):
        """ Say hello to the user """
        wx.MessageBox('Hello again from wxPython')


    def OnAbout(self, event):
        """ Display an about box """
        wx.MessageBox('This is a wxPython Hello World sample',
                      'About Hello World 2',
                      wx.OK|wx.ICON_INFORMATION)


if __name__ == '__main__':
    # when the module is run (not imported) then create the app, the
    # frame, show it and start the event loop
    app = wx.App()
    frame = HellowFrame(None, title='Hello world 2')
    frame.Show()
    app.MainLoop()