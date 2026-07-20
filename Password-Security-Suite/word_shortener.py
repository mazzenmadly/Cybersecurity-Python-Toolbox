x=input()
def test(x) :
    if len(x)<2 :
      print ("error")
    else:
      print (x[:2] +str(len (x))+x[-2:])
       
test(x)






