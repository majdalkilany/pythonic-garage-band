from pythonic_garage_band.band import Band ,Musician,Guitarist,Bassist,Drummer
import pytest


@pytest.fixture
def test_prep_data (): 
    majd = Drummer('majd')
    ahmad = Guitarist("ahmad")
    khaled = Bassist('khaled')
    

    return {
    'majd' : majd ,
    'ahmad' : ahmad,
    'khaled':khaled
    

    }

 
 



#    Musician test 



def test_musician_ansrumant(test_prep_data):
        expected = [test_prep_data['majd'],test_prep_data['ahmad'],test_prep_data['khaled']]
        actual = Musician.all_members()
        assert expected == actual


def test_new_band () :

    # Band('1')
    accepted = []
    actual = Band.band_names
    assert accepted == actual

                  
                  
                  
                          #Drummer test 







def test_drumer_ansrumant(test_prep_data):
    expected = "i am a Drummer !!? "
    actual = test_prep_data['majd'].get_instrument()
    assert expected == actual

def test_drumer_solo(test_prep_data):
    expected = "i am playing on my drums "    
    actual = test_prep_data['majd'].play_solo()
    assert expected == actual

def test_drumer_str (test_prep_data):
    expected = ' class   <majd >' 
    actual = test_prep_data['majd'].__str__()
    assert expected == actual

def test_drumer_repr (test_prep_data):
    expected = 'majd ' 
    actual = test_prep_data['majd'].__repr__()
    assert expected == actual



#Bassist test 


def test_bassist_ansrumant(test_prep_data):
    expected = "i am a Bassist  "
    actual = test_prep_data['khaled'].get_instrument()
    assert expected == actual

def test_bassist_solo(test_prep_data):
    expected =  "i am playing on my bass "      
    actual = test_prep_data['khaled'].play_solo()
    assert expected == actual

def test_bassist_str (test_prep_data):
    expected = ' class   <khaled >' 
    actual = test_prep_data['khaled'].__str__()
    assert expected == actual

def test_bassist_repr (test_prep_data):
    expected = 'khaled ' 
    actual = test_prep_data['khaled'].__repr__()
    assert expected == actual



            # guterst test 



def test_guitarist_ansrumant(test_prep_data):
    expected = "i am a Guitarist  "
    actual = test_prep_data['ahmad'].get_instrument()
    assert expected == actual

def test_guitarist_solo(test_prep_data):
    expected = "i am playing on my guitar "    
    actual = test_prep_data['ahmad'].play_solo()
    assert expected == actual

def test_guitarist_str (test_prep_data):
    expected = ' class   <ahmad >' 
    actual = test_prep_data['ahmad'].__str__()
    assert expected == actual

def test_guitarist_repr (test_prep_data):
    expected = 'ahmad ' 
    actual = test_prep_data['ahmad'].__repr__()
    assert expected == actual

   



                          #band test 
