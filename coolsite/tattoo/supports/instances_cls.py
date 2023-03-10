from .support_cls import *

main_menu_info_cls = MainData("Tattoo", "Татуировка", "main_text")
history_info = MainData("History", "История", "history_text")

################   Экземпляры класса TattooStyle   #####################################################################
oldSchool = TattooStyle(1, "OldSchool", "Традиционный стиль (Олд Скул)", "OldSchool")
newSchool = TattooStyle(2, "NewSchool", "Нью скул", "NewSchool")
realism = TattooStyle(3, "Realism", "Реализм", "Realism")
biomechanics = TattooStyle(4, "Biomechanics", "Биомеханика", "Biomechanics")
graphic = TattooStyle(5, "Graphic", "Графика", "Graphic")
japanese = TattooStyle(6, "Japanese", "Японские татуировки", "Japanese")
blackwork = TattooStyle(7, "Blackwork", "Блэкворк", "Blackwork")
lettering = TattooStyle(8, "Lettering", "Леттеринг", "Lettering")
chicano = TattooStyle(9, "Chicano", "Чикано", "Chicano")
ornamental = TattooStyle(10, "Ornamental", "Орнаментал", "Ornamental")
