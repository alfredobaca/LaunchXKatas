text = """Interesting facts about the Moon.
        The Moon is Earth's only satellite.
        There are several interesting facts about the Moon and how it affects life here on Earth.
        On average, the Moon moves 4cm away from the Earth every year.
        This yearly drift is not significant enough to cause immediate effects on Earth.
        The highe"""
textSpace = text.split('\n')
arrayWords = ['average','temperature','distance']
for sentence in textSpace:
    for arrayWords in arrayWords:
        if arrayWords in sentence:
            print(sentence)
            break
for sentence in textSpace:
    for arrayWords in arrayWords:
        if arrayWords in sentence:
            print(sentence.replace(' C', ' Celsius'))
            break
name = "Moon"
gravity = 0.00162 # in kms
planet = "Tierra"
titulo = 'datos sobre la grabedad sobre la '+planet
hechos = f"""{'-'*80} 
Nombre del planeta: {planet} 
Gravedad en {name}: {gravity * 1000} m/s2 
"""
template = f"""{titulo.title()} 
{hechos} 
""" 
print(template)
