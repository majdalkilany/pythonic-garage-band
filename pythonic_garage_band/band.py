from pythonic_garage_band.pythonic_garage import Musician ,Guitarist ,Drummer ,Bassist
class Band (): 
    band_names = []

    def __init__(self,name) :
        self.name = str(name) 
        # print(members)
        self.members = Musician.all_members()
        Band.band_names.append(self.members)

    def play_solo(self) :
        the_members = Musician.all_members()
        solo_players = []
        for i in the_members :

             solo_players.append(f' "i am { i} and i am a solo player from the class Band')
        return solo_players

    def __str__(self):
        return f"str method from band class {self.name}"
    
    def __repr__(self):
        return f"repr method from band class {self.name}"
        

    @classmethod
    def to_list() : 
        return Band.band_names
 
 
        return Band.band_names
if __name__=="__main__":
    

    

    majd = Drummer('majd')
    print(majd)
    print(majd.get_instrument())
    print(majd.play_solo())

    basil = Guitarist('Basil')
    print(basil)
    print(basil.get_instrument())
    print(basil.play_solo())

    ibrahim = Bassist('ibrahim')
    print(ibrahim)
    print(ibrahim.get_instrument())
    print(ibrahim.play_solo())
    print(Musician.__str__)

    Khaled = Band("Beatles")
    print(Khaled.play_solo())

    print(Musician.all_members())

    print(Band.band_names)

