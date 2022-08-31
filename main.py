from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI()

#Raiz
@app.get("/")
def raiz():
    return {"Olá": "Seja bemvindo a Guerra Galáctica"}

#Model

class Cavaleiro(BaseModel):
        id: int
        nome:str
        constelação:str
        armadura: str

#db

base_de_dados=[
    Cavaleiro(id=1,nome="Seiya",constelação="Pégasus",armadura="Bronze"),
    Cavaleiro(id=2,nome="Shiryu",constelação="Dragão",armadura="Bronze")
]

#Get All

@app.get('/cavaleiros')
def get_todos_os_cavaleiros():
    return base_de_dados

#Get Id

@app.get("/cavaleiros/{id_cavaleiro}")
def get_cavaleiro_usando_id(id_cavaleiro: int):
    for cavaleiro in base_de_dados:
        if(cavaleiro.id == id_cavaleiro):
            return cavaleiro

    return {"Status": 404,"Mensagem":"Não encontrou cavaleiro"}

# Post

@app.post("/cavaleiros")
def insere_cavaleiro(cavaleiro: Cavaleiro):
    # criar regras de negócio
    base_de_dados.append(cavaleiro)
    return cavaleiro
