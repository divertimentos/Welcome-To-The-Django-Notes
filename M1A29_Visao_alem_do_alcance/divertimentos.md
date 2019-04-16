# M1A29: Visão além do alcance

* ## Mindset:
  * A melhor pergunta é "Qual é o seu problema?"/"O que você não consegue fazer?", em vez de "o que você precisa?". E é verdade. O cliente não necessariamente sabe do que ele precisa.
  * Ciclo de feedback curto:
    * O prazo já é algo dado; a qualidade já é intrínseca ao trabalho do programador; a única variável importante é o escopo.
    * Estimativas só fazem sentido prático para projetos longos, como projetos de 6 meses, por exemplo.
    * É dos fatos concretos que você extrai projeções, e não de estimativas

* ## **Live Software**
  * Projeto embrionário: tudo nasce pequeno.

  * Execução de ponta a ponta: em vez de criar partes do sistema, criar um MVP que atenda minimamente aos requisitos iniciais do cliente

  * ### **Decida apenas o necessário:**
    * O código precisa ser feito para ser refatorado sempre que precisar
    * "Não pode ser caro mudar o código. Se for caro mudar o código, a saúde do código vai decaindo com o tempo, com toda certeza." (HB)

  * ### **O fluxo revela a estrutura**
    * O banco de dados não é a coisa mais importante do sistema; o mais importante é o fluxo.
    * O fluxo é como o código é organizado: o que chamam o quê, para ir de ponta a ponta
    * Quando o fluxo funciona, implementar/incrementar coisas nele se torna mais fácil
    * Quando mais difícil está mudar o seu código, mais caro vai ser a manutenção

  * ### **A realidade revela a necessidade**

    * Embora o trabalho de desenvolvimento seja muito técnico em requeira muita atenção, nem sempre código é o mais importante. No caso da Morena, um Google Docs com o conteúdo que ela precisa mostrar seria mais importante do que um sistema inteiro construído em Django mas que só tivesse *lorem ipsum* como conteúdo
    * Fazer o código funcionar não é o suficiente
    * O grande prolema do mercao de desenvolvimento de software é o programador se comportar como custo, e não como investimento (HB)

* ## Programe como um chef

  * ###  Layout do projeto

    * O diretório de trabalho, fora do eventex, é parte do seu trabalho de modo geral
    * O diretório o projeto é onde estão as coisas que serão entregues a alguém
    * Se inspirar na organização de diretórios e arquivos do Unix

  * ### Aliases e comandos auxiliares

    * Importância da organização

    * A importância de ser preguiçoso para a implementação do DRY

    * Com o fluxo de trabalho ajustado é possível remover a necessidade de repetição

    * A sua máquina é a **sua máquina**. Ela está inteiramente customizada para a sua produtividade, para a forma como você funciona, para a forma como você pensa, para a forma como você aborda os problemas

    * Apenas otimize aquilo que você mede: mede o que acontece no presente e pode ser otimizado. Otimização precoce é um pecado.

    * PDCA: **P**lan, **D**o, **C**heck, **A**ct

    * Deixar o idealismo de lado para entregar resultados

    * ### Se tá difícil, tá errado

      * Se você tá brigando com a máquina, com o ambiente, com o servidor, com a sua cadeira etc., tá errado. Você não deve ter insumos entre você e o resultado

  ***

   ## Autonomation

  * Setup com 1 comando
    * Não depender de packages dos outros. O fork é seu amigo.

  ## Pronto é quando está NO AR

  A consolidação do projeto é colocar o código no ar.

  * ### 1 código para N instâncias

    * Inversão de dependência
    * Ter N instâncias do projeto para simplificar a criação de ambientes de homologação
    * [The Twelve-Factor App](https://12factor.net/pt_br/): as 12 características fundamentais de um software escalável.

  * ### Deploy tem risco arquitetural

    * Deploys no início do projeto são vantajosos para que se garanta que o projeto continue no ar do início ao fim
    * Se você coloca no software *na rua* já no começo, isso é valor para o cliente, pois ele percebe o valor do que está sendo feito desde sempre. Código, para quem não é desenvolvedor, é mato.

  * ### Simplicidade do deploy impacta a frequência

    * Keep it simple, stupid (KISS)
    * Encurtar o caminho entre ideias e a execução delas é um objetivo
    * Faça o necessário, não mais que o necessário
    * Não trabalhar pro medo, trabalhar pro valor do cliente

  * ### O Heroku é barato

    * 

  ## A arma secreta do Tony Stark

  
