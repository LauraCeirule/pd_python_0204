def celsijs_uz_farenheitu(Celsija):  #Pārveido no celsija grādiem uz fārenheita grādiem
  return (Celsija * 9/5) + 32

def farenheitu_uz_celsijs(farenheitu): #Pārveido no fārenheita grādiem uz celsija grādiem
  return (farenheitu - 32) * 5/9

temperatuura = "Ievadi temperatūru:"
print(temperatuura)
  
temperatura = float(input())
print("Ievadi norādītās temperatūras mērvienību (C/F):") #Jautā sākotnējo temperatūras mērvienību

mervieniba = input()


if mervieniba == "C":
    result = celsijs_uz_farenheitu(temperatura)
    print(f"{temperatura} Celsija grādi ir {result} Fārenheita grādi.") 
    
elif mervieniba == "F":
  result = farenheitu_uz_celsijs(temperatura)
  print(f"{temperatura} Fārenheita grādi ir {result} Celsija grādi.")
  
else:
  print("Nepareiza mērvienība. Lūdzu sāc no jauna un ievadi 'C' vai 'F'.")


