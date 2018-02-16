class Word():
    meaning = 'N/A'
    p_s = 'N/A'
    translation = {}

def __init__(self,meaning,p_s,translation):
    self.meaning = meaning
    self.p_s = p_s
    self.translation = translation

def to_korean(self):
    if 'Korean' in self.translation:
        translation_word = self.translation['Korean']
        return translation_word
    return None


bts = Word("my life","noun",{"Korean" : "bangtan sonyeondan",
                             "english" : "beyond the scene",
                             "french" : "BTS"}
            )
bts.meaning = "my life"
bts.p_s = "noun"
bts.translation = {"Korean" : "bangtan sonyeondan",
                   "english" : "beyond the scene",
                   "french" : "BTS"}

dictionary = {'bts':bts}

print dictionary['bts'].to_korean()
