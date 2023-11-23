# LinkedIn Recruiter Connection

`Esse projeto foi feito em alguns minutos para relembrar como usar Selenium.
Sinta-se à vontade para corrigir os defeitos, e aplicar boas práticas.`

Este é um projeto Python que utiliza a biblioteca Selenium para automatizar a interação com o LinkedIn, permitindo a
conexão com recrutadores de forma automatizada.

Nota: Este projeto é apenas um exemplo educacional, e é importante usar automação com responsabilidade e dentro dos
termos de uso do LinkedIn para evitar ações que possam violar as políticas da plataforma.

# Requisitos

- Python 3
- Poetry

# Instalação

- Clone esse repositório:

```shell
git clone https://github.com/uricholiveira/Linkedin.Automation.git
```

- Na pasta raiz, instale as dependências do projeto com:

```shell
poetry install
```

- Altere o **.env-example** para **.env**, e substitua as variáveis de ambiente.

- Rode o projeto com:

```shell
python main.py
```

# Próximos Passos
- [ ] Utilizar Typer.CLI no projeto
- [ ] Adicionar os parâmetros de busca de forma dinâmica (Exemplo: região, hashtags, etc)
- [ ] Adicionar um banco de dados local
- [ ] Validar o envio de mensagens duplicadas (não enviar para uma pessoa que já recebeu)