# import time
# start=time.time()
# n=10
# major_ticker_lenght=4
# for i in range(0,n+1):
#     print("-"*major_ticker_lenght,i)
#     if i==n:
#         break
#     for j in range(1,major_ticker_lenght*2):
#          if j==major_ticker_lenght:
#             print("---")
#          elif j%2==1:
#              print("-")
#          else:
#              print("--")
# end=time.time()
# print(end-start)
import time
start=time.time()
def draw_line(ml,label=""):
    print("-"*ml,label)
def draw_interval(cl):
    if cl>0:
        draw_interval(cl-1)
        draw_line(cl)
        draw_interval(cl-1)
def draw_ruler(n,ml):
    draw_line(ml,'0')
    for i in range(1,n+1):
        draw_interval(ml-1)
        draw_line(ml,str(i))
draw_ruler(2,4)
end=time.time()
print(end-start)