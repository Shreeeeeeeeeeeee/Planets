#solar system

import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

st.title('Trajectory of Planets')
st.header('',divider='rainbow')
pla1=st.checkbox("Sun")
pla2=st.checkbox("Mercury")
pla3=st.checkbox("Venus")
pla4=st.checkbox("Earth")
pla5=st.checkbox("Mars")
pla6=st.checkbox("Jupiter")
pla7=st.checkbox("Saturn")
pla8=st.checkbox("Uranus")
pla9=st.checkbox("Neptune")
pla10=st.checkbox("Pluto")
pla11=st.checkbox("Haleys Comet")
pla12=st.checkbox("All")
#pla=st.radio('Select the planet',("Sun","Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune","Pluto","Haleys Comet","All"))

#SUN

def starsun():
    sun=np.linspace(0,2*np.pi,5000)
    a=0.00464
    b=0.00464

    x=a*np.cos(sun)
    y=b*np.sin(sun)

    plt.plot(x,y,color='blue')
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.axis("equal")
    plt.xlim(-0.5,0.5)
    plt.ylim(-0.5,0.5)
    plt.grid()
    plt.savefig('graph.jpg')
    st.image('graph.jpg')

#MERCURY

def merc():
    planet=np.linspace(0,2*np.pi,5000)
    p=0.387
    q=0.3873

    x=0.079567+p*np.cos(planet)
    y=q*np.sin(planet)

    plt.plot(x,y,color='green')
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.axis("equal")

    sun = np.linspace(0, 2 * np.pi, 5000)
    a = 0.00464
    b = 0.00464

    x = a * np.cos(sun)
    y = b * np.sin(sun)

    plt.plot(x, y, color='blue')
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.axis("equal")

    plt.grid()
    plt.savefig('graph.jpg')
    st.image('graph.jpg')

#VENUS

def ven():
    planet=np.linspace(0,2*np.pi,5000)
    p=0.723
    q=0.72297

    x=0.0049164+p*np.cos(planet)
    y=q*np.sin(planet)

    plt.plot(x,y,color='yellow')
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.axis("equal")

    sun = np.linspace(0, 2 * np.pi, 5000)
    a = 0.00464
    b = 0.00464

    x = a * np.cos(sun)
    y = b * np.sin(sun)

    plt.plot(x, y, color='blue')
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.axis("equal")

    plt.grid()
    plt.savefig('graph.jpg')
    st.image('graph.jpg')

#EARTH

def ear():
    planet=np.linspace(0,2*np.pi,5000)
    p=1
    q=0.99986

    x=0.0167+p*np.cos(planet)
    y=q*np.sin(planet)

    plt.plot(x,y,color='pink')
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.axis("equal")

    sun = np.linspace(0, 2 * np.pi, 5000)
    a = 0.00464
    b = 0.00464

    x = a * np.cos(sun)
    y = b * np.sin(sun)

    plt.plot(x, y, color='blue')
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.axis("equal")
    plt.grid()
    plt.savefig('graph.jpg')
    st.image('graph.jpg')

#MARS

def mar():
    planet=np.linspace(0,2*np.pi,5000)
    p=1.524
    q=1.5173

    x=0.14234+p*np.cos(planet)
    y=q*np.sin(planet)

    plt.plot(x,y,color='cyan')
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.axis("equal")

    sun = np.linspace(0, 2 * np.pi, 5000)
    a = 0.00464
    b = 0.00464

    x = a * np.cos(sun)
    y = b * np.sin(sun)

    plt.plot(x, y, color='blue')
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.axis("equal")

    plt.grid()
    plt.savefig('graph.jpg')
    st.image('graph.jpg')

#JUPITER

def jup():
    planet=np.linspace(0,2*np.pi,5000)
    p=5.203
    q=5.1969

    x=0.25182+p*np.cos(planet)
    y=q*np.sin(planet)

    plt.plot(x,y,color='magenta')
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.axis("equal")
    sun = np.linspace(0, 2 * np.pi, 5000)
    a = 0.00464
    b = 0.00464

    x = a * np.cos(sun)
    y = b * np.sin(sun)

    plt.plot(x, y, color='blue')
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.axis("equal")

    plt.grid()
    plt.savefig('graph.jpg')
    st.image('graph.jpg')

