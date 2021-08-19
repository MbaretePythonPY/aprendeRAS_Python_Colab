#!/usr/bin/env python
# -*- coding: latin-1 -*-
import os
import sys
import csv
import time
import datetime
import math
from tkinter import*
from PIL import Image, ImageTk
from reportlab.lib.units import mm, inch
from reportlab.pdfgen import canvas as pdf
from mbarete import geometria
global d,canvas_width,canvas_height
d={
    'img':os.getcwd()+'\\'+"img"+'\\',
    'audio':os.getcwd()+'\\'+"audio"+'\\'
    }
canvas_width = 1100
canvas_height =1000
print(datetime.datetime.now())
def timeConOsPath():
    import os, sys,time
    #time ,pruebas con la libreria time:
    print('time.gmtime(0):',time.gmtime(0)) #
    print('time.ctime(0):',time.ctime(0))
    print('sys.argv[0]:',sys.argv[0])
    print('os.path.getatime(sys.argv[0]):',os.path.getatime(sys.argv[0]))
    print('time.ctime(os.path.getmtime(sys.argv[0])):',time.ctime(os.path.getmtime(sys.argv[0])),'Tiempo de la ultima modificación de path')
    print('time.ctime(os.path.getctime(sys.argv[0])):',time.ctime(os.path.getctime(sys.argv[0])),'En algunos sistemas (como Unix) es la hora del ultimo cambio de metadatos y, en otros (como Windows), es el tiempo de creacion de path')
    print('time.ctime(os.path.getatime(sys.argv[0])):',time.ctime(os.path.getatime(sys.argv[0])),'Hora del ultimo acceso de path')
    print(r'strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime(os.path.getatime(sys.argv[0]))):',time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime(os.path.getatime(sys.argv[0]))))
def VariablesDeEntorno():
    import os
    variables_de_entorno={env:os.environ[env] for env in os.environ}
    for variable in variables_de_entorno: 
        print("%s: %s" % (variable, variables_de_entorno[variable]))
def powerPath(pwd=os.getcwd()):
    import os
    """
        El módulo   os.path   siempre es el módulo adecuado para el sistema operativo en el cual Python está operando, 
        y por lo tanto es utilizable para rutas locales. Sin embargo, también puedes importar y utilizar los módulos 
        individuales si deseas manipular una ruta que siempre está en uno de los diferentes formatos. Todos tienen la misma interfaz:
            posixpath para rutas con estilo UNIX
            ntpath para rutas Windows
    """
    supportUnicode=os.path.supports_unicode_filenames #True si se pueden utilizar cadenas Unicode arbitrarias como nombres de archivo (dentro de las limitaciones impuestas por el sistema de archivos).
    print(supportUnicode)
    pwdA=pwd #obtengo la ruta path de mi ubicacion actual donde se esta ejecutando este Script 
    os.chdir(pwdA)
    os.chdir('..')
    pwdB=os.getcwd() #obtengo la ruta path de la carpeta de nivel superior a la carpeta actual donde se esta ejecutando este Script 
    os.chdir(pwdA)
    fullPathA=[pwdA+'\\'+d for d in os.listdir(pwdA)] # obtenemos la lista de archivos en la direccion pwd y luego le agregamos la ruta completa al archivo
    fullPathB=[pwdB+'\\'+d for d in os.listdir(pwdB)] # obtenemos la lista de archivos en la direccion pwd y luego le agregamos la ruta completa al archivo
    print('os.path.commonpath(fullPathA+fullPathB)',os.path.commonpath(fullPathA+fullPathB)) #Retorna la sub-ruta común más larga de cada nombre de ruta en la secuencia paths. 
    print('os.path.commonprefix(fullPathA+fullPathB)',os.path.commonprefix(fullPathA+fullPathB)) #Retorna el prefijo de ruta más largo (tomado carácter por carácter) que es un prefijo de todas las rutas en list. 
    pathB=''
    power={}
    for path in fullPathA:   #recorremos todos los archivos para obtener los datos de cada archivo
        if not pathB:
            pathB=path
        # obtenemos metadatos y datos del path
        power['basename'] = os.path.basename(path)   #Retorna un nombre base de nombre de ruta path.
        power['abspath']= os.path.abspath(path)  #Retorna una versión normalizada y absoluta del nombre de ruta path.
        power['dirname']= os.path.dirname(path)  #Retorna el nombre del directorio de la ruta path.
        power['exists'] = os.path.exists(path)   #Retorna True si path se refiere a una ruta existente o un descriptor de archivo abierto. Retorna False para enlaces simbólicos rotos. En algunas plataformas, esta función puede retornar False si no se concede permiso para ejecutar os.stat() en el archivo solicitado, incluso la ruta path existe físicamente.
        power['lexists'] = os.path.lexists(path) #Retorna True si path se refiere a un camino existente. Retorna True para los enlaces simbólicos rotos
        power['expanduser'] = os.path.expanduser(path) #En Unix y Windows, retorna el argumento con un componente inicial de ~ o ~user reemplazado por el directorio home de user
        power['expandvars']=os.path.expandvars(path)#Retorna el argumento con variables de entorno expandidas.
        power['ultimoAcceso'] = os.path.getatime(path)#Retorna la hora del ultimo acceso de path. El valor de retorno es un numero de punto flotante que da el numero de segundos desde la epoca 
        power['ultimaModificacion'] = os.path.getmtime(path)#Retorna el tiempo de la ultima modificación de path. El valor de retorno es un numero de punto flotante que da el numero de segundos desde la epoca
        power['creacionOModificacion']=os.path.getctime(path)#Retorna el ctime del sistema que, en algunos sistemas (como Unix) es la hora del ultimo cambio de metadatos y, en otros (como Windows), es el tiempo de creacion de path. El valor retornado es un numero que da el numero de segundos desde la epoca
        power['getsize'] =os.path.getsize(path)#Retorna el tamaño en bytes de path, Lanza una excepcion OSError si el archivo no existe o es inaccesible
        power['isabs'] = os.path.isabs(path) #Retorna True si path es un nombre de ruta de acceso absoluto. En Unix, eso significa que comienza con una barra diagonal, en Windows que comienza con una barra diagonal (invertida) despues de cortar una letra de unidad potencial.
        power['isfile'] =os.path.isfile(path)#Retorna True si path es un archivo existing. Esto sigue los enlaces simbólicos, por lo que tanto islink() como isfile() pueden ser verdaderos para la misma ruta.
        power['isdir'] = os.path.isdir(path)#Retorna True si path es un directorio existing. Esto sigue los enlaces simbólicos, por lo que tanto islink() como isdir() pueden ser verdaderos para la misma ruta.
        power['islink'] =os.path.islink(path)#Retorna True si path hace referencia a una entrada de directorio existing que es un enlace simbólico. Siempre False si el entorno de ejecución de Python no admite vínculos simbólicos.
        power['ismount']=os.path.ismount(path)#Retorna True si el nombre de ruta path es un mount point: un punto en un sistema de archivos donde se ha montado un sistema de archivos diferente. En POSIX, la función comprueba si el elemento primario de path, path/.., se encuentra en un dispositivo diferente de path, o si path/.. y path apuntan al mismo i-node en el mismo dispositivo — esto debería detectar puntos de montaje para todas las variantes Unix y POSIX. No es capaz de detectar de forma fiable los montajes de enlace en el mismo sistema de archivos. En Windows, una raíz de letra de unidad y un recurso compartido UNC siempre son puntos de montaje, y para cualquier otra ruta de acceso GetVolumePathName se llama para ver si es diferente de la ruta de acceso de entrada.
        power['join']=os.path.join(path, sys.argv[0])
        #Unir uno o más componentes de ruta de acceso de forma inteligente. El valor retornado es la concatenación de path y cualquier miembro de *paths 
        #con exactamente un separador de directorios (os.sep) después de cada parte no vacía, excepto la última, lo que significa que el resultado solo 
        #terminará en un separador si la última parte está vacía. Si un componente es una ruta absoluta, todos los componentes anteriores se desechan y 
        #la unión continúa desde el componente de ruta absoluta.
        #En Windows, la letra de la unidad no se restablece cuando se encuentra un componente de ruta absoluta (por ejemplo, r'\foo'). 
        #Si un componente contiene una letra de unidad, todos los componentes anteriores se desechan y la letra de unidad se restablece. 
        #Ten en cuenta que, dado que hay un directorio actual para cada unidad, `` os.path.join («c:», «foo») `` representa una ruta 
        #relativa al directorio actual en la unidad C: (c:foo),, no c:\foo.
        power['normcase']=os.path.normcase(path)#Normaliza las mayúsculas y minúsculas de un nombre de ruta. En Windows convierte todos los caracteres en el nombre de ruta a minúsculas y también convierte las barras inclinadas hacia atrás en barras inclinadas hacia atrás. En otros sistemas operativos, retorna la ruta sin cambios.
        power['normpath']=os.path.normpath(path)#Normaliza un nombre de ruta colapsando separadores redundantes y referencias de nivel superior para que A//B, A/B/, A/./B y A/foo/../B se transformen en``A/B``. Esta modificación de cadena puede que modifique el significado de la ruta que contenga enlaces simbólicos. En Windows, convierte las barras inclinadas hacia adelante en barras hacia atrás. Para normalizar mayúsculas y minúsculas, utiliza normcase().
        power['realpath']=os.path.realpath(path)#Retorna la ruta canónica del nombre de archivo especificado, eliminando cualquier enlace simbólico encontrado en la ruta (si es que tienen soporte por el sistema operativo).
        power['relpath']=os.path.relpath(path, start=os.curdir)#Retorna un nombre de ruta relativo a path desde el directorio actual o de un directorio start opcional. Este es un cálculo de ruta: No se accede al sistema de archivos para confirmar la existencia o la naturaleza de path o start.
        #start toma de forma predeterminada el valor de os.curdir.
        power['samefile']=os.path.samefile(pathB, path)#Retorna True si ambos argumentos de nombre de ruta refieren al mismo archivo o directorio. Esto se determina por el número de dispositivo y el número de i-node y lanza una excepción si una llamada de os.stat() en alguno de los nombres de ruta falla.
        #sameOpenFile=os.path.sameopenfile(os.stat(pathB), os.stat(path))#Retorna True si los descriptores de archivo fp1 y fp2 se refieren al mismo archivo.        
        power['samestat']=os.path.samestat(os.stat(pathB), os.stat(path))#Retorna True si las tuplas de stat (stat1 y stat2) refieren al mismo archivo. Estas estructuras pueden haber sido retornadas por os.fstat(), os.lstat(), o os.stat(). Esta función implementa la comparación subyacente utilizada por: samefile() y sameopenfile().
        power['split']=os.path.split(path)#Divide el nombre de la ruta path * en un par, `` (head, tail) `` donde *tail es el último componente del nombre de la ruta y head es todo lo que conduce a eso. La parte head nunca contendrá una barra; si head termina en una barra, tail estará vacía. Si no hay barra inclinada en path, head estará vacío. Si path está vacía, tanto head como tail estarán vacíos. Las barras diagonales finales se eliminan de head a menos que sea la raíz (solo una o más barras). En todos los casos, join(head, tail) retorna una ruta a la misma ubicación que path (pero las cadenas pueden diferir). 
        power['splitdrive']=os.path.splitdrive(path)
        #Divide el nombre de ruta path en un par (drive, tail) donde drive es un punto de montaje o una cadena vacía. En sistemas que no utilizan especificaciones de unidad, drive siempre será una cadena vacía. En todos los casos, drive + tail será lo mismo que path.
        #En Windows, divide un nombre de ruta en unidad / punto compartido UNC y ruta relativa.
        #Si la ruta contiene una letra de unidad, la unidad contendrá todo hasta los dos puntos inclusive. p.ej. splitdrive("c:/dir") retorna ("c:", "/dir")
        #Si la ruta contiene una ruta UNC, drive contendrá el nombre de host y el recurso compartido, hasta el cuarto separador, pero sin incluirlo. p.ej. splitdrive("//host/computer/dir") retorna ("//host/computer", "/dir")
        power['splitext']=os.path.splitext(path)#Divide el nombre de ruta path en un par (root, ext) de tal forma que root + ext == path, y ext queda vacío o inicia con un punto y contiene a lo mucho un punto. Se ignoran los puntos iniciales del nombre base; splitext('.cshrc') retorna ('.cshrc', '').
        print('\n')
        for atributo in power:
            print('.'+atributo+': ',power[atributo])
