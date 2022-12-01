from cgitb import text
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
master = Tk()
master.title(&#39;tk&#39;)
master.geometry(&#39;800x800&#39;)
Label(master,text=&#39;Title &#39;).grid(row=0)
Label(master, text=&#39;Last Name &#39;).grid(row=1)
Label(master,text=&#39;First Name &#39;).grid(row=2)
Label(master, text=&#39;Share with &#39;).grid(row=3)
Label(master,text=&#39;Business number &#39;).grid(row=4)
Label(master, text=&#39;Mobile Number &#39;).grid(row=5)
Label(master, text=&#39;Email Address &#39;).grid(row=6)
Label(master, text=&#39;Date of Arrival &#39;).grid(row=7)
Label(master,text=&#39;Date of Departure &#39;).grid(row=8)
Label(master, text=&#39;Name on Credit Number &#39;).grid(row=9)
Label(master,text=&#39;Credit Card Number &#39;).grid(row=10)
Label(master, text=&#39;Expire Date &#39;).grid(row=11)
Label(master,text=&#39;CVV Number &#39;).grid(row=12)
Label(master,text=&#39;Payment &#39;).grid(row=13)
for i in range(0,14):
ei= Entry(master, width=50).grid(row=i,column=1)
var1 = IntVar()
Checkbutton(master, text=&quot;Credit Card&quot;,variable=var1).grid(row=13,
column=1, sticky=W,ipady=10, ipadx=10)
var2 = IntVar()
Checkbutton(master,text=&quot;Direct bank Transfer&quot;,
variable=var2).grid(row=13,column=2, sticky=W,ipady=10,ipadx=10)

Label(master,font=(&quot;Arial&quot;, 10), text= &#39;Negotiated Rates:
&#39;).grid(row=14,column=0)
var3 = IntVar()
Checkbutton(master,text=&quot;Deluxe Room Single &quot;,
variable=var3).grid(row=15,column=0, sticky=W,ipady=10,ipadx=10)
Label(master,text=&#39;R 1700 &#39;).grid(row=15,column=1)
var4 = IntVar()
Checkbutton(master,text=&quot;Deluxe Room Double &quot;,
variable=var4).grid(row=15,column=2, sticky=W,ipady=10,ipadx=10)
Label(master,text=&#39;R 1700 &#39;).grid(row=15,column=3)
var5 = IntVar()
Checkbutton(master,text=&quot;Suites Room Single &quot;,
variable=var5).grid(row=16,column=0, sticky=W,ipady=10,ipadx=10)
Label(master,text=&#39;R 1700 &#39;).grid(row=16,column=1)
var6 = IntVar()
Checkbutton(master,text=&quot;Suites Room Double &quot;,
variable=var6).grid(row=16,column=2, sticky=W,ipady=10,ipadx=10)
Label(master,text=&#39;R 1700 &#39;).grid(row=16,column=3)
Label(master,font=(&quot;Arial&quot;, 10), text= &#39;Room Preference:
&#39;).grid(row=17,column=0)
var7 = IntVar()
Checkbutton(master,text=&quot;King Bed &quot;, variable=var7).grid(row=18,
column=0,
sticky=W,ipady=10,ipadx=10)
var8 = IntVar()
Checkbutton(master,text=&quot;Twin-Two Single Beds
&quot;,variable=var8).grid(row=18, column=2, sticky=W,ipady=10,ipadx=10)
Label(master,font=(&quot;Arial&quot;, 10), text= &#39;The above rates are quoted
per room, per night. The rates includes breakfast, 14% vat, and
Excludes 1% Tourism Levy &#39;).place(x=0,y=500)
Label(master,font=(&quot;Arial&quot;, 10), text= &#39;and a voluntary R10 donation
to the Ambela Community Trust that will be levies onto your
account.&#39;).place(x=0,y=525)
Label(master,font=(&quot;Arial&quot;, 10), text= &#39;Credit Card will be changed
on receipt of this form and details will also be used to settle all
incidentals &#39;).place(x=0,y=550)
Label(master,font=(&quot;Arial&quot;, 10), text= &#39;not settle on departure. A
copy of the final folio will be sent to you should there be any
unsettled changes.&#39;).place(x=0,y=575)
Label(master,font=(&quot;Arial&quot;, 10), text= &#39;In order to qualify for the
above rates your booking needs to be made on or before 15th January
2016&#39;).place(x=0,y=600)
Label(master,font=(&quot;Arial&quot;, 10), text= &#39;Terms and conditions can be
found on the next page&#39;).place(x=0,y=625)
Label(master,font=(&quot;Arial&quot;, 10), text= &#39;The rate is valid for seven
days before and after the conference dates. Check in time is 14:00 &amp;
check out time is 11:00&#39;).place(x=0,y=650)
Label(master,font=(&quot;Arial&quot;, 10), text= &#39;By your signature hereto,
you are accepting all terms and conditions specified on this form
and confirm that all information&#39;).place(x=0,y=675)
Label(master,font=(&quot;Arial&quot;, 10), text= &#39;given is current and
accurate.&#39;).place(x=0,y=700)
Label(master,font=(&quot;Arial&quot;, 10),
text=&#39;Signature___________________&#39;).place(x=0,y=740)
Label(master,font=(&quot;Arial&quot;, 10),
text=&#39;Pointname___________________&#39;).place(x=400,y=740)

Label(master,font=(&quot;Arial&quot;, 10),
text=&#39;Date________________________&#39;).place(x=0,y=765)
master.mainloop()