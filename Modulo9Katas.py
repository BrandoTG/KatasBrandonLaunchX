def promedio(values):
    total=sum(values)
    cantidad=len(values)
    return total / cantidad

def lecturas (Depositointerno, DepositoExterno, DepositoEmergencia):
    
    return f'''Fuel Report:
    Promedio total: {promedio([Depositointerno,DepositoExterno,DepositoEmergencia])}%
    Deposito Principal: {Depositointerno}%
    Deposito Externo: {DepositoExterno}%
    Hydrogen tank: {DepositoEmergencia}% 
    '''
    
print(lecturas(50,45,15))

#Ejercicio 2: Trabajo con argumentos de palabra clave

def informe_mision (tiempo_prelanzamiento,tiempo_vuelo,destino,tanque_externo,tanque_interno):
    return f'''
    Tiempo Prelanzamiento: {tiempo_prelanzamiento} minutos
    Tiempo de Vuelo: {tiempo_vuelo} minutos
    Destino: {destino}
    Tanque Externo: {tanque_externo}%
    Tanque Interno: {tanque_interno}%
'''

print(informe_mision(1030,2030,'Marte',25,38))

def informe_mision_v2(Destino, *Minutos, **CombustibleReserva):
    Reporte = f"""
    Destino:  {Destino}
    Tiempo total de viaje: {sum(Minutos)} Minutos
    Combustible disponible: {sum(CombustibleReserva.values())}
    """
    for nombre_deposito, galones in CombustibleReserva.items():
        Reporte += f"Deposito {nombre_deposito} --> {galones} galones restantes\n"
    return Reporte

print(informe_mision_v2("Luna", 8, 11, 55, principal=300000, externo=200000))
    


