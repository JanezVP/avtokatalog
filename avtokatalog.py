
class vozni_park (object):
    def __init__(self, znamka, model, stevilo_kilometrov, servis):
        self.znamka = znamka
        self.model = model
        self.stevilo_kilometrov = stevilo_kilometrov
        self.servis = servis

    def izpisi_katalog(self):
        return (self.znamka  + ", " + self.model  + ", " "prevozenih: " + self.stevilo_kilometrov  + " km" + ", " + "zadnji servis: " + self.servis)


prvi = vozni_park(znamka ="fiat", model="punto", stevilo_kilometrov="10", servis="1980")
drugi = vozni_park(znamka ="opel", model="astra", stevilo_kilometrov="100", servis="2000")


avtokatalog = [prvi, drugi]
print "Vas vozni park je: "

for tretji in avtokatalog:
    print  tretji.izpisi_katalog()

while True:
    odgovor = raw_input("Zelite koncati? da/ne ")
    if odgovor == "da":
                        break
    znamka = raw_input("znamka ")
    model = raw_input("model ")
    stevilo_kilometrov = raw_input("kilometri ")
    servis = raw_input("servis ")

    katalog = vozni_park(znamka, model, stevilo_kilometrov, servis)

    avtokatalog.append(katalog)

for katalog in avtokatalog:
    print(katalog.izpisi_katalog())
    


