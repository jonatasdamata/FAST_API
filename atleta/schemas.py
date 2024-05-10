from typing import Annoted
from pydantic import BaseModel, Field, PositiveFloat

class Atleta(BaseModel):
    nome: Annoted[str, Field(descreption='Nome do atleta', examples='Jhon', max_length=50)]
    cpf: Annoted[str, Field(descreption='CPF do atleta', examples='12345678900', max_length=11)]
    idade: Annoted[int, Field(descreption='Idade do atleta', examples='25')]
    peso: Annoted[PositiveFloat, Field(descreption='Peso do atleta', examples='75.5')]
    altura: Annoted[PositiveFloat, Field(descreption='Altura do atleta', examples='1.70')]
    sexo: Annoted[str, Field(descreption='Sexo do atleta', examples='M', max_length=1)]