#SATURN

def sat():
    planet=np.linspace(0,2*np.pi,5000)
    p=9.537
    q=9.5229

    x=0.5169+p*np.cos(planet)
    y=q*np.sin(planet)

    plt.plot(x,y,color='red')
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.axis("equal")
    sun = np.linspace(0, 2 * np.pi, 5000)
    a = 0.00464
    b = 0.00464

    x = a * np.cos(sun)
    y = b * np.sin(sun)

    plt.plot(x, y, color='blue')
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.axis("equal")

    plt.grid()
    plt.savefig('graph.jpg')
    st.image('graph.jpg')

#URANUS

def ura():
    planet=np.linspace(0,2*np.pi,5000)
    p=19.191
    q=19.1696

    x=0.90581+p*np.cos(planet)
    y=q*np.sin(planet)

    plt.plot(x,y,color='olive')
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.axis("equal")
    sun = np.linspace(0, 2 * np.pi, 5000)
    a = 0.00464
    b = 0.00464

    x = a * np.cos(sun)
    y = b * np.sin(sun)

    plt.plot(x, y, color='blue')
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.axis("equal")

    plt.grid()
    plt.savefig('graph.jpg')
    st.image('graph.jpg')


#NEPTUNE

def nep():
    planet=np.linspace(0,2*np.pi,5000)
    p=30.069
    q=30.0678

    x=0.2585+p*np.cos(planet)
    y=q*np.sin(planet)

    plt.plot(x,y,color='gray')
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.axis("equal")
    sun = np.linspace(0, 2 * np.pi, 5000)
    a = 0.00464
    b = 0.00464

    x = a * np.cos(sun)
    y = b * np.sin(sun)

    plt.plot(x, y, color='blue')
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.axis("equal")

    plt.grid()
    plt.savefig('graph.jpg')
    st.image('graph.jpg')

#PLUTO


def plu():
    planet=np.linspace(0,2*np.pi,5000)
    p=39.482
    q=38.2404

    x=9.8231+p*np.cos(planet)
    y=q*np.sin(planet)

    plt.plot(x,y)
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.axis("equal")
    sun = np.linspace(0, 2 * np.pi, 5000)
    a = 0.00464
    b = 0.00464

    x = a * np.cos(sun)
    y = b * np.sin(sun)

    plt.plot(x, y, color='blue')
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.axis("equal")

    plt.grid()
    plt.savefig('graph.jpg')
    st.image('graph.jpg')

#ALL
def all():
    # SUN
    sun = np.linspace(0, 2 * np.pi, 5000)
    a = 0.00464
    b = 0.00464

    x = a * np.cos(sun)
    y = b * np.sin(sun)

    plt.plot(x, y)
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.axis("equal")

    # MERCURY
    planet = np.linspace(0, 2 * np.pi, 5000)
    p = 0.387
    q = 0.3873

    x = 0.079567 + p * np.cos(planet)
    y = q * np.sin(planet)

    plt.plot(x, y)
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.axis("equal")

    # VENUS
    planet = np.linspace(0, 2 * np.pi, 5000)
    p = 0.723
    q = 0.72297

    x = 0.0049164 + p * np.cos(planet)
    y = q * np.sin(planet)

    plt.plot(x, y)
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.axis("equal")

    # EARTH
    planet = np.linspace(0, 2 * np.pi, 5000)
    p = 1
    q = 0.99986

    x = 0.0167 + p * np.cos(planet)
    y = q * np.sin(planet)

    plt.plot(x, y)
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.axis("equal")

    # MARS
    planet = np.linspace(0, 2 * np.pi, 5000)
    p = 1.524
    q = 1.5173

    x = 0.14234 + p * np.cos(planet)
    y = q * np.sin(planet)

    plt.plot(x, y)
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.axis("equal")

    # JUPITER
    planet = np.linspace(0, 2 * np.pi, 5000)
    p = 5.203
    q = 5.1969

    x = 0.25182 + p * np.cos(planet)
    y = q * np.sin(planet)

    plt.plot(x, y)
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.axis("equal")

    # SATURN
    planet = np.linspace(0, 2 * np.pi, 5000)
    p = 9.537
    q = 9.5229

    x = 0.5169 + p * np.cos(planet)
    y = q * np.sin(planet)

    plt.plot(x, y)
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.axis("equal")

    # URANUS
    planet = np.linspace(0, 2 * np.pi, 5000)
    p = 19.191
    q = 19.1696

    x = 0.90581 + p * np.cos(planet)
    y = q * np.sin(planet)

    plt.plot(x, y)
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.axis("equal")

    # NEPTUNE
    planet = np.linspace(0, 2 * np.pi, 5000)
    p = 30.069
    q = 30.0678

    x = 0.2585 + p * np.cos(planet)
    y = q * np.sin(planet)

    plt.plot(x, y)
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.axis("equal")

    # PLUTO
    planet = np.linspace(0, 2 * np.pi, 5000)
    p = 39.482
    q = 38.2404

    x = 9.8231 + p * np.cos(planet)
    y = q * np.sin(planet)

    plt.plot(x, y)
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.axis("equal")

    # HALLEYS COMET
    planet = np.linspace(0, 2 * np.pi, 5000)
    p = 17.834
    q = 4.53448

    x = 17.2479 + p * np.cos(planet)
    y = q * np.sin(planet)

    plt.plot(x, y)
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.axis("equal")

    plt.title("Solar System  (202235)")
    plt.savefig("Solar System.png", dpi=500)
    plt.grid()
    plt.savefig('graph.jpg')
    st.image('graph.jpg')

