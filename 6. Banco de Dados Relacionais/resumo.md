# Resumo sobre Banco de Dados

## Aprendendo SQL - Structured Query Language

### Conceitos Básicos
SQL é uma linguagem de consulta estruturada que permite a manipulação e gerenciamento de dados em bancos de dados.

### Tipos de Banco de Dados
- **Relacionais/SQL**
- **Não Relacionais/NoSQL**
- **Orientado a Objetos**
- **Hierárquico**

### Sistema de Gerenciamento de Banco de Dados (SGBD)
Um SGBD é responsável por gerenciar e organizar os dados, oferecendo funcionalidades como CRUD (Create, Read, Update, Delete).

### Estrutura de um Banco de Dados Relacional
Os bancos de dados relacionais são organizados em tabelas, que contêm colunas e linhas.

#### Chaves Primárias e Estrangeiras
- **Chave Primária**: Identifica de forma única cada registro.
- **Identificadores Estrangeiros**: Referenciam chaves primárias de outras tabelas.

### Características dos Bancos de Dados Relacionais
- Relacionamento entre tabelas
- Linguagem de consulta estruturada
- Integridade referencial
- Normalização de dados
- Segurança
- Flexibilidade e extensibilidade
- Suporte a transações ACID

### ACID
- **Atomicidade**: Todas as operações devem ser executadas com sucesso ou nenhuma é.
- **Consistência**: Garante que o banco de dados saia de um estado consistente para outro.
- **Isolamento**: Cada transação é executada isoladamente.
- **Durabilidade**: Alterações são permanentes após o commit.

### Organização da SQL
Dividida em:
- **DQL**: Linguagem de consulta de dados (ex. SELECT)
- **DML**: Linguagem de manipulação de dados (ex. INSERT, UPDATE, DELETE)
- **DDL**: Linguagem de definição de dados (ex. CREATE, ALTER, DROP)
- **DCL**: Linguagem de controle de dados (ex. GRANT, REVOKE)
- **DTL**: Linguagem de transformação de dados (ex. BEGIN, COMMIT, ROLLBACK)

### Sintaxe Básica
- Nomes devem começar com letra ou sublinhado (_).
- Podem conter letras, números e sublinhados.
- São case sensitive.

### Modelagem de Bancos de Dados Relacionais
O Modelo de Entidades e Relacionamento (MER) é representado por Diagramas Entidade Relacionamento (DER).

### Tabelas, Colunas e Linhas
As tabelas armazenam dados organizados em colunas (atributos) e linhas (registros).

#### Comando CREATE TABLE
Define colunas e restrições (unique, not null, etc.).

#### Tipos de Dados
- Integer
- Decimal
- String
- Outros

### Operações CRUD
- **INSERT**: Adiciona novos registros.
- **SELECT**: Recupera dados.

### Atomicidade de Dados - Formas Normais (1FN)
Cada valor em uma tabela deve ser atômico e indivisível.

### Tipos de JOIN
- **INNER JOIN**: Retorna informações comuns a ambas as tabelas.
- **LEFT JOIN**: Retorna tudo da tabela da esquerda e correspondências da direita.
- **RIGHT JOIN**: Retorna tudo da tabela da direita e correspondências da esquerda.
- **FULL JOIN**: Retorna todas as linhas de ambas as tabelas.

### Subconsultas
Consultas aninhadas que utilizam resultados de outras consultas.

### Funções Agregadas
Realizam cálculos nas colunas:
- COUNT
- SUM
- AVG
- MIN
- MAX

### Análise de Execução
Utiliza o comando EXPLAIN para entender o plano de execução de uma consulta.

## Bancos de Dados Não Relacionais (NoSQL)
- Não seguem modelos de tabelas e relacionamentos.
- Projetados para alto volume de dados e escalabilidade.
- Alta flexibilidade na estrutura de dados.

### Vantagens
- Flexibilidade de modelos
- Alta escalabilidade
- Melhor desempenho em consultas intensivas
- Tolerância a falhas

### Desvantagens
- Menor consistência imediata
- Menor suporte a consultas complexas (depende do SGBD)

### Tipos de Banco de Dados NoSQL
- **Key-Value**: Armazena dados como pares chave-valor (ex. DynamoDB).
- **Documento**: Armazena documentos semi-estruturados (ex. MongoDB).
- **Coluna**: Armazena dados em formato de colunas (ex. Apache Cassandra).
- **Grafos**: Armazena dados interconectados (ex. Neo4j).

## Introdução ao MongoDB
Banco de dados NoSQL orientado a documentos, ideal para grandes volumes de dados e modelagem flexível.

### Vantagens do MongoDB
- Flexibilidade na modelagem de dados
- Escalabilidade horizontal
- Consultas ricas e suporte a consultas complexas
- Alta disponibilidade

### Desvantagens do MongoDB
- Menor consistência imediata
- Consultas complexas exigem planejamento
- Maior consumo de espaço de armazenamento

### Estrutura do MongoDB
Composto por um ou mais databases, que contêm coleções de documentos.

#### Coleções
Agrupamentos lógicos de documentos, sem exigência de esquema.

#### Coleções
As coleções são agrupamentos lógicos de documentos no MongoDB. Elas não exigem um esquema fixo, permitindo que os documentos dentro de uma coleção tenham estruturas diferentes.

**Características das Coleções:**
- Os nomes das coleções devem seguir algumas regras:
    - Devem começar com uma letra ou um caractere de sublinhado (_).
    - Podem conter letras, números e caracteres de sublinhado.
    - Não podem ser vazios.
    - Não podem ter mais de 64 bytes de comprimento.

#### Documentos
Os documentos são as unidades básicas de dados armazenadas em uma coleção.

**Características dos Documentos:**
- Armazenados em formato BSON (Binary JSON), que permite estruturas flexíveis e semiestruturadas.
- Cada documento possui um identificador único chamado _id.
- Composto por pares de chaves e valores.
- O tamanho máximo de um documento é de 16 MB.
- Suportam aninhamento de documentos, permitindo estruturas hierárquicas.
- Oferecem flexibilidade na evolução do esquema, permitindo alterações sem interrupções.

* jsonformatter.curiousconcept.com

#### Documentos
Armazenados em BSON, com estrutura flexível e semiestruturada.

#### Modelagem de dados orientada para consultas
A modelagem de dados no MongoDB deve ser orientada  pelas consultas que serão realizadas com mais frequencia.

**Inner Documents:**

Denormalizar dados para evitar junções custosas. Dados relacionados podem ser armazenados na mesma estrutura.

**Modelar usuário com estratégia desnormalizada**

**Quando utilizar inner documments:**
- Os dados aninhados são específicos para o documento pai
- Os dados aninhhados são sempre acessados juntamente com o documento pai
- A cardinalidade do relacionamento é um pra muitos (um usuário pode ter várias reservas)

**Quando não utilizar inner documments:**

Se os dados aninhados precisam ser consultados e atualizados independentemente do documento pai, é mais adequado utilizar coleções separadas.
