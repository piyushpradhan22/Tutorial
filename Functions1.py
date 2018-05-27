def info_args(*args,**kwargs):
    """" Takes multiple arguments as list and dictionary"""
    print(args)
    print(kwargs)

info_args('Hello','abc','def','ghi','jkl','mno',name='Piyush',age=22,address='Odisha',company='cognizant')
argss=['hello','Piyush','Pradhan']
kwargss={'piyush':222,'mark1':5555,'Mark2':63566}
info_args(argss,kwargss)
info_args(*argss,**kwargss)
info_args()