def powerPDF():
    import os,datetime
    from reportlab.lib.units import mm, inch
    from reportlab.pdfgen import canvas as pdf
    #inicia codigo de la prueba
    #Copyright ReportLab Europe Ltd. 2000-2017
    #see license.txt for license details
    #history https://hg.reportlab.com/hg-public/reportlab/log/tip/src/reportlab/lib/pagesizes.py
    #__version__='3.4.18'
    #ISO 216 standard paer sizes; see eg https://en.wikipedia.org/wiki/ISO_216
    hoja={
        'A0':(841*mm,1189*mm),
        'A1':(594*mm,841*mm),
        'A2':(420*mm,594*mm),
        'A3':(297*mm,420*mm),
        'A4':(210*mm,297*mm),
        'A5':(148*mm,210*mm),
        'A6':(105*mm,148*mm),
        'A7':(74*mm,105*mm),
        'A8':(52*mm,74*mm),
        'A9':(37*mm,52*mm),
        'A10':(26*mm,37*mm),
        'B0':(1000*mm,1414*mm),
        'B1':(707*mm,1000*mm),
        'B2':(500*mm,707*mm),
        'B3':(353*mm,500*mm),
        'B4':(250*mm,353*mm),
        'B5':(176*mm,250*mm),
        'B6':(125*mm,176*mm),
        'B7':(88*mm,125*mm),
        'B8':(62*mm,88*mm),
        'B9':(44*mm,62*mm),
        'B10':(31*mm,44*mm),
        'C0':(917*mm,1297*mm),
        'C1':(648*mm,917*mm),
        'C2':(458*mm,648*mm),
        'C3':(324*mm,458*mm),
        'C4':(229*mm,324*mm),
        'C5':(162*mm,229*mm),
        'C6':(114*mm,162*mm),
        'C7':(81*mm,114*mm),
        'C8':(57*mm,81*mm),
        'C9':(40*mm,57*mm),
        'C10':(28*mm,40*mm)
    }
    print([hj for hj in hoja])
    txt={}
    txt.setdefault('Nombre',input('Ingrese su nombre: '))
    txt.setdefault('Direccion',input('Ingrese su direccon de domicilio : '))
    txt.setdefault('Telefono',input('Ingrese su numero de telefono: '))
    txt.setdefault('Nacimiento',input('Ingrese su Fecha Nacimiento: '))
    txt.setdefault('Sangre',input('Ingrese su tipo de sangre: '))
    label=[key for key in txt]
    Lsize=700
    print("Los valores ingresados son")
    for key in txt:
        print(key,':',txt[key])
    canvas = pdf.Canvas(txt['Nombre']+".pdf", pagesize=hoja['A4'])
    canvas.setLineWidth(.3)
    canvas.setFont('Helvetica', 12)
    canvas.drawString(30,750,'CARTA DE PRUEBA')
    canvas.drawString(30,735,"setFont('Helvetica', 12)")
    canvas.drawString(500,750,str(datetime.date.today()))
    canvas.line(480,747,580,747)
    canvas.drawString(275,725,'ESTIMADO:')
    canvas.drawString(500-(len(txt['Nombre'])*3),725,txt['Nombre'])
    canvas.line(378,723,580,723)
    for x in range(0,len(txt),1):
        canvas.drawString(30,Lsize-(x*15),str(label[x])+':')
        canvas.line(120,Lsize-(x*15),580,Lsize-(x*15))
        canvas.drawString(120,Lsize-(x*15),txt[label[x]])
    canvas.save()
    if os.path.isfile(os.getcwd()+'\\'+txt['Nombre']+".pdf"):
        print("Abriendo el archivo "+'"'+txt['Nombre']+'.pdf"')
        os.system('"'+txt['Nombre']+'.pdf"')
