from fastapi import FastAPI,HTTPException
from pydantic import BaseModel , Field
import requests
app = FastAPI()

URL_FRUITYVICE = "https://www.fruityvice.com/api/fruit"

SUCOS: dict[int, dict] = {}

class SucoUpdate(BaseModel):
    frutas: list[str] = Field(min_length=1)
    
class SucoCreate(BaseModel):
    nome: str
    frutas: list[str] = Field(min_length=1)
    tem_gosto_de: str
    

@app.get("/frutas/{nome}")
def buscar_fruta(nome: str):
    return consultar_fruta(nome)

def consultar_fruta(nome: str):
    resposta = requests.get(f"{URL_FRUITYVICE}/{nome}")

    if resposta.status_code == 404:
        raise HTTPException(
            status_code=404,
            detail=f"a fruta {nome} nao foi encontrada"
        )
    resposta.raise_for_status()
    dados = resposta.json()

    return {
        "nome": dados["name"],
        "calorias": dados["nutritions"]["calories"],
        "açucar": dados["nutritions"]["sugar"]
    }
    
def calcular_totais(frutas: list[str]):

    nutricoes = [consultar_fruta(f) for f in frutas]
    total_calorias = round(sum(n["calorias"] for n in nutricoes), 2)
    total_acucar = round(sum(n["açucar"] for n in nutricoes), 2)
    return total_calorias, total_acucar



@app.post("/sucos", status_code=201)
def criar_suco(dados: SucoCreate):
    total_calorias, total_acucar = calcular_totais(dados.frutas)

    novo_id = max(SUCOS.keys(), default=0) + 1
    suco = {
        "id": novo_id,
        "nome": dados.nome,
        "frutas": dados.frutas,
        "tem_gosto_de": dados.tem_gosto_de,
        "total_calorias": total_calorias,
        "total_acucar": total_acucar
    }
    SUCOS[novo_id] = suco

    return suco


@app.get("/sucos")
def listar_sucos():
    return list(SUCOS.values())

@app.put("/sucos/{id}")
def atualizar_suco(id: int, dados: SucoUpdate):
    suco = SUCOS.get(id)
    if suco is None:
        raise HTTPException(
            status_code=404,
            detail=f"o suco {id} nao foi encontrado"
        )

    total_calorias, total_acucar = calcular_totais(dados.frutas)

    suco["frutas"] = dados.frutas
    suco["total_calorias"] = total_calorias
    suco["total_acucar"] = total_acucar

    return suco