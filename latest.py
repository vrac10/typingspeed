from tkinter import *
import words

wrd_st=set(words.a1)
wrd=list(wrd_st)
root=Tk()
var=StringVar()
l=0
m=0
over=0
mistake=0
ev_c=0
sec=60
min=0
ch=0

def restart():
    global wrd_st,wrd,l,m,over,mistake,ev_c,sec,min
    wrd_st=set(words.a1)
    wrd=list(wrd_st)
    l=0
    m=0
    over=0
    mistake=0
    ev_c=0
    sec=60
    min=0
    bre.destroy()
    t1.config(state='normal')
    t1.delete('1.0','end')
    t1.insert('1.0',wrd[0:13])
    t1.tag_add('tn','1.0','end')
    t1.config(state='disabled')
    lb2.config(text=wrd[13:26])
    lb3.config(text=wrd[m][l])
    lbt.config(text='01:00')
    en1.bind('<Key>',tak)
    
def tak(event):
    global l,m,over,mistake,ev_c,sec,min,ch
    def inner():
        global sec,min
        sec-=1
        ss=f'{sec}' if sec>9 else f'0{sec}'
        ms=f'{min}' if min>9 else f'{min}'
        lbt.config(text=ms+':'+ss)
        if sec==0:
            wc=(m+l/m)*60/59
            en1.unbind(event)
            lbt.config(text="")
            t1.config(state='normal')
            t1.delete('1.0','end')
            t1.insert('1.0',"Your time's up")
            t1.config(state='disabled')
            lb2.config(text="Your typing Speed is "+str(wc)[0:4]+" words per minute")
            lb3.config(text='')
            en1.delete(0,END)
            bre.pack()
        if sec!=0:
            global ko
            ko=lbt.after(1000,inner)
    if ev_c==0:
        ev_c=1
        inner()
    typed=event.keysym
    
    if mistake==0 and over==0:
        if typed=='space':
            mistake=1
            t1.config(state='normal')
            t1.insert('1.'+str(ch),' ')
            t1.tag_add('er','1.'+str(ch),'1.'+str(ch+1))
            t1.tag_config('er',background='red')
            t1.config(state='disabled')
            print('mistake')
        elif typed=='BackSpace':
            if l!=0:
                l-=1
            else:
                over=1
                m-=1
                l=len(wrd[m-1])-1
            ch-=1
        elif typed==wrd[m][l]:
            if l!=len(wrd[m])-1:
                l+=1
            else:
                over=1
            ch+=1
        elif typed!=wrd[m][l]:
            mistake+=1
            t1.config(state='normal')
            t1.insert('1.'+str(ch),typed)
            t1.tag_add('er','1.'+str(ch),'1.'+str(ch+1))
            t1.tag_config('er',background='red')
            t1.config(state='disabled')
            print('mistake')
    
    elif mistake!=0 and over==0:
        if typed=='BackSpace':
            mistake-=1
            t1.config(state='normal')
            t1.tag_remove('er','1.'+str(ch+mistake),'1.'+str(ch+mistake+1))
            if mistake!=0:
                t1.tag_add('er','1.'+str(ch+mistake),'1.'+str(ch+mistake+1))
                t1.tag_config('er',background='red')
            t1.delete('1.'+str(ch+mistake),'1.'+str(ch+mistake+1))
            t1.config(state='disabled')
        else:
            mistake+=1
            t1.config(state='normal')
            t1.insert('1.'+str(ch+mistake-1),event.char)
            t1.tag_add('er','1.'+str(ch+mistake-1),'1.'+str(ch+mistake))
            t1.tag_config('er',background='red')
            t1.config(state='disabled')
            print('mistake')
    
    elif mistake==0 and over==1:
        if typed=='space':
            over=0
            m+=1
            l=0
            ch+=1
        elif typed=='BackSpace':
            over=0
            ch-=1
        else:
            mistake+=1
            t1.config(state='normal')
            t1.insert('1.'+str(ch+mistake-1),event.char)
            t1.tag_add('er','1.'+str(ch+mistake-1),'1.'+str(ch+mistake))
            t1.tag_config('er',background='red')
            t1.config(state='disabled')
            print('mistake')
    
    elif mistake!=0 and over==1:
        if typed=='BackSpace':
            mistake-=1
            t1.config(state='normal')
            t1.tag_remove('er','1.'+str(ch+mistake),'1.'+str(ch+mistake+1))
            if mistake!=0:
                t1.tag_add('er','1.'+str(ch+mistake),'1.'+str(ch+mistake+1))
                t1.tag_config('er',background='red')
            t1.delete('1.'+str(ch+mistake),'1.'+str(ch+mistake+1))
            t1.config(state='disabled')
        else:
            mistake+=1
            t1.config(state='normal')
            t1.insert('1.'+str(ch+mistake-1),event.char)
            t1.tag_add('er','1.'+str(ch+mistake-1),'1.'+str(ch+mistake))
            t1.tag_config('er',background='red')
            t1.config(state='disabled')
            print('mistake')
    
    if over!=1:
        lb3.config(text=wrd[m][l])
    else:
        lb3.config(text='_')

    if m%13==0 and l==0 and m<74 and m!=0:
        t1.config(state="normal")
        t1.tag_delete('tn','1.0','end')
        t1.tag_config('tn',justify='center')
        t1.delete('1.0','end')
        t1.insert('1.0',wrd[m:m+13])
        t1.tag_add('tn','1.0','end')
        lb2.config(text=wrd[m+13:m+26])
        en1.delete(0,END)
        ch=0

root.geometry('800x500')
root.title('Typing_Practice')

f1=Frame(root)
f1.pack(side='top')
f2=Frame(root)
f2.pack(side='top')
f3=Frame(root)
f3.pack(side='top')

t1=Text(f1,font=('Arial',15),height=1,width=60,relief='flat',bg='Ghostwhite')
t1.tag_config('tn',justify='center')
t1.insert('1.0',wrd[0:13])
t1.tag_add('tn','1.0','end')
t1.config(state='disabled')
t1.pack()

#lb1=Label(f1,text=wrd[0:13],font=('Arial',15))
lb2=Label(f1,text=wrd[13:26],font=('Arial',15))
lb2.pack(side='top')
en1=Entry(f2,textvariable=var,width=60,font=('Arial',15))
en1.pack(side='left')
lb3=Label(f3,text=wrd[m][l],font=('Arial',15))
lbt=Label(f2,text='01:00',width=8,font=('Arial',15))
lbt.pack(side='left')
lb3.pack(side='top')
bre=Button(root,text='Restart',command=restart,bg='yellow',font=('Arial',15))

en1.bind('<Key>',tak)

root.mainloop()