def showAlbum():
    from tkinter import Tk, Scrollbar,Canvas,Frame,IntVar,Entry,Button
    from PIL import Image, ImageTk
    import os
    global d,canvas_width,canvas_height
    def dibujar(alto,ancho):
        my_canvas_height=int(int(len(lista)/int(range(0,canvas_width,ancho)[-1]/ancho))*alto+alto)
        miFrameinicio.configure(bg='#090929',width = canvas_width, height=my_canvas_height)
        canvas.configure(bg='#090929',width = canvas_width, height=my_canvas_height)
        canvas.create_polygon((0,0,canvas_width,0,canvas_width,my_canvas_height,0,my_canvas_height),fill='#090929')
        #miniatura={}
        contador=0
        for y in range(30,my_canvas_height,alto):
            for x in range(0,canvas_width-ancho,ancho):
                if contador==len(lista):
                    break
                img=Image.open(pwd+str(lista[contador]))
                redimencionar=(img.size[0]*(ancho/img.size[0]),img.size[1]*(ancho/img.size[0])) if img.size[0]>img.size[1] else (img.size[0]*(alto/img.size[1]),img.size[1]*(alto/img.size[1]))
                redimencionar=(int(redimencionar[0]),int(redimencionar[1]))
                print(redimencionar,str(lista[contador]))
                if '.jpg' in str(lista[contador])[-5:]:
                    img.save(pwd+str(lista[contador]).replace('.jpg','.png'),'png')
                    img=Image.open(pwd+str(lista[contador]).replace('.jpg','.png'))
                miniatura[contador]={'img':img.resize(redimencionar)}
                miniatura[contador]['PhotoImage']=ImageTk.PhotoImage(miniatura[contador]['img'])
                miniatura[contador]['widget']=Label(miFrameinicio,image=miniatura[contador]['PhotoImage'])
                #miniatura[contador]['widget'].image=miniatura[contador]['PhotoImage']
                #miniatura[contador]['widget'].place(x=x,y=y)
                canvas.create_image(x+int((ancho-redimencionar[0])/2),y+int((alto-redimencionar[1])/2),image=miniatura[contador]['PhotoImage'],anchor='nw')
                if ".jpg" in str(lista[contador])[-5:]:
                    os.remove(pwd+str(lista[contador]))
                contador=contador+1
        raiz.update()
        c.config(scrollregion=c.bbox("all"))
        raiz.geometry(str(canvas_width)+"x"+str(canvas_height)+"+10+10")
        
    pwd=d['img']
    alto=200
    ancho=200
    print('Ubicacion:',pwd)
    #inicia codigo de la prueba
    lista=[img for img in os.listdir(pwd) if (((".jpg" in img[-5:]) and (not ".png" in img)) or ((".png" in img[-5:]) and (not ".jpg" in img)) or ((".jpeg" in img[-5:]) and (not ".png" in img)) )]
    miniatura={}
    contador=0
    print(canvas_width//ancho)
    my_canvas_height=int(int(len(lista)/int(range(0,canvas_width,ancho)[-1]/ancho))*alto+alto)
    raiz=Tk()
    scrollbar=Scrollbar(raiz)
    c = Canvas(raiz, yscrollcommand=scrollbar.set)
    scrollbar.config(command=c.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    miFrameinicio=Frame(c)
    miFrameinicio.configure(width = canvas_width, height=my_canvas_height)
    canvas = Canvas(miFrameinicio, width=canvas_width, height=my_canvas_height)
    canvas.place(x=0, y=0)
    c.pack(side="left" , fill="both", expand=True)
    c.create_window(0,0,window=miFrameinicio, anchor='nw')
    c.config(scrollregion=c.bbox("all"))
    img_ancho=IntVar(value=ancho)
    img_alto=IntVar(value=alto)
    entry_ancho=Entry(miFrameinicio,textvariable=img_ancho,width=10)
    entry_ancho.place(x=10, y=10)
    entry_alto=Entry(miFrameinicio,textvariable=img_alto,width=10)
    entry_alto.place(x=110, y=10)
    btn_aplicar=Button(miFrameinicio,text='Aplicar',command=lambda: dibujar(img_alto.get(),img_ancho.get()),width=10)
    btn_aplicar.place(x=210, y=10)
    dibujar(img_alto.get(),img_ancho.get())
    #raiz.update()
    #c.config(scrollregion=c.bbox("all"))
    #raiz.geometry(str(canvas_width)+"x"+str(canvas_height)+"+10+10")
    print("Mostrando las imagenes con tkinter y PIL...")
    raiz.focus_force()
    raiz.mainloop()    
def ButtonConImagen():
    from tkinter import Tk,PhotoImage,Button
    from PIL import Image
    import os
    global canvas_width,canvas_height,d
    pwd=d['img']
    file=[str(img) for img in os.listdir(d['img']) if (('.png' in img[-4:]) or ('.jpg' in img[-4:]))][0]
    raiz = Tk() 
    raiz.geometry(str(canvas_width)+"x"+str(canvas_height))
    try:
        #guardo la imagen con formato PNG, usando el modulo Image, de esta forma tkinter siempre podra cargar la nueva imagen correctamente
        #la nueva imagen generada con Image.save("nuevoArchivoMiFoto.PNG") normalmente siempre se carga bien los programas con Tkinter
        Image.open(pwd+file).save(pwd+file.replace('.jpg','.png'))

    except IOError:
        print("No se puede convertir la imagen")
    #el archivo de origen puede ser JPG o PNG, lo importante es guardas la imagen en PNG
    #redimensionamos la imagen con Image.resize((200,200)), los parametros alto y ancho en una tupla ejem:(alto,ancho), alto y ancho en pixeles
    #luego, al cargar la imagen y mostrala en pantalla con Tkinter ocupara las dimensiones que le dimos con 'Image.resize'. GUardo la IMagen en un
    #archivo nuevo en formato PNG generado con Image.save("myNuevaImagen.png","png")
    imgOriginal = Image.open(pwd+file.replace('.jpg','.png')).resize((200,200)).save(pwd+'myNuevaImagen.png','png')
    #cargamos el nuevo archivo "myNuevaImagen.png" creado en la linea anterior
    imgNueva =  PhotoImage(file=pwd+"myNuevaImagen.png")
    #creamos un widget Button y le pasamos la variable que contiene la nueva imagen con image=imgNueva 
    #el parametro text="Botonio", quedara debajo de la imagen y alineada con la imagen, el boton ocupara el lugar de la imagen mas el Texto
    #si no le damos texto ,ejemplo: Button(raiz, image=imgNueva, bd=0, etc etc ...) el boton tomara las medidas de la imagen
    boton = Button(raiz, image=imgNueva,text=pwd+"myNuevaImagen.png", bd=0, compound="top",command=lambda:print("Click XD"))
    boton.place(x=0, y=50)
    raiz.mainloop()
def playlist(pwd='.'):
    import os
    #inicia codigo de la prueba
    tiempo=45
    ignorarArchivo=['Crear Lista.py','0000_archivos.txt']
    formatos=['.mp3','.mp4','.wav','.avi','.webm','.ogg','.m4a','.mkv','.rmvb','.vob','.wmv']
    playListFile=pwd+'\\'+"000_playList.m3u"
    if playListFile in os.listdir(pwd):
        os.remove(playListFile)
    palabra=input("ingrese una palabra para filtrar los archivos : ")
    midir=[archivo for archivo in os.listdir(pwd) if ((archivo not in ignorarArchivo) and (os.path.isfile(pwd+'\\'+archivo)))]
    midir=[archivo for archivo in midir if [archivo for exten in formatos if (exten in archivo[-6:].lower()) ] ]
    midir=[archivo for archivo in midir if (palabra.lower() in archivo.lower())]
    filtro=[
        ('ú','u'),
        ('á','a'),
        ('é','e'),
        ('í','i'),
        ('ó','o'),
        ('ú','u'),
        ('_',''),
        ('-',''),
        ('¡',''),
        ('!',''),
        ('  ',' ')
        ]
    for contador in range(0,len(midir),1):
            archivo=str(midir[contador]).lower()
            for change in filtro:
                archivo=archivo.replace(change[0],change[1])
            os.rename(pwd+'\\'+midir[contador], pwd+'\\'+archivo)
            midir[contador]=archivo
    playList=open(playListFile,"a")
    playList.write('#EXTM3U\n')
    for contador in range(0,len(midir),1):
        playList.write('#EXTINF:'+str(tiempo)+','+str(midir[contador])+'\n')
        playList.write(pwd+'\\'+str(midir[contador])+'\n')
    playList.close()
    if midir:
        os.system(playListFile)
def decoradores():
    import time
    """
        practica con decoradores
        la funcion 'decorador' se ejecutara automaticamente cada ves que ejecutemos las funciones decoradas con esta funcion
        la funcion 'decorador' recive como parametro la funcion 'funcion_parametro' que fue decorada, junto con sus argumentos de posicion *vars y los argumentos con palabras claves **vars_claves
        la funcion 'decorador' retornara otra funcion 'funcionInterior', esta funcion interna ejecuta su propio codigo, y dentro de esta funcion intarna ejecutamos la funcion_parametro 
    """
    def decorador(funcion_parametro):
        def funcionInterior(*args,**kwargs):
            print("Funcion:",funcion_parametro.__name__)
            print("Entradas:",*args,**kwargs)
            ret=funcion_parametro(*args,**kwargs)
            print("Salidas:",ret,'\n')
            return ret
        return funcionInterior
    """ 
        la funcion 'decoradorPlus' recive la funcion decoradoa con sos respectivos 
        argumentos, aparte tambien recive un parametro asignada a la clave arg como 
        cualquier funcion normal. De acuerdo al valor de 'arg' decorara la funcion decorada con una funcion interna de 'decoradorPlus'     
    """
    def decoradorPlus(arg=""):
        def decoradortiempo(funcion):
            def funcionInterior(*args,**kwargs):
                inicio=time.time()
                print("Funcion:",funcion.__name__)
                ret=funcion(*args,**kwargs)
                print("Tiempo de Ejecucion:",time.time()-inicio)
                return ret
            return funcionInterior
        def decoradorSimple(funcion):
            def funcionInterior(*args,**kwargs):
                print("Funcion:",funcion.__name__)
                print("Entradas:",*args,**kwargs)
                ret=funcion(*args,**kwargs)
                print("Salidas:",ret)
                return ret
            return funcionInterior

        if arg=="tiempo":
            return decoradortiempo
        else:
            return decoradorSimple
    """
        la funcion 'testFuncion' recive como argumento posicional, una 
        funcion, el valor que debe retornar dicha funcion, seguido de 
        los argumentos que recive dicha funcion
    """
    def testFuncion(funcion,retorna,*test_args):
        test=True
        if retorna!=funcion(*test_args):
            test=False
        return test
    """
        decoramos la funcion 'resta', con la funcion 'decoradorPlus' sin pasarle la clave opcional 'arg'
    """
    @decoradorPlus()
    def resta(a,b):
        return (a-b)

    """
        decoramos la funcion 'suma', con la funcion 'decoradorPlus' y le pasamos la clave opcional 'arg' igual a "tiempo"
    """
    @decoradorPlus(arg='tiempo')
    def suma(a,b):
        return (a+b)

    print(testFuncion(resta,40,50,10))
    print(testFuncion(suma,40,50,10))
def aspas(x=10,y=10,escalar=1.0,dividir=120,baseRadio=375.0,altura=375.0,revolucion=360,rotorRadio=12.0,fondo=200.0):
    baseRadio=375.0*escalar
    altura=375.0*escalar
    rotorRadio=12.0*escalar
    fondo=200.0*escalar
    # retorna un poligono de una aspa de un aerogenerador de viento 
    print('escalar:',escalar,'x:',x,'y:',y,'dividir:',dividir,'baseRadio:', baseRadio,'altura:', altura,'revolucion:', revolucion,'rotorRadio:', rotorRadio,'fondo:', fondo)
    datos={'x':x,'y':y,'dividir':dividir,'baseRadio':baseRadio,'altura': altura,'revolucion': revolucion,'rotorRadio': rotorRadio,'fondo': fondo}
    geo=geometria()
    xR=[0.0]
    yR=[rotorRadio]
    zR=[-1*(fondo/baseRadio)*(baseRadio-rotorRadio)]
    xA=[0.0]
    yA=[baseRadio]
    zA=[0.0]
    tanA=baseRadio/altura
    for ang in range(1,revolucion,1):
        if (((altura-((altura/float(revolucion))*float(ang)))*tanA) >= rotorRadio):
            rad=math.radians(float(ang))
            zA.append((altura/float(revolucion))*float(ang))
            p=((altura-zA[-1])*tanA)
            yA.append(p*math.cos(rad))
            xA.append(p*math.sin(rad))
            zR.append((-1*(((fondo+zA[-1])/p)*(p-rotorRadio))+zA[-1]))
            yR.append((rotorRadio)*math.cos(rad))
            xR.append((rotorRadio)*math.sin(rad))
            fin=ang
    xOut=[0]
    yOut=[geo.dist([xR[0],yR[0],zR[0]],[xA[0],yA[0],zA[0]])]
    xIn =[0]
    yIn =[0]
    for n in range(1,fin+1,1):
        A=[xA[n-1],yA[n-1],zA[n-1]] #punto que ya esta en el plano
        B=[xR[n-1],yR[n-1],zR[n-1]] #punto origen que ya esta en plano
        C=[xA[n],yA[n],zA[n]]       #punto que se agregara al plano
        xO=geo.dist(geo.alt(C,A,B),C)
        yO=geo.dist(geo.alt(C,A,B),B)
        #print(math.degrees(angRad([0,1,0],resta([xIn[-1],yIn[-1],0],[xOut[-1],yOut[-1],0]))))
        rot= -1*math.fabs(geo.angRad([0,1,0],geo.resta([xIn[-1],yIn[-1],0],[xOut[-1],yOut[-1],0])))
        xRot, yRot=geo.rotar(rot,[xO,yO,0])
        xTras, yTras=geo.trasladar([xIn[-1],yIn[-1],0],[xRot,yRot,0])
        yOut.append(yTras)
        xOut.append(xTras)
        A=[xA[n],yA[n],zA[n]]
        B=[xR[n-1],yR[n-1],zR[n-1]]
        C=[xR[n],yR[n],zR[n]]
        xO= geo.dist(geo.alt(C,A,B),C)
        yO= geo.dist(geo.alt(C,A,B),B) if geo.dist(geo.alt(C,A,B),A)<geo.dist(A,B) else geo.dis(geo.alt(C,A,B),B)*(-1)
        rot= -1*math.fabs(geo.angRad([0,1,0],geo.resta([xIn[-1],yIn[-1],0],[xOut[-1],yOut[-1],0])))
        xRot, yRot=geo.rotar(rot,[xO,yO,0])
        xTras, yTras=geo.trasladar([xIn[-1],yIn[-1],0],[xRot,yRot,0])
        yIn.append(yTras)
        xIn.append(xTras)
    for n in range(0,len(xOut),dividir):
        datos[str(n)+'grados']=str(int(n))+' grados, alturaRelativa= '+str(int(fondo+zR[n]))+'mm, largo= '+str(geo.dist([xIn[n],yIn[n],0],[xOut[n],yOut[n],0]))+', angulo= '+str(math.degrees(geo.angRad([0,0,1],geo.resta([xR[n],yR[n],zR[n]],[xA[n],yA[n],zA[n]]))))
    datos[str(fin)+'grados']=str(int(fin))+' grados, alturaRelativa= '+str(int(fondo+zR[fin]))+'mm, largo= '+str(geo.dist([xIn[fin],yIn[fin],0],[xOut[fin],yOut[fin],0]))+', angulo= '+str(math.degrees(geo.angRad([0,0,1],geo.resta([xR[fin],yR[fin],zR[fin]],[xA[fin],yA[fin],zA[fin]]))))
    textos = [[xIn[n]+x, yIn[n]+y,geo.ang(geo.resta([xIn[n]+(x), yIn[n]+(y),0],[xOut[n]+x, yOut[n]+y,0]),[-1,0,0])-180,'__'+str(n)+' grados'] for n in range(0,len(xOut),dividir)]+[geo.medio([xOut[fin]+x, yOut[fin]+y,0], [xIn[fin]+(x), yIn[fin]+(y),0])[0:2]+[geo.ang(geo.resta([xIn[fin]+(x), yIn[fin]+(y),0],[xOut[fin]+x, yOut[fin]+y,0]),[-1,0,0])-180,'__'+str(fin)+' grados']]
    lineas = [[xOut[n]+(x), yOut[n]+(y), xIn[n]+(x), yIn[n]+(y)] for n in range(0,len(xOut),dividir)]+[[xOut[fin]+(x), yOut[fin]+(y), xIn[fin]+(x), yIn[fin]+(y)]]
    poligono = [[xOut[n]+(x),yOut[n]+(y)] for n in range(0,len(xOut),1)]+[[xIn[n]+(x),yIn[n]+(y)] for n in range(len(xIn)-1,0,-1)]+[[xIn[0]+(x),yIn[0]+(y)]]+[[xOut[0]+x,yOut[0]+y]]
    datos['giroReal'] = fin
    return poligono, lineas, datos,textos
def poligonoToPDF(debug=1,calibrar=1,miniatura=1,margenes=[],REALmm=[200.0,200.0],datos={},printTEXT=[[100,100,0,"hola"],[100,100,90,"hola"],[100,100,180,"hola"],[100,100,270,"hola"]],REALsize=[0.0,0.0],escalar=1.0,cuadricular=1,imprimirHojasEnblanco=0, poligonos=[[(10,10),(15,15),(15,20),(20,20),(10,20),(10,10)]], lineas=[(10,10,0,0),(15,15,0,0),(15,20,0,0),(20,20,0,0),(10,20,0,0),(10,10,0,0)], fin = 6):
    from reportlab.lib.colors import tan, black, green
    from reportlab.lib.units import mm
    from reportlab.pdfgen import canvas
    fontSize=10
    hoja={
        'A0':(841*mm,1189*mm),
        'A1':(594*mm,841*mm),
        'A2':(420*mm,594*mm),
        'A3':(297*mm,420*mm),
        'A4':(210*mm,297*mm),
        'A5':(148*mm,210*mm),
        'A6':(105*mm,148*mm),
        'A7':(74*mm,105*mm),
        'A8':(52*mm,74*mm),
        'A9':(37*mm,52*mm),
        'A10':(26*mm,37*mm),
        'B0':(1000*mm,1414*mm),
        'B1':(707*mm,1000*mm),
        'B2':(500*mm,707*mm),
        'B3':(353*mm,500*mm),
        'B4':(250*mm,353*mm),
        'B5':(176*mm,250*mm),
        'B6':(125*mm,176*mm),
        'B7':(88*mm,125*mm),
        'B8':(62*mm,88*mm),
        'B9':(44*mm,62*mm),
        'B10':(31*mm,44*mm),
        'C0':(917*mm,1297*mm),
        'C1':(648*mm,917*mm),
        'C2':(458*mm,648*mm),
        'C3':(324*mm,458*mm),
        'C4':(229*mm,324*mm),
        'C5':(162*mm,229*mm),
        'C6':(114*mm,162*mm),
        'C7':(81*mm,114*mm),
        'C8':(57*mm,81*mm),
        'C9':(40*mm,57*mm),
        'C10':(28*mm,40*mm),
        'oficio':(216*mm,330*mm)
    }
    Xmm=200.0/REALmm[0]
    Ymm=200.0/REALmm[1]
    page=hoja['A4']
    escala=escalar
    escalaX,escalaY=(REALsize[0]/(page[0]/mm)) if REALsize[0]>0.0 else 1.0,(REALsize[1]/(page[1]/mm)) if REALsize[1]>0.0 else 1.0
    menorX,menorY,mayorX,mayorY=0,0,0,0
    poligono=poligonos
    lines=lineas
    textos=printTEXT

    for polig in range(0,len(poligono),1): 
        for p in range(0,len(poligono[polig]),1):
            poligono[polig][p]=[poligono[polig][p][0]*mm*Xmm , poligono[polig][p][1]*mm*Ymm]
        for p in poligono[polig]:
            if p[0]<menorX:
                menorX=p[0]
            if p[0]>mayorX:
                mayorX=p[0]
            if p[1]<menorY:
                menorY=p[1]
            if p[1]>mayorY:
                mayorY=p[1]    
    for l in range(0,len(lines),1): 
        lines[l] = [lines[l][0]*mm*Xmm,lines[l][1]*mm*Ymm,lines[l][2]*mm*Xmm,lines[l][3]*mm*Ymm]
        menorX=lines[l][0] if lines[l][0]<menorX else menorX
        mayorX=lines[l][0] if lines[l][0]>mayorX else mayorX
        menorX=lines[l][2] if lines[l][2]<menorX else menorX
        mayorX=lines[l][2] if lines[l][2]>mayorX else mayorX
        menorY=lines[l][1] if lines[l][1]<menorY else menorY
        mayorY=lines[l][1] if lines[l][1]>mayorY else mayorY
        menorY=lines[l][3] if lines[l][3]<menorY else menorY
        mayorY=lines[l][3] if lines[l][3]>mayorY else mayorY
        #print(lines[l])
    mayorX=mayorX-menorX
    mayorY=mayorY-menorY
    divisionX=1
    divisionY=1
    if (page[0]*escalaX) < mayorX:
        divisionX=int(mayorX/(page[0]*escalaX))+1
        
    if (page[1]*escalaY) < mayorY:
        divisionY=int(mayorY/(page[1]*escalaY))+1
    geo=geometria()
    planos=[]
    #trasladamos todos los puntos de todos los poligonos al primer Cuadrante
    for t in range(0,len(textos),1):
        print(textos[t])
        textos[t][0]=textos[t][0]*mm*Xmm-(menorX)
        textos[t][1]=textos[t][1]*mm*Ymm-(menorY)
    for polig in range(0,len(poligono),1): 
        for p in range(0,len(poligono[polig]),1):
            poligono[polig][p]=(poligono[polig][p][0]-(menorX),poligono[polig][p][1]-(menorY))
    for l in range(0,len(lines),1): 
        lines[l] = [lines[l][0]-menorX,lines[l][1]-menorY,lines[l][2]-menorX,lines[l][3]-menorY]
    #pasamos las lineas a poligonos
    divX=[x*page[0]*escalaX for x in range(0,divisionX,1)]+[mayorX]
    divY=[y*page[1]*escalaY for y in range(0,divisionY,1)]+[mayorY]
    print("cortando")
    for l in range(0,len(lines),1): 
        v=[lines[l][2]-lines[l][0],lines[l][3]-lines[l][1],0]
        oX = lines[l][0] if v[0]==0.0 else -1.0
        oY = lines[l][1] if v[1]==0.0 else -1.0
        Yf=lines[l][1] if lines[l][1]>lines[l][3] else lines[l][3]
        Yi=lines[l][1] if lines[l][1]<lines[l][3] else lines[l][3]
        Xf=lines[l][0] if lines[l][0]>lines[l][2] else lines[l][2]
        Xi=lines[l][0] if lines[l][0]<lines[l][2] else lines[l][2]
        # dividimos en Y
        div=[divY[d] for d in range(0,len(divY)-1,1) if ((divY[d]<=Yi) and (divY[d+1]>=Yi))]
        div = div[0] if div else 0.0
        puntos = [[(((float(y)/10.0)-lines[l][1])/(v[1]/v[0])+lines[l][0]) if v[0]!=0.0 else lines[l][0],(float(y)/10.0)] for y in range(int(div*10),int(Yf*10),int(page[1]*escalaY*10))[1:]]
        # dividimos en X
        div=[divX[d] for d in range(0,len(divX)-1,1) if ((divX[d]<=Xi) and (divX[d+1]>=Xi))]
        div = div[0] if div else 0.0
        puntos += [[float(x)/10.0,(((float(x)/10.0)-lines[l][0])*(v[1]/v[0])+lines[l][1]) if v[1]!=0.0 else lines[l][1]] for x in range(int(div*10),int(Xf*10),int(page[0]*escalaX*10))[1:]]
        polig=[lines[l][0:2]]
        distancias=[[geo.dist(lines[l][0:2]+[0],p+[0]),p[0],p[1]] for p in puntos]
        for p in range(0,len(puntos),1):
            menor=geo.dist(lines[l][0:2]+[0],lines[l][2:]+[0])
            pos=0
            for x in range(0,len(distancias),1):
                if distancias[x][0]<menor:
                    menor=distancias[x][0]
                    pos=x
            polig += [[(((distancias[pos][2]-1.0)-lines[l][1])/(v[1]/v[0])+lines[l][0]) if v[0]!=0.0 else lines[l][0],distancias[pos][2]-1.0]]
            polig += [[(((distancias[pos][2]+1.0)-lines[l][1])/(v[1]/v[0])+lines[l][0]) if v[0]!=0.0 else lines[l][0],distancias[pos][2]+1.0]]
            distancias.pop(pos)
        polig += [lines[l][2:]]
        poligono += [polig]
    margen=margenes if margenes else [((page[0]*(1.0-escalaX))/2),((page[1]*(1.0-escalaY))/2)]
    txt=[]
    for x in range(0,divisionX,1):
        for y in range(0,divisionY,1):
            txt= [[]]+txt
            for t in textos:
                if (((page[0]*escalaX)>=(t[0]-(x*page[0]*escalaX))) and ((t[0]-(x*page[0]*escalaX))>=0.0) ) and (((page[1]*escalaY) >= (t[1]-(y*page[1]*escalaY)))  and ((t[1]-(y*page[1]*escalaY))>=0.0)) :
                    txt[0] += [[ t[0]-(x*page[0]*escalaX)+margen[0],t[1]-(y*page[1]*escalaY)+margen[1],t[2],t[3] ]]
    for polig in range(0,len(poligono),1): 
        plano=[]
        matriz=[]
        for x in range(0,divisionX,1):
            for y in range(0,divisionY,1):
                plano = [[]] + plano
                matriz += [[divisionX-x-1,divisionY-y-1]]
                for p in poligono[polig]:
                    if (((page[0]*escalaX)>=(p[0]-(x*page[0]*escalaX))) and ((p[0]-(x*page[0]*escalaX))>=0.0) ) and (((page[1]*escalaY) >= (p[1]-(y*page[1]*escalaY)))  and ((p[1]-(y*page[1]*escalaY))>=0.0)) :
                        plano[0] += [ [(p[0]-(x*page[0]*escalaX))+margen[0] , (p[1]-(y*page[1]*escalaY))+margen[1]]]
                        
        planos += [plano]
    global canvas
    canvas = canvas.Canvas(datos['archivo'], pagesize=page)
    def texto(x,y,ang,txt):
        print(x,y,ang,txt)
        canvas.saveState()
        rad=-1*math.radians(float(ang))
        i, j=geo.rotar(rad,[x,y,0])
        canvas.rotate(ang)
        canvas.drawString(i,j,str(txt))
        canvas.restoreState()

    def cuadriculando(cuadricular):
        if cuadricular:
            canvas.saveState()
            canvas.setDash(1,10)
            canvas.setLineWidth(0.1)
            #linea Vartical
            canvas.line((page[0]/2), page[1]-margen[1], (page[0]/2), margen[1])
            #linea Horizontal
            canvas.line(margen[0],(page[1]/2),page[0]-margen[0],(page[1]/2))
            #linea Diagonal de Superior Izquierdo a inferior derecho
            canvas.line(margen[0], page[1]-margen[1], page[0]-margen[0],margen[1])
            #linea Diagonal de inferior Izquierdo a Superior Derecho
            canvas.line(margen[0],margen[1],page[0]-margen[0],page[1]-margen[1])
            #limites
            canvas.setDash(5,5)
            canvas.setLineWidth(0.3)
            #limite horizontal superior
            canvas.line((page[0]/2)-50, page[1]-margen[1],(page[0]/2)+50, page[1]-margen[1])
            #limite horizontal inferior
            canvas.line((page[0]/2)-50, margen[1],(page[0]/2)+50, margen[1])
            #limite Vertical Derecho
            canvas.line((page[0]-margen[0]), (page[1]/2)-50,(page[0]-margen[0]), (page[1]/2)+50)
            #limite Vertical Izquierdo
            canvas.line((margen[0]), (page[1]/2)-50,(margen[0]), (page[1]/2)+50)
            canvas.restoreState()
            
    if not calibrar:
        hojaConDibujo=[0]*(divisionY*divisionX)
        print(hojaConDibujo)
        canvas.setLineWidth(3)
        for x in range(0,(divisionY*divisionX),1):
            dibujado=0
            if txt[x]:
                for t in txt[x]:
                    texto(*t)
            for p in range(0,len(planos),1):
                if len(planos[p][x])>1:
                    hojaConDibujo[x] = 1        
                if len(planos[p][x])>1 or imprimirHojasEnblanco:
                    cuadriculando(cuadricular)
                    dibujado=1
                    for g in range(0,len(planos[p][x])-1,1):
                        canvas.line(planos[p][x][g][0], planos[p][x][g][1], planos[p][x][g+1][0], planos[p][x][g+1][1])
            if dibujado:
                canvas.drawString(10.0*mm,800,str(matriz[x]))
                canvas.drawString(page[0]-20.0*mm,(15*mm),str(x+1))
                canvas.showPage()
                canvas.setLineWidth(3)
        print(hojaConDibujo)
        datos['cantidadTotalDeHojas']=divisionX*divisionY
        datos['HojasEnBlanco']=str([x+1 for x in range(0,len(hojaConDibujo),1) if hojaConDibujo[x]==0 ])
        datos['HojasConDibujo']=str([x+1 for x in range(0,len(hojaConDibujo),1) if hojaConDibujo[x]>0 ])
    canvas.setLineWidth(0.3)
    canvas.setFont('Helvetica', fontSize)
    contador=1
    datos['miniatura']=str(bool(miniatura))
    datos['tipoDeHoja']='A4'
    datos['medidasDeLaHoja']=[page[0]/mm,page[1]/mm]
    datos['ALTOdelDibujo']=mayorY/mm
    datos['ANCHOdelDibujo']=mayorX/mm
    datos['imprimirHojasEnblanco']=str(bool(imprimirHojasEnblanco))
    canvas.setLineCap(1) #extremo de la linea redondeada
    cuadriculando(cuadricular)
    canvas.setDash(6,3)# sucesion de 6 puntos trazados y 3 no trazados
    for x in datos:
        if (page[1]-(contador*fontSize*mm))<(fontSize*mm):
            canvas.showPage()
            canvas.setLineCap(1)
            contador=1
            cuadriculando(cuadricular)
            canvas.setDash(6,3)# sucesion de 6 puntos trazados y 3 no trazados
        canvas.drawString(30+margen[0],page[1]-(contador*fontSize*2.0)-margen[1],str(x)+':')
        #((0,len(str(datos[x])),40))
        canvas.line(100+((len(x)-10)*5 if len(x)>10 else 0)+margen[0],page[1]-(contador*fontSize*2.0)-2-margen[1],580-margen[0],page[1]-(contador*fontSize*2.0)-2-margen[1])
        canvas.drawString(100+((len(x)-10)*5 if len(x)>10 else 0)+margen[0],page[1]-(contador*fontSize*2.0)-margen[1],str(datos[x]))
        contador += 1
    canvas.setLineWidth(1)
    canvas.setDash(1,0) #dibuja 1 puntos y ignora 0 puntos
    canvas.setLineCap(2) #extremo de la linea cuadrada
    #linea que agarra toda la hoja de izquierda a derecha, osea horizontal
    canvas.drawString((page[0]/2),page[1]-(contador*fontSize*2.0)+5,str(page[0]/mm)+'mm. RealANCHO')
    canvas.line(0, page[1]-(contador*fontSize*2.0), page[0], page[1]-(contador*fontSize*2.0))
    contador+=1
    #100mm horizontales
    canvas.drawString((page[0]/2),page[1]-(contador*fontSize*2.0)+5,str(100)+'mm. REALmmX')
    canvas.line((page[0]/2)-50.0*mm, page[1]-(contador*fontSize*2.0), (page[0]/2)+50.0*mm, page[1]-(contador*fontSize*2.0))

    texto(page[0]-10.0*mm-margen[0],(page[1]/2),90.0,str(page[1]/mm)+'mm. RealALTO')
    texto(page[0]-20.0*mm-margen[0],(page[1]/2),90.0,str(100)+'mm. REALmmY')
    #100mm verticales
    canvas.line(page[0]-10.0*mm-margen[0], page[1], page[0]-10.0*mm-margen[0], 0.0)
    #linea que agarra toda la hoja de arriba a abajo, osea vertical
    canvas.line(page[0]-20.0*mm-margen[0], (page[1]/2)+50.0*mm, page[0]-20.0*mm-margen[0], (page[1]/2)-50.0*mm)    
    canvas.save()
    print("Ok")
def planos():
    escala=1.0
    puntos,lineas,datos,textos = aspas(escalar=escala)
    datos['plano']="Hoja de una turbina de viento"
    datos['archivo']="plano_escala_1.0_Turbina_eolica.pdf"
    datos['UnidadDeMedida']="milimetros"
    datos['escala']=str(escala)
    poligonoToPDF(calibrar=0,miniatura=1,poligonos=[puntos],lineas=lineas,datos=datos, printTEXT=textos)
    if input("Ya imprimio y saco las medidas de la hoja de prueba? S/N:").lower()=="s":
        RealANCHO=float(input("RealANCHO: "))
        RealALTO=float(input("RealALTO: "))
        REALmmX=float(input("REALmmX: "))
        REALmmY=float(input("REALmmY: "))
        margenX=float(input("margen superior: "))
        margenY=float(input("margen Izquierdo: "))
        miniatura=int(input("ImprmirMiniatura 1/0 : "))
        #=float(input(": "))
        poligonoToPDF(calibrar=0,miniatura=miniatura,REALsize=[RealANCHO,RealANCHO],margenes=[margenX,margenY],REALmm=[REALmmX,REALmmY],poligonos=[puntos],lineas=lineas,datos=datos)
def red():
    from mbarete import internet
    ip=internet()
    print('ip.lan_ip:',ip.lan_ip,'ip.wan_ip:',ip.wan_ip)
def servidor_HTTP_python(LAN=1):
    import socket   
    import threading
    if LAN:
        s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('10.255.255.255',1))
        ip=s.getsockname()
        s.close()
        host = ip[0]
    else:
        host = '127.0.0.1'
    port = 8080
    format_encode='utf-8'
    numerosMagicos={
        'png':{'inicio':b'\x89PNG\r\n'},
        'gif1':{'inicio':b'GIF89a'},
        'gif2':{'inicio':b'GIF87a'},
        'jpg1':{'inicio':b'\xff\xd8\xff\xdb'},
        'jpg2':{'inicio':b'\xff\xd8\xff\xe0'},
        'jpg':{'inicio':b'\xff\xd8\xff\xee'},
        'webp':{'inicio':b'RIFF\xb0y\x00\x00WEBPVP8'},
        'exe':{'inicio':b'MZ'},
        'pdf':{'inicio':b'%PDF-'},
        'OggS':{'inicio':b'OggS'},
        'matroska':{'inicio':b'\x1a\x45\xdf\xa3'},
        'script':{'inicio':b'#!'},
        'sql':{'inicio':b'SQLite format 3'},
        'faxx':{'inicio':b'FORM????FAXX'},
        'zip1':{'inicio':b'\x50\x4b\x03\x04'},
        'zip2':{'inicio':b'\x50\x4b\x05\x06'},
        #'zip3':{'inicio':b'PK␅␆'},
        #'rar':{'inicio':b'Rar!␚␇␀'},
        #'windowMedia':{'inicio':b'0&²uŽfÏ␑¦Ù␀ª␀bÎl'},
        #'Photoshop':{'inicio':b'8BPS'},
        'wav':{'inicio':b'RIFF????WAVE'},
        #'avi':{'inicio':b'RIFF????AVI␠'},
        #'1mp3':{'inicio':b'ÿû'},
        #'2mp3':{'inicio':b'ÿó'},
        #'3mp3':{'inicio':b'ÿò'},
        'mp3':{'inicio':b'ID3'},
        'CD_DVD':{'inicio':b'CD001'},
        'midi':{'inicio':b'MThd'},
        #'MicrosoftOffice':{'inicio':b'ÐÏ␑à¡±␚á'},
        #'debutante':{'inicio':b'!␊'},
        'webpGoogle':{'inicio':b'RIFF????WEBP'},
        'mp4':{'inicio':b'ftypisom'},
        'blender':{'inicio':b'BLENDER'}
        }
        #'':{'inicio':b''},
        #'':{'inicio':b''}
    global status
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()
    print(f"\nServidor HTTP corriendo en la direccion 'http://{host}:{port}/'")
    status=True
    clients = []
    usernames = []
    def requestToDictionary(request,add={}):
        """
            b'POST /subir HTTP/1.1'
            b'Host: 127.0.0.1:8080'
            b'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0'
            b'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
            b'Accept-Language: es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3'
            b'Accept-Encoding: gzip, deflate'
            b'Content-Type: multipart/form-data; boundary=---------------------------1262949829386019333586660223'
            b'Content-Length: 225'
            b'Origin: http://127.0.0.1:8080'
            b'Connection: keep-alive'
            b'Referer: http://127.0.0.1:8080/'
            b'Upgrade-Insecure-Requests: 1'
            b'Sec-Fetch-Dest: document'
            b'Sec-Fetch-Mode: navigate'
            b'Sec-Fetch-Site: same-origin'
            b'Sec-Fetch-User: ?1'
            b''
            b'-----------------------------1262949829386019333586660223'
            b'Content-Disposition: form-data; name="archivo"; filename=""'
            b'Content-Type: application/octet-stream'
            b''
            b''
            b'-----------------------------1262949829386019333586660223--'

        """
        if b'\r\n\r\n' in request:
            post=[ request.split(b'\r\n\r\n')[-1]]
        requ=[r.decode(format_encode) for r in request.split(b'\r\n')]
        ret={}
        for i in requ:
            if ('POST' in i) or ('GET' in i):
                ret['method']=i.split(' ')[0]
                ret['sub_dominio']=i.split(' ')[1]
                ret['http']=i.split(' ')[2]
            if 'User-Agent:' in i:
                ret['User_Agent']=i[len('User_Agent: '):-1]
            if 'Content-Disposition:' in i:
                ret['form_data']={
                    'name':i.split('form-data; ')[-1].split(';')[0][len('name='):-1],
                    'filename':i.split('form-data; ')[-1].split(';')[1][len(' filename="'):-1]
                }
            if 'Content-Type: multipart/form-data;' in i:
                ret['boundary']=i.split('boundary=')[-1]
            
        if add:
            for a in add:
                ret[a]=add[a]
        return ret
    def respond(client, address):
        responder=False
        request=b''
        ok=True
        cabezera=True
        porcion=1024*5
        binario=None
        info={}
        while ok:
            datos_Bytes=client.recv(porcion)
            if (b'Android' in datos_Bytes) and (b'boundary' in datos_Bytes):
                info=requestToDictionary(datos_Bytes)
                datos_Bytes=client.recv(porcion)
            if (porcion > len(datos_Bytes)) and (b'\r\n' in datos_Bytes):
                ok = False
            if cabezera:
                if (b'\r\n\r\n' in datos_Bytes) or info:
                    cabezera=False
                    for b in numerosMagicos:
                        if numerosMagicos[b]['inicio'] in datos_Bytes:
                            binario=b
                    if binario:
                        request=datos_Bytes.split(numerosMagicos[binario]['inicio'])[0]
                        info=requestToDictionary(request,add=info)
                        subiendo = open(info['form_data']['filename'],"wb")
                        subiendo.write(numerosMagicos[binario]['inicio']+datos_Bytes.split(numerosMagicos[binario]['inicio'])[-1])
                        while binario:
                            datos_Bytes=client.recv(porcion)
                            if info['boundary'].encode(format_encode) in datos_Bytes:
                                subiendo.write(datos_Bytes.split(info['boundary'].encode(format_encode))[0])
                                request=info['boundary'].encode(format_encode)+datos_Bytes.split(info['boundary'].encode(format_encode))[-1]
                                binario=False
                            else:
                                subiendo.write(datos_Bytes)
                        subiendo.close()
                        print("Subido:",info['form_data']['filename'])
                    else:
                        request+=datos_Bytes
                else:
                    request+=datos_Bytes
            else:
                request+=datos_Bytes
        print('request:',request)
        info = requestToDictionary(request,add=info)
        if ''!= request:
            print(info)
            if '/cerrar' in  info['sub_dominio']:
                print('Servidor Apagado')
                client.close()
                server.close()
                status=False
            elif ('GET' in info['method']):
                if '/' ==  info['sub_dominio']:
                    myfile = 'index.html'
                elif 'pruebaGet' in info['sub_dominio']:
                    myfile='index.html' 
                elif 'video' in info['sub_dominio']:
                    myfile='bibliografia/ONE_PUNCH_PARTE_9.mp4'
                else:
                    myfile='media/GET.html'
                    file=open(myfile,'wb')
                    file.write(request)
                    file.close()
            elif ('POST' in info['method']):
                if 'pruebaPost' in info['sub_dominio']:
                    myfile='media/pruebaPost.html'
                    file=open(myfile,'wb')
                    file.write(request)
                    file.close()
                else:
                    myfile='media/POST.html'
                    file=open(myfile,'wb')
                    file.write(request)
                    file.close()

            try:
                print('myfile',myfile)
                header='HTTP/1.1 200 OK\n'
                if myfile.endswith('.jpg'): 
                    mimetype='image/jpg'
                elif myfile.endswith('.css'): 
                    mimetype='text/css'
                elif myfile.endswith('.pdf'): 
                    mimetype='application/pdf'
                elif myfile.endswith('.mp4'): 
                    mimetype='video/mp4'
                else: 
                    mimetype='text/html'
                header += 'Content-Type: '+str(mimetype)+'\n\n'
            except Exception as e:
                header='HTTP:/1.1 404 Not Found \n\n'
                response=f'<html><body>Error 404: File NOt Found<br> {e} </body></html>'.encode(format_encode)
            header=header.encode(format_encode)
            client.send(header)
            file=open(myfile,'rb')
            client.send(file.read())
            file.close()
        client.close()
        print("fin de coneccion")
            
        
    def receive_connections():
        while status:
            client, address = server.accept()
            thread = threading.Thread(target=respond, args=(client, address))
            thread.start()
        print("fin de servicio")
    receive_connections()
    server.close()
def administrador_servidor_HTTP_python(LAN=1):
    import socket   
    import threading
    if LAN:
        s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('10.255.255.255',1))
        ip=s.getsockname()
        s.close()
        host = ip[0]
    else:
        host = '127.0.0.1'
    port = 8080
    format_encode='utf-8'
    def iniciar():
        thread = threading.Thread(target=servidor_HTTP_python)
        thread.start()
        servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(host, port)
        servidor.connect((host, port))
        return servidor
    def cerrar(servidor):
        servidor.send('cerrar'.encode(format_encode))
        return servidor
    def recargar(servidor):
        servidor.send('reiniciar'.encode(format_encode))
        return servidor
    def info(servidor):
        servidor.send('info'.encode(format_encode))
        return servidor
    comandos={'cerrar':cerrar,'recargar':recargar,'info':info}
    servidor=iniciar()
    while True:
        command=input('Ingrese un comando:'+str([c for c in comandos]))
        if command in comandos:
            servidor=comandos[command](servidor)
        if command=='':
            cerrar(servidor)
            break
