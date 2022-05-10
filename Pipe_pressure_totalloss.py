import tkinter as tk


# Mathematical Calculations


def analiz():
    q = float(flow2.get())
    od = float(pipeouterdiameter2.get())
    t = float(pipewallthickness2.get())
    L = float(pipelength2.get())
    bx = float(SuddenContract2.get())
    by = float(SuddenEnlargement2.get())
    sh = float(statichead2.get())
    scn = float(SuddenContractionNumber1.get())
    ascv = float(AngleStopCheckValve1.get())
    m60 = float(miltre601.get())
    sen = float(SuddenEnlargementNumber1.get())
    fvspd = float(StrainerPoppetDisc1.get())
    m75 = float(miltre751.get())
    gv = float(gatevalve1.get())
    fvshd = float(strainerhingeddisc1.get())
    m90 = float(miltre901.get())
    scv = float(swingcheckvalve1.get())
    bvfb = float(ballvalve1.get())
    e15 = float(elbow151.get())
    glv = float(globevalve1.get())
    bv = float(butterfly1.get())
    e1 = float(elbow11.get())
    agv = float(angleglobevalve1.get())
    vtp = float(valvethroughpass1.get())
    rb = float(returnbend1.get())
    lcv = float(liftcheckvalve1.get())
    vrp = float(valverightpass1.get())
    ftr = float(flowthroughrun1.get())
    sp = float(smoothpass1.get())
    m15 = float(miltre151.get())
    ftb = float(flowthroughbr1.get())
    tdcv = float(tiltingdisc1.get())
    m30 = float(miltre301.get())
    pep = float(pipeentranceinward1.get())
    stopcv = float(stopcheckvalve1.get())
    m45 = float(miltre451.get())
    pef = float(pipeentranceflush1.get())
    other = float(otherkfactor1.get())

    u = 1.044
    p = 1025
    rop = 0.05

    d = float(od - 2 * t)
    v = float(q / (3600 * (d * 0.001)** 2 * 0.786))
    re = float(1000 * v * d / u)
    k = float(rop / d)

    i = float(0.5 * (1 - bx ** 2) / bx ** 4)
    j = float((1 - by** 2)** 2 / by** 4)

    result = float((i * scn) + (j * sen) + 0.14 * gv + 0.9 * scv + 6.12 * glv + 2.7 * agv +
                 10.8 * lcv + 0.99 * sp + 0.72 * tdcv + 7.2 * stopcv + 3.6 * ascv + 7.56 * fvspd + 1.35 * fvshd +
                 0.05 * bvfb + 0.81 * bv + 0.54 * vtp + 1.62 * vrp + 0.07 * m15 + 0.14 * m30 + 0.27 * m45 +
                 0.45 * m60 + 0.72 * m75 + 1.08 * m90 + 0.25 * e15 + 0.36 * e1 + 0.9 * rb + 0.36 * ftr + 1.08 * ftb +
                 0.78 * pep + 0.5 * pef + 0.5 * other)

    zlz = math.log(((6.9 / re) + (k / 3.7)** 1.11)** 2, 10)

    f = float(1 / -1.8 * zlz)
    fh = float(f * (L / (d * 0.001)) * (v** 2 / (2 * 9.81)))
    fih = float(result * v** 2 / (9.81 * 2))
    th = float(sh + fh + fih)

    totalloss['text'] = str((th * p * 9.81) / 100000)


###########################################
window = tk.Tk()
window.geometry("920x965+500+30")
window.title("ARTI Engineering")

etiket = tk.Label(text="Pressure Loss Control", font="Verdana 18 bold")
etiket.place(x=330, y=20)

flow2 = tk.Entry(width=10)
flow2.place(x=200, y=70)
flow = tk.Label(text="Flow (Q)")
flow['font'] = "Verdana 10"
flow['fg'] = "#000000"  # FFAABB 16lık kod
flow.place(x=130, y=67)  # FF=red, AA=grey, BB=blue

flow1 = tk.Label(text="m3/h")
flow1['font'] = "Verdana 8"
flow1['fg'] = "#000000"
flow1.place(x=265, y=72)

############################################
pipeouterdiameter2 = tk.Entry(width=10)
pipeouterdiameter2.place(x=200, y=110)
pipeouterdiameter = tk.Label(text="Pipe Outer Diameter (OD)")
pipeouterdiameter['font'] = "Verdana 10"
pipeouterdiameter['fg'] = "#000000"
pipeouterdiameter.place(x=20, y=107)

