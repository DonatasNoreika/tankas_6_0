
from tankas import Tankas

tankas = Tankas()

while True:
    tankas.info()
    veiksmas = input("a - kairėn\nd - dešinėn\nw - pirmyn\ns - atgal\n")
    match veiksmas:
        case "a":
            tankas.kairen()
        case "d":
            tankas.desinen()
        case "w":
            tankas.pirmyn()
        case "s":
            tankas.atgal()