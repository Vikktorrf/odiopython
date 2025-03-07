##fizz buzz en python
"""
kk tengo que seguir estudiando python, este problema ya lo hice como 5 veces XDDD y sigo teniendo el mismo problema con la primera condicional
ya que por alguna razon que desconozco lo sigo poniendo al ultimo cuando deberia ir primero, aca bn mensote pero algun dia se me quedara grabado
"""

for i in range(100):
    print("fizzbuzz" if i%5<1 and i%3<1 else "fizz" if i%3<1 else "buzz" if i%5<1 else i)
    pass
