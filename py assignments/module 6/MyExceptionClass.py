class MyError(Exception):
    def __init__(self,value):
        self.value=value
    def __str__(self):
        return(repr(self.value))
try:
    print("start")
    raise(MyError(3*2))
    print("close")
except MyError as error:
    print('A New Exception occured:',error.value)