pipeouterdiameter1 = tk.Label(text="mm")
pipeouterdiameter1['font'] = "Verdana 8"
pipeouterdiameter1['fg'] = "#000000"
pipeouterdiameter1.place(x=265, y=112)

############################################

pipewallthickness2 = tk.Entry(width=10)
pipewallthickness2.place(x=200, y=150)
pipewallthickness = tk.Label(text="Pipe Wall Thickness (t)")
pipewallthickness['font'] = "Verdana 10"
pipewallthickness['fg'] = "#000000"
pipewallthickness.place(x=35, y=147)

pipewallthickness1 = tk.Label(text="mm")
pipewallthickness1['font'] = "Verdana 8"
pipewallthickness1['fg'] = "#000000"
pipewallthickness1.place(x=265, y=152)

############################################

pipelength2 = tk.Entry(width=10)
pipelength2.place(x=200, y=190)
pipelength = tk.Label(text="Pipe Length (L)")
pipelength['font'] = "Verdana 10"
pipelength['fg'] = "#000000"
pipelength.place(x=86, y=187)

pipelength1 = tk.Label(text="m")
pipelength1['font'] = "Verdana 8"
pipelength1['fg'] = "#000000"
pipelength1.place(x=265, y=192)

############################################

SuddenContract2 = tk.Entry(width=10)
SuddenContract2.place(x=200, y=230)
SuddenContract = tk.Label(text="Sudden Contraction (B)")
SuddenContract['font'] = "Verdana 10"
SuddenContract['fg'] = "#000000"
SuddenContract.place(x=32, y=227)

############################################

SuddenEnlargement2 = tk.Entry(width=10)
SuddenEnlargement2.place(x=200, y=270)
SuddenEnlargement = tk.Label(text="Sudden Enlargement (B)")
SuddenEnlargement['font'] = "Verdana 10"
SuddenEnlargement['fg'] = "#000000"
SuddenEnlargement.place(x=28, y=267)

############################################

statichead2 = tk.Entry(width=10)
statichead2.place(x=200, y=310)
statichead = tk.Label(text="Static Head ")
statichead['font'] = "Verdana 10"
statichead['fg'] = "#000000"
statichead.place(x=110, y=307)

statichead1 = tk.Label(text="m")
statichead1['font'] = "Verdana 8"
statichead1['fg'] = "#000000"
statichead1.place(x=265, y=312)

############################################

Analysis = tk.Button(text="Analysis", font="Verdana 18", width=10, command=analiz).place(x=120, y=355)

totalloss2 = tk.Entry(width=20)
totalloss2.place(x=530, y=365)
totalloss = tk.Label(text="Total Loss ")
totalloss['font'] = "Verdana 14 bold"
totalloss['fg'] = "#000000"
totalloss.place(x=400, y=360)

totalloss1 = tk.Label(text="bar")
totalloss1['font'] = "Verdana 10"
totalloss1['fg'] = "#000000"
totalloss1.place(x=660, y=365)

############################################

Number1 = tk.Label(text=" Number ")
Number1['font'] = "Verdana 10 bold "
Number1['fg'] = "#000000"
Number1.place(x=198, y=430)

Number2 = tk.Label(text=" Number ")
Number2['font'] = "Verdana 10 bold "
Number2['fg'] = "#000000"
Number2.place(x=508, y=430)

Number3 = tk.Label(text=" Number ")
Number3['font'] = "Verdana 10 bold "
Number3['fg'] = "#000000"
Number3.place(x=828, y=430)

############################################

SuddenContractionNumber1 = tk.Entry(width=10)
SuddenContractionNumber1.place(x=200, y=450)
SuddenContractionNumber = tk.Label(text="Sudden Contraction")
SuddenContractionNumber['font'] = "Verdana 10"
SuddenContractionNumber['fg'] = "#000000"
SuddenContractionNumber.place(x=53, y=450)

############################################

AngleStopCheckValve1 = tk.Entry(width=10)
AngleStopCheckValve1.place(x=510, y=450)
AngleStopCheckValve = tk.Label(text="Angle Stop Check Valve")
AngleStopCheckValve['font'] = "Verdana 10"
AngleStopCheckValve['fg'] = "#000000"
AngleStopCheckValve.place(x=335, y=450)

############################################

miltre601 = tk.Entry(width=10)
miltre601.place(x=830, y=450)
miltre60 = tk.Label(text="Miltre Bend 60")
miltre60['font'] = "Verdana 10"
miltre60['fg'] = "#000000"
miltre60.place(x=720, y=450)

############################################


