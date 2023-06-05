from tkinter import *
import sympy as sp
import numpy as np
import math


class Calc(Tk):
    def __init__(self):
        super().__init__()
        self.title("Complex Calculator")
        self.geometry('700x700+500+50')

    def sum(self):
        self._sum = Button(self, text="z1 + z2", font=30, bd=5)
        self._sum.bind('<Button-1>', self.sum_window)
        self._sum.grid(row=0, column=0, ipady=30, ipadx=30)

    def sub(self):
        self._sum = Button(self, text="z1 - z2", font=30, bd=5)
        self._sum.bind('<Button-1>', self.sub_window)
        self._sum.grid(row=0, column=1, ipady=30, ipadx=30)

    def product(self):
        self._product = Button(self, text="z1 * z2", font=30, bd=5)
        self._product.bind('<Button-1>', self.product_window)
        self._product.grid(row=1, column=0, ipady=30, ipadx=30)

    def div(self):
        self._div = Button(self, text="z1 / z2", font=30, bd=5)
        self._div.bind('<Button-1>', self.div_window)
        self._div.grid(row=1, column=1, ipady=30, ipadx=30)

    def module(self):
        self._module = Button(self, text="|z|", font=40, bd=5)
        self._module.bind('<Button-1>', self.module_window)
        self._module.grid(row=2, column=0, ipady=30, ipadx=30)

    def argument(self):
        self._argument = Button(self, text="Arg(z)", font=40, bd=5)
        self._argument.bind('<Button-1>', self.argument_window)
        self._argument.grid(row=2, column=1, ipady=30, ipadx=30)

    def root(self):
        self._root = Button(self, text=" N'th Root ", font=40, bd=5)
        self._root.bind('<Button-1>', self.root_window)
        self._root.grid(row=2, column=3, ipady=30, ipadx=30)

    def trig(self):
        self._trig = Button(self, text="Trig Form", font=40, bd=5)
        self._trig.bind('<Button-1>', self.trig_window)
        self._trig.grid(row=2, column=2, ipady=30, ipadx=30)

    def conj(self):
        self._conj = Button(self, text="z̄", font=40, bd=5)
        self._conj.bind('<Button-1>', self.conj_window)
        self._conj.grid(row=0, column=2, ipady=30, ipadx=30)

    def func(self):
        self._func = Button(self, text="f(z)", font=30, bd=5)
        self._func.bind('<Button-1>', self.func_window)
        self._func.grid(row=3, column=0, ipady=30, ipadx=30)

    def analytic(self):
        self._an = Button(self, text="f(z) analytic", font=30, bd=5)
        self._an.bind('<Button-1>', self.analytic_window)
        self._an.grid(row=3, column=1, ipady=30, ipadx=30)
        Label(self, text="ℂomplex ℂalculator", font=('Latin Modern', 30,'italic')).place(x=300, y=600)
        Label(self, text="by Ibragim Aldiar", font=('Latin Modern', 10, 'italic')).place(x=300, y=645)
        Label(self, text="(use j instead of i and real numbers for x,y // example: 1+1j)", font=('Latin Modern', 10, 'italic')).place(x=300, y=100)
        Label(self, text="(for functions use x,y form // example: (x+j*y)**2", font=('Latin Modern', 10, 'italic')).place(x=300, y=350)

    def sin(self):
        self._sin = Button(self, text="sin(z)", font=30, bd=5)
        self._sin.bind('<Button-1>', self.sin_window)
        self._sin.grid(row=4, column=0, ipady=30, ipadx=30)

    def cos(self):
        self._cos = Button(self, text="cos(z)", font=30, bd=5)
        self._cos.bind('<Button-1>', self.cos_window)
        self._cos.grid(row=4, column=1, ipady=30, ipadx=30)

    def tan(self):
        self._tan = Button(self, text="tan(z)", font=30, bd=5)
        self._tan.bind('<Button-1>', self.tan_window)
        self._tan.grid(row=4, column=2, ipady=30, ipadx=30)

    def cot(self):
        self._cot = Button(self, text="cot(z)", font=30, bd=5)
        self._cot.bind('<Button-1>', self.cot_window)
        self._cot.grid(row=4, column=3, ipady=30, ipadx=30)

    def sinh(self):
        self._sinh = Button(self, text="sinh(z)", font=30, bd=5)
        self._sinh.bind('<Button-1>', self.sinh_window)
        self._sinh.grid(row=5, column=0, ipady=30, ipadx=30)

    def cosh(self):
        self._cosh = Button(self, text="cosh(z)", font=30, bd=5)
        self._cosh.bind('<Button-1>', self.cosh_window)
        self._cosh.grid(row=5, column=1, ipady=30, ipadx=30)

    def sum_enter(self, event):
        self.res.delete(0, 'end')
        self.c1 = self.e.get()
        self.c1 = self.c1.replace(" ", "")
        self.c2 = self.e2.get()
        self.c2 = self.c2.replace(" ", "")
        res = complex(self.c1) + complex(self.c2)
        self.res.insert(0, res)

    def prod_enter(self, event):
        self.res.delete(0, 'end')
        self.c1 = self.e.get()
        self.c1 = self.c1.replace(" ", "")
        self.c2 = self.e2.get()
        self.c2 = self.c2.replace(" ", "")
        res = complex(self.c1) * complex(self.c2)
        self.res.insert(0, res)

    def div_enter(self, event):
        self.res.delete(0, 'end')
        self.c1 = self.e.get()
        self.c1 = self.c1.replace(" ", "")
        self.c2 = self.e2.get()
        self.c2 = self.c2.replace(" ", "")
        res = complex(self.c1) / complex(self.c2)
        self.res.insert(0, res)

    def sub_enter(self, event):
        self.res.delete(0, 'end')
        self.c1 = self.e.get()
        self.c1 = self.c1.replace(" ", "")
        self.c2 = self.e2.get()
        self.c2 = self.c2.replace(" ", "")
        res = complex(self.c1) - complex(self.c2)
        self.res.insert(0, res)

    def mod_enter(self, event):
        self.res.delete(0, 'end')
        self.c1 = self.e.get()
        self.c1 = self.c1.replace(" ", "")
        z = complex(self.c1)
        res = sp.sqrt(int(z.real ** 2 + z.imag ** 2))
        print(res)
        self.res.insert(0, res)

    def conj_enter(self, event):
        self.res.delete(0, 'end')
        self.c1 = self.e.get()
        self.c1 = self.c1.replace(" ", "")
        z = complex(self.c1)
        c = z.conjugate()
        if z.imag < 0:
            self.res.insert(0, c)
        else:
            self.res.insert(0, c)

    def arg(self, z):
        if z.real > 0:
            self.arg_z = math.atan(z.imag / z.real)
            self.arg_z = math.degrees(self.arg_z)

        elif z.real < 0 and z.imag >= 0:
            self.arg_z = math.degrees(math.atan(z.imag / z.real)) + math.degrees(math.pi)

        elif z.real < 0 and z.imag < 0:
            self.arg_z = math.degrees(math.atan(z.imag / z.real)) - math.degrees(math.pi)

        elif z.real == 0 and z.imag > 0:
            self.arg_z = 90

        elif z.real == 0 and z.imag < 0:
            self.arg_z = -90

        return self.arg_z

    def arg_enter(self, event):
        self.res.delete(0, 'end')
        self.c1 = self.e.get()
        self.c1 = self.c1.replace(" ", "")
        z = complex(self.c1)
        self.res.insert(0, f"{self.arg(z)}° + 2πk")

    def trig_enter(self, event):
        self.res.delete(0, 'end')
        self.c1 = self.e.get()
        self.c1 = self.c1.replace(" ", "")
        z = complex(self.c1)
        mod_z = sp.sqrt(int(z.real ** 2 + z.imag ** 2))
        arg_z = round(self.arg(z), 2)
        self.res.insert(0, f'{mod_z}(cos({arg_z}) + isin({arg_z})')

    def root_enter(self, event):
        self.res.delete(0, 'end')
        self.c1 = self.e.get()
        self.c1 = self.c1.replace(" ", "")
        n = self.e2.get()
        z = complex(self.c1)
        mod_z = (sp.sqrt(int(z.real ** 2 + z.imag ** 2)))
        arg_z = round(self.arg(z), 2)
        self.res.insert(0, f'{mod_z}**1/{n}(cos({arg_z}+2πk / {n}) + isin({arg_z}+2πk / {n})')

    def func_enter(self, event):
        self.res.delete(0, 'end')
        self.reals.delete(0, 'end')
        self.ims.delete(0, 'end')
        self.c1 = self.e.get()
        # f = (x+ i*y)**3 - i*(x- i*y)
        f = self.e.get().replace('j', f'{sp.I}')
        f = sp.simplify(f)
        print(sp.simplify(f))
        f = sp.expand(f)
        print(sp.expand(f))
        s = str(f)
        imag = []
        real = []
        split = s.split()
        for i in split:
            if 'I*' in i:
                a = i.replace('I*', '')
                if i == split[0]:
                    imag.append(a)
                else:
                    imag.append(split[split.index(i) - 1] + a)
            elif i not in '+-*/':
                if i == split[0]:
                    real.append(i)
                else:
                    real.append(split[split.index(i) - 1] + i)
        print('real:', real, 'imag:', imag)

        self.res.insert(0, f)
        self.reals.insert(0, real)
        self.ims.insert(0, imag)

    def analytic_enter(self, event):
        self.dudx.delete(0, 'end')
        self.dvdy.delete(0, 'end')
        self.dudy.delete(0, 'end')
        self.dvdx.delete(0, 'end')
        x, y = sp.symbols('x y')
        # f = (x+ i*y)**3 - i*(x- i*y)
        f = self.e.get().replace('j', f'{sp.I}')
        f = sp.simplify(f)
        print(sp.simplify(f))
        f = sp.expand(f)
        print(sp.expand(f))
        s = str(f)
        imag = []
        real = []
        split = s.split()
        for i in split:
            if 'I*' in i:
                a = i.replace('I*', '')
                if i == split[0]:
                    imag.append(a)
                else:
                    imag.append(split[split.index(i) - 1] + a)
            elif i not in '+-*/':
                if i == split[0]:
                    real.append(i)
                else:
                    real.append(split[split.index(i) - 1] + i)
        print('real:', real, 'imag:', imag)
        U = ''.join(real)
        V = ''.join(imag)
        print('real:', U, 'imag:', V)

        try:
            dudx = sp.diff(U, x)
            self.dudx.insert(0, dudx)
        except Exception as e:
            print(e)

        try:
            dvdy = sp.diff(V, y)
            self.dvdy.insert(0, dvdy)
        except Exception as e:
            print(e)

        try:
            dudy = sp.diff(U, y)
            self.dudy.insert(0, dudy)
        except Exception as e:
            print(e)

        try:
            dvdx = sp.diff(V, x)
            self.dvdx.insert(0, dvdx)
        except Exception as e:
            print(e)
        try:
            if dudx == dvdy and dudy == -1 * dvdx:
                Label(self.w, text="FUNCTION IS ANALYTIC ", font=20).place(x=250, y=600)

            else:
                Label(self.w, text="FUNCTION IS NOT ANALYTIC", font=20).place(x=250, y=600)
        except Exception as e:
            print(e)
            Label(self.w, text="FUNCTION IS NOT ANALYTIC", font=20).place(x=250, y=600)

    def sin_enter(self, event):
        self.res.delete(0, 'end')
        self.c1 = self.e.get()
        self.c1 = self.c1.replace(" ", "")
        z = complex(self.c1)
        r = np.sin(z.real) * np.cosh(z.imag)
        im = np.cos(z.real) * np.sinh(z.imag)
        if im < 0:
            self.res.insert(0, f'{r}{im}j')
        else:
            self.res.insert(0, f'{r}+{im}j')

    def cos_enter(self, event):
        self.res.delete(0, 'end')
        self.c1 = self.e.get()
        self.c1 = self.c1.replace(" ", "")
        z = complex(self.c1)
        r = np.cos(z.real) * np.cosh(z.imag)
        im = np.sin(z.real) * np.sinh(z.imag)
        if im < 0:
            self.res.insert(0, f'{r}+{im}j')
        else:
            self.res.insert(0, f'{r}-{im}j')

    def tan_enter(self, event):
        self.res.delete(0, 'end')
        self.c1 = self.e.get()
        self.c1 = self.c1.replace(" ", "")
        z = complex(self.c1)
        r1 = np.sin(z.real) * np.cosh(z.imag)
        im1 = np.cos(z.real) * np.sinh(z.imag)

        r2 = np.cos(z.real) * np.cosh(z.imag)
        im2 = np.sin(z.real) * np.sinh(z.imag)

        c = complex(r1, im1) / complex(r2, -1 * im2)
        if c.imag < 0:
            self.res.insert(0, f'{c.real}{c.imag}j')
        else:
            self.res.insert(0, f'{c.real}+{c.imag}j')

    def cot_enter(self, event):
        self.res.delete(0, 'end')
        self.c1 = self.e.get()
        self.c1 = self.c1.replace(" ", "")
        z = complex(self.c1)
        r1 = np.sin(z.real) * np.cosh(z.imag)
        im1 = np.cos(z.real) * np.sinh(z.imag)

        r2 = np.cos(z.real) * np.cosh(z.imag)
        im2 = np.sin(z.real) * np.sinh(z.imag)

        c = complex(r2, -1 * im2) / complex(r1, -im1)
        if c.imag < 0:
            self.res.insert(0, f'{c.real}{c.imag}j')
        else:
            self.res.insert(0, f'{c.real}+{c.imag}j')

    def sinh_enter(self, event):
        self.res.delete(0, 'end')
        self.c1 = self.e.get()
        self.c1 = self.c1.replace(" ", "")
        z = complex(self.c1)
        r = np.sinh(z.real) * np.cos(z.imag)
        im = np.cosh(z.real) * np.sin(z.imag)

        if im < 0:
            self.res.insert(0, f'{r}{im}j')
        else:
            self.res.insert(0, f'{r}+{im}j')

    def cosh_enter(self, event):
        self.res.delete(0, 'end')
        self.c1 = self.e.get()
        self.c1 = self.c1.replace(" ", "")
        z = complex(self.c1)
        r = np.cosh(z.real) * np.cos(z.imag)
        im = np.sinh(z.real) * np.sin(z.imag)

        if im < 0:
            self.res.insert(0, f'{r}{im}j')
        else:
            self.res.insert(0, f'{r}+{im}j')

    def sum_window(self, event):
        self.w = Toplevel()
        self.w.geometry('700x700+500+50')
        sum_img = PhotoImage(file="images/sum.png")
        Label(self.w, image=sum_img).place(x=150, y=200)
        self.l = Label(self.w, text="Complex Number 1", font=20)
        self.l.pack()  # side=LEFT
        self.e = Entry(self.w, bd=5, font=20)
        self.e.pack()  # )
        Label(self.w, text="Complex Number 2", font=20).pack()
        self.e2 = Entry(self.w, bd=5, font=20)
        self.e2.pack()
        Label(self.w, text="Result: ", font=20).place(x=250, y=270)
        self.res = Entry(self.w, bd=5, font=20)
        self.res.place(x=250, y=300)
        self.Enter = Button(self.w, text="ENTER", bd=5)
        self.Enter.bind('<Button-1>', self.sum_enter)
        self.Enter.pack()
        self.w.mainloop()

    def sub_window(self, event):
        self.w = Toplevel()
        self.w.geometry('700x700+500+50')
        sum_img = PhotoImage(file="images/sub.png")
        Label(self.w, image=sum_img).place(x=150, y=200)
        self.l = Label(self.w, text="Complex Number 1", font=20)
        self.l.pack()  # side=LEFT
        self.e = Entry(self.w, bd=5, font=20)
        self.e.pack()  # )
        Label(self.w, text="Complex Number 2", font=20).pack()
        self.e2 = Entry(self.w, bd=5, font=20)
        self.e2.pack()
        Label(self.w, text="Result: ", font=20).place(x=250, y=270)
        self.res = Entry(self.w, bd=5, font=20)
        self.res.place(x=250, y=300)
        self.Enter = Button(self.w, text="ENTER", bd=5)
        self.Enter.bind('<Button-1>', self.sub_enter)
        self.Enter.pack()
        self.w.mainloop()

    def conj_window(self, event):
        self.w = Toplevel()
        self.w.geometry('700x700+500+50')
        sum_img = PhotoImage(file="images/conj.png")
        Label(self.w, image=sum_img).place(x=250, y=200)
        self.l = Label(self.w, text="Complex Number ", font=20)
        self.l.pack()  # side=LEFT
        self.e = Entry(self.w, bd=5, font=20)
        self.e.pack()  # )
        Label(self.w, text="Result: ", font=20).place(x=250, y=270)
        self.res = Entry(self.w, bd=5, font=20)
        self.res.place(x=250, y=300)
        self.Enter = Button(self.w, text="ENTER", bd=5)
        self.Enter.bind('<Button-1>', self.conj_enter)
        self.Enter.pack()
        self.w.mainloop()

    def product_window(self, event):
        self.w = Toplevel()
        self.w.geometry('700x700+500+50')
        sum_img = PhotoImage(file="images/prod.png")
        Label(self.w, image=sum_img).place(x=130, y=200)
        self.l = Label(self.w, text="Complex Number 1", font=20)
        self.l.pack()  # side=LEFT
        self.e = Entry(self.w, bd=5, font=20)
        self.e.pack()  # )
        Label(self.w, text="Complex Number 2", font=20).pack()
        self.e2 = Entry(self.w, bd=5, font=20)
        self.e2.pack()
        Label(self.w, text="Result: ", font=20).place(x=250, y=270)
        self.res = Entry(self.w, bd=5, font=20)
        self.res.place(x=250, y=300)
        self.Enter = Button(self.w, text="ENTER", bd=5)
        self.Enter.bind('<Button-1>', self.prod_enter)
        self.Enter.pack()
        self.w.mainloop()

    def div_window(self, event):
        self.w = Toplevel()
        self.w.geometry('700x700+500+50')
        sum_img = PhotoImage(file="images/div.png")
        Label(self.w, image=sum_img).place(x=250, y=170)
        self.l = Label(self.w, text="Complex Number 2", font=20)
        self.l.pack()  # side=LEFT
        self.e = Entry(self.w, bd=5, font=20)
        self.e.pack()  # )
        Label(self.w, text="Complex Number 1", font=20).pack()
        self.e2 = Entry(self.w, bd=5, font=20)
        self.e2.pack()
        Label(self.w, text="Result: ", font=20).place(x=250, y=270)
        self.res = Entry(self.w, bd=5, font=20)
        self.res.place(x=250, y=300)
        self.Enter = Button(self.w, text="ENTER", bd=5)
        self.Enter.bind('<Button-1>', self.div_enter)
        self.Enter.pack()
        self.w.mainloop()

    def module_window(self, event):
        self.w = Toplevel()
        self.w.geometry('700x700+500+50')
        sum_img = PhotoImage(file="images/mod.png")
        Label(self.w, image=sum_img).place(x=230, y=170)
        self.l = Label(self.w, text="Complex Number", font=20)
        self.l.pack()  # side=LEFT
        self.e = Entry(self.w, bd=5, font=20)
        self.e.pack()
        Label(self.w, text="Result: ", font=20).place(x=250, y=270)
        self.res = Entry(self.w, bd=5, font=20)
        self.res.place(x=250, y=300)
        self.Enter = Button(self.w, text="ENTER", bd=5)
        self.Enter.bind('<Button-1>', self.mod_enter)
        self.Enter.pack()
        self.w.mainloop()

    def argument_window(self, event):
        self.w = Toplevel()
        self.w.geometry('700x700+500+50')
        sum_img = PhotoImage(file="images/arg1.PNG")
        sum_img2 = PhotoImage(file="images/arg2.PNG")
        Label(self.w, image=sum_img).place(x=150, y=170)
        Label(self.w, image=sum_img2).place(x=150, y=400)
        self.l = Label(self.w, text="Complex Number", font=20)
        self.l.pack()  # side=LEFT
        self.e = Entry(self.w, bd=5, font=20)
        self.e.pack()
        Label(self.w, text="Result: ", font=20).place(x=250, y=270)
        self.res = Entry(self.w, bd=5, font=20)
        self.res.place(x=250, y=300)
        self.Enter = Button(self.w, text="ENTER", bd=5)
        self.Enter.bind('<Button-1>', self.arg_enter)
        self.Enter.pack()
        self.w.mainloop()

    def root_window(self, event):
        self.w = Toplevel()
        self.w.geometry('700x700+500+50')
        sum_img = PhotoImage(file="images/root.png")
        Label(self.w, image=sum_img).place(x=60, y=160)
        self.l = Label(self.w, text="Complex Number", font=20)
        self.l.pack()
        self.e = Entry(self.w, bd=5, font=20)
        self.e.pack()
        Label(self.w, text="N", font=20).pack()
        self.e2 = Entry(self.w, bd=5, font=20)
        self.e2.pack()
        Label(self.w, text="Result: ", font=20).place(x=250, y=270)
        self.res = Entry(self.w, bd=5, font=20)
        self.res.place(x=200, y=300, height=60, width=400)
        self.Enter = Button(self.w, text="ENTER", bd=5)
        self.Enter.bind('<Button-1>', self.root_enter)
        self.Enter.pack()
        self.w.mainloop()

    def trig_window(self, event):
        self.w = Toplevel()
        self.w.geometry('700x700+500+50')
        sum_img = PhotoImage(file="images/trig.png")
        Label(self.w, image=sum_img).place(x=170, y=170)
        self.l = Label(self.w, text="Complex Number", font=20)
        self.l.pack()  # side=LEFT
        self.e = Entry(self.w, bd=5, font=20)
        self.e.pack()
        Label(self.w, text="Result: ", font=20).place(x=250, y=270)
        self.res = Entry(self.w, bd=5, font=20)
        self.res.place(x=200, y=300, height=50, width=300)
        self.Enter = Button(self.w, text="ENTER", bd=5)
        self.Enter.bind('<Button-1>', self.trig_enter)
        self.Enter.pack()
        self.w.mainloop()

    def func_window(self, event):
        self.w = Toplevel()
        self.w.geometry('700x700+500+50')
        self.l = Label(self.w, text="Complex Function", font=20)
        self.l.pack()
        self.e = Entry(self.w, bd=5, font=20)
        self.e.pack()
        Label(self.w, text="Result: ", font=20).place(x=250, y=270)
        self.res = Entry(self.w, bd=5, font=20)
        self.res.place(x=200, y=300, height=50, width=300)
        self.Enter = Button(self.w, text="ENTER", bd=5)
        Label(self.w, text="Real part: ", font=20).place(x=250, y=370)
        self.reals = Entry(self.w, bd=5, font=20)
        self.reals.place(x=200, y=400, height=50, width=300)
        Label(self.w, text="Imaginary part: ", font=20).place(x=250, y=470)
        self.ims = Entry(self.w, bd=5, font=20)
        self.ims.place(x=200, y=500, height=50, width=300)
        self.Enter.bind('<Button-1>', self.func_enter)
        self.Enter.pack()
        self.w.mainloop()

    def analytic_window(self, event):
        self.w = Toplevel()
        self.w.geometry('700x700+500+50')
        sum_img = PhotoImage(file="images/analytic.PNG")
        Label(self.w, image=sum_img).place(x=170, y=90)
        self.l = Label(self.w, text="Complex Function", font=20)
        self.l.pack()
        self.e = Entry(self.w, bd=5, font=20)
        self.e.pack()

        Label(self.w, text="∂u/∂x: ", font=20).place(x=250, y=170)
        self.dudx = Entry(self.w, bd=5, font=20)
        self.dudx.place(x=200, y=200, height=50, width=300)

        self.Enter = Button(self.w, text="ENTER", bd=5)

        Label(self.w, text="∂v/∂y: ", font=20).place(x=250, y=270)
        self.dvdy = Entry(self.w, bd=5, font=20)
        self.dvdy.place(x=200, y=300, height=50, width=300)

        Label(self.w, text="∂u/dy: ", font=20).place(x=250, y=370)
        self.dudy = Entry(self.w, bd=5, font=20)
        self.dudy.place(x=200, y=400, height=50, width=300)

        Label(self.w, text="∂v/∂x: ", font=20).place(x=250, y=470)
        self.dvdx = Entry(self.w, bd=5, font=20)
        self.dvdx.place(x=200, y=500, height=50, width=300)

        self.Enter.bind('<Button-1>', self.analytic_enter)
        self.Enter.pack()
        self.w.mainloop()

    def sin_window(self, event):
        self.w = Toplevel()
        self.w.geometry('700x700+500+50')
        sum_img = PhotoImage(file="images/sin.png")
        Label(self.w, image=sum_img).place(x=20, y=160)
        self.l = Label(self.w, text="Complex Number", font=20)
        self.l.pack()
        self.e = Entry(self.w, bd=5, font=20)
        self.e.pack()
        Label(self.w, text="Result: ", font=20).place(x=250, y=270)
        self.res = Entry(self.w, bd=5, font=20)
        self.res.place(x=100, y=300, height=50, width=500)
        self.Enter = Button(self.w, text="ENTER", bd=5)

        self.Enter.bind('<Button-1>', self.sin_enter)
        self.Enter.pack()
        self.w.mainloop()

    def cos_window(self, event):
        self.w = Toplevel()
        self.w.geometry('700x700+500+50')
        sum_img = PhotoImage(file="images/cos.png")
        Label(self.w, image=sum_img).place(x=20, y=160)
        self.l = Label(self.w, text="Complex Number", font=20)
        self.l.pack()
        self.e = Entry(self.w, bd=5, font=20)
        self.e.pack()
        Label(self.w, text="Result: ", font=20).place(x=250, y=270)
        self.res = Entry(self.w, bd=5, font=20)
        self.res.place(x=100, y=300, height=50, width=500)
        self.Enter = Button(self.w, text="ENTER", bd=5)

        self.Enter.bind('<Button-1>', self.cos_enter)
        self.Enter.pack()
        self.w.mainloop()

    def tan_window(self, event):
        self.w = Toplevel()
        self.w.geometry('700x700+500+50')
        sum_img = PhotoImage(file="images/tan.png")
        Label(self.w, image=sum_img).place(x=170, y=160)
        self.l = Label(self.w, text="Complex Number", font=20)
        self.l.pack()
        self.e = Entry(self.w, bd=5, font=20)
        self.e.pack()
        Label(self.w, text="Result: ", font=20).place(x=250, y=270)
        self.res = Entry(self.w, bd=5, font=20)
        self.res.place(x=100, y=300, height=50, width=500)
        self.Enter = Button(self.w, text="ENTER", bd=5)

        self.Enter.bind('<Button-1>', self.tan_enter)
        self.Enter.pack()
        self.w.mainloop()

    def cot_window(self, event):
        self.w = Toplevel()
        self.w.geometry('700x700+500+50')
        sum_img = PhotoImage(file="images/cot.png")
        Label(self.w, image=sum_img).place(x=170, y=160)
        self.l = Label(self.w, text="Complex Number", font=20)
        self.l.pack()
        self.e = Entry(self.w, bd=5, font=20)
        self.e.pack()
        Label(self.w, text="Result: ", font=20).place(x=250, y=270)
        self.res = Entry(self.w, bd=5, font=20)
        self.res.place(x=100, y=300, height=50, width=500)
        self.Enter = Button(self.w, text="ENTER", bd=5)

        self.Enter.bind('<Button-1>', self.cot_enter)
        self.Enter.pack()
        self.w.mainloop()

    def sinh_window(self, event):
        self.w = Toplevel()
        self.w.geometry('700x700+500+50')
        sum_img = PhotoImage(file="images/sinh.png")
        Label(self.w, image=sum_img).place(x=5, y=160)
        self.l = Label(self.w, text="Complex Number", font=20)
        self.l.pack()
        self.e = Entry(self.w, bd=5, font=20)
        self.e.pack()
        Label(self.w, text="Result: ", font=20).place(x=250, y=270)
        self.res = Entry(self.w, bd=5, font=20)
        self.res.place(x=100, y=300, height=50, width=500)
        self.Enter = Button(self.w, text="ENTER", bd=5)

        self.Enter.bind('<Button-1>', self.sinh_enter)
        self.Enter.pack()
        self.w.mainloop()

    def cosh_window(self, event):
        self.w = Toplevel()
        self.w.geometry('700x700+500+50')
        sum_img = PhotoImage(file="images/cosh.png")
        Label(self.w, image=sum_img).place(x=5, y=160)
        self.l = Label(self.w, text="Complex Number", font=20)
        self.l.pack()
        self.e = Entry(self.w, bd=5, font=20)
        self.e.pack()
        Label(self.w, text="Result: ", font=20).place(x=250, y=270)
        self.res = Entry(self.w, bd=5, font=20)
        self.res.place(x=100, y=300, height=50, width=500)
        self.Enter = Button(self.w, text="ENTER", bd=5)

        self.Enter.bind('<Button-1>', self.cosh_enter)
        self.Enter.pack()
        self.w.mainloop()


calc = Calc()
calc.sum()
calc.sub()
calc.conj()
calc.product()
calc.div()
calc.module()
calc.root()
calc.argument()
calc.trig()
calc.func()
calc.sin()
calc.cos()
calc.tan()
calc.cot()
calc.sinh()
calc.cosh()
calc.analytic()
calc.mainloop()
