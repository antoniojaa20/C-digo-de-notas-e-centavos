dinheiro = float(input())

#NOTAS

notasde100 = dinheiro // 100
dinheiro = dinheiro - notasde100 * 100

notasde50 = dinheiro // 50
dinheiro = dinheiro - notasde50 * 50

notasde20 = dinheiro // 20
dinheiro = dinheiro - notasde20 *20

notasde10 = dinheiro // 10
dinheiro = dinheiro - notasde10 * 10

notasde5 = dinheiro // 5
dinheiro = dinheiro - notasde5 * 5

notasde2 = dinheiro // 2
dinheiro = dinheiro - notasde2 * 2

#MOEDAS

moedasde100 = dinheiro // 1
dinheiro = dinheiro - moedasde100 * 1
dinheiro = float("%.2f" % dinheiro)

moedasde50 = dinheiro // 0.50
dinheiro = dinheiro - moedasde50 * 0.50
dinheiro = float("%.2f" % dinheiro)

moedasde25 = dinheiro // 0.25
dinheiro = dinheiro - moedasde25 * 0.25
dinheiro = float("%.2f" % dinheiro)

moedasde10 = dinheiro // 0.10
dinheiro = dinheiro - moedasde10 * 0.10
dinheiro = float("%.2f" % dinheiro)

moedasde5 = dinheiro // 0.05
dinheiro = dinheiro - moedasde5 * 0.05
dinheiro = float("%.2f" % dinheiro)

moedasde1 = dinheiro / 0.01

print('NOTAS:')
print('%d nota(s) de R$ 100.00'% notasde100)
print('%d nota(s) de R$ 50.00'% notasde50)
print('%d nota(s) de R$ 20.00'% notasde20)
print('%d nota(s) de R$ 10.00'% notasde10)
print('%d nota(s) de R$ 5.00'% notasde5)
print('%d nota(s) de R$ 2.00'% notasde2)
print('MOEDAS:')
print('%d moeda(s) de R$ 1.00'% moedasde100)
print('%d moeda(s) de R$ 0.50'% moedasde50)
print('%d moeda(s) de R$ 0.25'% moedasde25)
print('%d moeda(s) de R$ 0.10'% moedasde10)
print('%d moeda(s) de R$ 0.05'% moedasde5)
print('%d moeda(s) de R$ 0.01'% moedasde1)