SuddenEnlargementNumber1 = tk.Entry(width=10)
SuddenEnlargementNumber1.place(x=200, y=490)
SuddenEnlargementNumber = tk.Label(text="Sudden Enlargement")
SuddenEnlargementNumber['font'] = "Verdana 10"
SuddenEnlargementNumber['fg'] = "#000000"
SuddenEnlargementNumber.place(x=48, y=490)

############################################

StrainerPoppetDisc1 = tk.Entry(width=10)
StrainerPoppetDisc1.place(x=510, y=490)
StrainerPoppetDisc = tk.Label(text="F.V. With Strainer Poppet Disc")
StrainerPoppetDisc['font'] = "Verdana 10"
StrainerPoppetDisc['fg'] = "#000000"
StrainerPoppetDisc.place(x=290, y=490)

############################################

miltre751 = tk.Entry(width=10)
miltre751.place(x=830, y=490)
miltre75 = tk.Label(text="Miltre Bend 75")
miltre75['font'] = "Verdana 10"
miltre75['fg'] = "#000000"
miltre75.place(x=720, y=490)

############################################


gatevalve1 = tk.Entry(width=10)
gatevalve1.place(x=200, y=530)
gatevalve = tk.Label(text="Gate Valve")
gatevalve['font'] = "Verdana 10"
gatevalve['fg'] = "#000000"
gatevalve.place(x=110, y=530)

############################################

strainerhingeddisc1 = tk.Entry(width=10)
strainerhingeddisc1.place(x=510, y=530)
strainerhingeddisc = tk.Label(text="F.V. With Strainer Hinged Disc")
strainerhingeddisc['font'] = "Verdana 10"
strainerhingeddisc['fg'] = "#000000"
strainerhingeddisc.place(x=292, y=530)

############################################

miltre901 = tk.Entry(width=10)
miltre901.place(x=830, y=530)
miltre90 = tk.Label(text="Miltre Bend 90")
miltre90['font'] = "Verdana 10"
miltre90['fg'] = "#000000"
miltre90.place(x=720, y=530)

############################################


swingcheckvalve1 = tk.Entry(width=10)
swingcheckvalve1.place(x=200, y=570)
swingcheckvalve = tk.Label(text="Swing Check Valve")
swingcheckvalve['font'] = "Verdana 10"
swingcheckvalve['fg'] = "#000000"
swingcheckvalve.place(x=57, y=570)

############################################

ballvalve1 = tk.Entry(width=10)
ballvalve1.place(x=510, y=570)
ballvalve = tk.Label(text="Ball Valve Full Bore")
ballvalve['font'] = "Verdana 10"
ballvalve['fg'] = "#000000"
ballvalve.place(x=368, y=570)

############################################

elbow151 = tk.Entry(width=10)
elbow151.place(x=830, y=570)
elbow15 = tk.Label(text="Elbow 1.5D")
elbow15['font'] = "Verdana 10"
elbow15['fg'] = "#000000"
elbow15.place(x=741, y=570)

############################################


globevalve1 = tk.Entry(width=10)
globevalve1.place(x=200, y=610)
globevalve = tk.Label(text="Globe Valve")
globevalve['font'] = "Verdana 10"
globevalve['fg'] = "#000000"
globevalve.place(x=105, y=610)

############################################

butterfly1 = tk.Entry(width=10)
butterfly1.place(x=510, y=610)
butterfly = tk.Label(text="Butterfly Valve")
butterfly['font'] = "Verdana 10"
butterfly['fg'] = "#000000"
butterfly.place(x=393, y=610)

############################################

elbow11 = tk.Entry(width=10)
elbow11.place(x=830, y=610)
elbow1 = tk.Label(text="Elbow 1D")
elbow1['font'] = "Verdana 10"
elbow1['fg'] = "#000000"
elbow1.place(x=754, y=610)

############################################

angleglobevalve1 = tk.Entry(width=10)
angleglobevalve1.place(x=200, y=650)
angleglobevalve = tk.Label(text="Angle Globe Valve")
angleglobevalve['font'] = "Verdana 10"
angleglobevalve['fg'] = "#000000"
angleglobevalve.place(x=64, y=650)

############################################

valvethroughpass1 = tk.Entry(width=10)
valvethroughpass1.place(x=510, y=650)
valvethroughpass = tk.Label(text="3-Way Valve Through Passage")
valvethroughpass['font'] = "Verdana 10"
valvethroughpass['fg'] = "#000000"
valvethroughpass.place(x=288, y=650)

############################################

