import pygame

WIDTH = 500
HEIGHT = 300

TITLE = "Clicker animal"
FPS = 30


# Objetos
    # Mode menu
fondo_1 = Actor("fondo2")
box_1 = Actor("box1", (50, 275))
box_2 = Actor("box1", (100, 275))
box_3 = Actor("box1", (75, 225))
play = Actor("play3", (250, 150))
salida_icono = Actor('x_2', (470, 30))
taller_icono = Actor('taller_3', (400, 100))
chispitas_icono = Actor('electricidad_2', (400, 200))
tienda_icono = Actor('mercadona_2', (75, 100))
    # Mode etapa_1
fondo_2 = Actor("fondo1")
granja_icono = Actor('granja_3', (100, 80))
madera_icono = Actor('madera_2', (100, 220))
vender_icono = Actor('dinero_2', (402, 170))
hacha_icono = Actor('axe_3', (170, 220))
piedra_icono = Actor('piedra_2', (250, 220))
pico_icono = Actor('pico_3', (320, 220))
    # Mode etapa_2
mina_fondo = Actor('mina_fondo_1')
iron_age_icono_1 = Actor('iron_age_2', (250, 250))
iron_icono = Actor('hierro_3', (70, 100))
minar_icono = Actor('minar_icono_2', (150, 100))
horno_icono = Actor('horno_3', (50, 250))
flecha_icono = Actor('flecha_2', (150, 250))
carbon_icono = Actor('carbon_2', (300, 110))
    # Mode seleccion
bosque_icono = Actor('bosque_1', (100, 100))
iron_age_icono = Actor('iron_age_2', (400,100))
ordenador_icono = Actor('ordenador_4', (250, 200))
    # Mode taller
taller_fondo = Actor('taller_6')
axe_taller = Actor('pico_6', (70, 100))
pico_taller = Actor('hacha_4', (70, 230))
change_icono = Actor('next_2', (400, 250))
    # Mode taller_2
fondo_taller_2 = Actor('fondo_taller_3')
maquina_vapor_icono_2 = Actor('maquina_vapor_3', (70, 70))
panel_solar_icono = Actor('panel_solar_3', (70, 225))
    # Mode taller_3
fondo_taller_3 = Actor('fondo_taller_9')
ordenador_taller = Actor('ordenador_7', (125, 150))
    # Mode tesla
fondo_electricidad = Actor('fondo_electricidad_6')
maquina_de_vapor_icono = Actor('maquina_vapor_3', (70, 70))
pala_icono = Actor('pala_1', (150, 70))
boton_mas = Actor('boton_+_3', (100, 150))
boton_menos = Actor('boton_-_3', (50, 150))
    # Mode mercadona
mercadona_fondo = Actor('mercadona_8')
maquina_vapor_icono_3 = Actor('maquina_vapor_3', (300, 70))
panel_solar_icono_2 = Actor('panel_solar_3', (300, 225))
    # Mode mercadona_2
mercadona_fondo_2 = Actor('mercadona_10')
madera_icono_1 = Actor('madera_2', (70, 70))
piedra_icono_1 = Actor('piedra_2', (70, 220))
iron_icono_1 = Actor('hierro_3', (250, 70))
iron_age_icono_2 = Actor('iron_age_2', (400, 70))
carbon_icono_1 = Actor('carbon_2', (240, 225))
trigo_icono = Actor('tigo_2', (400, 220))
    # Mode end
end_fondo = Actor('end_3', (250, 175))
fondo_end = Actor('fondo2_end_3', (235, 145))
box_4 = Actor("box_end", (100, 250))
box_5 = Actor("box_end", (60, 250))
box_6 = Actor("box_end", (80, 215))
fin = Actor("fin_2", (240, 150))
taller_icono_2 = Actor('taller_3', (375, 100))
tienda_icono_2 = Actor('mercadona_2', (100, 100))

# Variables
dinero = 0
click = 1
mode = 'menu'
granja_si_no = 0
puntos = 0
etapa = 1
tab = 0
    #Objetos
madera = 10000000
click_madera = 1
hachas = 0

