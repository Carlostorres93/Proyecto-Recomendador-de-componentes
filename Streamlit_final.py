#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st
import numpy as np
import pandas as pd
import requests
import math
import matplotlib.pyplot as plt
import seaborn as sns
import random


PS = pd.read_csv('power-supply_clean.csv')
CASE = pd.read_csv('case_clean.csv')
MB = pd.read_csv('motherboard_clean.csv')

# Configurar el tema de seaborn para todos los gráficos
sns.set_theme(style="darkgrid")

# Establecer el contexto y estilo de matplotlib para que coincida con el tema de Streamlit
plt.style.use('dark_background')

def mostrar_pantalla_de_inicio():
    st.title("Bienvenido al Maravilloso Mundo de los Componentes de Computadora")
    st.write("Configura tu PC y aprende, además, a diferenciar las características de cada uno de sus componentes principales.")
    st.image("https://hardzone.es/app/uploads-hardzone.es/2019/08/Intel-Tiger-Lake-01.jpg", use_column_width=True)  # URL de la imagen
    st.write("Elige en el menú lateral qué te apetece hoy")
def mostrar_historia():
    st.title("Historia del IT")
    imagen = "https://i.postimg.cc/x840s1KY/Evolucion-IT.jpg"
    st.image(imagen, use_column_width=True)

    # Estilo personalizado para los botones
    button_style = """
        border: 2px solid;
        border-color: #FFD700; /* Dorado */
        color: #FFD700 !important; /* Dorado */
        background-color: transparent;
        padding: 10px 15px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
    """

    # CSS personalizado para los botones
    st.markdown("""
    <style>
    .stButton>button {
        border: 2px solid;
        border-color: #FFD700; /* Dorado */
        color: #FFD700 !important; /* Dorado */
        background-color: transparent;
        padding: 10px 15px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
    }
    .stButton>button:hover {
        border-color: #FFD700; /* Dorado */
        background-color: #FFD700; /* Dorado */
        color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

    # Contenedor para los botones
    col1, col2, col3, col4 = st.columns(4)

    # Botones para seleccionar la sección de la historia
    if col1.button("Historia del PC", key="historia_pc", help="Haz clic aquí para leer la historia del PC"):
        st.subheader("Historia del PC")
        st.write("""Aunque los primeros ordenadores se crearon en los años 1940, éstos no utilizaban microprocesadores. 
Hasta los años 70, el ordenador era algo exclusivo de las grandes corporaciones. En 1943, el presidente de IBM, Thomas J. 
Watson , dijo: ‘Creo que hay un mercado para cinco computadoras en el mundo‘. Esto nos da idea de la exclusividad de los 
primeros tiempos. En 1971 se inventó el microprocesador, lo que trajo el desarrollo de los ordenadores personales y el 
surgimiento de toda una industria que cambiaría la sociedad.

Como hemos apuntado, la introducción del ordenador personal supuso una gran revolución, tanto en el mundo de la empresa como en los hogares. De pronto, aquello que todas las empresas hacían a mano se podía automatizar. Gestionar la contabilidad, hacer las nóminas o preparar informes no volvieron a ser lo mismo. Lo que se tardaba días en hacer, de pronto, se podía realizar en pocas horas.

Esta revolución llegó también al hogar, donde cada vez más personas abandonaban la máquina de escribir por la comodidad del procesador de textos. El ordenador personal supuso también una nueva forma de entretenimiento. El juego come cocos (Pac-man) o el simulador de vuelos de Microsoft (Microsoft Flight Simulator) son de aquella época. También lo son aplicaciones como la hoja de cálculo (Lotus 1-2-3), el procesador de textos (WordStar) o el gestor de bases de datos (dBase II o clipper).

## **Creación del entorno apropiado**

A finales de los años 1930 y principios de los 1940, a la Leland Stanford Junior University, más conocida como Universidad de Stanford, se les ocurrió la idea de alquilar terrenos de la universidad para crear el Parque Industrial Stanford.

En ese entorno se crearon empresas míticas como Schockley Semiconductor Laboratory. Esta empresa fue fundada por William Schockley, premio Nobel y coinventor del transistor. Empleados de Schockley crearon Fairchild Semiconductor en 1957. Fairchild es la primera empresa mundial que trabajaba exclusivamente con silicio. A su vez, empleados de Fairchild, ya desaparecida, crearon otras compañías importantes de semiconductores de la zona, entre ellas Intel o AMD.

A comienzos de 1970, toda la zona de Silicon Valley estaba repleta de empresas de semiconductores que abastecían a las empresas de ordenadores, también situadas en la zona. El entorno de Silicon Valley ha jugado un papel clave en la historia de los microprocesadores. De hecho, la mayoría de las empresas importantes del sector, siguen teniendo sede en este lugar.""")
        imagen_garage_pc = "https://i.postimg.cc/htw2SW0j/ordenador-personal-garaje-hewlet-packard-600x270-1.jpg"
        st.image(imagen_garage_pc, use_column_width=True)
        st.caption("<span style='color: white;'>Garaje en el que empezó Hewlett-Packard</span>", unsafe_allow_html=True)
        
        st.write("""Silicon Valley ha dado lugar a muchas historias. La más conocida quizás sea la de los ‘chicos del garaje‘. Willian R. Hewlett y David Packard fueron alumnos de Universidad de Stanford. Para poder ganar algo de dinero, decidieron instalar un pequeño taller de electrónica en el garaje de la casa donde se alojaban. Construyeron un oscilador de audio, un instrumento de prueba utilizado por los ingenieros de sonido. Se vendió tan bien que, en 1939 acabaron creando la compañía Hewlett-Packard. Tan solo dos años más tarde, ya tenían un centenar de empleados, diez años después contaban con 200, y en 1984 alcanzaron los 80.000 empleados.

Gracias a al ambiente tecnológico e industrial creado por la universidad de Stanford, la zona ha atraído a multitud de emprendedores e inversores que ha dado como resultado a este ecosistema único.

Por cierto, el nombre de Silicom Valley o Valle del Silicio se lo dio C. Hoefleren 1971 cuando era director de un pequeño semanario llamado Microelectronics News.

## **Nacimiento del microprocesador**

En el año 1971, la empresa japonesa Busicom, fabricante de calculadoras, contactó con Intel para que le integrara en un solo chip todos los circuitos electrónicos de su nueva calculadora. Intel le encargó este proyecto a Ted Hoff, quien, en vez de hacer un circuito cerrado para ese propósito específico, se le ocurrió hacer un procesador de información de uso general. La particularidad era que podía ser programado para distintas tareas.

A finales de 1971 Intel tenía disponible su nuevo circuito integrado: el Intel 4004. Como se trataba de un tipo de circuito diferente, al año siguiente le dieron el nombre de microprocesador. Rápidamente se vio el gran potencial de este nuevo tipo de circuitos. Distintas empresas se apuntaron. En 1974 ya había 19 modelos de microprocesadores, en 1975 el número era de 40, y en 1976, de 54.""")
        imagen_primer_procesador = "https://i.postimg.cc/yd7qfGnY/ordenador-personal-Intel-C4004-300x193-1.jpg"
        st.image(imagen_primer_procesador, use_column_width=True)
        st.caption("<span style='color: white;'>Intel 4004, primer procesador de la historia</span>", unsafe_allow_html=True)
        
        st.write("""El Intel 4004 constaba de 2300 transistores, un sumador de números de 4 bits, 16 registros de 4 bits, un registro acumulador, una pequeña pila de estados lógicos (stack), un bus de datos de 4 bits, un juego de 45 instrucciones y podía gestionar hasta 45 bytes.

El Intel 8008, creado en 1972, mejoraría considerablemente las características de su predecesor. En cualquier caso, aunque estos primeros microprocesadores tenían ciertas capacidades de programación, en realidad estaban pensados para cumplir una función específica, por ejemplo, ser utilizados para fabricar una calculadora.

En 1974 aparece el que se considera como el primer microprocesador de propósito general: el Intel 8080. Su juego de instrucciones se aumentó a 111 y su capacidad de direccionamiento a 64 Kbytes. Con el Intel 8080 se empezó a imaginar claramente el gran potencial que tenían estos pequeños chips.""")
        imagen_microprocesadores = "https://i.postimg.cc/kD3LbhVm/microprocesador-I8080-M6800-chips-600x220-1.jpg"
        st.image(imagen_microprocesadores, use_column_width=True)
        st.caption("<span style='color: white;'>Microprocesadores Intel 8080 y Motorola 6800</span>", unsafe_allow_html=True)
        
        st.write("""Ese mismo año nació otro mito: el primer microprocesador de Motorola, el M6800. Este microprocesador fue utilizado por varios de los primeros ordenadores creados en los años 1970.

## **Los primeros ordenadores personales**

Hasta la fecha, los ordenadores eran sistemas grandes y caros que solo se podían permitir los gobiernos y las grandes empresas. Además, los usuarios finales de estos equipos no interactuaban directamente con la máquina, sino que preparaban las tareas en tarjetas perforadas que luego introducían en el ordenador para que las ejecutara. La última tecnología de estos grandes equipos, a los que curiosamente se les llamaba minicomputadoras, los equipaba con multitud de chips individuales, pero no disponían de microprocesadores en un chip.

La primera aportación de los microprocesadores al mundo de los ordenadores se produjo de la mano de los ordenadores personales. Esto es, se empezaron a crear pequeños ordenadores de uso individual. Estas primeras unidades se vendían a menudo como un kit electrónico dirigido principalmente a aficionados. Por ejemplo, la revista de electrónica estadounidense Radio-Electronics presentó en 1974 el kit Mark-8 (basado en el Intel 8008). Poco después, la revista Popular Electronics describía cómo fabricarse un ordenador basado en el Intel 8080.""")
        imagen_revistas = "https://i.postimg.cc/fbyZZpm2/ordenador-personal-revistas-600x385-1.jpg"
        st.image(imagen_revistas, use_column_width=True)
        st.caption("<span style='color: white;'>Revistas de electrónica de la época</span>", unsafe_allow_html=True)
        
        st.write("""Aunque no tiene nada que ver con la historia, permítanme mencionar que yo mismo construiría uno de estos unos años más tarde. En aquel caso, rediseñe las placas de circuito impreso para adaptar el equipo a los componentes que encontré en las tiendas de electrónica de mi barrio. Hay que recordar que, en aquellos tiempos no había Internet. El microprocesador utilizado fue el MOS 6502, la CPU más barata que vendían entonces.

## **Los primeros ordenadores que tuvimos en casa**

Se suele decir que 1977 fue el año del lanzamiento masivo de los ordenadores personales. Los más famosos en Estados Unidos fueron el Apple II (evolución del Apple I que Steve Wozniak había construido en su garaje pocos años antes), el TRS-80 (Tandy Radio Shack Z-80) y el Commodore PET 2001. En Europa teníamos el ZX Spectrum o los CPC de Amstrad. EL Apple II y el primer modelo de Commodore utilizaban los microprocesadores 6502 de MOS. Los otros tres modelos utilizaban los microprocesadores Z80 de Zilog. Se vendieron millones de unidades.""")
    
        imagen_ordenadores = "https://i.postimg.cc/j5RHL6qF/ordenador-personal-commodore-spectrum-600x200-1.jpg"
        st.image(imagen_ordenadores, use_column_width=True)
        st.caption("<span style='color: white;'>Ordenadores Commodore 64 y ZX-spectrum</span>", unsafe_allow_html=True)
        
        st.write("""En 1978 apareció otro famoso microprocesador: el Intel 8086. Éste disponía de un bus de datos de 16 bits y una capacidad de direccionamiento de 1 Megabytes. Le siguieron muchos otros microprocesadores, como el Z8000 de Zilog, el NS16000 de National, el TI9900 de Texas Instruments o el 68000 de Motorola. Éste último es el que venía en los primeros modelos de Apple Macintosh lanzados en los años 1980.

## **Nacimiento del IBM PC**

IBM vio el gran potencial que estaban teniendo los ordenadores personales. En 1980 crearon un equipo, dirigido por William C. Lowe, para diseñar el ordenador personal de IBM. Este equipo recomendó que, para acelerar el proceso de fabricación, debiera hacerse un diseño abierto donde los componentes fueran aportados por otros fabricantes.

En agosto de 1981 IBM lanzó un nuevo ordenador personal al que denominó IBM PC (por personal computer). Este primer PC no solo cambiaría drásticamente la historia de la informática doméstica y empresarial, sino que lanzaría al estrellato a empresas como Microsoft e Intel. Microsoft aportaría el sistema operativo DOS e Intel aportaría el microprocesador de arquitectura x86.

Cuando se creó el primer PC, los ordenadores personales de la época eran de 8 bits (bus interno). No obstante, el legendario fundador de Microsoft Corporation, Bill Gate, convenció a IBM para hacer del PC un ordenador de 16 bits. IBM eligió el microprocesador 8088 de Intel para su primer PC. Este tenía un bus interno de 16 bits, pero a diferencia del 8086, su bus de datos externo era de tan sólo 8 bits, con lo que podía trabajar con los componentes de 8 bits, que en esa época eran mucho más baratos y abundantes que los de 16 bits.""")
        imagen_ordenador_personal = "https://i.postimg.cc/mDqYZPkc/ordenador-personal-IBM-PC-de-1981-600x400-1.jpg"
        st.image(imagen_ordenador_personal, use_column_width=True)
        st.caption("<span style='color: white;'>Ordenador personal IBM-PC de 1981</span>", unsafe_allow_html=True)
        
        st.write("""Cuando IBM se decidió por utilizar la arquitectura x86 de Intel, no quería depender de un solo proveedor. Así que le exigió a Intel que licenciara la fabricación de sus microprocesadores para que otras empresas pudieran fabricarlos. Entre ellas, estaba AMD. Aunque unos años más tarde Intel dejó de licenciar sus diseños, esto fue el comienzo de la lucha tecnológica entre Intel y AMD (ver el artículo Historia de Intel vs AMD).

## **Cómo Microsoft se hizo con el sistema operativo del IBM PC**

IBM quiso desarrollar el proyecto del PC a corto plazo. Como no tenían un sistema operativo propio para este proyecto, lo buscaron fuera. Un ingeniero de software amigo del Lowe, el Director del proyecto, conocía vagamente a Bill Gates. En aquel tiempo, Gates tenía 24 años y había abandonado la Universidad de Harvard para entrar en el negocio de los ordenadores. Había creado la empresa Microsoft y ya contaba con 31 empleados.

En julio de 1980 se reunieron con Gates y, lo cierto, es que no les impresionó. Así que acudieron a la que entonces era la empresa de software más reconocida del momento, Digital Research. Sin embargo, el Presidente de Digital, Gary Kildall, prefirió no asistir a la reunión porque quería pilotar su avión nuevo. Los abogados que acudieron en su lugar se centraron en temas legales. Los de IBM se fueron con la impresión de que Digital no les tomaba en serio y que su única opción a corto plazo era Microsoft.

Por su parte, Bill Gates se dio cuenta que Microsoft no podía escribir un sistema operativo desde cero en los plazos que les marcaba IBM. Para resolverlo, compró un sistema operativo llamado QDOS (acrónimo de Quick and Dirty Operating System) para adaptarlo. Microsoft pagó 75.000 dólares por QDOS. IBM quería que Microsoft fuese completamente responsable de hacer funcionar el sistema operativo. Así que Microsoft conservó todos los derechos del mismo.""")
        imagen_msdos = "https://i.postimg.cc/fTWzW849/ordenador-personal-MSDOS-600x257-1.jpg"
        st.image(imagen_msdos, use_column_width=True)
        st.caption("<span style='color: white;'>Sistema operativo MS-DOS</span>", unsafe_allow_html=True)
        
        st.write("""Microsoft terminó desarrollando el sistema operativo del IBM PC y le puso el nombre MS-DOS, sistema operativo de disco (IBM lo vendía como PC-DOS). Gracias a esto, y a que tenía todos los derechos del mismo, Microsoft terminaría estableciendo los estándares del sistema operativo del PC. Diez años más tarde, Microsoft alcanzaría el valor de mercado de 27.000 millones de dólares.

Aunque le salieron algunos competidores, como el DR-DOS (Digital Research DOS) surgido en 1988, finalmente Microsoft dominó completamente este mercado.

## **Gloria y muerte de IBM PC**

Nadie se imaginó lo que sucedería a continuación. Las ventas del ordenador IBM PC superaron todas las expectativas. El PC de IBM generó el primer año más de mil millones de dólares en ingresos. Otras empresas, como Apple o Tandy Corp ya vendían ordenadores personales desde hacía tiempo (desde 1977), pero hasta que IBM no creó su famoso PC no estalló el mercado. EL IBM PC se convertiría en el estándar de la industria.

Este éxito atrajo a otras muchas marcas a crear sus propios ordenadores compatibles con el de IBM. En 1982, Compaq replicó legalmente el BIOS de IBM PC, demostrando que podía copiarse. Luego empezaron a aparecer empresas que vendían modelos clónicos a un precio muy inferior. El primer clon compatible con PC fue lanzado en junio de 1982, menos de un año después del debut del PC.

Adicionalmente, el software para PC creció rápidamente. Se habló que un año después del lanzamiento del PC había más de 750 paquetes de software disponibles. Esto es cuatro veces más que lo que consiguió Apple el primer año.

Todo lo anterior hizo que el mercado de clientes de este tipo de ordenadores creciera fuertemente. El interés no estaba solo en la empresa, sino que más de la mitad de las ventas eran a usuarios particulares. En 1984, los ingresos de IBM del mercado del PC eran de 4.000 millones de dólares.

Sin embargo, IBM era un empresa gigante. El grueso de su negocio no era la venta de PC, por lo que nunca le prestó una excesiva atención. Aunque, excepcionalmente había logrado desarrollar el PC muy rápidamente, IBM era una empresa muy burocrática. En cuanto se normalizaron los procedimientos internos, empezaron a alejarse del mercado y cometer grandes errores estratégicos. El resultado fue que en 2005, el fabricante chino de ordenadores Lenovo Group compró el negocio de PC de IBM por 1.750 millones de dólares.

El gran mérito del IBM PC
IBM no inventó el ordenador personal, ni hizo ningún descubrimiento tecnológico relevante en relación con este tipo de ordenadores. Hay quien piensa que si no hubiese existido IBM, la historia de los ordenadores personales se habría desarrollado de una forma similar. Quizás Apple, Tandy, Commodore o Sinclair habrían jugado un papel más relevante, pero nada más.

En cualquier caso, lo cierto es que, a diferencia de las otras empresas, IBM construyó un ordenador con una arquitectura abierta, no se guardó ningún secreto. Sus componentes eran genéricos, podían encontrarse fácilmente. Cualquier fabricante podía hacer su PC y comercializarlo. Los desarrolladores de software encontraron también un entorno ideal donde desenvolverse. Posiblemente sin darse cuenta, IBM creo un ecosistema que facilitó el rápido desarrollo y expansión de los ordenadores personales. Este, en mi opinión, ha sido su gran mérito.

En enero de 1983, la revista Time no proclamó un ‘Hombre del año’, como era habitual, sino a una ‘Máquina del año: el PC’.

## **Evolución del ordenador personal**

A lo largo de este milenio el ordenador personal ha evolucionado mucho. Los microprocesadores son cada vez más potentes, las pantallas tienen más resolución y están desapareciendo los elementos mecánicos. Esto hace posible que los ordenadores sean más pequeños y versátiles. Un PC actual trabaja unas cien mil veces más rápido que uno de los primeros modelos.

Por otro lado, Internet está cada vez más presente en la informática. Cada vez hay más aplicaciones que funcionan online y el almacenamiento local se está cambiando por tenerlo todo en la nube. Los grandes proveedores de software están dejando de vender productos para convertirse en proveedores de servicios. No venden programas, sino el uso del mismo.

Los smartphones y las tablets están jugando también un papel significativo. Hace no muchos años, si necesitabas utilizar una aplicación, solo tenías la opción de hacerlo en un ordenador personal. Hoy en día todos llevamos un teléfono móvil encima y, para mucha gente, esto es todo lo que necesitan.

Es posible que en los próximos años haya un cambio de paradigma y que deje de tener sentido disponer de un ordenador personal muy potente. En su lugar, bastará con tener un pequeño terminal desde donde acceder a los servicios a través de Internet. Además, nos servirá cualquier terminal, propio o ajeno.""")

    if col2.button("Breve historia de los microprocesadores", key="historia_microprocesadores", help="Haz clic aquí para leer sobre la historia de los microprocesadores"):
        st.subheader("Breve historia de los microprocesadores")
        st.write("""Desde que se fabricó el primer microprocesador en 1971 ha habido un esfuerzo constante por mejorar 
sus prestaciones. Teniendo en cuenta que se trata de un producto de muy alta tecnología, 
es de destacar la gran cantidad de inversión e ingenio que han sido necesarios derrochar para mantenerse vivo en esta carrera 
sin fin. Las aplicaciones de estos chips han crecido inmensamente y hoy en día forman parte de la mayoría de los equipos 
electrónicos que nos rodean. Estamos acostumbrados a una renovación tecnológica constante, por lo que las expectativas 
futuras en estos dispositivos siguen siendo muy elevadas. Echémosle un breve vistazo a la historia de los microprocesadores.""")
        imagen_calendario = "https://i.postimg.cc/pLg2PxY0/microprocesador-calendario-prehistoria-600x380-1.jpg"
        st.image(imagen_calendario, use_column_width=True)
        st.caption("<span style='color: white;'>Calendario de acontecimientos históricos relacionados con el microprocesador (prehistoria)</span>", unsafe_allow_html=True)
        
        st.write("""## **La creación de Silicon Valley, el entorno apropiado**

Para simplificarlo, se puede decir que los orígenes más recientes de la industria informática se remontan a finales de los años 1940. El hecho es que la Leland Stanford Junior University, con el objeto de conseguir dinero con el que poder atraer a buenos profesores para impulsar el desarrollo de la universidad, se les ocurrió crear el Parque Industrial Stanford alquilando los terrenos de la universidad.

Por ejemplo, en esta universidad estaban como alumnos Willian R. Hewlett y David Packard, los cuales, animados por el entonces famoso profesor Terman, decidieron instalar un pequeño taller de electrónica en el garaje de la casa donde se alojaban con el objeto de ganar algo de dinero. Acabaron creando la compañía Hewlett-Packard y, tan solo dos años más tarde, ya tenían un centenar de empleados, diez años después contaban con 200, y en 1984 alcanzaron los 80.000 empleados.

Todo esto ocurrió, no sólo gracias al ingenio de los “chicos del garaje”, sino, sobre todo, gracias al ambiente tecnológico e industrial creado por la universidad, y a los emprendedores y empresarios de la zona. Después de recibir varios nombres, al final la zona es conocida como Valle del Silicio o Silicon Valley. Este nombre se lo dio en 1971 C. Hoefler, director de un pequeño semanario llamado Microelectronics News.

En ese mismo lugar se fundó en 1957 Fairchild Semiconductor, primera empresa mundial que trabajaba exclusivamente con silicio. En Fairchild se inventó el primer circuito integrado en 1959. De esta empresa, ya desaparecida, nacieron todas las compañías importantes de semiconductores de la zona, entre ellas Intel. Fairchild se fundó con expertos procedentes de Schockley Semiconductor Laboratory, empresa fundada años atrás por el doctor William Schockley, premio Nobel y coinventor del transistor junto con John Barden y Walter Brattain en los laboratorios Bell.

A comienzos de 1970, toda la zona de Silicon Valley estaba repleta de empresas de semiconductores que abastecían a las de ordenadores, también locales. El entorno de Silicon Valley ha jugado un papel clave en la historia de los microprocesadores. De hecho, la mayoría de las empresas importantes del sector, siguen teniendo sede en este lugar.""")
        imagen_calendariodos = "https://i.postimg.cc/bN9CzRx4/Microprocesador-Calendario-Precedentes-600x412-1.jpg"
        st.image(imagen_calendariodos, use_column_width=True)
        st.caption("<span style='color: white;'>Calendario de acontecimientos históricos relacionados con el microprocesador (precedentes)</span>", unsafe_allow_html=True)
        
        st.write("""## **El primer microprocesador, el Intel 4004**

En el año 1971, la empresa japonesa Busicom pensó lanzar una nueva gama de calculadoras. La novedad tecnológica que se les ocurrió fue integrar sus circuitos electrónicos en un solo chip. Para fabricar estos nuevos circuitos integrados contactaron con Intel. Este proyecto lo dirigió Ted Hoff y, en vez de hacer un circuito integrado particular para esta calculadora, se le ocurrió hacer un procesador de información de uso general.

El 15 de octubre de 1971, Intel anunció su nuevo circuito integrado, el Intel 4004. Como se trataba de un tipo de circuito diferente, al año siguiente le dieron el nombre de microprocesador. Este fue el comienzo de la historia de los microprocesadores. En 1974 ya había 19 modelos de microprocesadores, en 1975 el número era de 40, y en 1976, de 54.

El Intel 4004 constaba de 2300 transistores, un sumador de números de 4 bits, 16 registros de 4 bits, un registro acumulador, una pequeña pila de estados lógicos (stack), un bus de datos de 4 bits, un juego de 45 instrucciones y podía gestionar hasta 45 bytes.

En 1972, Intel creó el 8008, mejorando considerablemente las características de su predecesor. Contaba con un bus de datos de 8 bits, un juego de 66 instrucciones y capacidad para direccionar hasta 16 Kbytes.

## **Historias alternativas al primer microprocesador**

Aunque la anterior es la historia más aceptada del origen del microprocesador, lo cierto es que en aquellos años hubo muchos ingenieros trabajando en la misma idea por distintos motivos. Como ocurre en otras ocasiones, es posible que la historia oficial no coincida exactamente con la realidad. Aunque no entremos en detalles, creo que merece la pena mencionar algunas alternativas:

- Gilbert Hyatt dice que inventó un microprocesador de un solo chip en 1968.

- La empresa Four-Phase Systems afirma haber diseñado su microprocesador AL1 en 1969 (liderado por Lee Boysel) .

- Texas Instruments (ingenieros Gary Boone y Michael Cochran) tuvieron listo su procesador de un solo chip casi al mismo tiempo que Intel, aunque no lo comercializarían hasta 1974.

- También podemos mencionar los trabajos pioneros de Ray Holt y Steve Geller de la compañía Garrett AiResearch o la del ingeniero Gus Roche de la empresa Computer Terminal Corporation (CTC).

## **El primer microprocesador de propósito general**

Aunque estos primeros microprocesadores tenían ciertas capacidades de programación, en realidad estaban pensados para cumplir una función específica, por ejemplo, ser utilizados para fabricar una calculadora. De hecho, el primer producto comercial en utilizar un microprocesador fue la calculadora Busicom 141-PF.

En 1974 aparece el Intel 8080. Este es considerado como el primer microprocesador de propósito general. Su juego de instrucciones se aumentó a 111 y su capacidad de direccionamiento a 64 Kbytes. Esto no solo supuso un tremendo avance en su potencial, sino que se empezó a imaginar que estos pequeños chips podían llegar a tener un potencial mucho mayor que el de ser un simple componente de una calculadora.

Ese mismo año nació otro mito, el primer microprocesador de Motorola, el M6800. Este microprocesador sería el utilizado por el exitoso ordenador Altair 8800.

## **Qué es un microprocesador**

El microprocesador es un chip electrónico que tiene la particularidad de leer un código de programa y ejecutar cada una de las acciones especificadas en dicho código. Algo que no es menos importante es que se puede comunicar con el exterior del chip leyendo valores y transmitiendo los suyos.

Para poder realizar este trabajo, las partes básicas del microprocesador son las siguientes:

- Unidad aritmético-lógica, ALU, que realiza las operaciones matemáticas.

- Unidad de control, que interpreta las instrucciones del programa y genera las respuestas adecuadas.

- Registros de almacenamiento para guardar datos y estados de forma temporal.""")
        imagen_partes = "https://i.postimg.cc/6376K3F1/microprocesador-partes-600x292-1.jpg"
        st.image(imagen_partes, use_column_width=True)
        st.caption("<span style='color: white;'>Partes de un microprocesador</span>", unsafe_allow_html=True)
        
        st.write("""Para sincronizar sus acciones, el microprocesador necesita los pulsos que emite un dispositivo llamado reloj. Por cada pulso, o por cada cierto número de pulsos, el microprocesador ejecuta una instrucción, pudiendo necesitar cada instrucción un número de pulsos distinto. El número de pulsos que se emiten cada segundo es la frecuencia de reloj. Originariamente las frecuencias eran del orden de MHz (megahercios o millones de pulsos por segundo) y hoy en día son del orden de GHz (miles de millones de pulsos por segundo). El microprocesador va ejecutando unas instrucciones a continuación de otras, tanto más rápidamente cuanta mayor frecuencia tenga su reloj.

Las distintas partes del microprocesador se comunican entre si a través de unos canales de comunicación internos llamados bus interno, por cada uno de estos canales circula un bit simultáneamente. Cuantos más bits tenga el bus interno, más información simultánea podrá intercambiar, y por tanto, más rápidamente funcionará.

Para que el microprocesador pueda comunicarse con el resto de los componentes del equipo del que forma parte (por ejemplo con las memorias, monitor o periféricos del ordenador) se dispone de un canal de comunicación conocido como bus externo. Cuantos más bits tenga el bus externo, más rápidamente se comunicará con el exterior y mejor será el rendimiento del conjunto.

##**Qué es la arquitectura de un microprocesador**

Todas las partes de los microprocesadores se construyen con un elemento electrónico elemental conocido como transistor. Cada microprocesador está formado por millones de transistores. Se conoce como arquitectura del microprocesador a la forma como están organizados estos transistores. Esto es, los componentes internos que forman el microprocesador y su organización.

Se puede decir que la arquitectura es lo que marca el rendimiento del microprocesador. De hecho, la potencia de los microprocesadores depende fundamentalmente de los bien organizado y equilibrado que estén sus componentes y, en segundo lugar, del número de componentes (transistores) que contenga.

Desde que se construyó el primer microprocesador, la obsesión de los fabricantes ha sido siempre conseguir chips que realicen un mismo proceso cada vez más rápido. Para ello, entre otras muchas cosas, se han mejorado los circuitos para que puedan soportar frecuencias de reloj más elevadas, ampliado el tamaño de los buses internos y externos, mejorando la construcción interna de la unidad de control o introduciendo más de una unidad de control en el mismo microprocesador.

Para hacernos una idea de lo que significa un cambio de arquitectura, cuando aparecieron los primeros microprocesadores, sus unidades de control se construían con la capacidad de poder interpretar un juego de instrucciones muy amplio (en lenguaje máquina), con la idea de facilitarle la labor a los programadores. Esto es lo que posteriormente se ha venido a llamar arquitectura CISC (Complex Instruction Set Computer, microprocesadores con juego de instrucciones complejo).

Todo fue bien hasta que en 1975 se hicieron estudios estadísticos y se dieron cuenta de que muchas de las instrucciones no eran apenas utilizadas. Esto les llevó a un replanteo del juego de instrucciones, logrando un microprocesador cuyo juego de instrucciones era mucho más reducido, teniendo además la ventaja de que se ejecutaban en un solo ciclo de reloj. El resultado es que se reducía considerablemente los tiempos medios de ejecución de los programas. A esta nueva forma de construir los microprocesadores se ha venido a llamar arquitectura RISC (Reduced Instruction Set Computer, microprocesadores con juego de instrucciones reducido). De forma general se puede decir que un microprocesador es RISC cuando todas sus instrucciones se realizan en un solo ciclo de reloj.

A lo largo de los años se han ido diseñando muchas nuevas arquitecturas. Cada una de ellas aportaba nuevas prestaciones al microprocesador, haciéndolo destacar en su lucha por el liderazgo tecnológico. Por ejemplo, la arquitectura Banias de Intel les permitió destacar en 2006 con sus nuevos microprocesadores Core 2. Intel mantuvo su liderazgo hasta que AMD sacó en 2017 una nueva arquitectura, llamada Zen, con la que superó en rendimiento a los microprocesadores de Intel.

## **El primer ordenador con microprocesador**

Hasta la fecha, los ordenadores eran sistemas grandes y caros que solo se podían permitir los gobiernos y las grandes empresas. Además, los usuarios finales de estos equipos no interactuaban directamente con la máquina, sino que preparaban las tareas en tarjetas perforadas que luego introducían en el ordenador para que las ejecutara. La tecnología de estos grandes equipos, a los que curiosamente se les llamaba minicomputadoras, los equipaba con multitud de chips individuales, pero no disponían de microprocesadores en un chip.

La primera aportación de los microprocesadores al mundo de los ordenadores se produjo de la mano de los ordenadores personales. Esto es, se empezaron a crear pequeños ordenadores de uso individual. Estas primeras unidades se vendían a menudo como un kit electrónico dirigido principalmente a aficionados. Por ejemplo, la revista de electrónica estadounidense Radio-Electronics presentó en 1974 el kit Mark-8 (basado en el Intel 8008). Poco después, la revista Popular Electronics describía cómo fabricarse un ordenador basado en el Intel 8080.""")
        imagen_altair = "https://i.postimg.cc/W1Pd7Mxp/microprocesador-altair-8800-600x428-1.jpg"
        st.image(imagen_altair, use_column_width=True)
        st.caption("<span style='color: white;'>MITS Altair 8800, el primer ordenador personal de éxito (1975)</span>", unsafe_allow_html=True)
        
        st.write("""Se suele decir que 1977 fue el año del lanzamiento masivo de los ordenadores personales. Los más famosos en Estados Unidos fueron el Apple II (evolución del Apple I que Steve Wozniak había construido en su garaje pocos años antes), el TRS-80 y el Commodore PET 2001. En Europa teníamos el ZX Spectrum o los CPC de Amstrad. EL Apple II y el primer modelo de Commodore utilizaban los microprocesadores 6502 de MOS. Los otros tres modelos utilizaban los microprocesadores Z80 de Zilog. Se vendieron millones de unidades.

En 1978 apareció otro famoso microprocesador: el Intel 8086. Éste disponía de un bus de datos de 16 bits y una capacidad de direccionamiento de 1 Megabytes. Le siguieron muchos otros microprocesadores, como el Z8000 de Zilog, el NS16000 de National, el TI9900 de Texas Instruments o el 68000 de Motorola. Éste último es el que venía en los primeros modelos de Apple Macintosh lanzados en los años 1980.""")
        imagen_sinclair = "https://i.postimg.cc/5yBHCgbC/Microprocesador-Sinclair-ZX-Spectrum48k-600x414-1.jpg"
        st.image(imagen_sinclair, use_column_width=True)
        st.caption("<span style='color: white;'>Ordenador Sinclair ZX Spectrum (el monitor era la TV) y su microprocesador Z80 de Zilog</span>", unsafe_allow_html=True)
        
        st.write("""## **Los microprocesadores de Intel**

Intel ha jugado un papel fundamental en la historia de los microprocesadores. No solo ideó el primer microprocesador, sino que, como veremos, ha estado siempre presente en el desarrollo de nuevos modelos. La historia de los ordenadores personales y de Intel han ido siempre de la mano.

La empresa IBM, fundada en 1911, se dedicaba a desarrollar y fabricar grandes ordenadores. Sin embargo, vio interesante introducirse en este floreciente mercado de los ordenadores domésticos. Para poder desarrollar el proyecto de forma rápida, en vez de hacerlo todo ellos mismos, como hacían siempre, pensaron que sería mejor contar con componentes existentes de otras empresas. Lograron terminar el proyecto en tan solo un año.

En agosto de 1981, IBM lanzó un nuevo ordenador personal al que denominó IBM PC (por personal computer u ordenador personal). Este primer PC no solo cambiaría drásticamente la historia de la informática doméstica y empresarial, sino que lanzaría al estrellato a empresas como Microsoft e Intel.

Cuando se creó el primer PC, los ordenadores personales de la época eran de 8 bits (bus interno), sin embargo, el legendario fundador de Microsoft Corporation, Bill Gate, convenció a IBM para hacer del PC un ordenador de 16 bits, e IBM eligió el microprocesador 8088 de Intel para su primer PC. Este tenía un bus interno de 16 bits, pero a diferencia del 8086, su bus de datos externo era de tan sólo 8 bits, con lo que podía trabajar con los componentes de 8 bits, que en esa época eran mucho más baratos y abundantes que los de 16 bits.""")
        imagen_ibm = "https://i.postimg.cc/vmKXqY9v/Microprocesador-IBM-PC-XT-600x460-1.jpg"
        st.image(imagen_ibm, use_column_width=True)
        st.caption("<span style='color: white;'>Ordenador IBM PC con microprocesador Intel 8088</span>", unsafe_allow_html=True)
        
        st.write("""IBM decidió comercializar este nuevo equipo como una arquitectura abierta. Esto suponía que otros fabricantes pudieran producir y vender componentes periféricos y software compatible sin necesidad de pagar licencias. El resultado es que a IBM le siguieron muchas otras marcas de ordenadores que fabricaban PC compatibles. El mercado creció tremendamente e Intel empezó siendo el proveedor de microprocesadores de todos.

La importancia de Intel fue tal que los PC fueron evolucionando sus equipos conforme Intel desarrollaba nuevos microprocesadores más potentes. Fueron muy relevantes sus microprocesadores 286, 386 y 486.

Intel era la pionera en este campo, pero las empresas fabricantes de ordenadores necesitaban más proveedores para garantizarse el suministro en caso de que Intel no pudiera abarcar toda la demanda. Esto llevó a Intel a dar licencias a otras empresas para que pudieran fabricar chips utilizando su arquitectura y sus diseños. El papel de estos otros fabricantes empezó a ser cada vez más relevante, sobre todo el de AMD, por lo que Intel cambió de opinión unos años más tardes. Intel dejó de dar licencias de sus microprocesador a partir de su modelo Pentium.

## **Otros fabricantes de microprocesadores**

Aunque lo más conocido del mundo de los microprocesadores sean los empleados en el mercado de los ordenadores personales, lo cierto es que estos microprocesadores solo suponen una parte pequeña de la fabricación mundial de este tipo de chips.

La mayoría de los equipos electrónicos de hoy en día llevan microprocesadores incorporados. No importa si es una lavadora o un automóvil de alta gama. Estamos rodeados de microprocesadores por todas partes. Existen microprocesadores de todo tipo y condición.""")
        imagen_otros = "https://i.postimg.cc/507JkFgR/Microprocesador-Otros-fabricantes-600x267-1.jpg"
        st.image(imagen_otros, use_column_width=True)
        st.caption("<span style='color: white;'>Ejemplos de otros fabricantes de microprocesadores</span>", unsafe_allow_html=True)
        
        st.write("""Por otro lado, el mundo de la telefonía móvil y tablets se ha desarrollado mucho en estos últimos años. La fabricación de microprocesadores para este tipo de dispositivos no deja de crecer. Fabricantes de microprocesadores como MediaTek, Qualcomm, Samsung, Huawei o Apple son especialistas en estos chips y merecerían un estudio aparte.

Además de los anteriores, cabe mencionar otros fabricantes importantes como Freescale, Nvidia, Spreadtrum o Texas Instrument.""")

    if col3.button("Historia de Intel vs AMD", key="historia_intel_amd", help="Haz clic aquí para leer sobre la historia de Intel vs AMD"):
        st.subheader("Historia de Intel vs AMD")
        st.write("""Intel vs AMD es un clásico de la lucha de dos empresas por el mercado. Mientras que Intel ha sido siempre
el líder de esta industria, AMD ha sabido demostrar que se puede ser un serio rival aunque se tengan muchos menos recursos. 
Veamos la historia de Intel vs AMD.

La lucha de ambas empresas no solo ha sido tecnológica, sino que ha estado siempre inmersa en demandas judiciales. A lo largo de la historia, Intel se ha comportado como una tortuga que avanza lentamente, pero con paso firme y constante. Por su parte, AMD ha tenido una evolución más errática. Ha dependido de factores (inversiones y talento) que unas veces les eran más favorables que otras. Esto le ha hecho parecerse más a la liebre del cuento. A veces ha avanzado mucho tecnológicamente, superando a Intel, y otras se ha dormido, siendo superada por su rival.""")
        imagen_carrera = "https://i.postimg.cc/Df6cMR08/Intel-vs-AMD-tortuga-liebre-600x338-1.jpg"
        st.image(imagen_carrera, use_column_width=True)
        st.caption("<span style='color: white;'>Carrera competitiva de Intel vs AMD</span>", unsafe_allow_html=True)
        
        st.write("""En este artículo se ha hecho el esfuerzo de sintetizar lo que han sido cuatro décadas de competición. Para ello, la comparación se ha centrado en los microprocesadores para ordenadores de sobremesa. No se han tenido en cuenta ni los microprocesadores para servidores ni para otros dispositivos, como los portátiles (laptops) o consolas. Tampoco se describen los detalles legales que ha acompañado a la lucha tecnológica.

## **Antecedentes de Intel vs AMD**

La empresa Fairchild Semiconductor fue fundada en Estados Unidos en 1957. Esta empresa, ya desaparecida, no solo introdujo en el mercado el primer circuito integrado comercialmente viable (lanzado ligeramente antes que el de Texas Instruments), sino que en ella trabajaron los fundadores de otras dos grandes empresas: Intel y AMD.

Intel la fundaron Bob Noyce y Gordon Moore en 1968. Ambos procedían de Fairchild Semiconductor. En el año 1971 Intel creo el primer procesador de la historia, el Intel 4004, un procesador de 4 bits y unos impresionantes 740kHz. En 1979 Intel lanzo el i8086, un procesador de 16bits y 10MHz. Con este microprocesador nació la arquitectura x86, la base de los ordenadores personales modernos, el PC.

AMD (Advanced Micro Devices) se fundó en 1969, un año después que Intel. Al igual que Intel, lo fundaron exempleados de Fairchild Semiconductor. En este caso fueron ocho: Jerry Sanders (que sería el presidente), Jack Gifford, Edwin Turney, John Carey, Larry Stenger, Frank Botte, Sven Simonsen y Jim Giles. Esta empresa se limitaba a producir circuitos integrados de semiconductores y memorias RAM. En los años 1980 empezó a fabricar microprocesadores con la licencia de Intel.

El origen de AMD no fue tan glorioso como el de Intel. Jerry Sanders, presidente de AMD, siempre solía decir que le costó 5 millones de minutos conseguir 5 dólares para financiar la nueva compañía. Lo decía en respuesta a que Arthur Rock, director financiero de Intel, presumía de haber reunido 5 millones de dólares para fundar Intel en solo 5 minutos.

Otra diferencia entre ambas empresas es que, mientras que AMD solo diseña los chips y tiene subcontratada su fabricación, Intel diseña y fabrica los suyos. Intel ha sido siempre el líder de esta industria, marcando los ritmos. Por su parte, AMD, aunque en ocasiones ha sacado productos pioneros, mejores que los de Intel, siempre ha estado a la sombra del primero. De hecho, AMD solo ha alcanzado un máximo del 22% de cuota de mercado de este tipo de microprocesadores.""")
        imagen_intelvsamd = "https://i.postimg.cc/262B0RGY/intel-vs-AMD-chips-600x294-1-300x147.jpg"
        st.image(imagen_intelvsamd, use_column_width=True)
        st.caption("<span style='color: white;'>Intel vs AMD</span>", unsafe_allow_html=True)
        
        st.write("""AMD ha estado luchando desde el primer día por sobrevivir en este mercado. Luchar contra los grandes presupuestos de investigación de Intel no ha sido fácil. A veces conseguía captar la inversión necesaria para reunir a grandes talentos que le proporcionaban productos excepcionales. Por desgracia, su evolución no ha sido constante, sino llena de altibajos. En su historia de competencia con Intel ha tenido momentos brillantes dentro de una lucha donde su gran mérito era y sigue siendo seguir manteniéndole el pulso al gigante. Este es el gran mérito de AMD.

## **El origen de la competencia Intel vs AMD**

A principios de la década de 1980 IBM elige la arquitectura de chip x86 de Intel para construir su famoso IBM PC. No obstante, como IBM no quería depender de un solo proveedor, le exige a Intel que licencie la fabricación de sus microprocesadores para que puedan fabricarlos otras empresas. Entre ellas, estaba AMD.

AMD fabricaba clones de los procesadores de Intel como el 8086 o los modelos posteriores (80286, 386 y 486). Además utilizaba las mismas denominaciones. El papel de estos otros fabricantes empezó a ser cada vez más relevante, por lo que Intel cambió de opinión y pensó que sus licenciados podían convertirse en una seria amenaza para su futuro. Así que dejó de otorgar licencias e intentó marcar diferencias con AMD, su principal rival.

Lo que se le ocurrió para diferenciarse fue intentar impedir que AMD utilizara las mismas denominaciones para sus microprocesadores. Intel denunció esta práctica, pero perdió su demanda al considerar el juez que no se podía tener derechos sobre un número. Esto llevó a Intel a empezar a identificar sus modelos con un nombre, no un número. El primer nombre utilizado fue Pentium (en lugar de 586).

El divorcio empezó con el modelo Intel Pentium, que Intel no licenció a otros fabricantes. Muchos de ellos se vieron forzados al cierre, pero AMD sobrevivió apostando por diseñar sus propios modelos de microprocesadores.

En el año 1996 AMD sacó su modelo K5 para competir con el Pentium de Intel. El K5 era compatible con las placas de Intel. Para poder sobrevivir en la lucha, AMD apostó por vender sus microprocesadores a precios bastante inferiores a los de Intel, pero con una relación rendimiento/precio que resultase muy competitiva a los fabricantes de ordenadores.""")
        imagen_tablaintelvsamd = "https://i.postimg.cc/TYr5sDCQ/Intel-vs-AMD-Microprocesadores-600x403-1.jpg"
        st.image(imagen_tablaintelvsamd, use_column_width=True)
        st.caption("<span style='color: white;'>Microprocesadores Intel y AMD más rápidos de cada año en ordenadores de sobremesa</span>", unsafe_allow_html=True)
        
        st.write("""## **1997. AMD se demuestra ser un serio rival de Intel**
        
Los modelos K6 lanzados en 1997 (y posteriormente K6-2 y K6-3) compitieron muy bien con los Pentium II y Pentium III de Intel. De hecho, se estima que como el 70% de los ordenadores de gama media o baja vendidos ese año equipaba los chips de AMD.

AMD hizo una nueva apuesta en 1999 y sacó sus modelos Athlon y Duron con una nueva arquitectura que denominaron K7. Estos famosos modelos no solo igualaban al Pentium III de Intel, sino que, en algunas configuraciones lograban superar su rendimiento.

Aunque Intel ha conseguido mantener una imagen de marca de calidad que AMD no ha logrado igualar, lo cierto es que los productos de AMD han competido técnicamente muy bien con los de Intel. Sus siguientes modelos Athlon XP y Sempron, lanzados en 2003, compitieron perfectamente con los Pentium IV de Intel.

AMD desarrolló una nueva arquitectura K8, sacando en 2003 su famoso Athlon 64. La gran ventaja es que conseguían ordenadores de 64 bits sobre la estructura de los antiguos modelos x86. Esto supuso una mejora significativa frente a los modelos de 32 bits existentes. Los directivos de AMD no dejaron de sorprenderse cuando Intel les solicitó una licencia para poder aplicar esta extensión de 64 bits a sus propios chips.

El liderazgo técnico de AMD volvió a darse en 2005 cuando introdujo los primeros procesadores con varios núcleos en el mercado de los ordenadores PC. Anteriormente solo se había utilizado esta solución en equipos servidores.""")
        imagen_velocidad = "https://i.postimg.cc/sgMdXpq4/Intel-vs-AMD-Evolucion-de-CPUs-600x387-1.jpg"
        st.image(imagen_velocidad, use_column_width=True)
        st.caption("<span style='color: white;'>Mejora de la velocidad del nuevo modelo de CPU con respecto al modelo anterior</span>", unsafe_allow_html=True)
        
        st.write("""## **2006. Intel aventaja de nuevo**
        
Intel reaccionó. Los modelos de Intel utilizaban una arquitectura de microprocesadores que denominaban Netburst (llamada también P68). Después de los últimos avances de AMD, se vieron obligados a desarrollar una nueva arquitectura que denominaron Banias. La mejora fue significativa para Intel y se convirtió en la base de sus exitosos modelos Core 2 Duo y Core 2 Quad. Consiguieron mejorar considerablemente su eficiencia y superar claramente a los nuevos de AMD, los Phenom x3 y x4.

Intel volvió a darle una vuelta de tuerca a su mejoras sacando los procesadores Core i7, i5 e i3. Con una microarquitectura que llamaron Nehalem consiguieron microprocesadores un 30% más rápido que los anteriores, utilizando igual frecuencia.

En esos momentos, AMD intentó distintas soluciones técnicas para seguir compitiendo con Intel en la gama alta de los microprocesadores pero, por desgracia, ninguna le dio los resultados esperados. Su nueva arquitectura llamada Bulldozer no pudo competir con la nueva de Intel, Sandy Bridge.

En 2006, AMD adquirió ATI, un fabricante de procesadores gráficos (GPU). Esto le permitió a AMD integrar el procesador gráfico, GPU, en el mismo chip del microprocesador. Aunque fue un gran paso para AMD, era algo que Intel ya podía hacer con sus chips. Fundamentalmente, esto ayudó a AMD a competir en el mercado de ordenadores portátiles.

Finalmente, en 2012, AMD decidió abandonar la gana alta y centrarse de nuevo en los microprocesadores de bajo precio. Para ello, saca una nueva arquitectura denominada Piledriver.

En ese momento, Intel se convirtió en el líder indiscutible de la gama alta. Ante la falta de presión competitiva, sus mejoras de los siguientes años se centraron en adaptaciones que mejorasen su proceso de fabricación o en integrar algunas nuevas tecnologías del momento.""")
        imagen_transistores = "https://i.postimg.cc/bJB1zftT/Intel-vs-AMD-transistores-600x390-1.jpg"
        st.image(imagen_transistores, use_column_width=True)
        st.caption("<span style='color: white;'>Evolución de microprocesadores de Intel y AMD en número de transistores</span>", unsafe_allow_html=True)
        
        st.write("""## **2017. AMD consiguió destacar de nuevo**
        
No obstante, como se suele decir, la historia continuó. AMD sacó en 2017 una nueva arquitectura, llamada Zen, que lo situó de nuevo en la carrera. Su gama de microprocesadores Ryzen, basados en la arquitectura Zen 2 y 3 pueden competir en rendimiento con los Intel Core i5 e i7. Para mejorarlo, AMD espera sacar en 2022 la versión 4 de la arquitectura Zen. Por su parte, Intel ha respondido con su procesador i9 basado en la arquitectura Rocket Lake.

Actualmente hay una lucha entre los procesadores AMD Ryzen 3, 5, 7 y 9 y los procesadores Intel Core i3, i5, i7 e i9. Es curioso que, después de tantos años, sigan dándose coincidencias en las nomenclaturas.

## **La historia continua**

La batalla tecnológica de ambas empresas continuará en los próximos años. Intel parece que se está centrada en desarrollar microprocesadores con velocidades de reloj más altas y con un menor número de núcleos. Por su parte, AMD parece que se está focalizando en integrar un número mayor de núcleos a frecuencias más bajas. Esto hace que los mercados óptimos de uno y otro sean levemente distintos.""")
        imagen_ventas = "https://i.postimg.cc/3rjDSGL1/Intel-VS-AMD-ventas-sobremesa-B-600x320-1.jpg"
        st.image(imagen_ventas, use_column_width=True)
        st.caption("<span style='color: white;'>Ventas de microprocesadores para ordenadores de sobremesa (Intel vs AMD)</span>", unsafe_allow_html=True)
        
        st.write("""Las ventas de microprocesadores para ordenadores portátiles (laptop) se mantiene, casi desde sus comienzos en una proporción 80%/20% a favor de Intel. En los microprocesadores para servidores Intel se ha ido quedando con casi la totalidad del mercado, donde AMD ha desaparecido. El único mercado donde hay una verdadera competencia entre ambas empresas es en el de microprocesadores para ordenadores de sobremesa (desktop). Desde hace algunos años, AMD está ganando terreno y en 2021 ha conseguido vencer de nuevo a Intel en las ventas en este mercado.""")

    if col4.button("Qué es la Ley de Moore", key="ley_moore", help="Haz clic aquí para leer sobre la Ley de Moore"):
        st.subheader("Qué es la Ley de Moore")
        st.write("""Moore dijo que el número de transistores por unidad de superficie en circuitos integrados se duplicaría 
cada dos años. Esta simple frase ha tenido una gran influencia en la mayoría de los avances de la era digital, 
desde el PC hasta las supercomputadoras. Siempre que se habla de la evolución de los ordenadores aparece la famosa Ley de Moore.

Los microprocesadores llevan décadas mejorando nuestras vidas. Estos pequeños chips, no solo están presentes en los ordenadores, sino en todo tipo de equipos electrónicos, desde un coche de última generación hasta un electrodoméstico, como la lavadora, o el control de la calefacción. Una particularidad que tienen los microprocesadores es que constantemente están saliendo modelos nuevos que mejoran los anteriores. Esto supone que los dispositivos que los usan pueden hacer más cosas y de forma más rápida. Por tanto, las grandes novedades tecnológicas están muy relacionadas con el avance de los microprocesadores.

## **Quién es Gordon Moore**

Gordon Earle Moore nació en 1929 en San Francisco (Estados Unidos). Estudió la carrera de Química y en 1954 obtuvo su doctorado en el Instituto de Tecnología de California. Empezó a trabajar en el laboratorio de semiconductores del físico William Shockley. Junto a John Bardeen y Walter Houser, Shockley recibiría el premio Nobel en Física en 1956 por sus trabajos de investigación sobre los semiconductores. Shockley fundaría la Shockley Semiconductor Laboratory, primera compañía de semiconductores instalada en Silicon Valley.

A pesar de ello, tanto Moore como otros siete compañeros abandonarían a Shockley en 1957 para formar parte de la empresa que había creado recientemente Sherman Fairchield: Fairchield Semiconductor. A Moore lo harían Director de Investigación y Desarrollo de esta empresa en 1965. Por este motivo, la revista Electronics lo entrevistó y, a una de las pregunta Moore respondió con la reflexión que luego se convertiría en la Ley Moore. La entrevista se publicaría el 19 de abril de 1965 y en ella Morre decía literalmente: ‘el número de transistores por pulgada cuadrada en los circuitos integrados se ha duplicado cada año desde que se inventó el circuito integrado’. Además añadiría que esta tendencia seguiría durante, al menos, los siguientes diez años.

Diez años más tarde corrigió su observación y dijo que la duplicación del número de transistores se daría cada dos años, no cada año. Esta corrección es la que ha quedado como definitiva en la conocida Ley Moore.""")
        imagen_gordon = "https://i.postimg.cc/BbhFh9qD/Ley-de-Moore-Gordon-Moore-y-Robert-Noyce-600x400-1.jpg"
        st.image(imagen_gordon, use_column_width=True)
        st.caption("<span style='color: white;'>Gordon Moore y Robert Noyce, fundadores de Intel</span>", unsafe_allow_html=True)
        
        st.write("""Junto con el empresario Robert Noyce, Moore fundo en 1968 la empresa NM Electronics (por Noyce y Moore). No obstante, poco después le cambiaron el nombre por Intel Corporation (por Integrated Electronics). Moore fue nombrado presidente de Intel en 1979 y ocupó este cargo hasta 1987. Por cierto, el cofundador Robert Noyce, no solo era el inventor del primer circuito integrado de silicio (lo patentó en julio de 1959), sino que también era cofundador de Fairchild Semiconductor.

El trabajo de Gordon Moore como científico y empresario ha sido merecedor de múltiples reconocimientos.

## **La Ley de Moore**

Desde el punto de vista de la fabricación, los circuitos integrados, incluidos los microprocesadores, no son más que un conjunto de transistores puestos en un chip. Uno de los puntos importante de la evolución de la tecnología de fabricación consiste en conseguir meter un mayor número de transistores en una misma superficie. Moore se dio cuenta de que la cadencia de integración de transistores en los circuitos integrados seguía un cierto patrón. Así que en 1965, cuando era Director de los laboratorios Fairchild Semiconductor dijo que el número de transistores que se logran integrar en los chips se duplicaría cada año. Diez años más tarde, en 1975, modificaría sus conclusiones anteriores y su ley quedaría establecida como: ‘El número de transistores por unidad de superficie en circuitos integrados se duplicará cada dos año’.""")
        imagen_representacion = "https://i.postimg.cc/LXWRvNc5/Ley-de-Moore-Grafico-600x334-1.jpg"
        st.image(imagen_representacion, use_column_width=True)
        st.caption("<span style='color: white;'>Representación de la Ley de Moore</span>", unsafe_allow_html=True)
        
        st.write("""El proceso de fabricación de los circuitos integrados, conocido como litografía, se mide por el tamaño que ocupa un transistor. Como son tan pequeños, la unidad de medida que se utiliza es el nanómetros (un nanómetro equivale a 0,000001 milímetros). Esto quiere decir que una litografía de 14 nm supone que cada transistor mide 0,000014 mm. Otra forma de medir este mismo concepto es por los millones de transistores por milímetro cuadrado o MTr/mm2.

## **Qué relación hay entre la Ley de Moore y la potencia de cálculo de los microprocesadores**

Cuando se enunció la Ley de Moore original no existían todavía los microprocesadores (el primero es de 1971). No obstante, como la ley hace referencia a los circuitos integrados en su conjunto, se le puede aplicar también a éstos. No obstante, la Ley de Moore solo habla de la evolución de la densidad de transistores por unidad de superficie, no de la potencia de los microprocesadores.

El factor que más influye en la potencia de cálculo de los microprocesadores no es el número de transistores que integra, sino cómo están organizados internamente estos transistores. Esto es lo que se conoce como arquitectura del microprocesador. Por tanto, duplicar la densidad no significa necesariamente duplicar la potencia de cálculo.""")
        imagen_chips = "https://i.postimg.cc/02y5xKf9/Ley-de-Moore-Oblea-600x300-1.jpg"
        st.image(imagen_chips, use_column_width=True)
        st.caption("<span style='color: white;'>Los chips se fabrican en obleas de múltiples unidades.</span>", unsafe_allow_html=True)
        
        st.write("""En los primeros años hubo una clara relación entre ambos valores. No obstante, llegó un momento en el que la Ley de Moore se seguía cumpliendo en relación con la duplicación de la densidad de transistores, mientras que la duplicación de la potencia de cálculo (conocido como escalado de Dennard) se quedó frenada.

## **Qué importancia tiene la Ley de Moore**

Como el paso del tiempo confirmaba que la Ley de Moore era válida, se convirtió en un objetivo que estaba presente en toda la industria de los semiconductores. Las empresas involucradas no sabían muy bien qué iba a hacer la competencia, pero la Ley de Moore se convirtió en un faro que dirigía su estrategia futura. Esto es, la Ley de Moore ha tenido una clara influencia en la planificación a largo plazo de la investigación y desarrollo de nuevos dispositivos.

Como esta ley ha influido, indirectamente, en el desarrollo de nuevos modelos de semiconductores, frecuentemente se afirma que la Ley de Moore es responsable de la mayoría de los avances en la era digital, desde el PC hasta supercomputadoras.

Un ejecutivo de Intel, Markus Weingartner, llegó a decir en 2016 en una entrevista a la revista Wired que ‘La Ley de Moore es una ley de economía, no de física‘. De hecho, completó su comentario diciendo que ‘Esta simple regla ha impulsado todos los avances en la revolución tecnológica durante más de medio siglo y aún define los límites de la expansión de la tecnología actual. Esta ley ha permitido planificar conceptos, como la inteligencia artificial o los vehículos autónomos, para poder hacerlos realidad‘.

## **¿Ha dejado de cumplirse la Ley de Moore?**

La Ley de Moore ha demostrado ser correcta durante las últimas cinco décadas, si embargo, parece que finalmente podría estar llegando a su final. Según un informe reciente de la ITRS (asociación que incluye los grandes del sector, incluido Intel y Samsung), la fabricación de transistores llegará un momento en el que no se puedan hacer más pequeños. No está claro si la motivación será por una cuestión física o de rentabilidad de la inversión necesaria pero, a partir de ese momento la Ley de Moore habrá llegado a su fin.

A pesar de lo anterior, lo cierto es que, los fabricantes siempre han encontrado formas, cada vez más innovadoras, de meter más transistores en sus chips. No obstante, sí parece que en los últimos años se está produciendo una cierta desaceleración del aumento de la densidad de integración de transistores en un semiconductor.""")
        imagen_densidad = "https://i.postimg.cc/DZmQtPzR/microprocesador-ley-Moore-600x293-1.jpg"
        st.image(imagen_densidad, use_column_width=True)
        st.caption("<span style='color: white;'>Evolución de la densidad de transistores.</span>", unsafe_allow_html=True)
        
        st.write("""El propio Moore dijo en una entrevista de 2007 que ‘el hecho de que los materiales estén hechos de átomos es la limitación fundamental … así que uno de estos días vamos a tener que dejar de hacer las cosas más pequeñas‘. El diámetro de un átomo varía entre 0,1 y 0,5 nanómetros. Intel construyó en 2014 el primer microprocesador con transistores de tan sólo 14 nanómetros (nm). Puede parecer pequeño, pero AMD hizo lo propio en 2019 con chips de 7 nm. Para continuar en la carrera, los fabricantes TSMC y Samsung empezaron la fabricación de chips a 5 nm en 2020.""")
        
        
        
        
def mostrar_componentes():
    st.title("Componentes de Computadora")
    
    # Definir el diccionario de componentes para la página componentes. Repasar las imágenes
    componentes = {
        "Procesador/CPU": """![Imagen Procesador](https://i.postimg.cc/mr2tYYZ0/CPU-1.jpg)

Central Processing Unit - Unidad Central de Procesamiento. Unidad de procesamiento encargada de interpretar las instrucciones de un hardware. 
Son como el cerebro de un ordenador, capaces de leer e interpretar las señales que les manda el usuario a través de los distintos componentes y resto de aplicaciones. Todo ello en cuestión de nanosegundos y en código binario.
También se encarga de generar información de salida en formato de vídeo a través de una pantalla o un monitor.
Las CPU son la parte esencial de cualquier ordenador. Sin ellas, sería imposible que un PC, portátil o móvil funcionase correctamente. De ahí que sea sumamente importante conocer bien qué tipo de procesador vamos a escoger a la hora de montar un 
ordenador nuevo. A la hora de comprar una CPU, es importante fijarse en sus características técnicas:
           
- **Frecuencia de reloj.** Este primer término hace referencia a la velocidad de reloj que hay dentro del propio procesador.  Es un valor que se mide en Mhz o Ghz y es básicamente la cantidad de potencia que alberga la CPU. 
La mayoría de ellas cuentan con una frecuencia base (para tareas básicas) y otra turbo que se utiliza para procesos más exigentes (para gaming, por ejemplo).
Consumo energético. Es normal que nos encontremos con CPU 's donde su consumo energético varíe notablemente. Es un valor que se muestra en vatios (W) y como es obvio, aquellos procesadores de gama superior, serán más propensos a consumir más energía. Ante esto, es importante también contar con una fuente de alimentación acorde a la potencia de nuestro procesador y tarjeta gráfica.
Número de núcleos. Con el avance de la tecnología, ya es posible encontrar tanto procesadores de Intel como de AMD que cuentan desde 2 hasta 64 núcleos. Estos cores son los encargados de llevar a cabo multitud de tareas de manera simultánea sin que el PC tenga que trabajar a “marchas forzadas”. Aquí depende también mucho del uso que le vayáis a dar a vuestro ordenador. Si lo vais a usar únicamente para tareas de ofimática, con una CPU de uno o dos núcleos será más que suficiente. Aunque si ya queréis hacer streaming, jugar o llevar a cabo labores de edición de vídeos, necesitaréis al menos cuatro.

- **Zócalo.** Es el tipo de conector con pines o socket al que debéis conectar a vuestra placa base. Es muy importante que os fijéis en este término, ya que de lo contrario, podéis comprar sin querer una CPU que sea incompatible con vuestra motherboard. Por ejemplo, las últimas de Intel suelen tener el socket LGA 1200, mientras que las de AMD con Ryzen son AM4.

- **Número de hilos.** Dentro de cada núcleo puede existir un hilo o core virtual, que tienen como objetivo llevar a cabo otros procesos más pesados sin que el rendimiento del PC o del portátil se vea afectado. Esta tecnología es lo que se conoce como “hyper-threading”, un término que acuñó Intel, pero que a día de hoy se usa indistintamente para cualquier marca.

- **Memoria caché.** A la hora de “recordar” cualquier tarea, el propio ordenador hace uso de la memoria RAM. Sin embargo, a veces esto no es del todo suficiente y por tanto es necesario que utilice la memoria caché de la propia CPU. Se caracteriza porque se llega a ella de forma más rápida y puede ser tipo L1, L2 y L3.


## **Ventajas y desventajas de los procesadores Intel**

Tras haber despejado todas las dudas en este ámbito, ahora vamos a hablar de las ventajas y desventajas que ofrecen las CPU de Intel.

- **Gran potencia en mononúcleo.** La gama de i3, i5, i7 e i9 son perfectas para aquellos usuarios que busquen la mejor potencia en procesos que requieren de un gran rendimiento o hacer overclock. Y es aquí donde Intel se lleva completamente la palma, sobre todo en lo que a gaming se refiere, aunque los Ryzen de AMD ya no tienen nada que envidiarles.

- **Mayor eficiencia energética.** Otro de los aspectos positivos de los procesadores Intel es que son más eficientes en términos de energía. Por ello, son muchos los usuarios que los eligen para no disparar el consumo eléctrico, aunque los AMD Ryzen, a pesar de la creencia popular,  también tienen un gran equilibrio entre potencia y consumo.

- **Precios algo inflados.** A lo largo de los años hemos visto como Intel ha apostado por unos precios algo desorbitados. Tras la adelantada por la izquierda de AMD sobre Intel, esta última deberá empezar a ofrecer mejores precios si no quiere que AMD siga comiéndole más y más cuota de mercado. El “monopolio sano” de Intel, tal y como dirían en Forocoches, parece haber llegado a su fin, y sin duda, esto es algo que beneficiara a todos los usuarios.

## **Ventajas y desventajas de los procesadores AMD**

AMD también es una empresa que tiene tanto sus puntos fuertes como débiles. Aquí los desgranamos:

- **Mayor número de núcleos.** AMD siempre le ha hecho la competencia a Intel ofreciendo procesadores con un mayor número de núcleos, algo a tener en cuenta si vamos a realizar multitarea. El AMD Ryzen Threadripper 3970X, con 32 núcleos y 64 subprocesos es un gran ejemplo de ello. 

- **Excelente relación calidad/precio.** Parece que el fiasco de la gama FX pasó ya a mejor vida. Con las CPU Ryzen hemos visto procesadores de gran potencia (sobre todo de la gama 5 o superior) incluso en su versión desbloqueada. Todo ello a precio de ganga que a veces no supera los 200 €, algo que sin duda ha propiciado el cambio de tendencia en el mercado de los mejores procesadores.

- **Poca disponibilidad en portátiles.** Si comparamos el número de portátiles con procesador Intel vs con procesador AMD, los segundos siguen siendo minoría, sobre todo si buscamos un portátil gaming. Sin embargo, la tendencia parece estar cambiando y cada vez más fabricantes optan por montar una CPU AMD en sus portátiles. 


## **Los mejores procesadores: Conclusiones finales**

### **Mejor procesador para ofimática**

- **Intel Core i3-10100 3.60 GHz.** Excelente CPU con una relación calidad precio inmejorable. Monta cuatro núcleos y 8 hilos con una frecuencia base del procesador de 3,60 Ghz y una memoria caché inteligente de 6 MB. Incluye compatibilidad con Wi-Fi 6 y con los socket LGA 1200.

- **AMD Ryzen 3 3200G 3.6 GHz BOX.** Procesador de gama baja de AMD con un rendimiento espectacular y completo. 4 núcleos y 4 hilos de 3,6 Ghz proporcionan la velocidad de procesamiento ideal para tareas básicas. 

### **Mejor procesador para gaming**

- **Intel Core i5-11600KF 3.9 GHz:** procesador i5 de la undécima generación de procesadores Intel. Optimizado para equipos gaming, el i5-11660KF cuenta con una velocidad de reloj de 3,9 Ghz, 6 núcleos y 12 hilos. 

- **AMD Ryzen 7 5800X 3.8GHz:** el AMD Ryzen 7 5800X se ha convertido en uno de los procesadores TOP del mercado. Con 8 núcleos, 16 hilos y una frecuencia que puede alcanzar hasta los 4,7 Ghz gracias al overcloking, es sin duda una de las mejores opciones para correr juegos de última generación. 

### **Mejor procesador para multitarea**

- **Intel Core i9-11900K 3.5 Ghz:** Si lo que buscas es un procesador para gaming que te sirva también para editar vídeos, realizar streamings o renderizar en 3D, este i9-11900K es seguramente la solución a tus problemas. Cuenta con 8 núcleos físicos junto a 16 virtuales y una potencia de 3,5 Ghz que puede llegar a los 5,1 Ghz en turbo.

- **AMD Ryzen 9 5950X 3.4 GHz:** Si tu apuesta es por AMD, tienes este Ryzen 9, la apuesta por la quinta generación con la tecnología más avanzada del mundo. Esta CPU cuenta con 16 núcleos y 32 hilos que alcanzan una potencia de 3,4 Ghz de base y hasta 4,9 Ghz en turbo. Una opción que no debes pasar por alto si quieres realizar multitarea.""",
        
"Tarjeta Gráfica": """![Imagen Grafica](https://i.postimg.cc/kXNjDbj0/elegir-tarjeta-grafica.jpg)
Renderiza las imágenes en la pantalla y ofrecer una visualización de alta calidad, procesando y ejecutando datos gráficos mediante técnicas, características y funciones gráficas avanzadas. Hay que diferenciar la GPU (unidad de procesamiento gráfico) de lo que es una tarjeta gráfica, porque lo primero es un chip, mientras que lo segundo es un producto terminado.
Las siglas GPU se refieren a Graphics Processing Unit o unidad de procesamiento gráficos y se trata de un chip encargado para acelerar la representación de gráficos 3D. Sin embargo, este concepto ha evolucionado mucho debido al avance tecnológico en desarrollo y en arquitecturas. La GPU realiza multitud de operaciones relacionadas con los datos 2D y 3D, como es decodificar y renderizar objetos animados y vídeos.

Ahora que tenemos claramente identificado qué es una GPU, vamos a explicaros qué es una tarjeta tarjeta gráfica como producto completo compuesto por:

- PCB, que es donde van soldados todos los componentes.
- Módulos de memoria (GRAM).
- Condensadores y demás componentes.
- Tuberías de calor.
- Ventiladores (o blower) y carcasa.

## **Qué tipos de tarjetas gráficas existen**

Las tarjetas gráficas son desarrolladas por dos marcas rivales: Nvidia vs AMD. Por regla general, las mejores tarjetas AMD ofrecen un rendimiento similar al de las mejores tarjetas Nvidia. Por lo que será más cuestión de precios, de stock y de gustos personales. Podemos encontrar diferentes modelos en función a dos características principales:

- Por **refrigeración**:
  - Activa: hacen uso de ventiladores.
  - Pasiva: hacen uso de aletas de aluminio para expulsar el calor por el método de convección.
  - Líquida: utilizan un bloque de agua que lleva conectado 2 tubos dirigidos a un radiador con uno o varios ventiladores para expulsar el calor fuera de la caja.
            
         
- Por **tamaño**:
  - 1 ventilador o Mini-ITX, ideales para PCs con dicho factor de forma.
  - 2 ventiladores, es el tamaño estándar aunque algún modelo puede encajar en un mini-ITX.
  - 3 ventiladores, un tamaño bastante grande y que no cabe en todas las cajas ATX.

## **Qué componentes tiene una una tarjeta gráfica**

### **GPU**

La principal pieza de una placa de vídeo es la GPU, la unidad de procesamiento gráfico. Se refiere a un procesador dedicado, justamente, al procesamiento de los gráficos. Lo que hace es aligerar la carga de trabajo del procesador central, acción que la convierte en la parte más importante de toda tarjeta gráfica y es la que determina el rendimiento de la misma.

### **GRAM**

Luego, encontramos la GRAM, la memoria gráfica de acceso aleatorio, que son chips de memoria que almacenar y transportan información. En este sentido, identificados dos tipos de memorias gráficas. Por una parte, la dedicada, memoria más eficiente cuando la tarjeta o la GPU disponen exclusivamente para sí este tipo de memorias. Por otro lado, está la compartida, utilizada cuando se emplea memoria en detrimento de la memoria de acceso aleatorio.
A su vez, la potencia de la memoria gráfica es el resultado de tres aspectos: capacidad, interfaz de memoria y frecuencia de memoria.

- **La capacidad** determina el número máximo de datos y texturas que puede procesar. Es un detalle muy relevante a tener en cuenta para resoluciones superiores a 1440p y monitores múltiples, donde cada imagen toma mucho más espacio.

- **La interfaz de memoria**, o bus de datos, resulta de la multiplicación del ancho de bits de cada chip por su número de unidades. Es un detalle clave para determinar el ancho de banda, es decir, la cantidad de datos que puede transferir en cierto tiempo.

- Por último, **la frecuencia de memoria** es, valga la redundancia, la frecuencia a la que la memoria puede transportar los datos ya procesados. Es así que se complementa con la interfaz y, entre ambas características, se determina el ancho de banda de la memoria.

## **Qué características tiene una tarjeta gráfica**

Por último vamos a hablarte de cuestiones más técnicas que guardan relación con el rendimiento y las características que tendrás que tener en cuenta a la hora de comprar una tarjeta gráfica.

### **Arquitectura**

En toda presentación de AMD o NVIDIA, veréis que hacen esfuerzos en enseñar el diseño de la arquitectura que van a usar todas las tarjetas gráficas de una generación. Es tan importante este diseño en el papel de la GPU que NVIDIA diferencia sus generaciones a través del nombre de la arquitectura (Maxwell, Pascal, Turing, Ampere, Ada Lovelace…).
AMD empezó a hacer lo mismo en 2018 con el nacimiento de RDNA, y posteriormente en 2020 con RDNA 2.

Se trata del diseño o enfoque del interior de una GPU junto con la interacción de los distintos componentes que hay en una tarjeta gráfica. Por ejemplo, la cantidad de núcleos que tiene una GPU, la forma en la que se distribuyen, las funciones asignadas a cada uno de ellos, el acceso a la memoria caché y su prioridad, etc.

### **Frecuencia: base, game y boost**

En casi todas las tarjetas gráficas encontraréis 3 frecuencias distintas:

- **Base**, que es el reloj a la que funciona la GPU en reposo.

- **Game**, el reloj cuando jugamos o seleccionamos un preset de overclock determinado.

- **Boost**, la frecuencia máxima teórica que podemos disfrutar en la GPU.

La frecuencia GPU se mide en MHz e indica lo rápido que los núcleos de una GPU pueden ser. A mayor refrigeración, mayor capacidad de tener una frecuencia más alta (más calor, requiere mejor refrigeración), por ello las tarjetas gráficas con 3 ventiladores o con bloques de agua manejan frecuencias más altas.
La **velocidad del reloj** es el número de veces que la GPU oscila por segundo. Por ejemplo, si tiene 2000 MHz, significa que se cicla 2 millones de veces por segundo.

Hay que diferenciar el Core Clock del Memory clock, siendo la segunda la velocidad de la memoria VRAM o memoria de vídeo. Cuando decimos VRAM nos referimos a la cantidad de memoria GDDR que tiene la GPU, siendo muy habitual encontrar 4 GB, 6 GB, 8 GB, 10-12 GB, 16 GB y 24 o más GB.

Tanto el Core clock, como el Memory clock se pueden ajustar en MSI Afterburner para hacer overclock, pero os aconsejo saber lo que hacéis y revisar las coberturas de garantía del producto antes de hacer nada. Esto te va ayudar para descartar modelos y saber qué tarjeta gráfica comprar en caso de querer overclock.

### **Ancho de banda y velocidad de memoria**

Diferente al Memory clock, tenemos la velocidad de memoria, que es medida en Gbps (Gigabits por segundo). Esto significa la velocidad de interfaz de la línea de datos del chip de memoria, que suele ser de 14 o 16 Gbps, aunque AMD lanzó las RX 6X50 con 18 Gbps.

Este valor es parte de la especificación de la memoria GDDR de turno (GDDR5, GDDR6, GDDR6X, etc.). Por este motivo, la tarjetas graficas RTX 3090 Ti lleva memoria GDDR6X y su velocidad de memoria es de 21 Gbps.

Por otro lado, está el ancho de banda de la memoria, que es medido en GB/segundo (o GB/s), diferenciado del ancho de banda de la interfaz (medido en bit). Con estos datos no vas a saber si una GPU es más potente que otra, pero son muy útiles para saber la potencia teórica del modelo.

### **Conectores, alimentación y salidas de vídeo**

Estas características sí que suponen ciertas diferencias entre tarjetas gráficas de cara al uso de las mismas y a su aprovechamiento. Primero, vamos a diferenciar conectores y salidas:
En una tarjeta gráfica te vas a encontrar:

- **Conectores PCIe** para alimentarla de energía directamente desde la fuente de alimentación. Varían según modelos y marcas, encontrando 6+4, 8+2 e, incluso un conector entero de 12 pines, ¡consulta el modelo antes de comprar!

- **Unos pines** que deben aterrizar en la ranura PCI-Express.

- Posiblemente un **switch o interruptor** para elegir un perfil de rendimiento o silencioso (ASUS hace mucho esto).

- **Salidas de vídeo:**
  - HDMI 2.1.
  - DisplayPort 1.4.
  - USB, en el caso de las más potentes para realidad virtual.

Este es uno de los factores determinantes a la hora de saber cómo elegir tu tarjeta gráfica ideal porque marca un antes y un después en cada generación. De nada sirve tener HDMI 2.1 en Turing o Pascal porque es casi imposible poner una de sus GPUs a más de 144 FPS en 4K en juegos de última generación.

Como consejo final, antes de comprar una tarjeta gráfica, se recomienda comparar modelos y ver comparativas de rendimiento gaming en YouTube porque seguro serán de ayuda. 
""", "Placa Base": """![Imagen Procesador](https://i.postimg.cc/LsjwHJdy/Placa-base-1.jpg)

La placa base es uno de los componentes más importantes a la hora de montar un ordenador. A esta pieza se conecta la memoria RAM, la CPU, los discos duros y la fuente de alimentación, elementos esenciales para que un ordenador funcione a pleno rendimiento.
Una placa base es un circuito impreso al que se conectan el resto de los componentes de un ordenador para que estos funcionen de manera óptima. También se las conoce con el nombre de placas madre.

Su función es que todos los elementos esenciales de un PC cuenten con energía eléctrica para responder en todo momento de manera adecuada y coordinar los flujos de datos.

## **Partes de una placa base**

### **Zócalo**

Recibe también el nombre de socket y es ahí donde se encastra la CPU correspondiente. Es muy importante que ambos compartan la nomenclatura y sean compatibles.

### **Chipset**

Es un conjunto de circuitos electrónicos que se encargan de gestionar las transferencias de datos entre los distintos componentes del ordenador. Se divide en dos secciones, llamadas northbridge y southbridge. En las placas actuales la primera suele estar integrada en el encapsulado del procesador.

### **Conectores de alimentación**

A través de ellos se proporciona energía eléctrica a los distintos componentes de la placa base, atendiendo siempre a sus distintos voltajes.

### **Ranuras o slots de memoria RAM**

Las placas madre cuentan también con una serie de slots o ranuras donde se conectan las memorias de acceso aleatorio (RAM).

### **VRM**

Este elemento se encarga de regular la velocidad de las ejecuciones que se dan tanto en la CPU como en el resto de periféricos.

### **Ranuras o slots de expansión**

Son un conjunto de ranuras o slots donde se pueden conectar tarjetas de expansión para así aumentar el rendimiento del ordenador. Las PCI-Express 0 x16 son las más recientes y es donde se conectan las GPU.

### **Conectores de entrada y salida**

Entre los que destacan los puertos USB, entradas VGA, DVI, HDMI o DisplayPort, así como los conectores Serial ATA (SATA) para los discos duros y sólidos, el M.2 para los nuevos NVMe y salidas de audio jack.

### **BIOS**

Es el programa de arranque con el que pueden ajustarse algunos parámetros básicos del PC, actualmente llamado UEFI.

### **Tarjetas de sonido y de red**

Permiten procesar el sonido y la conexión a internet de tu ordenador.

### **Conectores SATA**

Este componentes la conexión de los discos duros, tanto mecánicos como sólidos o SDDs

### **Conectores M.2**

Este componente es el más novedoso que se puede encontrar en una placa base. Permite enlazar únicamente unidades de almacenamiento de tal forma que no sobrecarguemos los slots de expansión.


## **¿Qué tipos de placas base existen?**

Tras listar todas las partes de una placa base, conozcamos ahora los distintos tipos que existen y cuáles son las más populares. La mayoría se dividen en lo que se conoce como factor de forma, que son los estándares que definen algunas características físicas de este componente, como su tamaño y orientación con respecto a la caja, el tipo de fuente de alimentación o la distribución de los dispositivos integrados. Según esta clasificación podemos diferenciar entre:

### **Placas base XT**

Fueron las primeras que se fabricaron, en el año 1983, y reciben este nombre por las siglas ‘eXtended Technology’. Se usaron, sobre todo, para las primeras computadoras de IBM PC XT. Estas placas tenían el mismo tamaño que un folio A4 y contaban únicamente con un conector externo para el teclado.

### **Placas base AT**

Un año más tarde surgieron las placas base AT (Advanced Techonology). Fueron las que tuvieron un formato más grande dentro de la historia del PC, ya que estaban divididas en dos partes. Se usaron desde 1984 hasta 1995.

### **Placas base ATX**

A partir de ese momento Intel desarrolló las placas base ATX o Advanced Technology eXtended. Fueron las primeras que disponían de conexiones exteriores junto a un conector de energía de 24 pines. Es la más extendida actualmente para cualquier tipo de ordenador. Dentro de este grupo también están las Micro-ATX, las Mini ATX y las E-ATX.

### **Placas base ITX**

Ean 2001 surgieron las placas base ITX (Integrated Technology eXtended). Sobre el papel tenían las mismas especificaciones que las MicroATX de Intel, con la particularidad de que su diseño permite integrar un mayor número de componentes.

### **Placas base DTX**

Por último, encontramos las placas base DTX. Este modelo salió a la luz en 2007 y, sobre todo, está destinado a mini-PCs. Es, por tanto, una opción ideal para quienes quieren montarse un ordenador de pequeñas dimensiones. Estas placas tienen un conector de energía de 24 pines y otro adicional de 2x2.""",
"Memoria RAM":"""![Imagen Procesador](https://i.postimg.cc/BbNtRZQb/Ram-1.jpg)

La RAM, o Memoria de Acceso Aleatorio (Random Access Memory en inglés), es un tipo de memoria volátil que se utiliza en los ordenadores y otros dispositivos electrónicos. Se utiliza para almacenar temporalmente datos e instrucciones que son necesarios para que la CPU (o procesador) pueda acceder rápidamente a ellos durante la ejecución de programas y procesos.

La RAM es de acceso aleatorio, lo que significa que la CPU puede acceder a cualquier ubicación de memoria de manera directa y casi instantánea, en lugar de tener que buscar secuencialmente como lo hace en los dispositivos de almacenamiento de datos más lentos, como los discos duros.

Explicado de una forma más sencilla; piensa que tu dispositivo, ya sea un móvil, un ordenador e incluso una TV, realiza muchísimas operaciones todo momento. Los resultados de estas operaciones pueden ser utilizadas en un futuro, por lo que necesitan una “libreta” donde ir apuntando toda esta información.

La RAM no es más que esta libreta. Seguramente te estás preguntando que porqué es necesaria la RAM si tienes otros tipos de memoria como puede ser el disco duro o bien la memoria de tu procesador. La respuesta a esto es sencilla: cada memoria tiene su propio tipo de uso.

La memoria caché del procesador es a la que más rápido se accede, pero trae el problema que lo que puedes almacenar en ella no llega a unos escasos megas. En cambio, la memoria física de un disco duro, SSD o NMVE, es cierto que es infinitamente superior a la caché respecto a espacio, pero también es infinitamente superior el tiempo que tienes que emplear para poder leer y guardar un dato.

De ahí sale la memoria RAM, es un tipo de memoria que está diseñada para encontrar el punto medio entre rapidez de acceso a los datos y cantidad de datos que puede almacenar.

Cada memoria tiene también sus características y la RAM trae entre ellas, que se trata de una memoria volátil, es decir, que si pasa el suficiente tiempo desde que almacenas un dato y lo dejas sin utilizar o cierras la aplicación que lo necesita o bien apagas tu ordenador, estos datos desaparecerán, no dejando rastro alguno.

Al final, la RAM es la memoria que utiliza el ordenador para que las aplicaciones puedan funcionar. Como podrás intuir también, a mayor RAM mayor cantidad de datos de aplicaciones podrás tener y por tanto el rendimiento de tu ordenador puede verse influido.

## **Tipos de RAM**

Existen muchos tipos de memoria RAM, los principales y más importantes son:

- **Dynamic Random Access Memory (DRAM)**: Cuando te haces el ordenador, es lo que “mal-llamamos” como RAM. Es un tipo de memoria volátil que puedes encontrar, la última generación en 2024 es la DDR5, pero antes de ella estaban la SDRAM, DDR, DDR2, DDR3 y DDR4.

- **Static Random Access Memory (SRAM)**: Es más rápida y más cara que la DRAM, pero también usa más energía. Se utiliza para cachés de alto rendimiento y en aplicaciones donde la velocidad es crítica como en ciertos componentes del procesador.

- **Video Random Access Memory (VRAM)**: Si eres gamer, esta te la sabes. Sino ya te lo decimos; esta es la memoria que utiliza la tarjeta gráfica para almacenar datos de imagen y video. Es diferente a la DRAM porque está precisamente diseñada para su uso en imágenes. Es muy importante para las aplicaciones que necesitan alto rendimiento gráfico como los juegos o la edición de video.

- **Magneto-resistive Random Access Memory (MRAM)**: Puede que os hayamos mentido diciendo que este tipo de memoria se borra cuando se apaga el equipo. La MRAM es una de las excepciones y es que utiliza las propiedades del magnetismo para almacenar los datos de manera persistente. Desgraciadamente no está muy extendido porque todavía está en fase de desarrollo.

- **Non-Volatile Random Access Memory (NVRAM)**: Es otro tipo de memoria RAM que es persistente incluso cuando se pierde la energía. Está diseñada para sistemas críticos que almacenan credenciales u otro tipo de datos que necesitamos que no se pierda.

## **Memoria de acceso aleatorio**

Sabemos que puede ser algo difuso este término de acceso aleatorio. Pero sí, como puedes intuir, la RAM es un tipo de memoria que guarda o lee información en cualquier posición aleatoria sin importar cuando se necesite.

Esto da mucha rapidez porque permite que los datos se lean o escriban de manera mucho más rápida ya que no hay que buscarlos de manera secuencial. Nos creas o no, el hacer la inserción y lectura de manera aleatoria por los programas, hacen que los conflictos cuando se intente acceder a los datos por dos aplicaciones diferentes a la misma celda se minimice exponencialmente. 

## **Latencia de la memoria RAM, ¿qué es y para qué sirve?**

La latencia CAS (conocida como CL) es otro de los aspectos que trae “locos” a muchos usuarios. La latencia mide la cantidad de tiempo que toma cierta información a la hora de desplazarse a su respectiva celda de memoria. Cuanto menos tarde, mayor será la eficiencia a la hora de llevar a cabo cualquier proceso. Pero es importante tener en cuenta que este valor va de la mano de la frecuencia, por lo que hay que fijarse en ambos valores a la hora de tomar una decisión

Dicho esto, cuando hablamos de CL, lo deseable es que el número sea lo más bajo posible. Conforme aumentemos de frecuencia, veremos que aumenta la latencia, siendo un efecto inevitable.

## **¿Qué frecuencia es mejor para mis memorias RAM?**

Esta pregunta va a tener diferente respuesta conforme pase el tiempo, pero la vamos a responder; más que nada porque veremos el paso de DDR4, DDR5, DDR6, así consecutivamente. Cada generación mejora los voltajes, los GBs por módulo y la frecuencia.

Grosso modo, la frecuencia define la potencia base de la memoria RAM y se mide en Megahercios (MHz), al igual que ocurre con la frecuencia de los procesadores.
Podemos llegar a confundir frecuencia de reloj, frecuencia de bus y velocidad de transferencia; sin embargo, cuando hablamos de frecuencia nos referimos al resultado total.

Es muy importante que antes de elegir la placa base, nos cercioremos de que la frecuencia es compatible con las memorias RAM que vayamos a comprar en el futuro. De lo contrario, la frecuencia se quedará limitada a lo que pueda ofrecer la placa base. No os preocupéis demasiado por si encontráis una placa base que acepta altas frecuencias y vuestra memoria tiene una más baja. 

¿Cuál es la mejor frecuencia para tus memorias RAM? La respuesta corta es la máxima a la que puedas optar, pero debes preguntarte por qué te importa tanto la frecuencia:

- ¿Es porqué quieres ganar FPS en juegos? Mejoran los FPS, pero no significativamente: aquí mandan las GPUs.

- ¿Mueves muchos datos? No mires solo a la RAM, sino al SSD.

- ¿Multitarea enorme? Pues sí es importante.


## **¿Cuánta RAM necesita mi ordenador?**

Te dejamos aquí una regla que jamás te fallará ten dos tarjeta RAMs siempre.

- 4GB de RAM: para pequeños ordenadores que no utilices para nada más que una navegación básica, un uso muy básico y que de verdad no quieras gastar dinero.

- 8GB de RAM: está bien para la mayoría de tareas del día a día, juegos sencillos y es el mínimo que os recomendamos para un pc que vayas a utilizar para la ofimática.

- 16GB de RAM: aquí ya empiezas a ir bien de recursos. Ideal para juegos normales, una edición de video sencillo y lo mínimo para los desarrolladores.

- 32GB de RAM: esta cantidad de memoria ram te servirá para gaming, para jugar a cualquier juego, para editar videos como un profesional e incluso para el diseño en 3D.""",
"Fuentes de Alimentación": """![Imagen Procesador](https://i.postimg.cc/ZKG0gQJr/Fuente-alimentacion-1.jpg)

Las fuentes de alimentación son esenciales en cualquier equipo: sin ellas no funciona ningún componente. Encargadas de suministrar energía a los diversos componentes que coexisten en un PC o portátil, se pueden diferenciar por su tamaño, su cableado, por su potencia y por su eficiencia energética.

## **Tipos de fuente de alimentación**

En primer lugar, hay que clasificar todas las fuentes de alimentación que existen en el mercado siguiendo 4 criterios generales: factor de forma o tamaño, cableado, refrigeración, potencia y eficiencia energética.

### **Según su factor de forma**

Ya sea por factor de forma o por tamaño, podemos encontrar las fuentes de alimentación ATX, SFX, SFX-L o TFX, siendo dichas dimensiones las más estandarizadas. 

- ATX. La mayoría de fuentes vienen con este formato, sus medidas son 150 mm de ancho y 86 mm de altura, además de que ofrecen más potencia que los demás formatos de fuentes. Hay una diferencia en cuanto a su profundidad: 

- ATX PS/2 para fuentes de 140 mm. 

- ATX PS/3 para fuentes de 100 mm. 

- SFX (Small Form Factor). Ideado para cajas con factor de forma Mini-ITX, tienen unas dimensiones de 125 mm de ancho y 63.5 mm de altura, siendo su diámetro de 100 mm. Cuenta con límites físicos obvios, por lo que cuesta ver potencias altas (más de 500 W) y las capacidades de refrigeración son más limitadas. 

- SFX-L. La “L” supone largey se refiere a que es algo más grande, en medidas: 125 x 63.5 x 130 mm. Aquí cambia la profundidad y el diámetro del ventilador, siendo la métrica más importante la profundidad de cara a instalarla en una caja pequeña. Suele ofrecer más potencia final, aunque no son baratas.

- TFX. Parecidas a unas cajas de zapatos, vienen a ser una fuente de alimentación de tamaño alargado estando su ventilador dispuesto en un extremo de la fuente, y no en medio de la misma. Sus medidas son de 85 mm de ancho, 65 mm de altura y 175 mm de profundidad. Eso sí, su potencia es la menor de todas. 

### **Cableado: fuentes modulares/semimodulares**

La distinción aquí es clara porque solo tendremos 3 opciones en cuanto a la administración del cableado:

- Nuestras opciones se resumen a las que ofrece la fuente de alimentación, disponiendo de las conexiones básicas y de algún adaptador, dependiendo mucho del modelo.

- Semi-modular. Son fuentes de alimentación que vienen con ciertos cables fijos, pero que ofrece posibilidad de usar conexiones modulares opcionales, especialmente en SATA y PCIe.

- Modular. Todas las conexiones son modulares, pudiendo usar únicamente las que necesitemos, y para ello tendremos varios cables en la caja de la fuente. 

### **Según su refrigeración**

En este sentido, solo encontramos 2 opciones de refrigeración, con la excepción de algunos modos semi-pasivos que tienen algunas fuentes activas. 

- **Activa.** Vienen a ser las opciones más comunes, equipando un ventilador para expulsar el calor generado por los componentes de la fuente de alimentación. Algunas fuentes más refinadas vienen con modos semi-pasivos con los que podemos disfrutar de 0 dB, es decir, pleno silencio, siempre que el PC tenga poca carga.

- **Pasiva.** Su refrigeración es mediante la convección, no equipando ningún ventilador y siendo muy silenciosas. Solo recomendamos su compra a aquellos que sepan refrigerar óptimamente su PC porque el calor del interior de la caja se disparará cuando exijamos el máximo rendimiento a nuestro equipo. 

### **Según su potencia**

La potencia de las fuentes de alimentación tiene un rango de vatios muy amplio, partiendo desde los 180 W y yendo hasta los 2.000 W. La mayoría de las personas optan entre una fuente de 450 W y 850 W debido a que no disfrutaremos nunca del 100% de toda su potencia, sino que para ello hay que tener en cuenta la eficiencia energética. """,
"Disco duro: HDD vs SSD":"""![Imagen Procesador](https://i.postimg.cc/Z5PYQK7S/discosduros-1.jpg)

Vamos a analizar las diferencias y características principales de los discos duros SSD, término que viene de Solid State Drive, contra las unidades de disco duro HDD, cuyo término procede en este caso de Hard Disk Drive. El objetivo es averiguar cuál va a resultar la mejor opción, HDD o SSD, para hacer nuestra compra.

## **Discos duros HDD**

Un disco duro HDD es un dispositivo de almacenamiento de datos que utiliza la grabación magnética para almacenar y recuperar información digital.

La principal diferencia del HDD  vs SSD es que este segundo utiliza memorias flash interconectadas sin movimiento, una unidad de disco duro o HDD está compuesta esencialmente por un plato de metal con revestimiento magnético.

Esta diferencia en la construcción hace que el funcionamiento y las características tambíen sean diferentes entre un SSD y un HDD. En un disco duro tradicional existe un revestimiento almacena los datos que cuenta con un cabezal magnético emparejado que lee y escribe datos mientras el disco gira.

Y es que a pesar de que los discos duros HDD son más antiguos, siguen siendo un dispositivo de almacenamiento muy popular entre los fabricantes y los consumidores porque son más accesibles y asequibles que las unidades de estado sólido.

## **Ventajas de un HDD vs SSD**

### **1. Más asequible que el SSD**

Una de las principales ventajas de un HDD es que es más asequible que el SSD en términos de inversión por gigabit. Y es que a partir de 1TB un SSD con una capacidad de almacenamiento similar a la de un disco duro puede ser el doble de cara.

Esto significa que los ordenadores de sobremesa o portátiles con unidades de HDD vs SSD son algo más baratos. Además, esto también se aplica a los discos duros externos de mayor capacidad.

### **2. Mayor capacidad de almacenamiento que las SSD**

Los discos duros HDD de entre  500 GB y 1 TB se han convertido en una capacidad de almacenamiento estándar para los ordenadores y las unidades externas. Por otro lado, en comparación con un disco duro, los ordenadores o dispositivos que utilizan un sistema de almacenamiento en SSD tienen una capacidad algo más limitada.

### **3. El HDD es más fácil de comprar en la mayoría de las tiendas**

Hay una abundancia de discos HDD internos o externos en el mercado. Los usuarios que deseen actualizar sus ordenadores o comprar un almacenamiento multimedia externo para hacer una copia de seguridad de sus datos encontrarán más conveniente utilizar un HDD vs SSD.

Sin embargo, los dispositivos que utilizan SSD también son cada vez más populares y la tecnología necesaria para producir esta contrapartida de HDD es cada vez más eficiente. Esto podría significar que los SSD pueden tener la misma disponibilidad en el futuro más cercano.

### **4. Mayor vida útil que las SSD**

La durabilidad en términos de ciclo de lectura y escritura es otra ventaja a mencionar de los HDD vs SSD. Las memorias flash de una unidad de estado sólido sólo se pueden utilizar para un número finito de escrituras. Un SSD no puede escribir un solo bit de información sin primero borrar y luego reescribir bloques de datos muy grandes de una sola vez. A medida que cada célula pasa por este ciclo, se vuelve más inútil.

## **Desventajas de un HDD vs SSD**

### **1. El HDD es más lento que el SSD**

Las diferentes variantes de los discos duros HDD tienen diferentes velocidades de lectura y escritura, dependiendo de su respectiva especificación de RPM o rotación por minuto. Pero aunque nos compremos el mejor modelo, no hay comparación entre la velocidad del SSD vs HDD.

Un ordenador con un sistema de almacenamiento con disco duro HDDD arrancará más lentamente que las SSD. Además, como un disco duro es propenso a la fragmentación de los datos debido a su superficie de grabación giratoria, es intrínsecamente más lento que los SSD sin fragmentación.

### **2. Mayor consumo de energía**

Otra desventaja de un HDD vs SSD es que consume más energía. El dispositivo de almacenamiento básicamente necesita más energía de entrada para girar el plato metálico y mover ese cabezal de lectura magnético. La implicación de esto es que los fabricantes optaron por un SSD para los ordenadores que son más compactos o que tienen una capacidad de batería limitada.

### **3. Produce ruido mientras está en funcionamiento**

El giro del plato metálico y el movimiento de vaivén del cabezal de lectura magnético crean ruidos mecánicos mientras un disco duro está en funcionamiento. Tanto el giro como el movimiento también crean vibraciones sutiles. Esto es más notorio durante el arranque o cuando un usuario almacena archivos grandes. El SSD es esencialmente libre de ruidos.

### **4. No es tan duradero comparado con SSD**

Una gran desventaja de un HDD es que es más propenso a fallos de seguridad o pérdida de datos y a la corrupción general del dispositivo.  Las partes mecánicas móviles de un disco duro lo hacen físicamente vulnerable a los daños mecánicos por caídas y golpes. Por ejemplo, el estrecho espacio entre el cabezal de lectura y el plato metálico hace que la unidad de disco duro sea propensa a sufrir arañazos en el plato mientras el cabezal roza el fino revestimiento magnético.

### **5. Es más grande**

Otra desventaja de un HDD vs SSD es un factor de forma más voluminoso.  Existe un límite en la fabricación de discos duros pequeños debido a la necesidad de un plato metálico giratorio y un cabezal de lectura móvil. Esto hace que los discos duros no sean adecuados para dispositivos de computación móviles como los portátiles. Ten en cuenta que los fabricantes de smartphones y ordenadores de mesa han utilizado un sistema de almacenamiento en SSD.

## **Discos duros SSD**

Los SSD son la evolución de los discos duros tradicionales, los HDD. Y es que la principal diferencia entre un SSD y un HDD es que este primero no tiene piezas móviles. Los SSD se basan en chips flash (como una memoria USB) lo que hace que sean extremadamente rápidos y menos volátiles que las HDD.

## **Ventajas de un SSD vs HDD**

### **1. Más rápido que los discos duros**

Debido a que un SSD no tiene partes mecánicas, es considerablemente más rápido que un HDD. La fragmentación de los datos en una unidad de estado sólido es insignificante, a diferencia de lo que ocurre en una unidad de disco duro, lo que la hace inherentemente más rápida.

Un SSD es de 25 a 100 veces más rápido que un HDD. Esto se traduce en tiempos de arranque más rápidos, transferencias de archivos más rápidas y mayor ancho de banda para la informática empresarial.

### **2. Bajo consumo de energía**

Un disco duro consume más energía porque depende de la rotación del plato de metal recubierto de imanes para leer y escribir datos. Un SSD no tiene partes móviles y no requiere trabajo mecánico para ser operativo.

Esto significa que si enfrentamos un HDD vs SSD, este segundo será el mejor para ordenadores de bajo consumo y dispositivos electrónicos de consumo porque disminuye la susceptibilidad de un ordenador o dispositivo al sobrecalentamiento.

### **3. Más duradero que los discos duros**

Una de las principales desventajas del HDD vs SSD es la susceptibilidad a la pérdida de datos y a la avería general del dispositivo debido a caídas y temblores.  Este inconveniente se debe a las piezas mecánicas o movibles dentro de un disco duro. Dado que las SSD no tienen piezas mecánicas o móviles, son más resistentes a las caídas y los temblores, lo que las hace más resistentes a la pérdida de datos causada por un trauma físico o externo.

### **4. No hay ruido durante el funcionamiento**

La ausencia de una placa metálica giratoria para almacenar datos y un brazo de lectura móvil hace que un SSD sea completamente silencioso mientras está en funcionamiento.  En un HDD es imposible alcanzar estas cotas de silencio porque la rotación del plato de metal y el movimiento de vaivén del brazo de lectura crean ruido y vibraciones, por muy sutiles que sean.

### **5. Más compacto que los discos duros**

Un SSD es considerablemente más compacto que un HDD debido a la ausencia de partes mecánicas o móviles.  Esto también significa que una unidad de estado sólido es un componente de almacenamiento más adecuado o ventajoso para los dispositivos electrónicos de consumo portátiles como los ultra-book y las tablets o Smartphones.

## **Desventajas de un SSD vs HDD**

### **1. Más caro que los discos duros**

Un SSD es más caro que un HDD B. En comparación con una unidad de disco duro, una unidad de estado sólido con una capacidad de almacenamiento similar por encima de los 500GB será más cara que un HDD. Esto se traduce en ordenadores u otros dispositivos más caros con sistemas de unidades de estado sólido que los que tienen sistemas de discos duros.

### **2. Capacidad de almacenamiento limitada**

Los actuales SSD del mercado tienen una capacidad de almacenamiento limitada. Los ordenadores o dispositivos con un sistema de almacenamiento en SSD suelen tener una capacidad de almacenamiento de 1 TB como máximo de media. Por el contrario, no es raro ver discos duros HDD con una capacidad de hasta 4 TB..

### **3. Mala disponibilidad**

Aunque cada vez menos, otra desventaja de los SSD vs HDD  es la disponibilidad, y es que los discos duros HDD son más abundantes en el mercado. Desde el almacenamiento interno de los ordenadores o dispositivos hasta el almacenamiento externo de medios, los discos duros son más fáciles de encontrar.

Pero como ya te hemos adelantado, el mercado de la electrónica de consumo se está inclinando ahora hacia dispositivos más compactos. Esto significa que las SSD también están disponibles, pero no son tan abundantes como los discos duros.

### **4. Vida útil más corta que los discos duros**

Aunque físicamente son más resistentes, un SSD tiene un ciclo de escritura limitado. Las memorias flash de una unidad de estado sólido sólo se pueden utilizar para un número finito de escrituras. Un SSD no puede escribir un solo bit de información sin borrar y luego reescribir bloques de datos muy grandes de una sola vez.

## **Conclusión ¿Cuál es mejor SSD o HDD?**

Llegados a este punto estamos bastante seguros de que conoces todas las características, virtudes y diferencias de los HDD vs SSD. Pero si todavía te cuesta decidirte vamos a darte unos últimos consejos rápidos. Pero una cosa está clara y la conclusión es que, ningún disco duro es mejor que otro, son tan diferentes que cada uno sirve para una cosa.

- Si necesitas mucho espacio, compra un HDD.

- Si necesitas que tu ordenador vaya más rápido, compra un SSD.

- Si eres gamer, compra un SSD.

- Si eres diseñador gráfico, fotógrafo o editor, compra un HDD.

- Si tienes poco presupuesto, compra un SSD de menor capacidad.

- Si estás moviendo archivos siempre del disco duro al pendrive, compra un SSD

- Si te da igual qué comprar, compra un SSD.""","Torres y Cajas de PC":"""![Imagen Procesador](https://i.postimg.cc/pTQXwVX8/Torrepc-1.jpg)

Placa base, memoria RAM, procesador, tarjeta gráfica, disco duro… Todos estos elementos son esenciales a la hora de montar un PC que pueda “con todo lo que le echen por delante”. Sin embargo, cualquiera de estos componentes carece de sentido sino se tiene una buena caja donde ensamblarlos. Un ordenador de altas prestaciones necesita de una buena refrigeración a través de todos sus componentes.

## **Formatos ATX, ITX y HTPC. ¿Qué diferencia hay?**

Empezaremos a hablar sobre el chasis, sin duda una de las características más importantes a la hora de elegir un componente como este y que tienen que ver sobre todo con el tipo de placa base que vamos a escoger.

Con el  auténtico “boom” y demanda que hay en la actualidad a la hora de jugar en la ‘PC Master Race’, hay que decir que cada vez la oferta y el catálogo es más amplio. De ahí que veamos necesario hacer la siguiente distinción.

- **Cajas HTPC.** No prestaremos mucha atención a este tipo por la verdad que solo se usan en el ámbito de la ofimática y multimedia en general. Las cajas HTPC se caracterizan por ser de pequeñas dimensiones y su predisposición suele ser en horizontal, algo que permite aprovechar mucho mejor el espacio disponible. Por esta razón, son un tipo que a las que las grandes empresas suelen acudir mucho ya que les permite ahorrar costes (son más económicas) y encima es posible poner después una pantalla encima de ellas.

- **Cajas ITX.** Estas también tuvieron su “público” hace tan solo unos años. Aunque la verdad que últimamente están perdiendo un poco de peso en el mercado. Entre sus características más notorias, cabe destacar sus más que reducidas dimensiones que permiten después ponerlas en habitaciones de poco espacio.  Muchas de ellas suelen tener forma cúbica, consiguiendo así un aspecto de lo más original. Y encima en su interior se pueden instalar todo tipo de periféricos de grandes dimensiones, algo que suele ocurrir sobre todo con los disipadores y GPU de gama media/alta.

- **Cajas ATX.** Sin duda “la reina de las cajas” dentro de la comunidad de jugones. Ofrecen un catálogo realmente amplio junto a un precio y unas prestaciones nada desdeñables. Otra de sus grandes bazas es que las podemos encontrar en tamaños y formas muy distintas que seguro que se adaptarán a nuestras necesidades. También permiten una más que optima colocación de todos los componentes (RAM, placa base, procesador, GPU…) con el único objetivo de que la refrigeración de todos ellos sea siempre sea óptima.

Además de las cajas que conocemos como torres de PC, conocemos otros formatos de "caja" para ensamblar los componentes de un ordenador. Vamos a ver otra forma de tipificar las cajas de ordenador.

A continuación te ayudamos a distinguir entre los diferentes tipos de cajas de PC para que a partir de ahora puedas identificarlos sin ningún problema.

## **Tipos de cajas de PC**

Como hemos dicho, hay muchas clasificaciones de tipos de cajas de PC, pero si nos basamos específicamente en la placa que pueden incluir en su interior, encontramos la siguiente clasificación:

### **Cajas de PC tipo torre**

Las cajas de tipo torre son las más grandes que pueden vincularse a un PC. De hecho, están pensadas para construir servidores SOHO (Small Office - Home Office).

Al pensar en incluir CPU para servidores, se trata de la caja de PC más grande de todas y, por tanto, no es la más habitual salvo en entornos de oficinas con importantes bases de datos o vinculadas al sector tecnológico.

Normalmente incluyen placas base con formato E-ATX, pero no son exclusivas para ellas, ya que también pueden incluir placas base ATX.

Estas últimas son más modestas y, a pesar de su capacidad, no suelen utilizarse en torres de PC. Sin embargo, sí que están siendo aprovechadas en el sector gaming.

Las torres de PC tienen suficiente tamaño como para incluir accesorios muy solicitados en el mundo gaming, desde componentes que mejoren la capacidad del ordenador, hasta elementos estéticos como luces de neón. Para todo ello hace falta más espacio que en una caja corriente, por eso las torres para PC son el formato ideal para estos usuarios.

### **Cajas de PC tipo semitorre**

Las cajas de PC tipo semitorre están presentes en hogares y oficinas de todo el mundo.

La integración de las placas base ATX ha encontrado en ellas el espacio perfecto para ofrecer a los usuarios una experiencia informática idónea, mejor incluso que la ofrecida con placas micro-ATX que requerían tarjetas de expansión para ser ampliadas.

Estas cajas semitorre tienen suficiente espacio para incluir placa base y otros componentes como RAM, procesador, tarjeta gráfica y mucho más. Gracias a ello permiten crear ordenadores que pueden servir desde para trabajar en el día a día hasta para juego online con las máximas prestaciones.

Además, su popularidad ha incentivado la creatividad. Hoy en día puedes encontrar cajas semitorre con diseños espectaculares y que encajarán perfectamente con el estilo que buscas, desde elegantes y sofisticadas, hasta modelos futuristas únicos.

### **Cajas de PC tipo microtorre**

El diseño más compacto de torre para PC es el de la microtorre, que además puede ser distinta según la placa base que incluye.

De esta forma distinguimos los siguientes formatos:

- **Mini-ITX:** Es el formato más pequeño de todos y también el más conocido. Puede incluir placas base de 17 x 17 cm, lo que deja fuera a las ATX e incluso a las Micro-ATX.

- **DTX:** Cajas de PC para placas base de tipo DTX, algo más pequeñas que las ATX corrientes. Incluye un slot de expansión adicional.

- **Mini-DTX:** Un formato híbrido entre los dos anteriores, pensado en esencia para placas DTX que puedan precisar dos puertos de conexión.

### **Cajas de PC tipo barebone**

Una caja barebone en realidad consiste en un ordenador ya preconfigurado, que tiene los componentes básicos para funcionar, tales como placa base y fuente de alimentación.

En la actualidad hay disponible una amplia variedad de barebones de diferentes estilos, todos ellos compactos y portátiles para llevar donde quieras.

Pese a su tamaño, son muy silenciosos y tienen diseños muy bien trabajados, para encajar perfectamente en cualquier escritorio. La opción ideal para contar con un ordenador básico sin ocupar prácticamente espacio.

## **La refrigeración.**

Los PC’s actuales llegan a ser tan potentes en su rendimiento, que obviamente consumirán más energía y por ende la temperatura de todos sus componentes se puede disparar si no hay una correcta refrigeración.

Una buena forma de evitarlo es obviamente eligiendo una caja de ordenador que sea los suficiente amplia y que permite instalar todos los componentes de una manera ordenada y sobre todo eficiente. Para ello, habrá que tener en cuenta los siguientes aspectos:

### **Los cables**

Si es la primera vez que montamos un PC seguro que nos volveremos locos con ellos. Por un parte, tenemos los que vienen con la propia caja y que básicamente están destinados a hacer las conexiones más básicas del ordenador como son las de botón de ‘RESET, ‘ON’ y OFF. A partir de ahí, solo hay que ir pasando los cables que vienen dentro de la propia fuente de alimentación (que suelen ser de los de mayor grosor” y después los que salen del propio disipador y conexiones SATA.

Huelga decir que hay que elegir una caja que permita disponer todos los cables de una forma ordenada. Todo ello sin mencionar que no debe ejercer demasiada presión a la hora de pasarlos por los distintos recovecos y orificios de la caja. De esta forma se evitarán cortocircuitos y sobrecalentamientos inesperados.

### **Ventiladores propios**

Cada vez son más las cajas que vienen con ventiladores tanto en la parte frontal, lateral como trasera. En muchas ocasiones el disipador que compramos para la CPU no es suficiente. Es aquí donde entran en juego los que vienen con la torre. Gracias a ellos, es posible que todo el aire “fluya” mejor a través de todos los componentes hasta que lo expulsan por el exterior.  Un ordenador no deja de ser como el motor de un coche que cuando más aceleremos, más se irá calentando. De ahí que sea muy necesario que la refrigeración sea la adecuada. Incluso son muchos los usuarios que optan por una refrigeración líquida.

Sobre todos aquellos que se decantan por productos AMD que siempre se han caracterizado por tener unas temperaturas bastante altas, algo que han arreglado un “poco” con la nueva gama de Ryzen, que tantos titulares está copando últimamente. Prestad mucha atención a futuras noticias, porque nuestro compi Adolfo siempre está al tanto de todo a la hora de informaros sobre estos procesadores.

## **El ruido excesivo puede ser algo muy molesto**

Es muy normal que con todos estos componentes, temperaturas y ventiladores, todo el orndeador llegue a hacer un ruido considerable. Aunque hay que decir que las compañías más punteras como Intel lanzan cada vez CPU y tarjetas gráficas realmente silenciosas sin que esto suponga sacrificar rendimiento.

Aunque esto no quiere decir que de vez en cuando estos hagan a veces un ruido algo molesto, sobre todo cuando los “exprimimos” al máximo a la hora de jugar a cualquier juego de esta generación. Sin embargo, a la hora de comprar una caja, no está de más fijarse en los siguientes aspectos para así conseguir el menor ruido posible.

- **Material aislante de sonido.** Existen muchas cajas que vienen con placas en sus materiales hechos con elementos aislantes del sonido como el caucho. La verdad que son una opción a tener muy en cuenta para todas aquellas personas que comparten casa o habitación y se tiran muchas horas delante del ordenador y quieren pasar “completamente desapercibidas”.

- **Excesivo uso de plásticos.** Hay que decir que el plástico no es el mejor elemento para aislar el sonido. Por tanto, a la hora de comprar una caja hay que prestar mucha atención a este aspecto. Algo parecido ocurre con los aceros que si son de una mala aleación pueden provocar que el ruido sea mayor.

- **Sistema anti vibración.** Con la cantidad de componentes que existen dentro de una caja, es muy normal que se produzcan multitud de vibraciones provenientes por ejemplo de los disipadores del CPU como de la propia tarjeta gráfica. En este sentido. Las cajas más actuales ofrecen todo tipo de sistemas antivibración, sobre todo en la base y en los laterales con el objetivo de que no se produzcan ruidos indeseados."""
,"Compatibilidad entre componentes de PC":"""![Imagen Procesador](https://i.postimg.cc/zBHPv3Rb/Compatibilidad-Componentes-1.jpg)

Cuando compramos un PC a piezas o queremos actualizar algún componente, podemos cometer errores en la elección. En ocasiones, no podemos conectar ciertos componentes por incompatibilidades, así que vamos a tratarlas todas a continuación.

## **La placa base y su compatibilidad con otros componentes**

Vamos a examinar la compatibilidad de la placa base con los componentes que conectamos en ella, habiendo importantes detalles a tener en cuenta en la configuración.

### **Compatibilidad de la placa base y el procesador**

La CPU y la placa base han de ser compatibles, y dicha compatibilidad se resume a lo siguiente.

#### **Compartir socket o zócalo.**

Tanto la placa base, como el procesador deben estar diseñados para el mismo socket; de lo contrario, la CPU no encajará a la hora de instalarla. Tened en cuenta que el procesador se instala en el socket (LGA1700, LGA1200, AM4, etc.), por lo que, si no es compatible, no cabrá en el hueco.

#### **El chipset de la placa base**

Aclarada la compatibilidad entre el procesador y la placa base, tenemos que acudir al chipset de la misma. El chipset controla las comunicaciones entre CPU, RAM, almacenamiento y más periféricos, siendo diseñados por Intel o AMD.

Aunque sean diseñados por Intel o AMD, quienes los distribuyen son MSI, ASUS, NZXT, EVGA, Biostar ASRock y GIGABYTE a través de sus placas base. Dentro de una generación de sockets, encontramos varios chipsets que se dividen por gamas: de entrada, mainstream y entusiasta.

Para el usuario, elegir entre un chipset u otro va a significar disfrutar de más o menos funciones en la placa base:

- Overclock en la CPU.

- Más soporte de frecuencias en RAM.

- Mejor conectividad.

- Overclock en las memorias RAM.

Por ejemplo, AM4 tiene 3 generaciones de chipsets (serie 300, 400 y 500) y, aunque los últimos Ryzen 5000 sean compatibles con AM4, no son compatibles con todas las placas de la serie 300.

Los fabricantes de placas base suelen actualizar ciertos modelos para el soporte de nuevos procesadores, pero hay veces que esto no es posible, ¿por qué? Porque las nuevas CPUs pueden tener necesidades de voltaje distintas e incompatibles con las placas base más antiguas (aunque tengan el mismo socket).

### **Compatibilidad de la placa base con memoria RAM**

Pueden surgir incompatibilidades a la hora de configurar un PC a piezas, especialmente cuando se trata de elegir placa base y memoria RAM. Te detallamos qué debes tener en cuenta respecto a la compatibilidad de la placa base y memoria RAM.

#### **Tipo de memoria RAM: DDR3, DDR4 o DDR5**

Esto es lo primero que debéis mirar cuando vais a comprar memoria RAM o una placa base: ambas deben ir al unísono. No podremos instalar módulo DDR3 en una placa base que soporte DDR4, como DDR4 en una placa con DDR5. Si te preguntas por qué, físicamente no encajan.

Así que, tenedlo en cuenta si vais a comprar memoria RAM, como si vais a configurar un PC a piezas.

Por otro lado, hacer mención especial para quienes queréis mejorar la memoria RAM de vuestro portátil: averiguad antes si se puede y ver qué memoria usa. Hay modelos en los que no se puede actualizar (especialmente los que llevan memoria LPDDR) porque llevan la RAM soldada o porque están cerrados de cierta manera que lo hacen inviable.

#### **Frecuencia de memoria RAM**

Muchos cometen el error de comprar memoria RAM con una frecuencia mayor que la soportada por la placa base. Esto es una pérdida de dinero porque habremos pagado más dinero por unas memorias RAM que van a funcionar mucho más lento de lo que deberían.

La placa base es la piedra angular de toda la configuración, y tenemos que leernos bien qué zócalo, chipset y características lleva. Entre éstas, encontramos la frecuencia de memoria RAM que soporta (2.666 MHz, 3.200 MHz, etc.), por lo que debemos comprar e instalar unos módulos acordes.

¿Qué ocurre si compramos módulos de la misma tecnología DDR, pero más rápidos de lo qué soporta la placa? Que funcionarán a la frecuencia por defecto (2133 MHz, normalmente) y que solo podremos subir su frecuencia a la máxima soportada por la placa base.

Por ejemplo, si la placa soporta un máximo de 2.666 MHz e instalamos módulos de 3.200 MHz, éstos funcionarán como máximo a 2.666 MHz, ¡estaremos perdiendo más de 500 MHz!

#### **Slots de la memoria RAM**

Como habréis visto, podéis comprar packs de 2 módulos, de 4 módulos o comprar un módulo que funcione en Single Channel. Antes de comprar nada, revisad cuántos slots o ranuras de memoria RAM tiene la placa base porque luego vienen las sorpresas.

Hay placas que solo tienen 2 slots, lo que nos obliga a tener configuraciones de 2 módulos o uno en Single Channel. En DDR4, puede ser un problema tener solo 2 ranuras si queremos instalar 32 GB o 64 GB en total porque elevará bastante el precio del pack.

Es cierto que existen packs de 2 módulos de 32 GB (64 GB en total), pero encarecen mucho el precio de las mismas porque obligan a los fabricantes de memoria RAM a insertar más memoria por módulo. Esto en la memoria RAM DDR5 no es un problema porque la densidad es mayor y los módulos parten de los 16 GB individuales, por lo que las configuraciones de 32 GB son muy usuales.

Por otro lado, cuidado con combinar memorias RAM de diferente capacidad: puede funcionar, como no hacerlo. En definitiva, antes de comprar nada, revisa qué slots tienes.

#### **Cuidado con el formato en los portátiles**

En el mercado encontraréis módulos SO-DIMM y DIMM: las memorias RAM usadas en portátiles son las SODIMM. Veréis que no tienen tanta frecuencia, que son algo más caras y que tienen menos capacidad, siendo también más pequeñas. Tienen un aspecto más “recortado” respecto a la versión de sobremesa.

### **Compatibilidad de la placa base con otros componentes**

Nos queda abordar la compatibilidad de la placa base con otros componentes, como es la tarjeta gráfica y los SSDs, por ejemplo.

#### **Tarjeta gráfica y placa base**

Las tarjetas gráficas hacen uso de una ranura PCI-Express y de una serie de raíles, algo a tener muy en cuenta con nuestra placa base. En términos de rendimiento, se ha visto que la diferencia entre PCIe 3.0 y 4.0 prácticamente no existe, pero sí existe cuando hacemos uso de 16 raíles (x16) u 8 raíles (x8).

Encontraréis una serie de ranuras PCI-Express en las placas base, pero debéis recordar que hay que usar la que más raíles ofrezca (x16, generalmente). Esta ranura es la más grande de todas y es la que está más cerca del socket de la CPU, incluso estando reforzada por acero en algunas placas base.

Si la GPU hace uso de PCIe 3.0 x16, perderá rendimiento si nuestra placa base no tiene una ranura PCIe 3.0 x16, sino que el máximo es x8.

Aconsejamos 2 cosas:

- Comprobar qué ranuras tenemos en la placa base y qué raíles ofrecen a través de la ficha técnica.

- Mirar qué interfaz PCIe usa la GPUen su ficha técnica.

De esta manera, podéis cuadrar ambos componentes sin problemas. Por ejemplo, las NVIDIA GeForce RTX 3000 y AMD Radeon RX 6000 hacen uso de PCI-Express 4.0, habiendo modelos que usan x16, x8 y otros x4.

#### **SSD y SSD M.2**

Con los SSD de 2.5 pulgadas no suele haber ningún problema porque hacen uso de la interfaz SATA, igual que los HDD. La mayoría de placas base incorporan 6 puertos SATA, por lo que instalar un SSD de 2.5 pulgadas nunca será un problema.

La cosa cambia cuando queremos instalar un SSD M.2: la placa base debe tener un slot preparado para ello y la de 2016-2017 pueden no tenerlo. Este slot hace uso de la interfaz PCI-Express, aunque no estemos conectando el SSD a una ranura PCIe.

Aquí hay que tener en cuenta 2 cosas:

- Los raíles que usa el slot M.2.

- La interfaz que usa el SSD: PCIe 3.0, 4.0 o 5.0.

#### **Factor de forma del SSD M.2.**

No solo tiene que haber compatibilidad entre SSD y placa base respecto al slot M.2, sino que dicho slot debe hacer uso de los raíles que necesita el SSD (normalmente x4). Además, hay una gran diferencia entre un SSD PCIe 3.0 y 4.0: concretamente, más de 3.000 MB/s de transferencia de datos.

Para terminar, cuidado con el factor de forma del SSD M.2. Éste viene reflejado en su ficha técnica, al igual que la placa base también lo establece en su ficha técnica. El factor de forma o formato del SSD M.2 se diferencia por Type o Tipo y por sus dimensiones, siendo las más comunes:

- Type 2280: 80 mm x 22 mm.

- Type2260: 60 mm x 22 mm.

- Type22100: 110 mm x 22 mm

- Type2242: 42 mm x 22 mm.

Esto lo debéis cotejar especialmente cuando vais a instalar un SSD M.2 en vuestro portátil, ya que el espacio es más limitado y los modelos no son compatibles con varios formatos. En el caso de las placas base, suele haber compatibilidad con la mayoría de formatos.

#### **Placa base y la caja PC**

La placa base tiene unos conectores internos en los que se conectan unas clavijas de la caja PC, teniendo como función conectar los puertos frontales de la caja PC con el sistema. Pues bien, la incompatibilidad viene cuando elegimos una caja PC que no soporta todas las conexiones frontales de la placa base.

De este modo, estaremos desaprovechando puertos que podríamos disfrutar porque nuestra placa base está habilitada por ello. Lo mismo ocurre al revés: que la caja PC soporte tecnologías avanzadas (USB 3.2) y la placa base se resuma a USB 3.1 y USB 3.0."""

        
    }
    
    componente_seleccionado = st.selectbox("Selecciona un componente", list(componentes.keys()))
    st.write(componentes[componente_seleccionado])

def mostrar_ml():
    st.title("Análisis de Componentes")
    # Leer el DataFrame
    data_CPU = pd.read_csv('cpu_ferran_clean.csv')  
    data_GPU = pd.read_csv('gpu_ferran_clean.csv')
    data_SSD = pd.read_csv('ssd_limpio.csv')
    data_RAM = pd.read_csv('Ram_clean.csv')
    
     # Establecer estilo de Streamlit para las tablas
    # Mostrar el DataFrame
    st.write('A continuación se muestra los siguientes datos:')

# Establecer estilos para las tablas
    st.markdown("""
    <style>
        .dataframe tbody tr th {
            color: white !important;
        }
        .dataframe tbody tr td {
            color: white !important;
        }
        .dataframe thead th {
            background-color: transparent !important;
        }
        .dataframe tbody tr:hover {
            background-color: rgba(255,255,255,0.3);
        }
    </style>
""", unsafe_allow_html=True)

# Mostrar las tablas
    st.markdown("### Tabla de CPU")
    st.write(data_CPU.head(5))

    st.markdown("### Tabla de GPU")
    st.write(data_GPU.head(5))

    st.markdown("### Tabla de RAM")
    st.write(data_RAM.head(5))

    st.markdown("### Tabla de SSD")
    st.write(data_SSD.head(5))
    
#     st.markdown("""<style>
#                     .dataframe th {
#                         color: white !important;
#                         background-color: black !important;
#                         font-weight: bold !important;
#                     }
#                     .dataframe td {
#                         color: white !important;
#                         background-color: black !important;
#                         font-weight: bold !important;
#                     }
#                     </style>
                    
#                     data_CPU.to_markdown()""",
#                 unsafe_allow_html=True
#                )

# data_CPU.style.to_latex()


    # Opción para seleccionar el tipo de componente
    chart_type = st.selectbox('Seleccione el tipo de componente:', ['CPU', 'GPU', 'RAM', 'SSD'])

    # Gráfico de barras
    if chart_type == 'CPU':
                
        st.subheader('Relacion entre Nombre y Precio de las CPU con mayor y menor Ranking')
        sns.set(style="dark")
        fig1, ax = plt.subplots(figsize=(10, 6))
        sns.scatterplot(x=data_CPU["Nombre"].head(20), y=data_CPU["Precio"].head(20),color='red', ax=ax)
        plt.title("Precio de cada CPU")
        plt.xlabel("Nombre")
        plt.ylabel("Precio")
        plt.xticks(rotation=90, ha='right')
        fig1.patch.set_facecolor('black')
        ax.set_facecolor('black')
        ax.xaxis.label.set_color('white')
        ax.yaxis.label.set_color('white')
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')
        # st.pyplot(fig1)

    
        # st.subheader('Relacion entre Nombre y Precio de las CPU con menor Ranking')
        sns.set(style="dark")
        fig2, ax = plt.subplots(figsize=(10, 6))
        sns.scatterplot(x=data_CPU["Nombre"].tail(20), y=data_CPU["Precio"].tail(20),palette="rocket", ax=ax)
        plt.title("Precio de cada CPU")
        plt.xlabel("Nombre")
        plt.ylabel("Precio")
        plt.xticks(rotation=90, ha='right')
        fig2.patch.set_facecolor('black')
        ax.set_facecolor('black')
        ax.xaxis.label.set_color('white')
        ax.yaxis.label.set_color('white')
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')
        # st.pyplot(fig2)
        
        # Mostrar las gráficas en Streamlit
        
        col1, col2 = st.columns(2)  # Dividir la pantalla en 2 columnas

        with col1:
            st.pyplot(fig1)  # Mostrar la primera gráfica en la primera columna

        with col2:
            st.pyplot(fig2)  # Mostrar la segunda gráfica en la segunda columna

        
        st.subheader('Relacion entre Nombre y Nº Nucleos de las CPU')
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.set(style="darkgrid")
        sns.barplot(x=data_CPU["Nombre"].head(20), y=data_CPU["Numero_Nucleos"].head(20), palette="viridis")
        plt.title("Nucleo de cada CPU")
        plt.xlabel("Nombre CPU")
        plt.ylabel("Nº Nucleo")
        plt.xticks(rotation=90)
        fig.patch.set_facecolor('black')
        ax.set_facecolor('black')
        ax.xaxis.label.set_color('white')
        ax.yaxis.label.set_color('white')
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')
        st.pyplot(fig)
        
    elif chart_type == 'GPU':
        
        st.subheader('Relacion entre Nombre y Precio de las GPU con mayor Ranking')
        sns.set(style="darkgrid")
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.boxplot(x=data_GPU["Chip"].head(100), y=data_GPU["Precio"].head(100), color='yellow')
        plt.title("Precio de cada GPU")
        plt.xlabel("Nombre Chip")
        plt.ylabel("Precio")
        plt.xticks(rotation=90, ha='right')
        fig.patch.set_facecolor('black')
        ax.set_facecolor('black')
        ax.xaxis.label.set_color('white')
        ax.yaxis.label.set_color('white')
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')
        st.pyplot(fig)

        st.subheader('Relacion entre Nombre y Precio de las GPU con peor Ranking')
        sns.set(style="darkgrid")
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.boxplot(x=data_GPU["Chip"].tail(50), y=data_GPU["Precio"].tail(50), color='yellow')
        plt.title("Precio de cada GPU")
        plt.xlabel("Nombre Chip")
        plt.ylabel("Precio")
        plt.xticks(rotation=90, ha='right')
        fig.patch.set_facecolor('black')
        ax.set_facecolor('black')
        ax.xaxis.label.set_color('white')
        ax.yaxis.label.set_color('white')
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')
        st.pyplot(fig)

                
        st.subheader('Conteo de los Fabricante')
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.set(style="darkgrid")
        conteo_Fabricante = data_GPU['Fabricante'].value_counts().head(25)
        sns.barplot(x=conteo_Fabricante.index, y=conteo_Fabricante.values, palette="pastel")
        plt.xlabel('Fabricantes')
        plt.ylabel('Frecuencia')
        plt.title('Conteo de nº de Fabricante en SSD')
        plt.xticks(rotation=90)
        fig.patch.set_facecolor('black')
        ax.set_facecolor('black')
        ax.xaxis.label.set_color('white')
        ax.yaxis.label.set_color('white')
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')
        st.pyplot(fig)



    elif chart_type == 'RAM':

        st.subheader('Relacion entre Nombre y Precio de las RAM con mayor Ranking')
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.set(style="darkgrid")
        sns.barplot(x=data_RAM["Nombre"].head(25), y=data_RAM["Precio"].head(25), palette="viridis")
        plt.title("Precio de cada RAM")
        plt.xlabel("Nombre Chip")
        plt.ylabel("Precio")
        plt.xticks(rotation=90)
        fig.patch.set_facecolor('black')
        ax.set_facecolor('black')
        ax.xaxis.label.set_color('white')
        ax.yaxis.label.set_color('white')
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')
        st.pyplot(fig)

        st.subheader('Relación entre Nombre y Latencia de las RAM de 32 GB')
        sns.set(style="darkgrid")
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.scatterplot(x=data_RAM["Nombre"].head(17), y=data_RAM["Latencia (ns)"].head(17), color='#FFA500')
        plt.title("Latencia de cada RAM de 32 GB")
        plt.xlabel("Nombre Chip", color='white', fontweight='bold')
        plt.ylabel("Latencia (ns)", color='white', fontweight='bold')
        plt.xticks(rotation=90, ha='right')
        fig.patch.set_facecolor('black')
        ax.set_facecolor('black')
        ax.xaxis.label.set_color('white')
        ax.yaxis.label.set_color('white')
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')
        st.pyplot(fig)
        
        
        st.subheader('Relacion entre Nombre y Velocidad de las RAM de 32 GB')
        sns.set(style="darkgrid")
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.scatterplot(x=data_RAM["Nombre"].head(17), y=data_RAM["Velocidad"].head(17), color='yellow')
        plt.title("Velocidad de cada RAM de 32 GB")
        plt.xlabel("Nombre Chip")
        plt.ylabel("Velocidad")
        plt.xticks(rotation=90, ha='right')
        fig.patch.set_facecolor('black')
        ax.set_facecolor('black')
        ax.xaxis.label.set_color('white')
        ax.yaxis.label.set_color('white')
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')
        st.pyplot(fig)
        
        

    elif chart_type == 'SSD':
        
        
        st.subheader('Conteo de los Fabricantes')
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.set(style="darkgrid")
        conteo_Fabricante = data_SSD['Fabricante'].value_counts()
        sns.barplot(x=conteo_Fabricante.index, y=conteo_Fabricante.values, palette="viridis")
        plt.xlabel('Fabricantes')
        plt.ylabel('Frecuencia')
        plt.title('Conteo de nº de Fabricante en SSD')
        plt.xticks(rotation=45)
        fig.patch.set_facecolor('black')
        ax.set_facecolor('black')
        ax.xaxis.label.set_color('white')
        ax.yaxis.label.set_color('white')
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')
        st.pyplot(fig)

        st.subheader('Conteo de los Nombres')
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.set(style="darkgrid")
        conteo_cache = data_SSD['Nombre'].head(50).value_counts()
        sns.barplot(x=conteo_cache.index, y=conteo_cache.values, palette="deep")
        plt.xlabel('Nombres SSD')
        plt.ylabel('Frecuencia')
        plt.title('Frecuencia de los Nombres en SSD')
        plt.xticks(rotation=90)
        fig.patch.set_facecolor('black')
        ax.set_facecolor('black')
        ax.xaxis.label.set_color('white')
        ax.yaxis.label.set_color('white')
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')
        st.pyplot(fig)
        
        st.subheader('Conteo de Interfaz')
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.set(style="darkgrid")
        conteo_cache = data_SSD['Interfaz'].value_counts()
        sns.barplot(x=conteo_cache.index, y=conteo_cache.values, palette="viridis")
        plt.xlabel('Interfaz')
        plt.ylabel('Frecuencia')
        plt.title('Conteo de Interfaces en SSD')
        plt.xticks(rotation=0)
        fig.patch.set_facecolor('black')
        ax.set_facecolor('black')
        ax.xaxis.label.set_color('white')
        ax.yaxis.label.set_color('white')
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')
        st.pyplot(fig)

        
def algoritmo_genetico(presupuesto, CPU, GPU, SSD, RAM):
    Muta = 0.15  # Probabilidad de mutacion
    N_padres = 40  # Numero de padres en la seleccion de cruces
    N_Poblacion = 100  # Numero de individuos en la poblacion
    GenMax = 500  # Número de generaciones max

    # Presupuesto máximo descontando los componentes genéricos
    presupuesto_maximo = presupuesto - 120 - 70 - 110

    def RandomCrom(Pres=presupuesto_maximo, CPU=CPU, GPU=GPU, SSD=SSD, RAM=RAM):
        Crom_List = []
        Total = 0
        while Total > Pres or Total == 0:
            CPU_Crom = random.randint(0, len(CPU) - 1)
            GPU_Crom = random.randint(0, len(GPU) - 1)
            SSD_Crom = random.randint(0, len(SSD) - 1)
            RAM_Crom = random.randint(0, len(RAM) - 1)
            Total = CPU['Precio'][CPU_Crom] + GPU['Precio'][GPU_Crom] + SSD['Precio'][SSD_Crom] + RAM['Precio'][
                RAM_Crom]
        Crom_List.append(CPU_Crom)
        Crom_List.append(GPU_Crom)
        Crom_List.append(SSD_Crom)
        Crom_List.append(RAM_Crom)
        return Crom_List

    def RankCrom(crom_list: list, df_cpu=CPU, df_gpu=GPU, df_ssd=SSD, df_ram=RAM):
        Rank_List = []
        Rank_List.append(df_cpu['Ranking'][crom_list[0]])
        Rank_List.append(df_gpu['Ranking'][crom_list[1]])
        Rank_List.append(df_ssd['Rank'][crom_list[2]])
        Rank_List.append(df_ram['Rank'][crom_list[3]])
        return Rank_List

    def FitMaker(RankPob: list):
        Fitness_list = []
        for i in range(len(RankPob)):
            Fitness_list.append(sum(RankPob[i]))
        return Fitness_list

    def PrecioCrom(Pob: list):
        Precio_list = []
        for i in range(len(Pob)):
            Precio_cr = 0
            for j in range(len(Pob[i])):
                if j == 0:
                    Precio_cr += CPU['Precio'][Pob[i][j]]
                if j == 1:
                    Precio_cr += GPU['Precio'][Pob[i][j]]
                if j == 2:
                    Precio_cr += SSD['Precio'][Pob[i][j]]
                if j == 3:
                    Precio_cr += RAM['Precio'][Pob[i][j]]
            Precio_list.append(round(Precio_cr, 2))
        return Precio_list

    def CruceNCromosomas(n=N_padres, Pob=[], i_padres=[], m=Muta):
        padres = []
        hijos_totales = []
        precio_hijos = []
        Precio_1 = []
        Precio_2 = []
        random.shuffle(i_padres)
        for i in range(0, len(i_padres), 2):
            # Primero creamos las parejas
            padres.append([i_padres[i], i_padres[i + 1]])
        for j in range(len(padres)):
            # Creacion de nuevos hijos mediante cruce homogeneo (intercambiamos)
            hijo_1 = []
            hijo_2 = []
            lista_aux = Pob[padres[j][0]]
            for k in range(len(Pob[padres[j][0]])):
                if k % 2 == 0:
                    hijo_1.append(Pob[padres[j][0]][k])
                    hijo_2.append(Pob[padres[j][1]][k])
                else:
                    hijo_1.append(Pob[padres[j][1]][k])
                    hijo_2.append(Pob[padres[j][0]][k])
            if random.random() < m:  # Calculamos aleatoriamente si muta o no
                nrandom = random.randint(0, len(hijo_1) - 1)
                Crom_random = RandomCrom()
                hijo_1[nrandom] = Crom_random[nrandom]
            if random.random() < m:  # Calculamos aleatoriamente si muta o no
                nrandom = random.randint(0, len(hijo_2) - 1)
                Crom_random = RandomCrom()
                hijo_2[nrandom] = Crom_random[nrandom]
            Precio_1 = []
            Precio_2 = []
            aux1 = []
            aux2 = []
            aux1.append(hijo_1)
            aux2.append(hijo_2)
            Precio_1 = PrecioCrom(aux1)
            Precio_2 = PrecioCrom(aux2)
            if Precio_1[0] <= presupuesto:  # Comprobar si el precio no excede el presupuesto
                hijos_totales.append(hijo_1)
                precio_hijos.append(Precio_1[0])
            if Precio_2[0] <= presupuesto:  # Comprobar si el precio no excede el presupuesto
                hijos_totales.append(hijo_2)
                precio_hijos.append(Precio_2[0])
        return hijos_totales

    Poblacion = []

    # Inicializar población inicial
    for _ in range(N_Poblacion):
        Poblacion.append(RandomCrom())

    for Gen in range(GenMax):
        Cromosomas_Padre = []
        for posicion, valor in enumerate(Poblacion):
            if len(Cromosomas_Padre) < N_padres:
                Cromosomas_Padre.append((valor, posicion))
            else:
                maximo_actual, max_posicion = min(Cromosomas_Padre)
                if valor < maximo_actual:
                    Cromosomas_Padre.remove((maximo_actual, max_posicion))
                    Cromosomas_Padre.append((valor, posicion))
        indices_Cromosomas_Padre = [posicion for _, posicion in Cromosomas_Padre]

        Hijos = CruceNCromosomas(Pob=Poblacion, i_padres=indices_Cromosomas_Padre)

        Poblacion_Nueva = []
        indices_Poblacion_Nueva = []

        Poblacion.extend(Hijos)

        for posicion, valor in enumerate(Poblacion):
            if len(Poblacion_Nueva) < N_Poblacion:
                Poblacion_Nueva.append(valor)
                indices_Poblacion_Nueva.append(posicion)
            else:
                maximo_actual = min(Poblacion_Nueva)
                max_posicion = indices_Poblacion_Nueva[Poblacion_Nueva.index(maximo_actual)]
                if valor < maximo_actual:
                    Poblacion_Nueva.remove(maximo_actual)
                    indices_Poblacion_Nueva.remove(max_posicion)
                    Poblacion_Nueva.append(valor)
                    indices_Poblacion_Nueva.append(posicion)

        Poblacion = Poblacion_Nueva

    Fitness_Total = FitMaker(Poblacion)

    mejor_pc_posiciones = Poblacion[Fitness_Total.index(min(Fitness_Total))]
    mejor_pc = [
        {'Componente': 'CPU', 'Nombre': CPU.loc[mejor_pc_posiciones[0], 'Nombre'],
         'Precio': CPU.loc[mejor_pc_posiciones[0], 'Precio']},
        {'Componente': 'GPU', 'Nombre': GPU.loc[mejor_pc_posiciones[1], 'Chip'],
         'Precio': GPU.loc[mejor_pc_posiciones[1], 'Precio']},
        {'Componente': 'SSD', 'Nombre': SSD.loc[mejor_pc_posiciones[2], 'Nombre'],
         'Capacidad(GB)': SSD.loc[mejor_pc_posiciones[2], 'Capacidad (GB)'],
         'Precio': SSD.loc[mejor_pc_posiciones[2], 'Precio']},
        {'Componente': 'RAM', 'Nombre': RAM.loc[mejor_pc_posiciones[3], 'Nombre'],
         'Velocidad': RAM.loc[mejor_pc_posiciones[3], 'Velocidad'],
         'Precio': RAM.loc[mejor_pc_posiciones[3], 'Precio']}
     ]
    fitness = min(Fitness_Total)

    # Información adicional
    F_Alim = 195 if GPU['Chip'][mejor_pc_posiciones[1]] == 'GeForce RTX 4090' or GPU['Chip'][mejor_pc_posiciones[1]] == 'Radeon RX 7900 XTX' else 12
    cpu_nombre = CPU['Nombre'][mejor_pc_posiciones[0]]
    Cpu_zocalo = 'AM5' if 'AMD' in cpu_nombre and ' 7' in cpu_nombre else 'AM4' if 'AMD' in cpu_nombre and ' 7' not in cpu_nombre else 'LGA1200' if '-10' in cpu_nombre or '-11' in cpu_nombre else 'LGA1700' if '-12' in cpu_nombre or '-13' in cpu_nombre or '-14' in cpu_nombre else None

    Mb_ex = 5 if Cpu_zocalo == 'AM5' else 7 if Cpu_zocalo == 'AM4' else 238 if Cpu_zocalo == 'LGA1200' else 19 if Cpu_zocalo == 'LGA1700' else None

    return mejor_pc, fitness, F_Alim, Cpu_zocalo, Mb_ex

def mostrar_configurador():
    CPU = pd.read_csv('cpu_ferran_clean.csv')
    GPU = pd.read_csv('gpu_ferran_clean.csv')
    SSD = pd.read_csv('SSD_limpio.csv')
    RAM = pd.read_csv('RAM_clean.csv')
    PS = pd.read_csv('power-supply_clean.csv')
    CASE = pd.read_csv('case_clean.csv')
    MB = pd.read_csv('motherboard_clean.csv')
    st.title("Configura tu Computadora")
    presupuesto_maximo = st.number_input("¿Qué presupuesto tienes?", min_value=0, max_value=10000, value=1500, step=100)
    

    st.selectbox('Seleccione el tipo de uso:', ['Ordenador de oficina','Ordenador de alto rendimiento'])

    if st.button("Haga click aquí para configurar su PC"):
        mejor_pc, fitness, *_ = algoritmo_genetico(presupuesto_maximo, CPU, GPU, SSD, RAM)
        
        if mejor_pc is not None:
            st.write("Procesador:", mejor_pc[0]['Nombre'], mejor_pc[0]['Precio'], "€")
            st.write("Tarjeta Gráfica:", mejor_pc[1]['Nombre'], mejor_pc[1]['Precio'], "€")
            st.write("Memoria SSD:", mejor_pc[2]['Nombre'], mejor_pc[2]['Precio'], "€")
            st.write("Memoria RAM:", mejor_pc[3]['Nombre'], mejor_pc[3]['Precio'], "€")
            st.write("--------------------------------------------------")
            st.write("Fuente de alimentación:", PS.loc[0, 'Nombre'], PS.loc[0, 'Precio'], "€")
            st.write("Caja:", CASE.loc[0, 'Nombre'], CASE.loc[0, 'Precio'], "€")
            st.write("Placa base:", MB.loc[0, 'Nombre'], MB.loc[0, 'Precio'], "€")
            precio_total_componentes = sum([mejor_pc[i]['Precio'] for i in range(4)])
            precio_total_adicional = PS.loc[0, 'Precio'] + CASE.loc[0, 'Precio'] + MB.loc[0, 'Precio']
            precio_total = precio_total_componentes + precio_total_adicional
            st.write("--------------------------------------------------")
            st.write("Precio:", precio_total, "€ de", presupuesto_maximo, "€ disponibles")
        else:
            st.write("No se encontró una configuración dentro del presupuesto proporcionado.")
            
def main():
    
    
    st.set_page_config(page_title="Explorador de Componentes de Computadora", page_icon=":computer:")

    st.sidebar.title('Menú')

    # Al cargar la aplicación, mostrar la pantalla de inicio por defecto y que, cuando elijas otra, elimine la pantalla de inicio
    if 'pagina_actual' not in st.session_state:
        st.session_state.pagina_actual = 'Inicio'

    if st.sidebar.button('Inicio'):
        st.session_state.pagina_actual = 'Inicio'
    
    if st.sidebar.button('Historia'):
        st.session_state.pagina_actual = 'Historia'
    
    if st.sidebar.button('Componentes'):
        st.session_state.pagina_actual = 'Componentes'

    if st.sidebar.button('Análisis de Componentes'):
        st.session_state.pagina_actual = 'Análisis de Componentes'
    
    if st.sidebar.button("Configurador de PC"):
        st.session_state.pagina_actual = "Configurador de PC"

    # Mostrar contenido según la página actual seleccionada sin la de inicio
    if st.session_state.pagina_actual == 'Inicio':
        mostrar_pantalla_de_inicio()
    elif st.session_state.pagina_actual == 'Componentes':
        mostrar_componentes()
    elif st.session_state.pagina_actual == 'Historia':
        mostrar_historia()
    elif st.session_state.pagina_actual == 'Análisis de Componentes':
        mostrar_ml()
    elif st.session_state.pagina_actual == "Configurador de PC":
        mostrar_configurador()


    # Aplicar estilos CSS para la página
    # Estilo para la página de incio, el menú e intento de imágenes. Preguntar Dani
    st.markdown(
        """
        <style>
        .stButton>button {
            color: white !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <style>
        .stApp {
            background-color: #201E1E; /* negro */
            color: #D8D8D8; /* blanco */
            font-size: 18px;
            font-family: 'Roboto', sans-serif;
            text-align: left;
        }
        h1 {
            color: #F2B134; /* dorado */
        }
        h2, h3, h4, h5, h6 {
            color: #CCCCCC; /* gris claro */
        }
        .st-cc span {
            color: #FFFFFF !important; /* blanco */
        }
        .sidebar .sidebar-content .stButton>button {
            color: #FFFFFF;
            background-color: #5C5858; /* gris oscuro */
        }
        .sidebar .sidebar-content {
            background-color: #5C5858; /* gris oscuro */
            color: #D8D8D8; /* blanco */
            background-image: url("menulateral.jpg"); /* Imagen de fondo */
            background-size: cover;
        }
        .sidebar .sidebar-content .sidebar-section .sidebar-section-list .stCheckbox label, .sidebar .sidebar-content .sidebar-section .sidebar-section-title, .sidebar .sidebar-content .sidebar-section .sidebar-section-list button {
            color: white;
        }
        .stButton>button {
            border: 2px solid;
            border-color: #FFD700; /* Dorado */
            color: #FFD700 !important; /* Dorado */
            background-color: transparent;
            padding: 10px 15px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
        }
        .stButton>button:hover {
            border-color: #FFD700; /* Dorado */
            background-color: #FFD700; /* Dorado */
            color: white !important;
        }
        /* Estilo para las tablas */
        .stDataFrame {
            color: white; /* Cambia el color del texto a blanco */
            font-weight: bold; /* Texto en negrita */
        }
        .dataframe { /* Estilo para el DataFrame en sí */
            background-color: transparent !important; /* Fondo transparente */
            border: none; /* Sin bordes */
        }
        .dataframe th { /* Estilo para los encabezados de las tablas */
            background-color: transparent !important; /* Fondo de los encabezados transparente */
            color: white; /* Color de los encabezados en blanco */
            font-weight: bold; /* Encabezados en negrita */
        }
        .dataframe td { /* Estilo para las celdas de las tablas */
            background-color: transparent !important; /* Fondo de las celdas transparente */
            color: white; /* Color del texto en las celdas en blanco */
        }
        div.stSelectbox > label {color: white;} /* Estilo añadido para selectbox */
        </style>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()


# In[ ]:


col1, col2 = st.columns([3, 1])


# In[ ]:


col1, col2, col3 = st.columns([1, 3, 1])


# In[3]:


#mejor_pc_posiciones[1]


# In[ ]:




