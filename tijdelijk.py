prijzen = {
    "Aardbei": 3,
    "Vanille": 4,
    "chocolade": 5
}
aanbieding = prijzen["Aardbei"] * 0.8
reclame_text = (f"Vandaag in de aanbieding: vanille-ijs, 1 liter - slechts € {aanbieding} ")
reclame_text2 = reclame_text[:63]
reclame_text3 = reclame_text2.upper()

reclame_text4 = reclame_text3.split()

for el in reclame_text4:
    if len(el) > 4:
        print(el.upper())
    else:
        print(el.lower())
   