piedra = 0
click_piedra = 1
numero_picos = 0
picos = 0

numero_granjas = 0
cosecha = 0
trigo = 0

hacha_si_no = 0
numero_hachas = 0

hierro_bruto = 0
hierro_refinado = 0
click_hierro = 1

carbon = 0
click_carbon = 1

energia = 0
click_energia = 1
maquina_vapor = 'no'
numero_maquinas = 0
perdida_energia = 1
panel_solar = 'no'
numero_paneles = 0
ordenador = 'no'

energia_maquina = 0
energia_panel = 0

plata = 0
oro = 0
plutonio = 0

def draw():
#Modo menu
    if mode == 'menu':
        fondo_1.draw()
        play.draw()
        box_1.draw()
        box_2.draw()
        box_3.draw()
        taller_icono.draw()
        tienda_icono.draw()
        screen.draw.text(puntos, center=(450, 30), color="red", fontsize = 24)
        if puntos >= 200000 and etapa >= 2:
            chispitas_icono.draw()
#Mode etapa_1
    elif mode == 'etapa_1':    
        fondo_2.draw()
        granja_icono.draw()
        madera_icono.draw()
        vender_icono.draw()
        hacha_icono.draw()
        salida_icono.draw()
        if granja_si_no == 0:
            screen.draw.text('Precio: 100$', center=(100, 80), color="red", fontsize = 24)
        if puntos >= 1000:
            piedra_icono.draw()
            pico_icono.draw()
            screen.draw.text('PIEDRA', center=(250, 250), color="black", fontsize = 24)
            screen.draw.text(piedra, center=(250, 270), color="white", fontsize = 24)
            screen.draw.text(numero_picos, center=(320, 220), color="white", fontsize = 24)
        screen.draw.text('TRRIGO', center=(100, 120), color="black", fontsize = 24)
        screen.draw.text(trigo, center=(100, 140), color="white", fontsize = 24)
        screen.draw.text('MADERA', center=(100, 250), color="black", fontsize = 24)
        screen.draw.text(madera, center=(100, 270), color="white", fontsize = 24)
        screen.draw.text('DINERO', center=(400, 260), color="black", fontsize = 24)
        screen.draw.text(dinero, center=(400, 235), color="black", fontsize = 24)
        screen.draw.text(numero_hachas, center=(170, 220), color="black", fontsize = 24)
#Mode etapa_2
    elif mode == 'etapa_2':    
        mina_fondo.draw()
        vender_icono.draw()
        salida_icono.draw()
        iron_icono.draw()
        minar_icono.draw()
        horno_icono.draw()
        flecha_icono.draw()
        iron_age_icono_1.draw()
        if puntos >= 200000:
            screen.draw.text(carbon, center=(300, 170), color="white", fontsize = 30)
            carbon_icono.draw()
        screen.draw.text('DINERO', center=(400, 260), color="white", fontsize = 24)
        screen.draw.text(dinero, center=(400, 235), color="white", fontsize = 24)
        screen.draw.text(hierro_bruto, center=(60, 170), color="white", fontsize = 30)
        screen.draw.text(hierro_refinado, center=(250, 250), color="white", fontsize = 30)
#Mode taller
    elif mode == 'taller':
        taller_fondo.draw()
        salida_icono.draw()
        axe_taller.draw()
        screen.draw.text('El hacha cuesta:', center=(200, 50), color="black", fontsize = 20)
        screen.draw.text('1000 de madera', center=(200, 70), color="white", fontsize = 15)
        screen.draw.text('100 de piedra', center=(200, 80), color="white", fontsize = 15)
        screen.draw.text('1000 de trigo', center=(200, 90), color="white", fontsize = 15)
        screen.draw.text(hachas, center=(300, 75), color="black", fontsize = 15)
        screen.draw.text('PIEDRA', center=(400, 50), color="black", fontsize = 24)
        screen.draw.text(piedra, center=(400, 70), color="white", fontsize = 24)
        screen.draw.text('TRRIGO', center=(400, 90), color="black", fontsize = 24)
        screen.draw.text(trigo, center=(400, 110), color="white", fontsize = 24)
        screen.draw.text('MADERA', center=(400, 130), color="black", fontsize = 24)
        screen.draw.text(madera, center=(400, 150), color="white", fontsize = 24)
        screen.draw.text('DINERO', center=(400, 170), color="black", fontsize = 24)
        screen.draw.text(dinero, center=(400, 190), color="black", fontsize = 24)
        if puntos >= 10000 and hachas >= 1:
            pico_taller.draw()
            screen.draw.text('El pico cuesta:', center=(200, 170), color="black", fontsize = 20)
            screen.draw.text('5000 de madera', center=(200, 190), color="white", fontsize = 15)
            screen.draw.text('500 de piedra', center=(200, 200), color="white", fontsize = 15)
            screen.draw.text('5000 de trigo', center=(200, 210), color="white", fontsize = 15)
            screen.draw.text(picos, center=(300, 195), color="black", fontsize = 15)
        if etapa >= 2:
            change_icono.draw()
