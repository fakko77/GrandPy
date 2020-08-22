class Killer:
    """ class for creat a City """
    def __init__(self, text):
        self.text = text

    def parser(self, dico):
        """ delete word depending on the dico """
        cpt = 0
        txt = self.text
        dicolen = len(dico)
        txt = txt.split()
        txtlen = len(txt)
        list = []
        while dicolen > cpt:
            cpt_txt = 0
            while txtlen > cpt_txt:
                if txt[cpt_txt] == dico[cpt]:
                    list.append(dico[cpt])
                    cpt_txt += 1
                cpt_txt += 1
            cpt += 1
            x = 0
        while x < len(list):
            txt.remove(list[x])
            x += 1
        return txt
