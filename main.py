class vzlom_pentagona:
    def __init__(self):
        self.data = [
            "parol ot pentagona: 228",
            "login ot pentagona: robertmuha303",
         " ",
            "полиция выехала за вами за взлом пентагона, быстрее оцените работу и полиция уйдет, у вас осталось: 2 века",
            " ",
            "сегодня в 8:30 я сделал открытие века",
         "в следующую секунду я открыл второе веко"
        ]

    def __iter__(self):
        for item in self.data:
            yield item


for brootforce in vzlom_pentagona():
    print(brootforce)