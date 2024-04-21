from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base      # --> Declaraçao de Base.
from sqlalchemy import Column, String, Integer        # --> Declarar Colunas
from sqlalchemy.orm import sessionmaker         # --> Query ORM

# Configuraçoes.
engine = create_engine('mysql+pymysql://root:@localhost:3306/cinema')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


# Entidades (Mapeamento declarativo)
class Filmes(Base):
    __tablename__ = "filmes"

    titulo = Column(String, primary_key=True)
    genero = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)

    def __repr__(self):
        return f'Filmes -->  [titulo: {self.titulo}, genero: {self.genero}, Ano: {self.ano}] \n '


# QUERY ( colocar registro no banco de dados )




# Insert
data_insert = Filmes(titulo = "Coringa", genero = "drama", ano=2019)
session.add(data_insert)
session.commit()  # sempre Commit() no fim de uma chamada


#Delete
session.query(Filmes).filter(Filmes.titulo == "the mummy").delete()
session.commit()


#Update
session.query(Filmes).filter(Filmes.genero == "drama").update({"ano": 2018}) # atualizando para ano 2018
session.commit()




# Select
data = session.query(Filmes).all()

print(data)
print(data[0].genero)






# mais cuidado com o banco de dados (fechando)
session.close()








