# sistema-de-inventario
# programa de auditoria para controlar el stock minimo y reabastecer inventario
# elmis mauricio porras santiago 
# 1064842767

# --- logica del negocio ---
def determinar_cantidad_a_pedir (stock_actual, stock_minimo):
 """
    determinar la cantidad de mercancia a pedir.
    sigue la logica: si esta por agotarse, se solicita realizar el pedido.
    de lo contrario, no se encarga y pasa arevisar el sigiente producto.
    """
 if stock_actual < stock_minimo:
  return stock_minimo - stock_actual
 else:
    return 0    
# --- programa principal ---
def main():
  # matriz de los productos
  # estructura de cada producto: [codigo, nombre del producto, stock actual, stock minimo]
  inventario = [
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
    [115, "gabetero plastico", 50, 51]
  ]

# =============================================================================================
# solicitar datos del in ventario actual
# =============================================================================================
  print("=== ingresa la cantidad actual de cada producto ===")

    # recorido de la matriz para determinar la cantidad a pedir de cada producto
  for producto in inventario:
      # mejora: desempaquetadodirecto de la lista en variables(indice 0, 1, 2, 3)
      codigo, nombre, actual, minimo = producto
      print(f"\nproducto: {nombre}")
      while True:
        try:
          actual = int(input("ingrese la cantidad actual del producto: "))
          break
        except ValueError:
          print("error: solo es valido ingresar numeros enteros. intenta de nuevo.")
      # esto guarda el nuevo valor dentro de la matriz para que no se pierda
      producto[2] = actual

# ============================================================================================
# generar y mostrar la tabla de resultados completos
# ============================================================================================

  print("_"* 50)
  print("  listado de productos a pedir")
  print("_"* 50)
  print(f"| {'articulo':<28} | {'cantidad a pedir':<5}|")
  print("_"* 50)

    # Recorre la matriz ya actualizada y muestra todo de una vez
  for producto in inventario:
      codigo, nombre, actual, minimo = producto
      # llama al modulo (funcion) pasando los parametros para determinar la cantidad a pedir
      cantidad_solicitada = determinar_cantidad_a_pedir(actual, minimo)

      # requisito de salida: imprimir el nombre del producto y la cantidad a pedir
      #(¡sin comillas internas para que use las variables reales!)
      print(f"| {nombre:<28} | {cantidad_solicitada:<5}|")
  print("_" * 50)


if __name__ == "__main__":
  main()