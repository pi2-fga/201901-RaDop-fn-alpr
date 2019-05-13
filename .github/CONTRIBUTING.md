# Contribuindo com o projeto

Caso queira contribuir com o projeto, talvez seja uma boa ideia começar pelo [README](https://github.com/radar-pi/fn-alpr) para conhecer um pouco mais sobre nós.
Outro documento importante e que deve ser lido é o [Código de Conduta](https://github.com/radar-pi/git-docs/blob/master/docs/CODE_OF_CONDUCT.md).

Obrigado por contribuir! :tada::+1: Sua ajuda será recebida com muita gratidão!

## Como eu posso contribuir?

### Reportando um Bug

* Esse projeto segue um padrão de [_Issues_](https://github.com/radar-pi/git-docs/blob/master/.github/ISSUE_TEMPLATE.md). Logo, caso encontre um _bug_, verifique se ele não se encontra em um a das nossas _Issues_. Os bugs devem ser marcados com _tag (label)_ __bug__.

* Se o _bug_ encontrado não consta nas _Issues_, basta abrir uma [Nova _Issue_](https://github.com/radar-pi/fn-alpr/issues/new).

### Adicionando e/ou modificando alguma funcionalidade

* Primeiro verifique que não existe nenhuma [_Issue_](https://github.com/radar-pi/fn-alpr/issues) a respeito dessa modificação e/ou adição.

* Caso não exista, crie uma [Nova _Issue_](https://github.com/radar-pi/fn-alpr/issues/new). Dê um título significativo a ela, coloque uma descrição e pelo menos uma _label_.

* As mudanças devem ser submetidas através de [_Pull Requests_](https://github.com/radar-pi/fn-alpr/compare). Você pode encontrar mais sobre isso no [_Pull Requests Template_](https://github.com/radar-pi/git-docs/blob/master/.github/PULL_REQUEST_TEMPLATE.md).

## Padrão de _Commit_

### Por questões de padronização recomendamos que sigam nosso estilo de _commit_

* Os _commits_ devem ser todos em __inglês__;

* Ele deve conter um título curto e objetivo do que foi feito naquele _commit_;

* Após esse título, deve-se descrever, com um pouco mais de detalhes, todas as atividades executadas.

* Caso esteja trabalhando em com algum associado assine nos seus _commits_ os seus parceiros

__Exemplo:__

    Creating project community files (Título curto e objetivo)

    Adds project license (Descrição de uma das atividades)

    Adds project code of conduct file

    Adds project contributing file

    Adds project issue template file

    Adds projects pull request file

    Co-authored-by: Peter Parker <peter.parker@email.com> (Assinatura de parceria)

## Política de _Branches_

Tendo como meta manter a integralidade e confiabilidade do código do projeto foi proposta a utilização de política de _branches_.
Essa Política de _Branches_ deverá guiar os desenvolvedores na forma de organização de suas contribuições ao repositório.
__OBS__: A política de _branches_ foi idealizada para trabalhar em conjunto com a ferramenta do _git flow_, sua documentação e mais informações podem ser acessadas [aqui](https://github.com/nvie/gitflow).

* __master__ - _Branch_ principal do repositório onde será permitida somente a integração de software consolidado e testado. Essa _branch_ será exclusiva para a entrega de _realeases_, ou seja, um conjunto maior de funcionalidades que integram o software. Aqui estará a versão _**stable**_ do software.

* __develop__ - _Branch_ para integração de novas funcionalidades, onde será permitido a entrega das _features_ desenvolvidas e que estão em um estágio avançado de completude. Será a _branch_ base para o início do desenvolvimento das _features_ e da correção de _bugs_. Aqui também será feito o _merge_ das _releases_.

* __feature/<nome-da-feature>__ - _Branch_ utilizada para o desenvolvimento de novas _features_ do _backlog_. Caso a feature tenha sida proposta por uma _issue_ do repositório e aceita no _backlog_ o nome deverá conter o número da _issue_.
 Ex: `feature/1-<nome-da-nova-feature>` (Considerando que a _feature_ tenha sido solicitada na _issue_ #1)

* __bugfix/<nome-do-bug>__ - _Branch_ utilizada para corrigir _bugs_ de baixa/média urgência e que não estão presentes na _branch_ __master__. Caso o _bug_ tenha sido reportado por uma _issue_ do repositório o nome deverá conter o número da _issue_.
 Ex: `bugfix/1-<descrição-do-bug>` (Considerando que o _bug_ tenha sido reportado na _issue_ #1)

* __hotfix/<nome-do-bug>__ - _Branch_ utilizada para corrigir _bugs_ de alta urgência e que estão presentes na _branch_ __master__. Caso o _bug_ tenha sido reportado por uma _issue_ do repositório o nome deverá conter o número da _issue_.
 Ex: `hotfix/1-<descrição-do-bug>` (Considerando que o _bug_ tenha sido reportado na _issue_ #1)

* __release/<versão-da-release>__ - _Branch_ onde será feito os ajustes finais/_build_ antes da entrega de uma versão do produto de software. Constará no nome da _branch_ a versão da _release_ a ser entregue.

* __support/<tema-ou-natureza>__ - _Branch_ onde serão executadas tarefas de suporte relacionadas ao software, como elaboração de documentações, correções de natureza de gerência de configuração e etc.