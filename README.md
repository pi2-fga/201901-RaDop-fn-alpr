# FN-ALPR

[![Build Status](https://travis-ci.org/radar-pi/fn-alpr.svg?branch=develop)](https://travis-ci.org/radar-pi/fn-alpr)

[![Maintainability](https://api.codeclimate.com/v1/badges/e9d5767289e175c0cb18/maintainability)](https://codeclimate.com/github/radar-pi/fn-alpr/maintainability)

[![Test Coverage](https://api.codeclimate.com/v1/badges/e9d5767289e175c0cb18/test_coverage)](https://codeclimate.com/github/radar-pi/fn-alpr/test_coverage)

A **Função ALPR** é a função responsável por tratar as imagens recebidas do radar e enviar à API do ALPR para que seja feito o reconhecimento (_OCR_) dos caracteres da placa. Logo com o dado enviado para este serviço será retornado um relatório com as placas encontradas na imagem.

## Parâmetros

Os parâmetros da função fn-alpr seguem o modelo de dados do pacote (_package_) de mensagens da arquitetura do sistema do radar. Eles consistem em um objeto JSON com o seguinte formato:

- **id**: Um UUID para identificar unicamente aquele pacote (tipo `string`).

- **type**: Qual o tipo da chamada de função, para que a função possa identificar se o pacote que ele recebeu é do seu domínio. Para a função ALPR só serão aceitos pacotes com a chave `alpr-call` (tipo `string`).

- **payload**: Será um outro objeto JSON com o conteúdo da mensagem (tipo `dict`).

    - **key**: A chave encriptada em base64 para a chamada na API do ALPR (tipo `string`).

    - **image**: A imagem encriptada em base64 para envio. Esta que será decodificada, pré-processada e enviada para a API do ALPR (tipo `string`).

- **time**: O dia e horário em que essa mensagem foi enviado no formato RFC3339, ou seja, `YYYY-MM-DDTHH:MM:SSZ` (tipo `string`).

__Exemplo__:

```json
{
  "id": "44b314eb-b67d-4b4f-b744-4772c5954601",
  "type": "alpr-call",
  "payload": {
    "key": "base64-encoded-key",
    "image": "base64-encoded-image"
  },
  "time": "2019-04-27T10:14:35Z"
}
```

## Tecnologias Utilizadas

- Plataforma OpenFaaS
    - _Self-Hosted_ Function as a Service
- Python 3
- JSON
- ALPR

## Ambiente de Desenvolvimento

Recomendado o uso de OpenFaaS local em Docker Swarm.

O guia para criar o ambiente local está disponível [na seção de _Deployment_ da documentação do OpenFaaS](http://docs.openfaas.com/deployment/docker-swarm/).

Editor de texto de preferência.

## Ambiente de Teste Local

Recomendados a utilização de um ambiente virtual criado pelo módulo `virtualenvwrapper`.
Existe um sítio virtual com instruções em inglês para a instalação que pode ser acessado [aqui](https://virtualenvwrapper.readthedocs.io/en/latest/install.html). Mas você pode também seguir o roteiro abaixo para a instalação do ambiente:

```shell
python3 -m pip install -U pip # Faz a atualização do pip
python3 -m pip install virtualenvwrapper # Caso queira instalar apenas para o usuário use a opt --user
```

Agora configure o seu shell para utilizar o virtualenvwrapper, adicionando essas duas linhas ao arquivo de inicialização do seu shell (`.bashrc`, `.profile`, etc.)

```shell
export WORKON_HOME=$HOME/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh
```

Caso queira adicionar um local específico de projeto basta adicionar uma terceira linha com o seguinte `export`:

```shell
export PROJECT_HOME=/path/to/project
```

Execute o arquivo de inicialização do shell para que as mudanças surtam efeito, por exemplo:

```shell
source ~/.bashrc
```

Agora crie um ambiente virtual com o seguinte comando (colocando o nome que deseja para o ambiente), neste exemplo usarei o nome composta:

```shell
mkvirtualenv fn-alpr
```

Para utilizá-lo:

```shell
workon fn-alpr
pip install -r compiler/requirements.txt # Irá instalar todas as dependências usadas no projeto
```

**OBS**: Caso o sua variável de ambiente *PROJECT_HOME* esteja _setada_ ao executar o `workon` você será levado para o diretório lá configurado.

Para outras configurações e documentação adicional acesse a página do [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/).

## Deploy Local para Desenvolvimento

Para deploy da função, basta seguir o roteiro abaixo:

```shell
$ faas build -f fn-alpr.yml
$ faas deploy -f fn-alpr.yml
```

Para utilizá-lo, teste pela interface web no endereço definido, chamar pela CLI, ou por requisição HTTP:

FaaS CLI:

```shell
$ echo $'{\n  "id": "44b314eb-b67d-4b4f-b744-4772c5954601",\n  "type": "alpr-call",\n  "payload": {\n    "key": "base64-encoded-key",\n    "image": "base64-encoded-image"\n  },\n  "time": "2019-04-27T10:14:35Z"\n}' | faas-cli invoke fn-alpr

HTTP-Request:

```shell
$ curl -d $'{\n  "id": "44b314eb-b67d-4b4f-b744-4772c5954601",\n  "type": "alpr-call",\n  "payload": {\n    "key": "base64-encoded-key",\n    "image": "base64-encoded-image"\n  },\n  "time": "2019-04-27T10:14:35Z"\n}' -X POST http://127.0.0.1:8080/function/fn-alpr
```

Exemplo de saída:

```shell
{"status_code": 200, "response": {"uuid": "85946387-d2f2-468d-96a5-6c71d0fa4a81", "data_type": "alpr_results", "epoch_time": 1557190354549, "processing_time": {"plates": 398.9972229003906, "total": 460.6129999883706}, "img_height": 1080, "img_width": 1440, "results": [{"plate": "AAA1234", "confidence": 93.51219940185547, "region_confidence": 42, "vehicle_region": {"y": 141, "x": 247, "height": 417, "width": 417}, "region": "br-sp", "plate_index": 0, "processing_time_ms": 73.81824493408203, "candidates": [{"matches_template": 1, "plate": "AAA1234", "confidence": 93.51219940185547}, {"matches_template": 0, "plate": "AAA1234", "confidence": 80.09203338623047}, {"matches_template": 0, "plate": "AAA1234", "confidence": 80.0918197631836}, {"matches_template": 1, "plate": "AAA1234", "confidence": 79.95366668701172}, {"matches_template": 1, "plate": "AAA1234", "confidence": 79.9520263671875}, {"matches_template": 0, "plate": "AAA1234", "confidence": 66.6716537475586}, {"matches_template": 0, "plate": "AAA1234", "confidence": 66.53350067138672}, {"matches_template": 0, "plate": "AAA1234", "confidence": 66.53164672851562}, {"matches_template": 1, "plate": "PAE7788", "confidence": 66.39348602294922}], "coordinates": [{"y": 401, "x": 399}, {"y": 400, "x": 511}, {"y": 437, "x": 512}, {"y": 438, "x": 400}], "matches_template": 1, "requested_topn": 10}], "credits_monthly_used": 5, "version": 2, "credits_monthly_total": 2000, "error": false, "regions_of_interest": [{"y": 0, "x": 0, "height": 1080, "width": 1440}]}}
```

## Execução do Ambiente de Testes

Para executar os testes do fn-alpr siga o roteiro descrito abaixo:

Primeiro assegure-se de que tem todas as dependências necessárias para executar o projeto.

```shell
$ pip install -r fn-alpr/requirements.txt
# Ou caso não esteja trabalhando com uma virtualenv
$ python3 -m pip install -r fn-alpr/requirements.txt
```

**OBS**: Caso queria instalar apenas para o usuário e não no sistema use a opt `--user` ao final do comando pip.

Agora que todas as dependências estão instaladas basta rodar o comando do pytest para verificar se o código está de acordo com o teste.

```shell
$ pytest fn-alpr/ # Executa os testes no pytest
$ py.test --cov=fn-alpr fn-alpr/ # Executa os testes e avalia a cobertura estática de código
$ py.test --cov=fn-alpr --cov-report html fn-alpr/ # Faz o mesmo papel que o comando anterior, além de gerar uma pasta htmlcov/ com uma página relatório da cobertura
$ flake8 fn-alpr/* # Executa o PEP8 linter nos arquivos python
```

Durante o `pytest` e o `py.test`, o terminal lhe apresentará um _output_ com o relatório dos testes e a cobertura de testes da aplicação. Para outras configuraões e documentação complementar acesse o sítio virtual do provedor do [pytest](https://docs.pytest.org/en/latest/) e do [coverage](https://pytest-cov.readthedocs.io/en/latest/).

Durante o `flake8`, o terminal lhe apresentará um relatório com os erros e _warnings_ do guia de estilo PEP8 do python, para demais configurações e documentações você pode acessar o sítio do [flake8](http://flake8.pycqa.org/en/latest/index.html) ou visualizar o estilo do [PEP8](https://www.python.org/dev/peps/pep-0008/).