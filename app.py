from fastapi import FastAPI
app = FastAPI()

lista_livros = []

@app.get("/livros")
def read_root():
    return lista_livros

@app.post("/livros")
def cadastrar_livro(livro:str):
    lista_livros.append(livro)
    return {"mensagem": "Livro cadastrado com sucesso"}

@app.delete("/livros")
def excluir_livro(livro:str):
    if livro in lista_livros:
        lista_livros.remove(livro)
        return {"mensagem": "Livro removido com sucesso"}
    else:
        return {"mensagem": "Livro não encontrado"}

@app.put("/livros")
def atualizar_livro(livro:str, livro_atualizado:str):
    if livro in lista_livros:
        lista_livros.remove(livro)
        lista_livros.append(livro_atualizado)
        return {"mensagem": "Livro atualizado com sucesso"}
    return {"mensagem": "Livro não encontrado"}