#HALLEYS COMET

def halc():
    planet=np.linspace(0,2*np.pi,5000)
    p=17.834
    q=4.53448
    x=17.2479+p*np.cos(planet)
    y=q*np.sin(planet)

    plt.plot(x,y,color='violet')
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.axis("equal")

    plt.title("Solar System  (202235)")
    plt.savefig("Solar System.png", dpi=500)
    sun = np.linspace(0, 2 * np.pi, 5000)
    a = 0.00464
    b = 0.00464

    x = a * np.cos(sun)
    y = b * np.sin(sun)

    plt.plot(x, y, color='blue')
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.axis("equal")

    plt.grid()
    plt.savefig('graph.jpg')
    st.image('graph.jpg')

if pla1 :
    st.image("36dg.gif",caption="The Sun")
    starsun()
if pla2:
    st.image("Mercury.gif",caption="Mercury")
    merc()
if pla3:
    st.image("venus.gif",caption="Venus")
    ven()
if pla4:
    st.image("Earth.gif",caption="Earth")
    ear()
if pla5:
    st.image("Mars.gif",caption="Mars")
    mar()
if pla6:
    st.image("Jupiter.gif",caption="Jupiter")
    jup()
if pla7:
    st.image("Saturn.gif",caption="Saturn")
    sat()
if pla8:
    st.image("Uranus.gif",caption="Uranus")
    ura()
if pla9:
    st.image("Neptune.gif",caption="Neptune")
    nep()
if pla10:
    st.image("Pluto.gif",caption="Pluto")
    plu()
if pla11:
    st.image("Halleys_Comet.gif",caption="Halley's Comet")
    halc()
if pla12:
    st.image("Solar_System.gif",caption="Solar System")
    all()

"""if pla=="Sun":
    st.image("36dg.gif",caption="The Sun")
    starsun()
elif pla=="Mercury":
    st.image("Mercury.gif",caption="Mercury")
    merc()
elif pla=="Venus":
    st.image("venus.gif",caption="Venus")
    ven()
elif pla=="Earth":
    st.image("Earth.gif",caption="Earth")
    ear()
elif pla=="Mars":
    st.image("Mars.gif",caption="Mars")
    mar()
elif pla=="Jupiter":
    st.image("Jupiter.gif",caption="Jupiter")
    jup()
elif pla=="Saturn":
    st.image("Saturn.gif",caption="Saturn")
    sat()
elif pla=="Uranus":
    st.image("Uranus.gif",caption="Uranus")
    ura()
elif pla=="Neptune":
    st.image("Neptune.gif",caption="Neptune")
    nep()
elif pla=="Pluto":
    st.image("Pluto.gif",caption="Pluto")
    plu()
elif pla=="All":
    st.image("Solar_System.gif",caption="Solar System")
    all()
elif pla=="Haleys Comet":
    st.image("Halleys_Comet.gif",caption="Halley's Comet")
    halc()"""


