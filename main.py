import random as r
meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "XD": "Se usa cuando se quiere referir en forma sarcastica algo",
            "AFK": "Se usa cuando alguien esta quieto por mucho tiempo",
            "GG": "Se usa despues de perder o ganar para demostrar respeto al rivar",
            "F": "Se usa en ocasiones tristes"
            }

print(meme_dict.keys())
word =  input("Escribe una palabra que no entiende o escribe sorprendeme :").upper()

if word in meme_dict.keys():
    print("El significado es:", meme_dict[word])
elif word == "sorprendeme":
    wordr = r.choice(list(meme_dict.keys()))
    print("La palabra es:", wordr, "el significado es:",meme_dict[wordr])
else:
    print("Esta palabra no se encuentra")