def servidor_CHAT_socket_python():
    import socket   
    import threading
    host = '192.168.43.134'
    port = 8080
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()
    print(f"Servidor corriendo en la direccion {host}:{port}")
    clients = []
    usernames = []
    def broadcast(message, _client):
        for client in clients:
            if client != _client:
                client.send(message)
    def handle_messages(client):
        while True:
            try:
                message = client.recv(1024)
                broadcast(message, client)
            except:
                index = clients.index(client)
                username = usernames[index]
                broadcast(f"ChatBot: {username} se desconecto".encode('utf-8'), client)
                clients.remove(client)
                usernames.remove(username)
                client.close()
                break

    def receive_connections():
        while True:
            client, address = server.accept()
            client.send("@username".encode("utf-8"))
            username = client.recv(1024).decode('utf-8')

            clients.append(client)
            usernames.append(username)

            print(f"{username} esta conectado desde {str(address)}")

            message = f"ChatBot: {username} se unio al chat!".encode("utf-8")
            broadcast(message, client)
            
            thread = threading.Thread(target=handle_messages, args=(client,))
            thread.start()

    receive_connections()
def cliente_CHAT_socket_python():
    import socket   
    import threading
    #username = input("Ingresa tu nombre de usuario: ")
    username = "Ingresa"
    host = '192.168.43.134'
    port = 8080
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    def receive_messages():
        while True:
            try:
                message = client.recv(1024).decode('utf-8')
                if message == "@username":
                    client.send(username.encode("utf-8"))
                else:
                    print('\n'+message+'\n<<< Tu:',end='')
            except:
                print("Houston! Tenemos Problemas")
                client.close()
                break
    def write_messages():
        while True:
            tu=input('<<< Tu:')
            if tu=='salir':
                client.close()
                break
            else:
                message = f"{username}: {tu}"
                client.send(message.encode('utf-8'))
    receive_thread = threading.Thread(target=receive_messages)
    receive_thread.start()
    write_thread = threading.Thread(target=write_messages)
    write_thread.start()
