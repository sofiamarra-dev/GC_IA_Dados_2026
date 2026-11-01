from fastapi import FastAPI,HTTPException
from pydantic import BaseModel , Field
import requests
app = FastAPI()

URL_FRUITYVICE = "https://www.fruityvice.com/api/fruit"

@app.get("/frutas/{nome}")
def buscar_fruta(nome:str):
   return consultar_fruta(nome)

def consultar_fruta(nome:str):
    resposta = requests.get(f"{URL_FRUITYVICE}/{nome}") 
  
    if resposta.status_code == 404:
        raise HTTPException (
            status_code = 404,
            detail = f"a fruta {nome} nao foi encontrada"
        )
    resposta.raise_for_status()
    dados = resposta.json()
    
    return {
        "nome":dados["name"],
        "calorias":dados["nutritions"]["calories"],
        "açucar":dados["nutritions"]["sugar"]
    }

SUCOS : dict[int,dict] = {
    1:{
        "id": 1 ,
        "nome":"Obscur",
        "frutas":["banana" ,"lemon"],
        "tem_gosto_de": "Amora com limão",
        "total_calorias": 150,
        "total_acucar" :15.4
        
        
    }
}
class SucoUpdate(BaseModel):
    frutas:list[str] = Field(min_length=1)
    
@app.put("/sucos/{id}")
def atulizar_suco(id:int, dados:SucoUpdate):
    suco = SUCOS.get(id)
    if suco is None :
        raise HTTPException(
            status_code= 404,
            detail = f"o suco {id} nao foi encontrado "
            
        )
    frutas = dados.frutas
    nutricoes = [consultar_fruta(f) for f in frutas] 
    suco["frutas"] = frutas
    suco["total_calorias"] = round(sum(n["calorias"] for n in nutricoes), 2)
    suco["total_acucar"] = round(sum(n["açucar"] for n in nutricoes), 2)
    return suco 