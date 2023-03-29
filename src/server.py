from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
from pydantic import BaseModel


app = FastAPI()


origins = [
     'http://localhost:5500',
     'http://127.0.0.1:5500'
]


app.add_middleware(
     CORSMiddleware,
     allow_origins=origins,
     allow_credentials=True,
     allow_methods=['*'],
     allow_headers= ['*']
)


id_base = 0

def idBase():
    global id_base
    id_base += 1
    return id_base


class Animal(BaseModel):
    id: Optional[int]
    nome: str
    idade: int
    sexo: str
    cor: str
    
banco: List[Animal] = []


@app.get('/animais')
def listar_animais():
    return banco


@app.get('/animais/{animal_id}')
def obter_animais(animal_id: int):
        for animal in banco:
             if animal.id == animal_id:
                  return animal
                          
        return {'mensagem': 'ID não encontrado'} 


@app.delete('/animais/{animal_id}')
def remover_animal(animal_id: int):
    posicao = -1
    # buscar a posição do animal
    for index, animal in enumerate(banco):
        if animal.id == animal_id:
            posicao = index
            break

    if posicao != -1:
        banco.pop(posicao)
        return {'mensagem': 'Animal removido com sucesso'}
    else:
        return {'mensagem': 'ID não encontrado'}  


@app.post('/animais')
def criar_animais(animal: Animal):
    animal.id = idBase()
    banco.append(animal)
    return None