def ahorcado(pwd=d['img']+"palabras.txt"):
    import random
    vidas='******'
    letrasCantadas=''
    file=open(pwd,'r')
    secretos=[line[:-1] for line in file]
    file.close()
    secreto=secretos[random.randrange(0,len(secretos))].upper()
    letra_inicio=random.randrange(0,len(secreto))
    palabra='_ '*len(secreto)
    letra=secreto[letra_inicio]
    while True:
        if (letra in secreto) and (letra not in letrasCantadas):
            letrasCantadas+=letra
            for x in range(len(secreto)):
                if  secreto[x]==letra:
                    palabra=palabra[:2*x]+letra[0]+palabra[2*x+1:]
        elif letra in letrasCantadas:
            print("La letra '"+letra+"', ya fue Cantada...")
            vidas=vidas[:-1]
        else:
            letrasCantadas+=letra
            vidas=vidas[:-1]
        print('\n\nPalabra Secreta:    '+palabra)
        print('Vidas:  '+vidas+', te quedan '+str(len(vidas))+' vidas.')
        print('Letras Cantadas:  '+letrasCantadas)
        if vidas:
            if [l for l in secreto if l not in letrasCantadas]:
                letra=input('Siguiente Letra: <<< ')[0].upper()
            else:
                if input("Muchas Felicidades Lograste Descubrir la palabra secreta "+secreto.upper()+". \n¿Si queres volver a jugar ingresa cualquier letra, sino es asi presiona enter? :<<<"):
                    secreto=secretos[random.randrange(0,len(secretos))]
                    letra_inicio=random.randrange(0,len(secreto))
                    palabra='_ '*len(secreto)
                    letra=secreto[letra_inicio]
                    letrasCantadas=''
                    vidas='******'
                else:
                    break
        else:
            print("Te quedaste sin vidas JAJAJA. \nLa palabra Secreta es: "+secreto)
            break