# Mode taller_2
    elif mode == 'taller_2':
        fondo_taller_2.draw()
        salida_icono.draw()
        maquina_vapor_icono_2.draw()
        panel_solar_icono.draw()
        screen.draw.text('La maquina de vapor cuesta:', center=(200, 30), color="white", fontsize = 25)
        screen.draw.text('10000 de madera', center=(200, 70), color="white", fontsize = 15)
        screen.draw.text('1500 de piedra', center=(200, 80), color="white", fontsize = 15)
        screen.draw.text('10000 de trigo', center=(200, 90), color="white", fontsize = 15)
        screen.draw.text('100 de hierro bruto', center=(200, 100), color="white", fontsize = 15)
        screen.draw.text('50 de hierro refinado', center=(200, 110), color="white", fontsize = 15)
        screen.draw.text('El panel solar cuesta:', center=(200, 150), color="white", fontsize = 25)
        screen.draw.text('15000 de madera', center=(200, 180), color="white", fontsize = 15)
        screen.draw.text('2000 de piedra', center=(200, 190), color="white", fontsize = 15)
        screen.draw.text('150 de hierro bruto', center=(200, 200), color="white", fontsize = 15)
        screen.draw.text('100 de hierro refinado', center=(200, 210), color="white", fontsize = 15)        
        screen.draw.text('PIEDRA', center=(400, 50), color="black", fontsize = 21)
        screen.draw.text(piedra, center=(400, 70), color="white", fontsize = 21)
        screen.draw.text('TRRIGO', center=(400, 90), color="black", fontsize = 21)
        screen.draw.text(trigo, center=(400, 110), color="white", fontsize = 21)
        screen.draw.text('MADERA', center=(400, 130), color="black", fontsize = 21)
        screen.draw.text(madera, center=(400, 150), color="white", fontsize = 21)
        screen.draw.text('HIERRO BRUTO', center=(400, 170), color="black", fontsize = 21)
        screen.draw.text(hierro_bruto, center=(400, 190), color="white", fontsize = 21)
        screen.draw.text('HIERRO REFINADO', center=(400, 210), color="black", fontsize = 21)
        screen.draw.text(hierro_refinado, center=(400, 220), color="white", fontsize = 21)
        if numero_paneles >= 1:
            change_icono.draw()

#Mode seleccion
    elif mode == 'seleccion':
        fondo_1.draw()
        salida_icono.draw()
        bosque_icono.draw()
        iron_age_icono.draw()
        if ordenador == 'si':
            ordenador_icono.draw()
#Mode tesla
    elif mode == 'mode_tesla':
        fondo_electricidad.draw()
        salida_icono.draw()
        maquina_de_vapor_icono.draw()
        pala_icono.draw()
        boton_mas.draw()
        boton_menos.draw()
        screen.draw.text(carbon, center=(400, 70), color="black", fontsize = 30)
        screen.draw.text('CARBON', center=(400, 50), color="black", fontsize = 24)
        screen.draw.text(energia, center=(400, 140), color="black", fontsize = 30)
        screen.draw.text('ENERGÍA', center=(400, 120), color="black", fontsize = 24)
        if numero_paneles >= 1:
            panel_solar_icono.draw()
