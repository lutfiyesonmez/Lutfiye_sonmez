# Fill in this file with the code from parsing JSON exercise
import json
dosya=open("lutfiye.json","r")
json_dosya=json.load(dosya)
print("ADINIZ : ",json_dosya["kimlik"]["ad"])
print("SOYADINIZ : ",json_dosya["kimlik"]["soyad"])
print("KIMLIGINIZ  : ",json_dosya["kimlik"])
