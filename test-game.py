import engine.ogengine as o # Başlangıç

 # Ekranın boyutunu ve adını değiştirir
o.set_screen("Caption", (800, 600))

# Ekranın ekran rengini değiştirir
o.set_background_color(o.black)

# Karakter oluşturma
o.create_character(True, o.red, 50, 50)

# Ekranı oluştur
o.run_game(True)