#Mode mercadona
    elif mode == 'mercadona':
        mercadona_fondo.draw()
        salida_icono.draw()
        axe_taller.draw()
        screen.draw.text('1 Cuesta 10000€', center=(70, 120), color="white", fontsize = 24)
        if puntos >= 10000 and hachas >= 1:
            pico_taller.draw()
            screen.draw.text('1 Cuesta 20000€', center=(70, 220), color="white", fontsize = 24)
        if etapa >= 2:
            maquina_vapor_icono_3.draw()
            screen.draw.text('1 Cuesta 100000€', center=(300, 120), color="white", fontsize = 24)
            panel_solar_icono_2.draw()
            screen.draw.text('1 Cuesta 200000€', center=(300, 220), color="white", fontsize = 24)
        change_icono.draw()
#Mode mercadona_2
    elif mode == 'mercadona_2':
        mercadona_fondo_2.draw()
        salida_icono.draw()
        madera_icono_1.draw()
        screen.draw.text('MADERA', center=(70, 120), color="black", fontsize = 24)
        screen.draw.text('1 Cuesta 1€', center=(70, 20), color="black", fontsize = 24)
        piedra_icono_1.draw()
        screen.draw.text('PIEDRA', center=(70, 270), color="black", fontsize = 24)
        screen.draw.text('1 Cuesta 2€', center=(70, 170), color="black", fontsize = 24)
        iron_icono_1.draw()
        screen.draw.text('H. CRUDO', center=(240, 120), color="black", fontsize = 24)
        screen.draw.text('1 Cuesta 5€', center=(240, 20), color="black", fontsize = 24)
        iron_age_icono_2.draw()
        screen.draw.text('H. REFINADO', center=(400, 120), color="black", fontsize = 24)
        screen.draw.text('1 Cuesta 10€', center=(400, 20), color="black", fontsize = 24)
        carbon_icono_1.draw()
        screen.draw.text('CARBON', center=(240, 275), color="black", fontsize = 24)
        screen.draw.text('1 Cuesta 1€', center=(240, 175), color="black", fontsize = 24)
        trigo_icono.draw()
        screen.draw.text('TRIGO', center=(400, 270), color="black", fontsize = 24)
        screen.draw.text('2 Cuestan 1€', center=(400, 170), color="black", fontsize = 24)
#Mode end
    elif mode == 'end':
        end_fondo.draw()
        fondo_end.draw()
        fin.draw()
        box_4.draw()
        box_5.draw()
        box_6.draw()
        taller_icono_2.draw()
        tienda_icono_2.draw()
#Mode taller_3
    elif mode == 'taller_3':
        fondo_taller_3.draw()
        ordenador_taller.draw()
        salida_icono.draw()
        screen.draw.text('EL ordenador cuesta:', center=(325, 70), color="white", fontsize = 35)
        screen.draw.text('20000 de madera', center=(325, 100), color="white", fontsize = 25)
        screen.draw.text('10000 de piedra', center=(325, 130), color="white", fontsize = 25)
        screen.draw.text('1000 de hierro bruto', center=(325, 160), color="white", fontsize = 25)
        screen.draw.text('1000 de hierro refinado', center=(325, 190), color="white", fontsize = 25)

def on_mouse_down(button, pos):
    global mode
    global puntos
    global dinero
    global etapa
    global madera
    global trigo
    global piedra
    global hierro_bruto
    global hierro_refinado
    global carbon
    global hachas
    global picos
    global granja_si_no
    global numero_granjas
    global numero_hachas
    global numero_picos
    global click_madera
    global click_piedra
    global click_hierro
    global click_carbon
    global axe_taller
    global maquina_vapor
    global numero_maquinas
    global tab
    global click_energia
    global perdida_energia
    global numero_paneles
    global energia_maquina
    global energia_panel
    global ordenador
