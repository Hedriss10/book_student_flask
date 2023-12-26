## Flask: Um Microframework Simples e Poderoso

### Primeiros Passos

Descobri que posso criar funções e renderizá-las no HTML de maneira simples e descomplicada com o Flask. Isso é bastante diferente do Django, que antes parecia confuso e não fazia sentido para mim. Também aprendi a realizar conexões com classes, instanciando objetos de forma simples. Além disso, compreendi como lidar com requisições de formulários, tanto através de `GET` quanto `POST`, renderizando em rotas específicas.

### Arquivos Estáticos

Aprendi a renderizar arquivos estáticos no Flask. O microframework reconhece a pasta `templates` para arquivos `.HTML` e, da mesma forma, para arquivos estáticos como `.css` e `.js`, ele os processa na pasta `static`.

**Dica:** É sempre útil criar um arquivo `base.html` que servirá de esqueleto para outros arquivos `.html`.

Aprofundei meu conhecimento em:

- Redirecionamento de páginas usando a função `redirect()`.
- Utilização do Bootstrap para estilizar páginas.
- Reutilização de trechos de template.
- Geração de URLs dinâmicas.

### Tratamento de Usuários

Aprendi a tratar a conexão e desconexão de usuários no site, bem como a manipular alertas no site usando os recursos `flash` e `session` do Flask, que utilizam cookies do navegador. Também descobri como passar o loop `for` para encontrar o diretório de arquivos estáticos, utilizando o comando `url_for({ "static", filename="css/bootstrap.css" })`.

Flask, além de ser mais fácil de usar para desenvolver pequenos projetos, mostra-se robusto e intuitivo, inclusive ao trabalhar com ORMs.


## ORM e SQLAlchemy 


Ao decorrer do tempo o termo de ``SQLAlchemy`` que vem da extensão do ``Flask`` que no caso é o ``ORM`` que é (Orientado, Relacional, Mapeado)