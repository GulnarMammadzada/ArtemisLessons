class Oyuncu:
    def __init__(self, ad,xal):
        self.name = ad
        self.xal = xal

    def xal_artir(self,miqdar):
        self.xal += miqdar
        print(self.xal)

oyuncu=Oyuncu("Ali",3)
oyuncu.xal_artir(2)