#Modo Menu
    if mode == 'menu' and button == mouse.LEFT:
        if play.collidepoint(pos):
            if puntos >= 100000 and etapa >= 2:
                mode = 'seleccion'
            else:
                mode = 'etapa_1'
        elif taller_icono.collidepoint(pos):
            mode = 'taller'
        elif box_2.collidepoint(pos):
            mode = 'mode_fran'
        elif chispitas_icono.collidepoint(pos):
            mode = 'mode_tesla'
        elif box_1.collidepoint(pos):
            piedra = 1000000
            madera = 1000000
            trigo = 1000000
            hierro_bruto = 1000000
            hierro_refinado = 1000000
            carbon = 1000000
            dinero = 9999999
            puntos = 9999999
        elif tienda_icono.collidepoint(pos):
            mode = 'mercadona'
#Modo etapa_1
    elif mode == 'etapa_1' and button == mouse.LEFT:
        if madera_icono.collidepoint(pos):
            madera += click_madera
            madera_icono.y = 200
            animate(madera_icono, tween='bounce_end', duration=0.5, y=220)
        elif granja_icono.collidepoint(pos) and dinero >= 100:
            granja_si_no = 1
            dinero -= 100
            numero_granjas += 1
            schedule_interval(cosecha, 5)
            granja_icono.y = 60
            animate(granja_icono, tween='bounce_end', duration=0.5, y=80)
        elif hacha_icono.collidepoint(pos) and dinero >= 300:
            hacha_si_no = 1
            dinero -= 300
            numero_hachas += 1
            schedule_interval(hacha, 5)
            hacha_icono.y = 210
            animate(hacha_icono, tween='bounce_end', duration=0.5, y=220)
        elif piedra_icono.collidepoint(pos):
            time.sleep(1)
            piedra_icono.y = 200
            animate(piedra_icono, tween='bounce_end', duration=0.5, y=220)
            piedra += click_piedra
        elif vender_icono.collidepoint(pos):
            trigo /= 2
            piedra *= 3
            dinero += piedra
            dinero += madera
            dinero += trigo
            puntos += madera
            puntos += trigo
            puntos += piedra
            trigo = 0
            madera = 0
            piedra = 0
        elif salida_icono.collidepoint(pos):
            mode = 'menu'
        elif pico_icono.collidepoint(pos) and dinero >= 1000:
            dinero -= 1000
            numero_picos += 1
            schedule_interval(pico, 2)
            pico_icono.y = 210
            animate(pico_icono, tween='bounce_end', duration=0.5, y=220)
#Modo etapa_2
    elif mode == 'etapa_2' and button == mouse.LEFT:
        if iron_icono.collidepoint(pos):
            minar_icono.y = 90
            animate(minar_icono, tween='decelerate', duration=0.25, y=100)
            time.sleep(3)
            hierro_bruto += click_hierro
        elif vender_icono.collidepoint(pos):
            hierro_bruto *= 5
            hierro_refinado *= 10
            dinero += hierro_bruto
            dinero += hierro_refinado
            hierro_refinado = 0
            hierro_bruto = 0
        elif horno_icono.collidepoint(pos) and hierro_bruto >= 1:
            time.sleep(5)
            hierro_bruto -= 1
            hierro_refinado += 1
        elif salida_icono.collidepoint(pos):
            mode = 'seleccion'
        elif carbon_icono.collidepoint(pos):
            carbon_icono.y = 100
            animate(carbon_icono, tween='decelerate', duration=0.25, y=110)
            carbon += click_carbon
#Modo taller
    elif mode == 'taller' and button == mouse.LEFT:
        if axe_taller.collidepoint(pos) and madera >= 1000 and trigo >= 1000 and piedra >= 100:
            trigo -= 1000
            madera -= 1000
            piedra -= 100
            hachas += 1
            click_madera *= 2
            schedule_interval(hacha, 2)
            axe_taller.y = 90
            animate(axe_taller, tween='bounce_end', duration=0.5, y=100)
        elif pico_taller.collidepoint(pos) and madera >= 5000 and trigo >= 5000 and piedra >= 500:
            madera -= 5000
            trigo -= 5000
            piedra -= 500
            picos += 1
            click_piedra *= 2
            schedule_interval(pico_funcion_taller, 5)
            pico_taller.y = 220
            animate(pico_taller, tween='bounce_end', duration=0.5, y=230)
            if picos >= 1:
                etapa = 2
        elif salida_icono.collidepoint(pos):
            mode = 'menu'
        elif change_icono.collidepoint(pos):
            mode = 'taller_2'
