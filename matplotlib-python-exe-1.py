Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import matplotlib.pyplot as plt
>>> import numpy as np
>>> x=np.array([1,2,3,4,5])
>>> y=np.array([10,20,30,40,50])
>>> plt.plot(x,y)
[<matplotlib.lines.Line2D object at 0x000002765BCE83D0>]
>>> plt.show()
>>> x=np.array([1,2,3,4,5])
>>> plt.plot(x,marker="o")
[<matplotlib.lines.Line2D object at 0x0000027661189F10>]
>>> plt.plot(x,"o:r")
[<matplotlib.lines.Line2D object at 0x0000027661196250>]
>>> 
>>> [<matplotlib.lines.Line2D object at 0x0000027661196250>]
SyntaxError: invalid syntax
>>> plt.plot(x,marker="o",ms="20",mfc="y")
[<matplotlib.lines.Line2D object at 0x00000276611964C0>]
>>> x=np.array([1,2,3,4,5])
>>> y=np.array([10,20,30,40,50])
>>>  plt.plot(x,y)
 
SyntaxError: unexpected indent
>>> x=np.array([1,2,3,4,5])
>>> y=np.array([10,20,30,40,50])
>>> plt.plot(x,marker="o")
[<matplotlib.lines.Line2D object at 0x0000027661196790>]
>>> plt.show()
>>> plt.plot(x,"o:r")
[<matplotlib.lines.Line2D object at 0x000002765A7B60D0>]
>>> plt.show()
>>> plt.plot(x,"*-b")
[<matplotlib.lines.Line2D object at 0x000002765A97CAF0>]
>>> plt.show()
>>> plt.plot(x,marker="o",ms="20")
[<matplotlib.lines.Line2D object at 0x000002765AA0BE80>]
>>> plt.show()
>>> plt.plot(x,marker="o",ms="10",mfc="y")
[<matplotlib.lines.Line2D object at 0x00000276611DAFD0>]
>>> plt.show()
>>> plt.plot(x,marker="o",ms="13",mfc="r",mec="y")
[<matplotlib.lines.Line2D object at 0x00000276612719A0>]
>>> plt.show()
>>> plt.plot(x,linestyle="dotted")
[<matplotlib.lines.Line2D object at 0x00000276614AED90>]
>>> plt.show()
>>> plt.plot(x.linestyle="dashed")
SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
>>> plt.plot(x,linestyle="dashed")
[<matplotlib.lines.Line2D object at 0x000002766154D040>]
>>> plt.show()
>>> plt.plot(x.line width="20")
SyntaxError: invalid syntax
>>> plt.plot(x,linewidth="20")
[<matplotlib.lines.Line2D object at 0x0000027661A2D0A0>]
>>> plt.show()
>>> plt.plot(x,y)
[<matplotlib.lines.Line2D object at 0x00000276620C46A0>]
>>> plt.show()
>>> plt.title("line graph")
Text(0.5, 1.0, 'line graph')
>>> plt.show()
>>> plt.ylable("yaxis")
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    plt.ylable("yaxis")
AttributeError: module 'matplotlib.pyplot' has no attribute 'ylable'
>>> plt.grid()
>>> plt.show()
>>> plt.grid(axis="x")
>>> plt.show()
>>> x=np.array(["A","B","C","D"])
>>> y=np.array([1,2,3,4])
>>> plt.bar(x,y,color="r")
<BarContainer object of 4 artists>
>>> plt.show()
>>> mylable=(["apple","kiwi","org","mango","cherry"])
>>> x=np.array([10,36,54,46,21])
>>> plt.pie(x)
([<matplotlib.patches.Wedge object at 0x000002765DE729A0>, <matplotlib.patches.Wedge object at 0x000002765DE72340>, <matplotlib.patches.Wedge object at 0x000002765DE72670>, <matplotlib.patches.Wedge object at 0x000002765DE58430>, <matplotlib.patches.Wedge object at 0x000002765DE58040>], [Text(1.08059345038942, 0.20571289452897284, ''), Text(0.5440156648084158, 0.9560580298512521, ''), Text(-1.015274786370709, 0.4233404164025817, ''), Text(-0.09300797772830068, -1.096060908927461, ''), Text(1.015274766552713, -0.42334046393102376, '')])
>>> plt.show()
>>> plt.pie(x,labels=mylable)
([<matplotlib.patches.Wedge object at 0x0000027661189FA0>, <matplotlib.patches.Wedge object at 0x00000276611893D0>, <matplotlib.patches.Wedge object at 0x0000027661189A00>, <matplotlib.patches.Wedge object at 0x0000027661189E20>, <matplotlib.patches.Wedge object at 0x000002765BCE8610>], [Text(1.08059345038942, 0.20571289452897284, 'apple'), Text(0.5440156648084158, 0.9560580298512521, 'kiwi'), Text(-1.015274786370709, 0.4233404164025817, 'org'), Text(-0.09300797772830068, -1.096060908927461, 'mango'), Text(1.015274766552713, -0.42334046393102376, 'cherry')])
>>> plt.show()
>>> separate=([0,0,0,0,0.4])
>>> plt.show()
>>> plt.pie(x,lables=mylale.separate=([0,0,0,0,0.4])
	
SyntaxError: invalid syntax
>>> plt.pie(x,lables=mylable.separate=([0,0,0,0,0.4])
	
SyntaxError: invalid syntax
>>> plt.pie(x,lables=mylable.star angle=90)
SyntaxError: invalid syntax
>>> plt.pie(x,lables=mylable.starangle=90)
SyntaxError: invalid syntax
>>> plt.pie(x,lables=mylable,starangle=90)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    plt.pie(x,lables=mylable,starangle=90)
TypeError: pie() got an unexpected keyword argument 'lables'
>>> plt.pie(x,labels=mylable,starangle=90)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    plt.pie(x,labels=mylable,starangle=90)
TypeError: pie() got an unexpected keyword argument 'starangle'
>>> plt.pie(x,lables=mylable.star angle=90)
SyntaxError: invalid syntax
>>> plt.pie(x,lables=mylable.starangle=90)
SyntaxError: invalid syntax
>>> plt.pie(x,lables=mylable,starangle="90")
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    plt.pie(x,lables=mylable,starangle="90")
TypeError: pie() got an unexpected keyword argument 'lables'
>>> plt.pie(x,labels=mylable.starangle="90")
SyntaxError: invalid syntax
>>> plt.show()
>>> plt.pie(x)
([<matplotlib.patches.Wedge object at 0x000002765A99D520>, <matplotlib.patches.Wedge object at 0x000002765A99C610>, <matplotlib.patches.Wedge object at 0x000002765A99DA90>, <matplotlib.patches.Wedge object at 0x000002765A99DF10>, <matplotlib.patches.Wedge object at 0x00000276614AA3D0>], [Text(1.08059345038942, 0.20571289452897284, ''), Text(0.5440156648084158, 0.9560580298512521, ''), Text(-1.015274786370709, 0.4233404164025817, ''), Text(-0.09300797772830068, -1.096060908927461, ''), Text(1.015274766552713, -0.42334046393102376, '')])
>>> plt.show()
>>> 