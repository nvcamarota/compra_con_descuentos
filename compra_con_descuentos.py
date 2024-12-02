"""
COMPRA CON DESCUENTOS
Escribir un programa en Python que solicite al usuario el monto total de la compra y la cantidad de artículos que está comprando. El programa debe determinar el descuento aplicable según las siguientes reglas:
1) Si la cantidad de artículos comprados es mayor o igual a 5 y el monto total es mayor a $10.000, aplica un descuento del 15%.
2) Si la cantidad de artículos comprador es menor a 5 pero mayor o igual a 3, aplica un descuento del 10%.
3) Si la cantidad de artículos comprados es menor a 3, no se aplica descuento.
Al final, el programa debe imprimir el monto total de la compra después de aplicar cualquier descuento o simplemente el monto original si no hay descuento.
"""

cantidad_articulos = int(input("Ingrese la cantidad de pulseras compradas: "))
monto = float(input("Ingrese el monto total a abonar por las pulseras: $"))

descuento = (monto * cantidad_articulos) / 100
monto_total = monto - descuento

if cantidad_articulos >= 5 and monto > 10000:
    print(f"Por la compra de {cantidad_articulos} pulseras, por un monto de ${monto:.2f}, te ofrecemos un descuento del %15, por lo que tu saldo total actualizado es de ${monto_total:.2f} \n ¡Gracias por tu compra!")
elif cantidad_articulos >= 3 and cantidad_articulos < 5:
    print(f"Por la compra de {cantidad_articulos} pulseras, por un monto de ${monto:.2f}, te ofrecemos un descuento del %10, por lo que tu saldo total actualizado es de ${monto_total:.2f}\n ¡Gracias por tu compra!")
else:
    print(f"Tu saldo total a abonar por {cantidad_articulos} pulseras es de ${monto:.2f}\n ¡Gracias por tu compra!")