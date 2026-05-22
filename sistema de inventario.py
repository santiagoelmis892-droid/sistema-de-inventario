# sistema-de-inventario
# programa de auditoria para controlar el stock minimo y reabastecer inventario
# elmis mauricio porras santiago
# 1064842767
# grupo 161

CODIGO_IDX = 0
NOMBRE_IDX = 1
STOCK_ACTUAL_IDX = 2
STOCK_MINIMO_IDX = 3

# --- logica del negocio ---
def determinar_cantidad_a_pedir(stock_actual: int, stock_minimo: int) -> int:
    """Determina la cantidad de mercancía a pedir."""
    return max(0, stock_minimo - stock_actual)


def obtener_entero_valido(prompt: str, minimo: int = 0) -> int:
    while True:
        texto = input(prompt).strip()
        if not texto:
            print("Error: debe ingresar un número.")
            continue

        try:
            valor = int(texto)
        except ValueError:
            print("Error: ingrese un número entero válido.")
            continue

        if valor < minimo:
            print(f"Error: el valor debe ser mayor o igual a {minimo}.")
            continue

        return valor


def crear_inventario():
    return [
        [101, "colchon 140*30", 10, 10],
        [102, "somier + espaldar 140", 5, 9],
        [103, "sillas allure", 100, 200],
        [104, "mesa plastica", 50, 40],
        [105, "ventilador de pedestal", 100, 60],
        [106, "colcha española 140", 100, 50],
        [107, "lavadora semiautomatica", 20, 30],
        [108, "refrigerador star 200 litros", 15, 10],
        [109, "televisor 40 pulgadas", 5, 5],
        [110, "licuadora vaso de vidrio", 150, 100],
        [111, "freidora de aire", 30, 30],
        [112, "mecedora de hierro", 20, 22],
        [113, "closet palermo", 10, 9],
        [114, "vajilla de ceramica", 80, 79],
        [115, "gabetero plastico", 50, 51],
    ]


def actualizar_stock_actual(inventario):
    print("=== ingresa la cantidad actual de cada producto ===")

    for producto in inventario:
        codigo = producto[CODIGO_IDX]
        nombre = producto[NOMBRE_IDX]
        print(f"\nProducto: {nombre} (código {codigo})")
        producto[STOCK_ACTUAL_IDX] = obtener_entero_valido(
            "ingrese la cantidad actual del producto: ", minimo=0
        )


def imprimir_reporte(inventario):
    print("_" * 60)
    print("  listado de productos a pedir")
    print("_" * 60)
    print(f" |{'codigo':<8} | {'articulo':<28} | {'cantidad a pedir':<12} | ")
    print("_" * 60)

    for producto in inventario:
        codigo = producto[CODIGO_IDX]
        nombre = producto[NOMBRE_IDX]
        actual = producto[STOCK_ACTUAL_IDX]
        minimo = producto[STOCK_MINIMO_IDX]
        cantidad_solicitada = determinar_cantidad_a_pedir(actual, minimo)
        print(f" | {codigo:<8} | {nombre:<28} | {cantidad_solicitada:<12} | ")

    print("_" * 60)


def main():
    inventario = crear_inventario()

    try:
        actualizar_stock_actual(inventario)
    except KeyboardInterrupt:
        print("\nEjecución interrumpida por el usuario.")
        return

    imprimir_reporte(inventario)


if __name__ == "__main__":
    main()