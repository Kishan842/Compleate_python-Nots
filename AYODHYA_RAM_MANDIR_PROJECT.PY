# PROJECT FOR RAM MANDIR. 

class Jai_Shree_Ram:
    Temple = "Ram Mandir"

    def __init__(Ram, Sita, Laxman, Hanuman, Bajarangi):
        Ram.Sita = Sita
        Ram.Laxman = Laxman
        Ram.Hanuman = Hanuman
        Ram.Bajarangi = Bajarangi
        print("\t\t\t\t--------------- Jai Shree Ram...🙏🚩 ---------------\n\t\t\t\t\n\t\t\t\tGood Is Comming...🕉️\n")

    def get_Details(Ram):
        print(f"\t\t\t\tThe Name of the First Good is {Ram.Sita} ||\n");print(f"\t\t\t\tAnd {Ram.Sita} his Wife name is {Ram.Laxman} ||\n")
        print(f"\t\t\t\tthere are {Ram.Sita} has one Brother and his name is {Ram.Hanuman} ||\n"); print(f"\t\t\t\t{Ram.Sita} Most dedicated Asistent Name is {Ram.Bajarangi} ||")

    def Celibration(Ram, promiss):
        print(f"Promiss of all world is Selibrate a {Ram.Temple}")
        print(promiss)
    
    @staticmethod
    def come():
        print("\t\t\t\tJai Shree Ram Har Har Mahdev...🙏🚩🕉️               \n")

    @staticmethod
    def Time():
        print("\t\t\t\tThe Good Time to Celibrate a Function is 12:24\n\t\t\t\tMinute in the Evening..\n\t\t\t\t-----------------------------------------------------\n")

Ram_Lala = Jai_Shree_Ram("Ram", "Sita", "Laxman", "Hanuman")
Ram_Lala.get_Details()
Ram_Lala.Time(); Ram_Lala.come()
