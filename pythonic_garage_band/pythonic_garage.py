from abc import abstractclassmethod

class Musician():
    members= []
    def __init__(self, name):
        self.name=name
        Musician.members.append(self)

    @abstractclassmethod
    def __str__(self) :
        '''
        this str method from super class to make every sub class have str method
        '''
        return f'Musican class  str <{self.name} >'

    
    @abstractclassmethod
    def __repr__(self) :
        '''
        this repr method from super class to make every sub class have repr method
        '''
        return f'{self.name} '


    @abstractclassmethod
    def get_instrument(self) :
                '''
                this get_instrument method from super class to make every sub class have 
                get_instrument method
                '''

                return "instrument from the Musician class "

    @abstractclassmethod
    def play_solo(self) :
        '''
        this play_solo method from super class to make every sub class have 
        play_solo method
        '''

        return "play_solo from the Musician class "    

    def all_members():
        return Musician.members

class Guitarist(Musician) :
    def __init__(self, name ):

         super().__init__(name)


    def __str__(self) :
        '''
        this str method from Guitarist class
        '''
        return f' class   <{self.name} >'

    
    def __repr__(self) :
        '''
        this repr method from Guitarist class
        '''
        return f'{self.name} '


    def get_instrument(self) :
        '''
        this get_instrument method from 
        '''

        return "i am a Guitarist  "

    def play_solo(self) :
        '''
        this play_solo method from 
        '''

        return "i am playing on my guitar "    


class Bassist(Musician) :
    def __init__(self, name ):

         super().__init__(name)


    def __str__(self) :
        '''
        this str method from Bassist class
        '''
        return f' class   <{self.name} >'

    
    def __repr__(self) :
        '''
        this repr method from Bassist class
        '''
        return f'{self.name} '


    def get_instrument(self) :
        '''
        this get_instrument method from Bassist
        '''

        return "i am a Bassist  "

    def play_solo(self) :
        '''
        this play_solo method from Bassist
        '''

        return "i am playing on my bass "    


class Drummer(Musician) :

    def __init__(self, name ):

         super().__init__(name)

    def __str__(self) :
        '''
        this str method from Drummer class
        '''
        return f' class   <{self.name} >'

    
    def __repr__(self) :
        '''
        this repr method from Drummer class
        '''
        return f'{self.name} '


    def get_instrument(self) :
        '''
        this get_instrument method from Drummer
        '''

        return "i am a Drummer !!? "

    def play_solo(self) :
        '''
        this play_solo method from  Drummer
        '''

        return "i am playing on my drums "    



if __name__=="__main__":
    pass
    # test = Band.play_solo('majd' ,['majd','mot'])
    # print(test)
    # print(Band.band_names)
    # majd = Drummer('majd')
    # print(majd)
    # print(majd.get_instrument())
    # print(majd.play_solo())

    # basil = Guitarist('Basil')
    # print(basil)
    # print(basil.get_instrument())
    # print(basil.play_solo())

    # ibrahim = Bassist('ibrahim')
    # print(ibrahim)
    # print(ibrahim.get_instrument())
    # print(ibrahim.play_solo())
    # print(Musician.__str__)

    # print(Musician.all_members())
