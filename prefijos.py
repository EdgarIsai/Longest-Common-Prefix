lista = ['alec', 's', 'alarma', 'asetat', 'alexis', 'alec']
prefijo = []
prefijos_finales = []

for palabra in lista:
    prefijo_valido = 1
    if not prefijo:
        prefijo.append(palabra[0])
        prefijo.append("")

        # Compara con las demas palabras para ver si cumple el prefijo
        n_excepciones = 0
        # Busca el prefijo comparando con las otras palabras
        for candidato in lista:
            # Si el candidato es palabra y no ha aparecido
            if candidato == palabra and n_excepciones == 0:
                n_excepciones += 1
                continue
            # Si se encuentra el prefijo
            elif prefijo[0] == candidato[0]:
                prefijo_valido = 1
                prefijo[0] = palabra[:len(prefijo[0])+1]
                break
            # No se encontro prefijo usando palabra como candidato
            else:
                prefijo_valido = 0

        # En caso de que no se encontrara prefijo con las demas palabras,
        # se borra el prefijo actual
        if prefijo_valido == 0:
            prefijo = []

    if prefijo:
        # Aumentamos el prefijo en una palabra
        posible = 1
        # Mientras pueda existir un prefijo mas grande:
        while posible:
            n_excepciones = 0
            # En caso de que el prefijo sea de la misma longitud que
            # la palabra se sale
            if len(prefijo[0]) == len(palabra) and prefijo_valido == 0:
                posible = 0
                continue
            # Busca el prefijo comparando con las otras palabras
            for candidato in lista:
                bandera = candidato[:len(prefijo[0])]
                # Si el candidato es palabra y no ha aparecido
                if candidato == palabra and n_excepciones == 0:
                    n_excepciones += 1
                    continue
                # Si se encuentra el prefijo

                elif prefijo[0] == candidato[:len(prefijo[0])]:
                    prefijo_valido = 1
                    posible = 1
                    break
                # No se encontro prefijo usando palabra como candidato
                elif len(candidato) < len(prefijo[0]):
                    prefijo_valido = 0
                    posible = 0
                    continue

                else:
                    prefijo_valido = 0
                    posible = 0

                if prefijo[0] == candidato:
                    prefijo_valido = 1
                    posible = 0
                    continue

                if prefijo[0] == candidato:
                    break
            # Si el prefijo que se intento no es valido se regresa al prefijo
            # anterior
            if not prefijo_valido:
                prefijo[0] = palabra[:len(prefijo[0])-1]
            # Agrega una letra al prefijo en caso de que el prefijo
            # intentado sea valido
            elif len(prefijo[0])+1 <= len(palabra):
                prefijo[0] = palabra[:len(prefijo[0])+1]
            else:
                break
        # Agregamos el posible prefijo
        prefijos_finales.append(prefijo[0])
        prefijo = []

# Limpia los prefijos finales para dejar prefijos validos
if len(prefijos_finales) > 0:
    prefijos_finales.sort()

    for n in range(len(prefijos_finales)-1):
        if prefijos_finales[0] in prefijos_finales[1]:
            prefijos_finales.pop(0)

    print(prefijos_finales)
else:
    print("No existe el prefijo")
