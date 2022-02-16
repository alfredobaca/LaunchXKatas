#1
def reporte(tanque1, tanque2, tanque3):
    total = (tanque1 + tanque2 + tanque3) / 3
    return f""" Reporte:
    Total : {total}%
    tanque1: {tanque1}%
    tanque2: {tanque2}%
    tanque3: {tanque3}%
    """
print(reporte(98, 40, 67))

def average(values):
    total = sum(values)
    number_of_items = len(values)
    return total / number_of_items

average([98, 40, 67]) 


def reporte(tanque1, tanque2, tanque3):
 
    return f""" Reporte:
    Total : {average([tanque1, tanque2, tanque3 ])}%
    tanque1: {tanque1}%
    tanque2: {tanque2}%
    tanque3: {tanque3}%
    """
print(reporte(98, 40, 67))

#2

def reporte_Mision(lanzamientoTiempo, vueloTiempo, destino, tanque1, tanque0):
    return f"""
    Mision a {destino}
    Total tiempo: {lanzamientoTiempo + vueloTiempo} minutos
    Total combustible: {tanque0 + tanque1} gallones
    """

print(reporte_Mision(20, 81, "Luna", 8000000, 9000))

def reporte_Mision(destino, *minutos, ** reserva):
    return f"""
    Mision {destino}
    Total tiempo: {sum(minutos)} minutos
    Total combustible: {sum(reserva.values())}
    """

print(reporte_Mision("Luna", 20, 25, 14, principal=300000, externo=200000))

def reporte_Mision(destino, *minutos, ** reserva):
    reporte = f"""
    Mision {destino}
    Total tiempo: {sum(minutos)} minutos
    Total combustible: {sum(reserva.values())}
    """
    for tanque, gallones in reserva.items():
        reporte += f"{tanque} tanque --> {gallones} gallones\n"
    return reporte
print(reporte_Mision("Luna", 10, 13, 55, principal=300000, externo=200000))