returnbend1 = tk.Entry(width=10)
returnbend1.place(x=830, y=650)
returnbend = tk.Label(text="Return Bend")
returnbend['font'] = "Verdana 10"
returnbend['fg'] = "#000000"
returnbend.place(x=732, y=650)

############################################


liftcheckvalve1 = tk.Entry(width=10)
liftcheckvalve1.place(x=200, y=690)
liftcheckvalve = tk.Label(text="Lift Check Valve")
liftcheckvalve['font'] = "Verdana 10"
liftcheckvalve['fg'] = "#000000"
liftcheckvalve.place(x=75, y=690)

############################################

valverightpass1 = tk.Entry(width=10)
valverightpass1.place(x=510, y=690)
valverightpass = tk.Label(text="3-Way Valve Right Passage")
valverightpass['font'] = "Verdana 10"
valverightpass['fg'] = "#000000"
valverightpass.place(x=309, y=690)

############################################

flowthroughrun1 = tk.Entry(width=10)
flowthroughrun1.place(x=830, y=690)
flowthroughrun = tk.Label(text="TEE Flow Through Run")
flowthroughrun['font'] = "Verdana 10"
flowthroughrun['fg'] = "#000000"
flowthroughrun.place(x=664, y=690)

############################################


smoothpass1 = tk.Entry(width=10)
smoothpass1.place(x=200, y=730)
smoothpass = tk.Label(text="L.C.V. Smooth paasege")
smoothpass['font'] = "Verdana 10"
smoothpass['fg'] = "#000000"
smoothpass.place(x=27, y=730)

############################################

miltre151 = tk.Entry(width=10)
miltre151.place(x=510, y=730)
miltre15 = tk.Label(text="Miltre Bend 15")
miltre15['font'] = "Verdana 10"
miltre15['fg'] = "#000000"
miltre15.place(x=397, y=730)

############################################

flowthroughbr1 = tk.Entry(width=10)
flowthroughbr1.place(x=830, y=730)
flowthroughbr = tk.Label(text="TEE Flow Through Branch")
flowthroughbr['font'] = "Verdana 10"
flowthroughbr['fg'] = "#000000"
flowthroughbr.place(x=642, y=730)

############################################


tiltingdisc1 = tk.Entry(width=10)
tiltingdisc1.place(x=200, y=770)
tiltingdisc = tk.Label(text="Tilting Disc Check Valves")
tiltingdisc['font'] = "Verdana 10"
tiltingdisc['fg'] = "#000000"
tiltingdisc.place(x=16, y=770)

############################################

miltre301 = tk.Entry(width=10)
miltre301.place(x=510, y=770)
miltre30 = tk.Label(text="Miltre Bend 30")
miltre30['font'] = "Verdana 10"
miltre30['fg'] = "#000000"
miltre30.place(x=397, y=770)

############################################

pipeentranceinward1 = tk.Entry(width=10)
pipeentranceinward1.place(x=830, y=770)
pipeentranceinward = tk.Label(text="Pipe Entrance Inward Projecting")
pipeentranceinward['font'] = "Verdana 10"
pipeentranceinward['fg'] = "#000000"
pipeentranceinward.place(x=598, y=770)

############################################


stopcheckvalve1 = tk.Entry(width=10)
stopcheckvalve1.place(x=200, y=810)
stopcheckvalve = tk.Label(text="Stop Check Valve")
stopcheckvalve['font'] = "Verdana 10"
stopcheckvalve['fg'] = "#000000"
stopcheckvalve.place(x=64, y=810)

############################################

miltre451 = tk.Entry(width=10)
miltre451.place(x=510, y=810)
miltre45 = tk.Label(text="Miltre Bend 45")
miltre45['font'] = "Verdana 10"
miltre45['fg'] = "#000000"
miltre45.place(x=397, y=810)

############################################

pipeentranceflush1 = tk.Entry(width=10)
pipeentranceflush1.place(x=830, y=810)
pipeentranceflush = tk.Label(text="Pipe Entrance Flush")
pipeentranceflush['font'] = "Verdana 10"
pipeentranceflush['fg'] = "#000000"
pipeentranceflush.place(x=680, y=810)

############################################

otherkfactor1 = tk.Entry(width=10)
otherkfactor1.place(x=510, y=850)
otherkfactor = tk.Label(text="Other 'K' factor")
otherkfactor['font'] = "Verdana 10"
otherkfactor['fg'] = "#000000"
otherkfactor.place(x=389, y=850)

############################################

Name = tk.Label(text="by Gürkan YILMAZ")
Name['font'] = "Verdana 10 italic"
Name['fg'] = "grey"
Name.place(x=770, y=890)

############################################

window.mainloop()
