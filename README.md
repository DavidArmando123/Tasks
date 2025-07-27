Criei um gerenciador de tasks onde é possivel cadastrar usuário, fazer login com JWT, cadastrar taks, listar, atualizar e eliminar.

Eis as rotas 

(user/) - POST. rota para criar ou cadastrar usuário
   {
  "username": "teu_username",
  "email":"seu_@email"
  "password": "tua_senha"
}

(tarefas/) - GET, POST, PUT, DELETE essa rota permite tanto criar e listar e como também atualizar e eliminar, tudo de acordo as possibilidades do Django.

  {
  "titulo": "Estudar Django",
  "descricao": "Ver vídeos e praticar",
  "status": "pendente",
  "data_vencimento": "2025-08-01"
}


(token/) - POST. Rota para efetuar o login e obter o acess e o refresh token 

  {
  "username": "teu_username",
  "password": "tua_senha"
}

(token/refresh/) para refresh token.

Foi isto que eu pude fazer.