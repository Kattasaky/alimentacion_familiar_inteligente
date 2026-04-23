def calcular_nutrientes_plato(plato):
    total = {
        "energia": 0,
        "grasas": 0,
        "carbohidratos": 0,
        "proteinas": 0,
        "sodio": 0,
        "azucar": 0,
    }

    for ingrediente in plato.ingrediente_set.all(): #recorremos los ingredientes del plato
        alimento = ingrediente.alimento #conexion de ingrediente con alimento
        gramos = ingrediente.cantidad_gramos or 0

        # cálculo proporcional
        total["energia"] += (alimento.energia or 0) * gramos / 100
        total["grasas"] += (alimento.grasas or 0) * gramos / 100
        total["carbohidratos"] += (alimento.carbohidratos or 0) * gramos / 100
        total["proteinas"] += (alimento.proteinas or 0) * gramos / 100
        total["sodio"] += (alimento.sodio or 0) * gramos / 100
        total["azucar"] += (alimento.azucar or 0) * gramos / 100

    return total

def generar_alertas(nutrientes, persona=None):
    alertas = []

    # 🚨 Ejemplo: hipertensión
    if nutrientes["sodio"] > 200:
        alertas.append("⚠️ Alto en sodio")

    # 🚨 Ejemplo: azúcar (hígado graso / ansiedad)
    if nutrientes["azucar"] > 25:
        alertas.append("🍬 Alto en azúcar")

    return alertas