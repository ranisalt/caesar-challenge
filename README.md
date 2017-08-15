# Caesar Challenge
Um de nossos desenvolvedores estava estudando sobre Cifra de César e resolveu aplicá-lo no nosso algoritmos para gerar chaves de APIs.
Mas, no meio dos seus estudos, acabou não prestando atenção e modificou todas as chaves de API do nosso banco de dados!<br/>
Infelizmente, ele não lembra o algoritmo que usou, mas sabemos que toda chave de API depois de descriptografada contém um texto legível como por exemplo `TresPratosDeTrigoParaTresTigresTristes`<br/>
Para gerar sua API_KEY, basta fazer um GET na rota x.com/register usando seu e-mail como parâmetro:
```
  GET /register?email=teste@teste.com HTTP/1.1
  Host: x.com
```
Que você receberá sua chave de API criptografada

Sua missão é descriptografá-la para conseguir fazer login em nossos sistemas e avisar o resto da equipe como resolver.
Após fazer o login, você receberá o email de contato da equipe, junto com as instruções dos próximos passos.

Para fazer login no sistema, basta fazer um POST na rota x.com/login usando seu email e chave de API como parâmetros:
```
POST /login HTTP/1.1
Host: x.com
Content-Type: application/json
{ 
    "email": "teste@teste.com", 
    "api_key": "API_KEY_TresPratosDeTrigoParaTresTigresTristes"
}
```
