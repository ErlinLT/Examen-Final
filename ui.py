
def table_row(rows):
    print("ID      Idioma      Frase      Autor")
    separador()
    for row in rows:
        id = row[0]
        idioma = row[1]
        frase = row[2]
        autor = row[3]
        print(id, idioma,frase,autor, sep="\t")

def separador(): #seperardor de lineas --------
    print("=" * 60)