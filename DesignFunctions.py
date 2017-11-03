def shape(t,size):
    for times in range(900):
        if times%2==0:
            t.color('cyan')
        else:
            t.color('red')
        t.forward(size)
        t.right(91)
        size+=1
def creation(t,size):
      for times in range(200):
        if times%2==0:
            t.color('cyan')
        else:
            t.color('red')
        t.forward(size)
        t.right(91)
        size+=1