def manipularArchivos(pwd=d['img'],f='',ret=0):
    bi=b''
    if not f:
        file=f
    else:
        file='subiendo'
    binario=open(file,'rb')
    for b in binario:
        bi+=b
    binario.close()
    print(bi[:1024])
    print(bi[-1024:])
def capturarNumerosMagicos(pwd=d['img'],f='',ret=0):
    bi={}
    miDir=os.listdir(pwd)
    muestra=100
    contador=0
    for file in miDir:
        bi[contador]={'name':file,'inicio':b''}
        binario=open(pwd+'\\'+file,'rb')
        for inicio in binario:
            bi[contador]['inicio']+=inicio
        binario.close()
        bi[contador]['fin']=bi[contador]['inicio'][-muestra:]
        bi[contador]['inicio']=bi[contador]['inicio'][:muestra]
        print('name',bi[contador]['name'])
        print('inicio',bi[contador]['inicio'])
        print('fin',bi[contador]['fin'])
        contador+=1

print(__name__)
if 'main' in __name__:
    import threading
    pruebas=[
        {'titulo':"salir",'f':exit},
        {'titulo':"Lista de las variables del sistema",'f':VariablesDeEntorno},
        {'titulo':"os.path, Manipulaciones comunes de nombre de ruta:",'f':powerPath},
        {'titulo':"Prueba para generar archivo pdf desde una variable de tipo diccionario",'f':powerPDF},
        {'titulo':'Visor de Imagenes Pro v0.1 XD hecho en Tkinter','f':showAlbum},
        {'titulo':"Modificar una imagen, redimensionar la imagen guardar como otro archivo nuevo, luego usar ese nuevo archivo dentro de widget Button",'f':ButtonConImagen},
        {'titulo':"Crear un archivo PLayList para reproducir con el 'Reproductor Multimedia' del sistema operativo",'f':playlist},
        {'titulo':"retorna un poligono, que seria una hoja de unas aspas de un aerogenerador de viento ",'f':aspas},
        {'titulo':"Genera un PDF del poligono que vos le pases",'f':poligonoToPDF},
        {'titulo':"generamos un plano en un PDF con los dos ejemplos 9 y 10",'f':planos},
        {'titulo':"time ,pruebas con la libreria time:",'f':timeConOsPath},
        {'titulo':"obtener ip publica y pribada:",'f':red},
        {'titulo':"Decoradores y funciones y parametros",'f':decoradores},
        {'titulo':"Servidor Socket Python",'f':servidor_CHAT_socket_python},
        {'titulo':"Cliente Socket Python",'f':cliente_CHAT_socket_python},
        {'titulo':"Administrador Servidor HTTP Python",'f':administrador_servidor_HTTP_python},
        {'titulo':"Servidor HTTP Python",'f':servidor_HTTP_python},
        {'titulo':"Ahorcado",'f':ahorcado},
        {'titulo':"leerBinario",'f':manipularArchivos},
        {'titulo':"Capturar numeros magicos:",'f':capturarNumerosMagicos}
        ]
    def f(num):
        print('######################################################################')
        print("PRUEBA",num,"Inicianda: "+pruebas[num]['titulo'])
        print('######################################################################'+'\n')
        hilo=threading.Thread(target=pruebas[num]['f'])

        #llamamos a la funcion
        hilo.start()

        #esperamos que termine
        hilo.join()
        #Aviso de que la funcion termino.
        print('\n'+"PRUEBA Terminada...")
        print('\n')
    if len(sys.argv)>1:
        f(int(sys.argv[1]))
        exit()        
    num=1
    while num > 0:
        num=0
        for prueba in range(0,len(pruebas),1):
            print(prueba,pruebas[prueba]['titulo'])
        inpu=input('Ingrese el numero de la siguiente prueba: ').split(' ')
        num=int(inpu[0] if inpu[0] != '' else 0)
        if num > 0:
            f(num)
        else:
            exit()
            
#https://youtube.com/playlist?list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS
#https://drive.google.com/drive/folders/1NXO6zm1WqKvr7x8ZI5U2PgZpkt6sAsYt?usp=sharing