#Modo taller_2
    elif mode == 'taller_2' and button == mouse.LEFT:
        if maquina_vapor_icono_2.collidepoint(pos) and madera >= 10000 and trigo >= 10000 and piedra >= 1500 and hierro_bruto >= 100 and hierro_refinado >= 50:
            trigo -= 10000
            madera -= 10000
            piedra -= 1500
            hierro_refinado -= 50
            hierro_bruto -= 100
            maquina_vapor =  'si'
            click_hierro *= 2
            click_madera *= 3
            click_piedra *= 3
            numero_maquinas += 1
            if numero_maquinas == 1:
                schedule_interval(electricidad_negativa, perdida_energia)
                schedule_interval(electricidad_positiva, 1) 
            schedule_interval(maquina_vapor_funcion, 5) 
            maquina_vapor_icono_2.y = 60
            animate(maquina_vapor_icono_2, tween='bounce_end', duration=0.5, y=70)
        elif panel_solar_icono.collidepoint(pos) and madera >= 20000 and trigo >= 20000 and piedra >= 2000 and hierro_bruto >= 350 and hierro_refinado >= 200:
            trigo -= 2000
            madera -= 2000
            piedra -= 2000
            hierro_refinado -= 200
            hierro_bruto -= 350
            panel_solar =  'si'
            click_hierro *= 10
            click_madera *= 10
            click_piedra *= 10
            click_carbon *= 10
            panel_solar_icono.y = 215
            numero_paneles += 1
            animate(panel_solar_icono, tween='bounce_end', duration=0.5, y=225)
        elif salida_icono.collidepoint(pos):
            mode = 'taller'
        elif change_icono.collidepoint(pos):
            mode = 'taller_3'
#Modo taller_3
    elif mode == 'taller_3' and button == mouse.LEFT:
        if salida_icono.collidepoint(pos):
            mode = 'menu'
        elif ordenador_taller.collidepoint(pos) and madera >= 20000 and piedra >= 10000 and hierro_bruto >= 1000 and hierro_refinado >= 1000:
            madera -= 20000
            piedra -= 10000
            hierro_refinado -= 1000
            hierro_bruto -= 1000
            ordenador = 'si'
            ordenador_taller.y = 140
            animate(ordenador_taller, tween='bounce_end', duration=0.5, y=150)
#Modo selección
    elif mode == 'seleccion' and button == mouse.LEFT:
        if bosque_icono.collidepoint(pos):
            mode = 'etapa_1' 
        elif iron_age_icono.collidepoint(pos):
            mode = 'etapa_2' 
        elif salida_icono.collidepoint(pos):
            mode = 'menu'
        elif ordenador_icono.collidepoint(pos) and ordenador == 'si':
            mode = 'end'
#Modo tesla
    elif mode == 'mode_tesla' and button == mouse.LEFT:
        if maquina_de_vapor_icono.collidepoint(pos):
            if maquina_vapor == 'si':
                maquina_de_vapor_icono.y = 60
                animate(maquina_de_vapor_icono, tween='bounce_end', duration=0.5, y=70)
        elif boton_mas.collidepoint(pos):
            if maquina_vapor == 'si':
                if tab < 10:
                    click_energia += 1
                    perdida_energia -= 0.1
                    tab += 0
        elif boton_menos.collidepoint(pos):
            if maquina_vapor == 'si':
                click_energia -= 1
                perdida_energia += 0.1
                tab -= 1
        elif salida_icono.collidepoint(pos):
            mode = 'menu'
