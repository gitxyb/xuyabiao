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
win = wx.Frame(None,title="xyb's Notepad",size = (410,340))	#显示框

#添加组件
savebutton = wx.Button(win,label="保存",pos=(325,5),size=(80,25))
openbutton = wx.Button(win,label="打开",pos=(240,5),size=(80,25))

filepath = wx.TextCtrl(win,pos=(5,5),size=(230,25))
contents = wx.TextCtrl(win,pos=(5,35),size=(400,300),style=wx.TE_MULTILINE|wx.HSCROLL)	#下拉显示

#事件处理
openbutton.Bind(wx.EVT_BUTTON,openFile)
savebutton.Bind(wx.EVT_BUTTON,savefile)

win.Show()
app.MainLoop()


