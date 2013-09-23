#coding:utf8

import wx

def openFile(x):
	fc = open(filepath.GetValue(),'r').read() #获取内容
	contents.SetValue(fc)
	
def savefile(x):
	fc = open(filepath.GetValue(),'w')
	fc.write(contents.GetValue())
	fc.close()

app = wx.App()
win = wx.Frame(None,title="xyb's Notepad")	#显示框
bkg = wx.Panel(win)

#添加组件
savebutton = wx.Button(bkg,label="保存")
openbutton = wx.Button(bkg,label="打开")

filepath = wx.TextCtrl(bkg)
contents = wx.TextCtrl(bkg,style=wx.TE_MULTILINE|wx.HSCROLL)	#下拉显示

#事件处理
openbutton.Bind(wx.EVT_BUTTON,openFile)
savebutton.Bind(wx.EVT_BUTTON,savefile)

#布局管理
headbox = wx.BoxSizer()
headbox.Add(filepath,proportion=1,flag=wx.EXPAND)
headbox.Add(openbutton,proportion=0,flag=wx.LEFT,border=5)
headbox.Add(savebutton,proportion=0,flag=wx.LEFT,border=5)

allbox = wx.BoxSizer(wx.VERTICAL)
allbox.Add(headbox,proportion=0,flag=wx.EXPAND|wx.ALL,border=5)
allbox.Add(contents,proportion=1,flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.BOTTOM,border=5)

bkg.SetSizer(allbox)

win.Show()
app.MainLoop()


