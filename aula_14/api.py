from fastapi import FastAPI,HTTPException
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