#Modo mercadona
    elif mode == 'mercadona' and button == mouse.LEFT:
        if salida_icono.collidepoint(pos):
            mode = 'menu'
        elif change_icono.collidepoint(pos):
            mode = 'mercadona_2'
        elif axe_taller.collidepoint(pos) and dinero >= 10000:
            dinero -= 10000
            hachas += 1
            click_madera *= 2
            schedule_interval(hacha, 2)
            axe_taller.y = 90
            animate(axe_taller, tween='bounce_end', duration=0.5, y=100)
        elif pico_taller.collidepoint(pos) and dinero >= 20000:
            dinero -= 20000
            picos += 1
            click_piedra *= 2
            schedule_interval(pico_funcion_taller, 5)
            pico_taller.y = 220
            animate(pico_taller, tween='bounce_end', duration=0.5, y=230)
            if picos >= 1:
                etapa = 2
        elif maquina_vapor_icono_3.collidepoint(pos) and dinero >= 100000:
            dinero -= 100000
            maquina_vapor =  'si'
            click_hierro *= 2
            click_madera *= 3
            click_piedra *= 3
            numero_maquinas += 1
            if numero_maquinas == 1:
                schedule_interval(electricidad_negativa, perdida_energia)
                schedule_interval(electricidad_positiva, 1) 
            schedule_interval(maquina_vapor_funcion, 5) 
            maquina_vapor_icono_3.y = 60
            animate(maquina_vapor_icono_3, tween='bounce_end', duration=0.5, y=70)
        elif panel_solar_icono_2.collidepoint(pos) and dinero >= 200000:
            dinero -= 200000
            panel_solar =  'si'
            click_hierro *= 10
            click_madera *= 10
            click_piedra *= 10
            click_carbon *= 10
            panel_solar_icono_2.y = 215
            numero_paneles += 1
            animate(panel_solar_icono_2, tween='bounce_end', duration=0.5, y=225)
#Modo mercadona_2
    elif mode == 'mercadona_2' and button == mouse.LEFT:
        if salida_icono.collidepoint(pos):
            mode = 'mercadona'
        elif madera_icono_1.collidepoint(pos) and dinero >= 1:
            dinero -= 1
            madera += 1
            madera_icono_1.y = 60
            animate(madera_icono_1, tween='bounce_end', duration=0.5, y=70)
        elif piedra_icono_1.collidepoint(pos) and dinero >= 2:
            dinero -= 2
            piedra += 1
            piedra_icono_1.y = 215
            animate(piedra_icono_1, tween='bounce_end', duration=0.5, y=225)
        elif iron_icono_1.collidepoint(pos) and dinero >= 5:
            dinero -= 5
            hierro_bruto += 1
            iron_icono_1.y = 60
            animate(iron_icono_1, tween='bounce_end', duration=0.5, y=70)
        elif iron_age_icono_2.collidepoint(pos) and dinero >= 10:
            dinero -= 10
            hierro_refinado += 1
            iron_age_icono_2.y = 60
            animate(iron_age_icono_2, tween='bounce_end', duration=0.5, y=70)
        elif carbon_icono_1.collidepoint(pos) and dinero >= 1:
            dinero -= 1
            carbon += 1
            carbon_icono_1.y = 215
            animate(carbon_icono_1, tween='bounce_end', duration=0.5, y=225)
        elif trigo_icono.collidepoint(pos) and dinero >= 1:
            dinero -= 1
            trigo += 2
            trigo_icono.y = 215
            animate(trigo_icono, tween='bounce_end', duration=0.5, y=225)
def update(dt):
    global energia
    global energia_maquina
    global energia_panel
    global carbon
    schedule_interval(energia_limpia, 1)
    energia = energia_maquina + energia_panel
    if carbon <= 0:
        perdida_energia = 0,1
    else:
        perdida_energia = 1
def energia_limpia():
    global energia_panel
    energia_panel = 100 * numero_paneles
def electricidad_negativa():
    global energia_maquina
    energia_maquina -= 1
def electricidad_positiva():
    global energia_maquina
    global carbon
    if carbon >= click_energia:
        energia_maquina = 30 * click_energia
        carbon -= click_energia
def maquina_vapor_funcion():
    global carbon
    carbon += 1
def pico():
    global piedra
    piedra += 10
def pico_funcion_taller():
    global piedra
    piedra += 100
def pico():
    global piedra
    piedra += 10
def cosecha():
    global trigo
    trigo += 20
def hacha():
    global madera
    madera += 30