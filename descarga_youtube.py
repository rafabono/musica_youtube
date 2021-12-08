import pytube,os,re

descargas = "musica"
fichero = "canciones.txt"
#crea fichero canciones
if os.path.exists(fichero):
    pass
else:
    print("Creando " + fichero + "....")
    document= open(fichero,'w')
    print("Pega las url de tus canciones en el fichero " +  fichero)
    document.close()
#crea directorio de descargas
if os.path.exists(descargas):
    pass
else:
    os.mkdir('musica')
document = open(fichero,'r')
music_list = document.readlines()
document.close()
error_list=[]

print("Descargando musica....")
for music in music_list:
    try:
        url = music
        yt = pytube.YouTube(url)
        st = yt.streams.filter(only_audio=True).first()
        st.download(descargas,filename=re.sub('\W+',' ', st.title)+".mp3")
        print ("Descargado: " + st.title)
    except Exception as e: 
        error_list.append("Error descargando: "+ music)
        print(e)
        
for error in  error_list:
    print(error)

print("Proceso finalizado...")