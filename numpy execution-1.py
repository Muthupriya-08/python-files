Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as smp
>>> arr=smp.array([1,2,3])
>>> print (arr)
[1 2 3]
>>> ar=smp.array([1,2,3,4],[5,6,7,8])
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    ar=smp.array([1,2,3,4],[5,6,7,8])
TypeError: Field elements must be 2- or 3-tuples, got '5'
>>> ar=smp.array([[1,2,3,4],[5,6,7,8]])
>>> print(arr[0][2])
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print(arr[0][2])
IndexError: invalid index to scalar variable.
>>> print(ar[0][2])
3
>>> print(ar[1,-1])
8
>>> ar[1][2]
7
>>> ar[0][2]
3
>>> a="array"
>>> a=a[:3:1]
>>> print(a)
arr
>>> arr=np.array([10,20,30,40,50])
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    arr=np.array([10,20,30,40,50])
NameError: name 'np' is not defined
>>> arr=smp.array([10,20,30,40,50])
>>> print(arr)
[10 20 30 40 50]
>>> arr=smp.array([10,20,30,40,50])
>>> print(arr.dtype)
int32
>>> arr=smp.array([True,False,False])
>>> print(arr.dtype)
bool
>>> arr=smp.array(["TRUE","FALSE","FALSE"])
>>> print(arr.dtype)
<U5
>>> a=smp.array([b'True',b'False',b'False'])
>>> print(a.dtype)
|S5
>>> a=smp.array([[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]])
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    a=smp.array([[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]])
TypeError: Field elements must be 2- or 3-tuples, got '[1, 2, 3]'
>>> a=smp.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
>>> print(a.ndim)
3
>>> arr=smp.arr(55)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    arr=smp.arr(55)
  File "C:\Users\USER\AppData\Local\Programs\Python\Python39\lib\site-packages\numpy\__init__.py", line 320, in __getattr__
    raise AttributeError("module {!r} has no attribute "
AttributeError: module 'numpy' has no attribute 'arr'
>>> arr=smp.array(55)
>>> print(arr.ndim)
0
>>> arr=np.arr([55,20],ndim=5)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    arr=np.arr([55,20],ndim=5)
NameError: name 'np' is not defined
>>> arr=smp.arr([55,20],ndim=5)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    arr=smp.arr([55,20],ndim=5)
  File "C:\Users\USER\AppData\Local\Programs\Python\Python39\lib\site-packages\numpy\__init__.py", line 320, in __getattr__
    raise AttributeError("module {!r} has no attribute "
AttributeError: module 'numpy' has no attribute 'arr'
>>> arr=smp.array([55,10])
>>> print(arr.ndim)
1
>>> arr=smp.array([[10,20,30],[1,2,3]],[[10,20,30],[1,2,3]])
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    arr=smp.array([[10,20,30],[1,2,3]],[[10,20,30],[1,2,3]])
TypeError: Field elements must be 2- or 3-tuples, got '[10, 20, 30]'
>>> arr=smp.array([[[10,20,30],[1,2,3]],[[10,20,30],[1,2,3]]])
>>> a
array([[[1, 2, 3],
        [4, 5, 6]],

       [[1, 2, 3],
        [4, 5, 6]]])
>>> print(arr[1,1])
[1 2 3]
>>> arr=smp.array([[10,20,30,40],[50,60,70,80],[1,2,3,4],[5,6,7,8]])
>>> print(arr[1:3])
[[50 60 70 80]
 [ 1  2  3  4]]
>>> print(arr[:1:3])
[[10 20 30 40]]
>>> print(arr(:1:3))
SyntaxError: invalid syntax
>>> 
KeyboardInterrupt
>>> print(arr(1:3))
SyntaxError: invalid syntax
>>> print(arr[3,2:4])
[7 8]
>>> arr=smp.array([[10,20,30,40],[50,60,70,80,90],[1,2,3,4,5],[6,7,8,9,10]])
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    arr=smp.array([[10,20,30,40],[50,60,70,80,90],[1,2,3,4,5],[6,7,8,9,10]])
ValueError: setting an array element with a sequence. The requested array has an inhomogeneous shape after 1 dimensions. The detected shape was (4,) + inhomogeneous part.
>>> arr=smp.array([[10,20,30,40],[50,60,70,80],[1,2,3,4],[5,6,7,8]])
>>> print(arr[2,1:2])
[2]
>>> print(arr[3,0:8])
[5 6 7 8]
>>> print(arr[::-1])
[[ 5  6  7  8]
 [ 1  2  3  4]
 [50 60 70 80]
 [10 20 30 40]]
>>> print(arr[-3:-1,0:2])
[[50 60]
 [ 1  2]]
>>> arr
              
