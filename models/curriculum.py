from pydantic  import BaseModel

class Curriculum(BaseModel):
        nome:str
        cargo:str
        idade:int

        def to_dict(self):
            return {"nome": self.nome, "cargo": self.cargo, "idade": self.idade}



