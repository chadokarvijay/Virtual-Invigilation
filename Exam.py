def questn_win():
    import sys
    import tkinter as tk
    import tkinter.ttk as ttk
    py3 = True
    
    import exam_
    
    def vp_start_gui():
        '''Starting point when module is the main routine.'''
        global val, w, root
        root = tk.Tk()
        exam_.set_Tk_var()
        top = Toplevel1 (root)
        exam_.init(root, top)
        root.mainloop()
    
    w = None
    def create_Toplevel1(rt, *args, **kwargs):
        '''Starting point when module is imported by another module.
           Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
        global w, w_win, root
        #rt = root
        root = rt
        w = tk.Toplevel (root)
        exam_.set_Tk_var()
        top = Toplevel1 (w)
        exam_.init(w, top, *args, **kwargs)
        return (w, top)
    
    def destroy_Toplevel1():
        global w
        w.destroy()
        w = None
    
    class Toplevel1:
        def __init__(self, top=None):
            '''This class configures and populates the toplevel window.
               top is the toplevel containing window.'''
            _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
            _fgcolor = '#000000'  # X11 color: 'black'
            _compcolor = '#d9d9d9' # X11 color: 'gray85'
            _ana1color = '#d9d9d9' # X11 color: 'gray85'
            _ana2color = '#ececec' # Closest X11 color: 'gray92'
            self.style = ttk.Style()
            if sys.platform == "win32":
                self.style.theme_use('winnative')
            self.style.configure('.',background=_bgcolor)
            self.style.configure('.',foreground=_fgcolor)
            self.style.configure('.',font="TkDefaultFont")
            self.style.map('.',background=
                [('selected', _compcolor), ('active',_ana2color)])
    
            top.attributes('-fullscreen',True)
            top.minsize(148, 1)
            top.maxsize(1924, 1055)
            top.resizable(1,  1)
            top.title("EXAM")
            top.configure(background="#ffffff")
            top.configure(cursor="circle")
            top.configure(highlightbackground="#d9d9d9")
            top.configure(highlightcolor="black")
    
            self.TFrame1 = ttk.Frame(top)
            self.TFrame1.place(relx=0.0, rely=0.0, relheight=0.315, relwidth=0.267)
            self.TFrame1.configure(relief='groove')
            self.TFrame1.configure(borderwidth="2")
            self.TFrame1.configure(relief="groove")
    
            self.Labelframe1 = tk.LabelFrame(self.TFrame1)
            self.Labelframe1.place(relx=0.019, rely=0.0, relheight=0.778
                    , relwidth=0.331)
            self.Labelframe1.configure(relief='groove')
            self.Labelframe1.configure(foreground="black")
            self.Labelframe1.configure(text='''Candidate image''')
            self.Labelframe1.configure(background="#c0c0c0")
            self.Labelframe1.configure(highlightbackground="#d9d9d9")
            self.Labelframe1.configure(highlightcolor="black")
    
            self.Canvas1 = tk.Canvas(self.Labelframe1)
            self.Canvas1.place(relx=0.065, rely=0.196, relheight=0.727
                    , relwidth=0.888, bordermode='ignore')
            self.Canvas1.configure(background="#d9d9d9")
            self.Canvas1.configure(borderwidth="2")
            self.Canvas1.configure(highlightbackground="#000000")
            self.Canvas1.configure(highlightcolor="black")
            self.Canvas1.configure(insertbackground="#000000")
            self.Canvas1.configure(relief="ridge")
            self.Canvas1.configure(selectbackground="blue")
            self.Canvas1.configure(selectforeground="white")
    
            self.Message2 = tk.Message(self.TFrame1)
            self.Message2.place(relx=0.039, rely=0.73, relheight=0.095
                    , relwidth=0.285)
            self.Message2.configure(background="#d9d9d9")
            self.Message2.configure(foreground="#000000")
            self.Message2.configure(highlightbackground="#d9d9d9")
            self.Message2.configure(highlightcolor="black")
            self.Message2.configure(text='''Vishwas Sahu''')
            self.Message2.configure(width=146)
    
            self.Message1 = tk.Message(self.TFrame1)
            self.Message1.place(relx=0.39, rely=0.063, relheight=0.286
                    , relwidth=0.285)
            self.Message1.configure(background="#d9d9d9")
            self.Message1.configure(foreground="#000000")
            self.Message1.configure(highlightbackground="#d9d9d9")
            self.Message1.configure(highlightcolor="black")
            self.Message1.configure(text='''Time Left
    
    162:30:09''')
            self.Message1.configure(width=146)
    
            self.Message3 = tk.Message(self.TFrame1)
            self.Message3.place(relx=0.39, rely=0.413, relheight=0.254
                    , relwidth=0.324)
            self.Message3.configure(background="#d9d9d9")
            self.Message3.configure(foreground="#ff0000")
            self.Message3.configure(highlightbackground="#ff0000")
            self.Message3.configure(highlightcolor="#ff0000")
            self.Message3.configure(text='''Warnings
    
    8 out of 70''')
            self.Message3.configure(width=166)
    
            self.TProgressbar1 = ttk.Progressbar(self.TFrame1)
            self.TProgressbar1.place(relx=0.448, rely=0.857, relwidth=0.448
                    , relheight=0.0, height=22)
            self.TProgressbar1.configure(length="230")
    
            self.Message5 = tk.Message(self.TFrame1)
            self.Message5.place(relx=0.448, rely=0.794, relheight=0.063
                    , relwidth=0.246)
            self.Message5.configure(background="#d9d9d9")
            self.Message5.configure(foreground="#000000")
            self.Message5.configure(highlightbackground="#d9d9d9")
            self.Message5.configure(highlightcolor="black")
            self.Message5.configure(text='''Noice level''')
            self.Message5.configure(width=126)
    
            self.Scrolledwindow1 = ScrolledWindow(top)
            self.Scrolledwindow1.place(relx=0.0, rely=0.32, relheight=0.67
                    , relwidth=0.268)
            self.Scrolledwindow1.configure(background="#ca44f7")
            self.Scrolledwindow1.configure(borderwidth="2")
            self.Scrolledwindow1.configure(highlightbackground="#d9d9d9")
            self.Scrolledwindow1.configure(highlightcolor="black")
            self.Scrolledwindow1.configure(insertbackground="black")
          
            self.Scrolledwindow1.configure(selectbackground="blue")
            self.Scrolledwindow1.configure(selectforeground="white")
            self.color = self.Scrolledwindow1.cget("background")
            self.Scrolledwindow1_f = tk.Frame(self.Scrolledwindow1,
                                background=self.color)
            self.Scrolledwindow1.create_window(0, 0, anchor='nw',
                                               window=self.Scrolledwindow1_f)
    
            self.Button1 = tk.Button(self.Scrolledwindow1)
            self.Button1.place(relx=0.082, rely=0.195, height=33, width=56)
            self.Button1.configure(activebackground="#ececec")
            self.Button1.configure(activeforeground="#000000")
            self.Button1.configure(background="#80ff00")
            self.Button1.configure(disabledforeground="#a3a3a3")
            self.Button1.configure(foreground="#000000")
            self.Button1.configure(highlightbackground="#d9d9d9")
            self.Button1.configure(highlightcolor="black")
            self.Button1.configure(pady="0")
            self.Button1.configure(text='''05''')
    
            self.Button2 = tk.Button(self.Scrolledwindow1)
            self.Button2.place(relx=0.286, rely=0.345, height=33, width=56)
            self.Button2.configure(activebackground="#ececec")
            self.Button2.configure(activeforeground="#000000")
            self.Button2.configure(background="#ff0000")
            self.Button2.configure(disabledforeground="#a3a3a3")
            self.Button2.configure(foreground="#000000")
            self.Button2.configure(highlightbackground="#d9d9d9")
            self.Button2.configure(highlightcolor="black")
            self.Button2.configure(pady="0")
            self.Button2.configure(text='''14''')
    
            self.Button3 = tk.Button(self.Scrolledwindow1)
            self.Button3.place(relx=0.286, rely=0.12, height=33, width=56)
            self.Button3.configure(activebackground="#ececec")
            self.Button3.configure(activeforeground="#000000")
            self.Button3.configure(background="#80ff00")
            self.Button3.configure(disabledforeground="#a3a3a3")
            self.Button3.configure(foreground="#000000")
            self.Button3.configure(highlightbackground="#d9d9d9")
            self.Button3.configure(highlightcolor="black")
            self.Button3.configure(pady="0")
            self.Button3.configure(text='''02''')
    
            self.Button4 = tk.Button(self.Scrolledwindow1)
            self.Button4.place(relx=0.49, rely=0.195, height=33, width=56)
            self.Button4.configure(activebackground="#ececec")
            self.Button4.configure(activeforeground="#000000")
            self.Button4.configure(background="#80ff00")
            self.Button4.configure(disabledforeground="#a3a3a3")
            self.Button4.configure(foreground="#000000")
            self.Button4.configure(highlightbackground="#d9d9d9")
            self.Button4.configure(highlightcolor="black")
            self.Button4.configure(pady="0")
            self.Button4.configure(text='''07''')
    
            self.Button5 = tk.Button(self.Scrolledwindow1)
            self.Button5.place(relx=0.49, rely=0.12, height=33, width=56)
            self.Button5.configure(activebackground="#ececec")
            self.Button5.configure(activeforeground="#000000")
            self.Button5.configure(background="#80ff00")
            self.Button5.configure(disabledforeground="#a3a3a3")
            self.Button5.configure(foreground="#000000")
            self.Button5.configure(highlightbackground="#d9d9d9")
            self.Button5.configure(highlightcolor="black")
            self.Button5.configure(pady="0")
            self.Button5.configure(text='''03''')
    
            self.Button6 = tk.Button(self.Scrolledwindow1)
            self.Button6.place(relx=0.286, rely=0.495, height=33, width=56)
            self.Button6.configure(activebackground="#ececec")
            self.Button6.configure(activeforeground="#000000")
            self.Button6.configure(background="#80ff00")
            self.Button6.configure(disabledforeground="#a3a3a3")
            self.Button6.configure(foreground="#000000")
            self.Button6.configure(highlightbackground="#d9d9d9")
            self.Button6.configure(highlightcolor="black")
            self.Button6.configure(pady="0")
            self.Button6.configure(text='''22''')
    
            self.Button7 = tk.Button(self.Scrolledwindow1)
            self.Button7.place(relx=0.082, rely=0.42, height=33, width=56)
            self.Button7.configure(activebackground="#ececec")
            self.Button7.configure(activeforeground="#000000")
            self.Button7.configure(background="#80ff00")
            self.Button7.configure(disabledforeground="#a3a3a3")
            self.Button7.configure(foreground="#000000")
            self.Button7.configure(highlightbackground="#d9d9d9")
            self.Button7.configure(highlightcolor="black")
            self.Button7.configure(pady="0")
            self.Button7.configure(text='''17''')
    
            self.Button8 = tk.Button(self.Scrolledwindow1)
            self.Button8.place(relx=0.082, rely=0.495, height=33, width=56)
            self.Button8.configure(activebackground="#ececec")
            self.Button8.configure(activeforeground="#000000")
            self.Button8.configure(background="#80ff00")
            self.Button8.configure(disabledforeground="#a3a3a3")
            self.Button8.configure(foreground="#000000")
            self.Button8.configure(highlightbackground="#d9d9d9")
            self.Button8.configure(highlightcolor="black")
            self.Button8.configure(pady="0")
            self.Button8.configure(text='''21''')
    
            self.Button9 = tk.Button(self.Scrolledwindow1)
            self.Button9.place(relx=0.49, rely=0.42, height=33, width=56)
            self.Button9.configure(activebackground="#ececec")
            self.Button9.configure(activeforeground="#000000")
            self.Button9.configure(background="#80ff00")
            self.Button9.configure(disabledforeground="#a3a3a3")
            self.Button9.configure(foreground="#000000")
            self.Button9.configure(highlightbackground="#d9d9d9")
            self.Button9.configure(highlightcolor="black")
            self.Button9.configure(pady="0")
            self.Button9.configure(text='''19''')
    
            self.Button10 = tk.Button(self.Scrolledwindow1)
            self.Button10.place(relx=0.49, rely=0.27, height=33, width=56)
            self.Button10.configure(activebackground="#ececec")
            self.Button10.configure(activeforeground="#000000")
            self.Button10.configure(background="#80ff00")
            self.Button10.configure(disabledforeground="#a3a3a3")
            self.Button10.configure(foreground="#000000")
            self.Button10.configure(highlightbackground="#d9d9d9")
            self.Button10.configure(highlightcolor="black")
            self.Button10.configure(pady="0")
            self.Button10.configure(text='''11''')
    
            self.Button11 = tk.Button(self.Scrolledwindow1)
            self.Button11.place(relx=0.082, rely=0.27, height=33, width=56)
            self.Button11.configure(activebackground="#ececec")
            self.Button11.configure(activeforeground="#000000")
            self.Button11.configure(background="#80ff00")
            self.Button11.configure(disabledforeground="#a3a3a3")
            self.Button11.configure(foreground="#000000")
            self.Button11.configure(highlightbackground="#d9d9d9")
            self.Button11.configure(highlightcolor="black")
            self.Button11.configure(pady="0")
            self.Button11.configure(text='''09''')
    
            self.Button12 = tk.Button(self.Scrolledwindow1)
            self.Button12.place(relx=0.082, rely=0.12, height=33, width=56)
            self.Button12.configure(activebackground="#80ff00")
            self.Button12.configure(activeforeground="#80ff00")
            self.Button12.configure(background="#80ff00")
            self.Button12.configure(disabledforeground="#a3a3a3")
            self.Button12.configure(foreground="#000000")
            self.Button12.configure(highlightbackground="#d9d9d9")
            self.Button12.configure(highlightcolor="black")
            self.Button12.configure(pady="0")
            self.Button12.configure(text='''01''')
    
            self.Button13 = tk.Button(self.Scrolledwindow1)
            self.Button13.place(relx=0.082, rely=0.345, height=33, width=56)
            self.Button13.configure(activebackground="#ececec")
            self.Button13.configure(activeforeground="#000000")
            self.Button13.configure(background="#80ff00")
            self.Button13.configure(disabledforeground="#a3a3a3")
            self.Button13.configure(foreground="#000000")
            self.Button13.configure(highlightbackground="#d9d9d9")
            self.Button13.configure(highlightcolor="black")
            self.Button13.configure(pady="0")
            self.Button13.configure(text='''13''')
    
            self.Button14 = tk.Button(self.Scrolledwindow1)
            self.Button14.place(relx=0.082, rely=0.57, height=33, width=56)
            self.Button14.configure(activebackground="#ececec")
            self.Button14.configure(activeforeground="#000000")
            self.Button14.configure(background="#80ff00")
            self.Button14.configure(disabledforeground="#a3a3a3")
            self.Button14.configure(foreground="#000000")
            self.Button14.configure(highlightbackground="#d9d9d9")
            self.Button14.configure(highlightcolor="black")
            self.Button14.configure(pady="0")
            self.Button14.configure(text='''25''')
    
            self.Button15 = tk.Button(self.Scrolledwindow1)
            self.Button15.place(relx=0.286, rely=0.57, height=33, width=56)
            self.Button15.configure(activebackground="#ececec")
            self.Button15.configure(activeforeground="#000000")
            self.Button15.configure(background="#80ff00")
            self.Button15.configure(disabledforeground="#a3a3a3")
            self.Button15.configure(foreground="#000000")
            self.Button15.configure(highlightbackground="#d9d9d9")
            self.Button15.configure(highlightcolor="black")
            self.Button15.configure(pady="0")
            self.Button15.configure(text='''26''')
    
            self.Button16 = tk.Button(self.Scrolledwindow1)
            self.Button16.place(relx=0.286, rely=0.27, height=33, width=56)
            self.Button16.configure(activebackground="#ececec")
            self.Button16.configure(activeforeground="#000000")
            self.Button16.configure(background="#80ff00")
            self.Button16.configure(disabledforeground="#a3a3a3")
            self.Button16.configure(foreground="#000000")
            self.Button16.configure(highlightbackground="#d9d9d9")
            self.Button16.configure(highlightcolor="black")
            self.Button16.configure(pady="0")
            self.Button16.configure(text='''10''')
    
            self.Button17 = tk.Button(self.Scrolledwindow1)
            self.Button17.place(relx=0.286, rely=0.195, height=33, width=56)
            self.Button17.configure(activebackground="#ececec")
            self.Button17.configure(activeforeground="#000000")
            self.Button17.configure(background="#80ff00")
            self.Button17.configure(disabledforeground="#a3a3a3")
            self.Button17.configure(foreground="#000000")
            self.Button17.configure(highlightbackground="#d9d9d9")
            self.Button17.configure(highlightcolor="black")
            self.Button17.configure(pady="0")
            self.Button17.configure(text='''06''')
    
            self.Button18 = tk.Button(self.Scrolledwindow1)
            self.Button18.place(relx=0.49, rely=0.345, height=33, width=56)
            self.Button18.configure(activebackground="#ececec")
            self.Button18.configure(activeforeground="#000000")
            self.Button18.configure(background="#80ff00")
            self.Button18.configure(disabledforeground="#a3a3a3")
            self.Button18.configure(foreground="#000000")
            self.Button18.configure(highlightbackground="#d9d9d9")
            self.Button18.configure(highlightcolor="black")
            self.Button18.configure(pady="0")
            self.Button18.configure(text='''15''')
    
            self.Button19 = tk.Button(self.Scrolledwindow1)
            self.Button19.place(relx=0.286, rely=0.42, height=33, width=56)
            self.Button19.configure(activebackground="#ececec")
            self.Button19.configure(activeforeground="#000000")
            self.Button19.configure(background="#80ff00")
            self.Button19.configure(disabledforeground="#a3a3a3")
            self.Button19.configure(foreground="#000000")
            self.Button19.configure(highlightbackground="#d9d9d9")
            self.Button19.configure(highlightcolor="black")
            self.Button19.configure(pady="0")
            self.Button19.configure(text='''18''')
    
            self.Button20 = tk.Button(self.Scrolledwindow1)
            self.Button20.place(relx=0.49, rely=0.495, height=33, width=56)
            self.Button20.configure(activebackground="#ececec")
            self.Button20.configure(activeforeground="#000000")
            self.Button20.configure(background="#80ff00")
            self.Button20.configure(disabledforeground="#a3a3a3")
            self.Button20.configure(foreground="#000000")
            self.Button20.configure(highlightbackground="#d9d9d9")
            self.Button20.configure(highlightcolor="black")
            self.Button20.configure(pady="0")
            self.Button20.configure(text='''23''')
    
            self.Button22 = tk.Button(self.Scrolledwindow1)
            self.Button22.place(relx=0.694, rely=0.12, height=33, width=56)
            self.Button22.configure(activebackground="#ececec")
            self.Button22.configure(activeforeground="#000000")
            self.Button22.configure(background="#80ff00")
            self.Button22.configure(disabledforeground="#a3a3a3")
            self.Button22.configure(foreground="#000000")
            self.Button22.configure(highlightbackground="#d9d9d9")
            self.Button22.configure(highlightcolor="black")
            self.Button22.configure(pady="0")
            self.Button22.configure(text='''04''')
    
            self.Button23 = tk.Button(self.Scrolledwindow1)
            self.Button23.place(relx=0.694, rely=0.195, height=33, width=56)
            self.Button23.configure(activebackground="#ececec")
            self.Button23.configure(activeforeground="#000000")
            self.Button23.configure(background="#80ff00")
            self.Button23.configure(disabledforeground="#a3a3a3")
            self.Button23.configure(foreground="#000000")
            self.Button23.configure(highlightbackground="#d9d9d9")
            self.Button23.configure(highlightcolor="black")
            self.Button23.configure(pady="0")
            self.Button23.configure(text='''08''')
    
            self.Button24 = tk.Button(self.Scrolledwindow1)
            self.Button24.place(relx=0.694, rely=0.345, height=33, width=56)
            self.Button24.configure(activebackground="#ececec")
            self.Button24.configure(activeforeground="#000000")
            self.Button24.configure(background="#80ff00")
            self.Button24.configure(disabledforeground="#a3a3a3")
            self.Button24.configure(foreground="#000000")
            self.Button24.configure(highlightbackground="#d9d9d9")
            self.Button24.configure(highlightcolor="black")
            self.Button24.configure(pady="0")
            self.Button24.configure(text='''16''')
    
            self.Button26 = tk.Button(self.Scrolledwindow1)
            self.Button26.place(relx=0.694, rely=0.87, height=33, width=56)
            self.Button26.configure(activebackground="#ececec")
            self.Button26.configure(activeforeground="#000000")
            self.Button26.configure(background="#80ff00")
            self.Button26.configure(disabledforeground="#a3a3a3")
            self.Button26.configure(foreground="#000000")
            self.Button26.configure(highlightbackground="#d9d9d9")
            self.Button26.configure(highlightcolor="black")
            self.Button26.configure(pady="0")
            self.Button26.configure(text='''38''')
    
            self.Button27 = tk.Button(self.Scrolledwindow1)
            self.Button27.place(relx=0.49, rely=0.87, height=33, width=56)
            self.Button27.configure(activebackground="#ececec")
            self.Button27.configure(activeforeground="#000000")
            self.Button27.configure(background="#80ff00")
            self.Button27.configure(disabledforeground="#a3a3a3")
            self.Button27.configure(foreground="#000000")
            self.Button27.configure(highlightbackground="#d9d9d9")
            self.Button27.configure(highlightcolor="black")
            self.Button27.configure(pady="0")
            self.Button27.configure(text='''37''')
    
            self.Button29 = tk.Button(self.Scrolledwindow1)
            self.Button29.place(relx=0.694, rely=0.495, height=33, width=56)
            self.Button29.configure(activebackground="#ececec")
            self.Button29.configure(activeforeground="#000000")
            self.Button29.configure(background="#80ff00")
            self.Button29.configure(disabledforeground="#a3a3a3")
            self.Button29.configure(foreground="#000000")
            self.Button29.configure(highlightbackground="#d9d9d9")
            self.Button29.configure(highlightcolor="black")
            self.Button29.configure(pady="0")
            self.Button29.configure(text='''24''')
    
            self.Button30 = tk.Button(self.Scrolledwindow1)
            self.Button30.place(relx=0.286, rely=0.87, height=33, width=56)
            self.Button30.configure(activebackground="#ececec")
            self.Button30.configure(activeforeground="#000000")
            self.Button30.configure(background="#80ff00")
            self.Button30.configure(disabledforeground="#a3a3a3")
            self.Button30.configure(foreground="#000000")
            self.Button30.configure(highlightbackground="#d9d9d9")
            self.Button30.configure(highlightcolor="black")
            self.Button30.configure(pady="0")
            self.Button30.configure(text='''36''')
    
            self.Button31 = tk.Button(self.Scrolledwindow1)
            self.Button31.place(relx=0.694, rely=0.42, height=33, width=56)
            self.Button31.configure(activebackground="#ececec")
            self.Button31.configure(activeforeground="#000000")
            self.Button31.configure(background="#80ff00")
            self.Button31.configure(disabledforeground="#a3a3a3")
            self.Button31.configure(foreground="#000000")
            self.Button31.configure(highlightbackground="#d9d9d9")
            self.Button31.configure(highlightcolor="black")
            self.Button31.configure(pady="0")
            self.Button31.configure(text='''20''')
    
            self.Button32 = tk.Button(self.Scrolledwindow1)
            self.Button32.place(relx=0.694, rely=0.27, height=33, width=56)
            self.Button32.configure(activebackground="#ececec")
            self.Button32.configure(activeforeground="#000000")
            self.Button32.configure(background="#80ff00")
            self.Button32.configure(disabledforeground="#a3a3a3")
            self.Button32.configure(foreground="#000000")
            self.Button32.configure(highlightbackground="#d9d9d9")
            self.Button32.configure(highlightcolor="black")
            self.Button32.configure(pady="0")
            self.Button32.configure(text='''12''')
    
            self.Button33 = tk.Button(self.Scrolledwindow1)
            self.Button33.place(relx=-0.776, rely=1.229, height=33, width=56)
            self.Button33.configure(activebackground="#ececec")
            self.Button33.configure(activeforeground="#000000")
            self.Button33.configure(background="#d9d9d9")
            self.Button33.configure(disabledforeground="#a3a3a3")
            self.Button33.configure(foreground="#000000")
            self.Button33.configure(highlightbackground="#d9d9d9")
            self.Button33.configure(highlightcolor="black")
            self.Button33.configure(pady="0")
            self.Button33.configure(text='''Button''')
    
            self.Button34 = tk.Button(self.Scrolledwindow1)
            self.Button34.place(relx=0.49, rely=0.72, height=33, width=56)
            self.Button34.configure(activebackground="#ececec")
            self.Button34.configure(activeforeground="#000000")
            self.Button34.configure(background="#80ff00")
            self.Button34.configure(disabledforeground="#a3a3a3")
            self.Button34.configure(foreground="#000000")
            self.Button34.configure(highlightbackground="#d9d9d9")
            self.Button34.configure(highlightcolor="black")
            self.Button34.configure(pady="0")
            self.Button34.configure(text='''29''')
    
            self.Button35 = tk.Button(self.Scrolledwindow1)
            self.Button35.place(relx=0.082, rely=0.87, height=33, width=56)
            self.Button35.configure(activebackground="#ececec")
            self.Button35.configure(activeforeground="#000000")
            self.Button35.configure(background="#80ff00")
            self.Button35.configure(disabledforeground="#a3a3a3")
            self.Button35.configure(foreground="#000000")
            self.Button35.configure(highlightbackground="#d9d9d9")
            self.Button35.configure(highlightcolor="black")
            self.Button35.configure(pady="0")
            self.Button35.configure(text='''35''')
    
            self.Button36 = tk.Button(self.Scrolledwindow1)
            self.Button36.place(relx=0.082, rely=0.795, height=33, width=56)
            self.Button36.configure(activebackground="#ececec")
            self.Button36.configure(activeforeground="#000000")
            self.Button36.configure(background="#80ff00")
            self.Button36.configure(disabledforeground="#a3a3a3")
            self.Button36.configure(foreground="#000000")
            self.Button36.configure(highlightbackground="#d9d9d9")
            self.Button36.configure(highlightcolor="black")
            self.Button36.configure(pady="0")
            self.Button36.configure(text='''31''')
    
            self.Button37 = tk.Button(self.Scrolledwindow1)
            self.Button37.place(relx=0.49, rely=0.795, height=33, width=56)
            self.Button37.configure(activebackground="#ececec")
            self.Button37.configure(activeforeground="#000000")
            self.Button37.configure(background="#80ff00")
            self.Button37.configure(disabledforeground="#a3a3a3")
            self.Button37.configure(foreground="#000000")
            self.Button37.configure(highlightbackground="#d9d9d9")
            self.Button37.configure(highlightcolor="black")
            self.Button37.configure(pady="0")
            self.Button37.configure(text='''33''')
    
            self.Button38 = tk.Button(self.Scrolledwindow1)
            self.Button38.place(relx=0.286, rely=0.795, height=33, width=56)
            self.Button38.configure(activebackground="#ececec")
            self.Button38.configure(activeforeground="#000000")
            self.Button38.configure(background="#80ff00")
            self.Button38.configure(disabledforeground="#a3a3a3")
            self.Button38.configure(foreground="#000000")
            self.Button38.configure(highlightbackground="#d9d9d9")
            self.Button38.configure(highlightcolor="black")
            self.Button38.configure(pady="0")
            self.Button38.configure(text='''32''')
    
            self.Button39 = tk.Button(self.Scrolledwindow1)
            self.Button39.place(relx=0.694, rely=0.795, height=33, width=56)
            self.Button39.configure(activebackground="#ececec")
            self.Button39.configure(activeforeground="#000000")
            self.Button39.configure(background="#80ff00")
            self.Button39.configure(disabledforeground="#a3a3a3")
            self.Button39.configure(foreground="#000000")
            self.Button39.configure(highlightbackground="#d9d9d9")
            self.Button39.configure(highlightcolor="black")
            self.Button39.configure(pady="0")
            self.Button39.configure(text='''34''')
    
            self.Button40 = tk.Button(self.Scrolledwindow1)
            self.Button40.place(relx=0.082, rely=0.72, height=33, width=56)
            self.Button40.configure(activebackground="#ececec")
            self.Button40.configure(activeforeground="#000000")
            self.Button40.configure(background="#80ff00")
            self.Button40.configure(disabledforeground="#a3a3a3")
            self.Button40.configure(foreground="#000000")
            self.Button40.configure(highlightbackground="#d9d9d9")
            self.Button40.configure(highlightcolor="black")
            self.Button40.configure(pady="0")
            self.Button40.configure(text='''27''')
    
            self.Button44 = tk.Button(self.Scrolledwindow1)
            self.Button44.place(relx=0.694, rely=0.72, height=33, width=56)
            self.Button44.configure(activebackground="#ececec")
            self.Button44.configure(activeforeground="#000000")
            self.Button44.configure(background="#80ff00")
            self.Button44.configure(disabledforeground="#a3a3a3")
            self.Button44.configure(foreground="#000000")
            self.Button44.configure(highlightbackground="#d9d9d9")
            self.Button44.configure(highlightcolor="black")
            self.Button44.configure(pady="0")
            self.Button44.configure(text='''30''')
    
            self.Button45 = tk.Button(self.Scrolledwindow1)
            self.Button45.place(relx=0.286, rely=0.72, height=33, width=56)
            self.Button45.configure(activebackground="#ececec")
            self.Button45.configure(activeforeground="#000000")
            self.Button45.configure(background="#80ff00")
            self.Button45.configure(disabledforeground="#a3a3a3")
            self.Button45.configure(foreground="#000000")
            self.Button45.configure(highlightbackground="#d9d9d9")
            self.Button45.configure(highlightcolor="black")
            self.Button45.configure(pady="0")
            self.Button45.configure(text='''28''')
    
            self.Message4 = tk.Message(self.Scrolledwindow1)
            self.Message4.place(relx=0.0, rely=0.0, relheight=0.06, relwidth=0.992)
            self.Message4.configure(background="#ff80ff")
            self.Message4.configure(font="-family {Pristina} -size 21")
            self.Message4.configure(foreground="#000000")
            self.Message4.configure(highlightbackground="#ff80ff")
            self.Message4.configure(highlightcolor="black")
            self.Message4.configure(text='''Question Portal''')
            self.Message4.configure(width=486)
    
            self.Message7 = tk.Message(self.Scrolledwindow1)
            self.Message7.place(relx=0.0, rely=0.63, relheight=0.06, relwidth=0.992)
            self.Message7.configure(background="#ff80ff")
            self.Message7.configure(font="-family {Vivaldi} -size 22 -slant italic")
            self.Message7.configure(foreground="#000000")
            self.Message7.configure(highlightbackground="#ff80ff")
            self.Message7.configure(highlightcolor="black")
            self.Message7.configure(text='''Section 2''')
            self.Message7.configure(width=486)
    
            self.Message8 = tk.Message(self.Scrolledwindow1)
            self.Message8.place(relx=0.0, rely=0.06, relheight=0.051, relwidth=0.994)
    
            self.Message8.configure(background="#ff80ff")
            self.Message8.configure(font="-family {Vivaldi} -size 22 -slant italic")
            self.Message8.configure(foreground="#000000")
            self.Message8.configure(highlightbackground="#d9d9d9")
            self.Message8.configure(highlightcolor="black")
            self.Message8.configure(text='''Section 1''')
            self.Message8.configure(width=487)
    
            self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
            top.configure(menu = self.menubar)
    
            self.Labelframe2 = tk.LabelFrame(top)
            self.Labelframe2.place(relx=0.271, rely=0.01, relheight=0.365
                    , relwidth=0.651)
            self.Labelframe2.configure(relief='groove')
            self.Labelframe2.configure(font="-family {Segoe UI} -size 24")
            self.Labelframe2.configure(foreground="black")
            self.Labelframe2.configure(text='''Question 14''')
            self.Labelframe2.configure(background="#f6f6f6")
            self.Labelframe2.configure(highlightbackground="#d9d9d9")
            self.Labelframe2.configure(highlightcolor="black")
    
            self.Message6 = tk.Message(self.Labelframe2)
            self.Message6.place(relx=0.024, rely=0.192, relheight=0.411
                    , relwidth=0.413, bordermode='ignore')
            self.Message6.configure(background="#f6f6f6")
            self.Message6.configure(font="-family {Segoe UI} -size 12")
            self.Message6.configure(foreground="#000000")
            self.Message6.configure(highlightbackground="#d9d9d9")
            self.Message6.configure(highlightcolor="black")
            self.Message6.configure(text='''Which polymer is known as synthetic wool?''')
            self.Message6.configure(width=516)
    
            self.Checkbutton1 = tk.Checkbutton(top)
            self.Checkbutton1.place(relx=0.286, rely=0.47, relheight=0.084
                    , relwidth=0.076)
            self.Checkbutton1.configure(activebackground="#ffffff")
            self.Checkbutton1.configure(activeforeground="#000000")
            self.Checkbutton1.configure(background="#ffffff")
            self.Checkbutton1.configure(disabledforeground="#a3a3a3")
            self.Checkbutton1.configure(font="-family {Segoe UI} -size 14")
            self.Checkbutton1.configure(foreground="#000000")
            self.Checkbutton1.configure(highlightbackground="#d9d9d9")
            self.Checkbutton1.configure(highlightcolor="black")
            self.Checkbutton1.configure(justify='left')
            self.Checkbutton1.configure(text='''(A) nylon''')
            self.Checkbutton1.configure(variable=exam_.che135)
    
            self.Checkbutton2 = tk.Checkbutton(top)
            self.Checkbutton2.place(relx=0.458, rely=0.49, relheight=0.045
                    , relwidth=0.072)
            self.Checkbutton2.configure(activebackground="#ececec")
            self.Checkbutton2.configure(activeforeground="#000000")
            self.Checkbutton2.configure(background="#ffffff")
            self.Checkbutton2.configure(disabledforeground="#a3a3a3")
            self.Checkbutton2.configure(font="-family {Segoe UI} -size 14")
            self.Checkbutton2.configure(foreground="#000000")
            self.Checkbutton2.configure(highlightbackground="#d9d9d9")
            self.Checkbutton2.configure(highlightcolor="black")
            self.Checkbutton2.configure(justify='left')
            self.Checkbutton2.configure(text='''(B) acrylic''')
            self.Checkbutton2.configure(variable=exam_.che136)
    
            self.Checkbutton3 = tk.Checkbutton(top)
            self.Checkbutton3.place(relx=0.292, rely=0.579, relheight=0.061
                    , relwidth=0.087)
            self.Checkbutton3.configure(activebackground="#ececec")
            self.Checkbutton3.configure(activeforeground="#000000")
            self.Checkbutton3.configure(background="#ffffff")
            self.Checkbutton3.configure(disabledforeground="#a3a3a3")
            self.Checkbutton3.configure(font="-family {Segoe UI} -size 14")
            self.Checkbutton3.configure(foreground="#000000")
            self.Checkbutton3.configure(highlightbackground="#d9d9d9")
            self.Checkbutton3.configure(highlightcolor="black")
            self.Checkbutton3.configure(justify='left')
            self.Checkbutton3.configure(text='''(C) polyester''')
            self.Checkbutton3.configure(variable=exam_.che137)
    
            self.Checkbutton4 = tk.Checkbutton(top)
            self.Checkbutton4.place(relx=0.448, rely=0.579, relheight=0.061
                    , relwidth=0.097)
            self.Checkbutton4.configure(activebackground="#ececec")
            self.Checkbutton4.configure(activeforeground="#000000")
            self.Checkbutton4.configure(background="#ffffff")
            self.Checkbutton4.configure(disabledforeground="#a3a3a3")
            self.Checkbutton4.configure(font="-family {Segoe UI} -size 14")
            self.Checkbutton4.configure(foreground="#000000")
            self.Checkbutton4.configure(highlightbackground="#d9d9d9")
            self.Checkbutton4.configure(highlightcolor="black")
            self.Checkbutton4.configure(justify='left')
            self.Checkbutton4.configure(text='''(D) bakelite''')
            self.Checkbutton4.configure(variable=exam_.che138)
    
            self.Button21 = tk.Button(top)
            self.Button21.place(relx=0.375, rely=0.869, height=73, width=106)
            self.Button21.configure(activebackground="#ececec")
            self.Button21.configure(activeforeground="#000000")
            self.Button21.configure(background="#80ff00")
            self.Button21.configure(disabledforeground="#a3a3a3")
            self.Button21.configure(foreground="#000000")
            self.Button21.configure(highlightbackground="#d9d9d9")
            self.Button21.configure(highlightcolor="black")
            self.Button21.configure(pady="0")
            self.Button21.configure(text='''Save and Next''')
    
            self.Button28 = tk.Button(top)
            self.Button28.place(relx=0.297, rely=0.869, height=73, width=106)
            self.Button28.configure(activebackground="#ececec")
            self.Button28.configure(activeforeground="#000000")
            self.Button28.configure(background="#80ff00")
            self.Button28.configure(disabledforeground="#a3a3a3")
            self.Button28.configure(font="-family {Segoe UI} -size 13")
            self.Button28.configure(foreground="#000000")
            self.Button28.configure(highlightbackground="#d9d9d9")
            self.Button28.configure(highlightcolor="black")
            self.Button28.configure(pady="0")
            self.Button28.configure(text='''Previous''')
    
            self.Labelframe3 = tk.LabelFrame(top)
            self.Labelframe3.place(relx=0.693, rely=0.559, relheight=0.365
                    , relwidth=0.27)
            self.Labelframe3.configure(relief='groove')
            self.Labelframe3.configure(font="-family {Segoe UI} -size 24")
            self.Labelframe3.configure(foreground="black")
            self.Labelframe3.configure(text='''Candidate''')
            self.Labelframe3.configure(background="#f3f3f3")
            self.Labelframe3.configure(highlightbackground="#d9d9d9")
            self.Labelframe3.configure(highlightcolor="black")
    
            self.style.map('TCheckbutton',background=
                [('selected', _bgcolor), ('active', _ana2color)])
            self.TCheckbutton1 = ttk.Checkbutton(top)
            self.TCheckbutton1.place(relx=0.859, rely=0.04, relwidth=0.052
                    , relheight=0.0, height=26)
            self.TCheckbutton1.configure(variable=exam_.tch145)
            self.TCheckbutton1.configure(takefocus="")
            self.TCheckbutton1.configure(text='''Auto next''')
    
            self.Button25 = tk.Button(top)
            self.Button25.place(relx=0.448, rely=0.889, height=53, width=146)
            self.Button25.configure(activebackground="#ececec")
            self.Button25.configure(activeforeground="#000000")
            self.Button25.configure(background="#ff0000")
            self.Button25.configure(disabledforeground="#a3a3a3")
            self.Button25.configure(foreground="#000000")
            self.Button25.configure(highlightbackground="#d9d9d9")
            self.Button25.configure(highlightcolor="black")
            self.Button25.configure(pady="0")
            self.Button25.configure(text='''Submit''')
    
    # The following code is added to facilitate the Scrolled widgets you specified.
    class AutoScroll(object):
        '''Configure the scrollbars for a widget.'''
        def __init__(self, master):
            #  Added the try-except clauses so that this class
            #  could be used for scrolled entry widget for which vertical
            #  scrolling is not supported.
            try:
                vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
            except:
                pass
            hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)
            try:
                self.configure(yscrollcommand=self._autoscroll(vsb))
            except:
                pass
            self.configure(xscrollcommand=self._autoscroll(hsb))
            self.grid(column=0, row=0, sticky='nsew')
            try:
                vsb.grid(column=1, row=0, sticky='ns')
            except:
                pass
            hsb.grid(column=0, row=1, sticky='ew')
            master.grid_columnconfigure(0, weight=1)
            master.grid_rowconfigure(0, weight=1)
            # Copy geometry methods of master  (taken from ScrolledText.py)
            if py3:
                methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                      | tk.Place.__dict__.keys()
            else:
                methods = tk.Pack.__dict__.keys() + tk.Grid.__dict__.keys() \
                      + tk.Place.__dict__.keys()
            for meth in methods:
                if meth[0] != '_' and meth not in ('config', 'configure'):
                    setattr(self, meth, getattr(master, meth))
    
        @staticmethod
        def _autoscroll(sbar):
            '''Hide and show scrollbar as needed.'''
            def wrapped(first, last):
                first, last = float(first), float(last)
                if first <= 0 and last >= 1:
                    sbar.grid_remove()
                else:
                    sbar.grid()
                sbar.set(first, last)
            return wrapped
    
        def __str__(self):
            return str(self.master)
    
    def _create_container(func):
        '''Creates a ttk Frame with a given master, and use this new frame to
        place the scrollbars and the widget.'''
        def wrapped(cls, master, **kw):
            container = ttk.Frame(master)
            container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
            container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
            return func(cls, container, **kw)
        return wrapped
    
    class ScrolledWindow(AutoScroll, tk.Canvas):
        '''A standard Tkinter Canvas widget with scrollbars that will
        automatically show/hide as needed.'''
        @_create_container
        def __init__(self, master, **kw):
            tk.Canvas.__init__(self, master, **kw)
            AutoScroll.__init__(self, master)
    
    import platform
    def _bound_to_mousewheel(event, widget):
        child = widget.winfo_children()[0]
        if platform.system() == 'Windows' or platform.system() == 'Darwin':
            child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
            child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
        else:
            child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
            child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
            child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
            child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))
    
    def _unbound_to_mousewheel(event, widget):
        if platform.system() == 'Windows' or platform.system() == 'Darwin':
            widget.unbind_all('<MouseWheel>')
            widget.unbind_all('<Shift-MouseWheel>')
        else:
            widget.unbind_all('<Button-4>')
            widget.unbind_all('<Button-5>')
            widget.unbind_all('<Shift-Button-4>')
            widget.unbind_all('<Shift-Button-5>')
    
    def _on_mousewheel(event, widget):
        if platform.system() == 'Windows':
            widget.yview_scroll(-1*int(event.delta/120),'units')
        elif platform.system() == 'Darwin':
            widget.yview_scroll(-1*int(event.delta),'units')
        else:
            if event.num == 4:
                widget.yview_scroll(-1, 'units')
            elif event.num == 5:
                widget.yview_scroll(1, 'units')
    
    def _on_shiftmouse(event, widget):
        if platform.system() == 'Windows':
            widget.xview_scroll(-1*int(event.delta/120), 'units')
        elif platform.system() == 'Darwin':
            widget.xview_scroll(-1*int(event.delta), 'units')
        else:
            if event.num == 4:
                widget.xview_scroll(-1, 'units')
            elif event.num == 5:
                widget.xview_scroll(1, 'units')
    
    vp_start_gui()
    
