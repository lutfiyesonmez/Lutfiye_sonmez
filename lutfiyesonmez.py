# Fill in this file with the code from parsing JSON exercise
import json
dosya=open("lutfiyesonmez.json","r")
json_dosya=json.load(dosya)
print("API_KEY : ",json_dosya["ad"])
print("API_KEY : ",json_dosya["soyad"])
print("API_KEY  : ",json_dosya["access_token"])
print("API_KEY : ",json_dosya["il"])
