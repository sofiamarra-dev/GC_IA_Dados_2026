from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
 
app = FastAPI(title="API do Cardápio 🍔")
 
# Modelo: como um item do cardápio deve ser
class Item(BaseModel):
    nome: str
    preco: float
    categoria: str  # ex: lanche, bebida, sobremesa
    disponivel: bool = True
 
 
# "Banco de dados" em memória (um dicionário)
cardapio = {
    1: Item(nome="X-Burguer", preco=25.0, categoria="lanche"),
    2: Item(nome="Batata Frita", preco=15.0, categoria="acompanhamento"),
    3: Item(nome="Refrigerante", preco=7.5, categoria="bebida"),
}
 
 
@app.get("/")
def inicio():
    return {"mensagem": "Bem-vindo à API do Cardápio! Acesse /docs"}
 
 
# GET - listar todos (com filtro opcional por query parameter)
# Ex: /itens  ou  /itens?categoria=bebida
@app.get("/itens")
def listar_itens(categoria: str | None = None):
    if categoria:
        return {id: item for id, item in cardapio.items() if item.categoria == categoria}
    return cardapio
 
 
# GET - buscar um item (path parameter)
# Ex: /itens/1
@app.get("/itens/{item_id}")
def buscar_item(item_id: int):
    if item_id not in cardapio:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    return cardapio[item_id]
 
 
# POST - criar um item novo
@app.post("/itens", status_code=201)
def criar_item(item: Item):
    novo_id = max(cardapio.keys(), default=0) + 1
    cardapio[novo_id] = item
    return {"id": novo_id, "item": item}
 
 
# PUT - atualizar um item existente
@app.put("/itens/{item_id}")
def atualizar_item(item_id: int, item: Item):
    if item_id not in cardapio:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    cardapio[item_id] = item
    return {"id": item_id, "item": item}