class Killer:
    """ class for creat a City """
    def __init__(self, text):
        self.text = text

    def parser(self, dico):
        """ delete word depending on the dico """
        cpt = 0
        txt = self.text
        dict_len = len(dico)
        txt = txt.split()
        txt_len = len(txt)
        list_stock = []
        while dict_len > cpt:
            cpt_txt = 0
            while txt_len > cpt_txt:
                if txt[cpt_txt] == dico[cpt]:
                    list_stock.append(dico[cpt])
                    cpt_txt += 1
                cpt_txt += 1
            cpt += 1
            x = 0
        while x < len(list_stock):
            txt.remove(list_stock[x])
            x += 1
        return txt
