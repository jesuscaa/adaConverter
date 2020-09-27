monedas = {"Dolar": 22.49, "AdaDolar":  0.131893, "Bitcoin":  207460.37}
userMonedas= {"pesos", "dolares", "adas", "euros"}



#input de usuarios
userMon= input ("¿Cual es su moneda local? ").upper()
userCon= input ("¿Que moneda desea comprar?").upper()



#if funcition

#Ada a pesos mexicanos
if userMon == "ADAS" and userCon == "PESOS" :
    a= int(input("¿Cuantas ADAs tienes? "))
    aP= a * monedas["Dolar"] * monedas["AdaDolar"]
    aP= str(aP)
    respuesta= ("Con sus {} Adas comprarira {} pesos".format(a, aP))
    print (respuesta)

#Pesos mexicanos a adas    
elif userMon == "PESOS" and userCon == "ADAS":
      
    p= int(input("¿Cuantos pesos tiene? "))
    pA= ((p/monedas["Dolar"])/ monedas["AdaDolar"])
    print("Con sus {} pesos mexicanos compraria {} adas".format(p,pA))
#Pesos a dolares
elif userMon == "PESOS" and userCon == "DOLARES":
    pesos= int(input("¿Cuantos pesos quieres cambiar? "))   
    pD= pesos/monedas["Dolar"]
    print("Con tus {} comprarias {} dolares".format(pesos,pD))





