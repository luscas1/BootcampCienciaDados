# Banco de Dados Relacionais

Aprendendo SQL - Structured Query Language

## Conceitos básicos

É uma coleção organizada de informações ou dados, estruturada.

## Tipos e banco de dados
* Relacionais/SQL
* Não Relacionais/NoSQL (Not only SQL)
* Orientado a objetos
* Hierárquico

## O que é um SGBD
Sistema de gerenciamento de banco de dados

### Funcionalidades:
CRUD

* Crate, Read, Update e Delete

## Estrutura de um DB relacional


## Chaves primárias

## Identificadores estrangeiros

## Caracteristicas

* Relacionamento entre tabelas
* Linguagem de consulta estruturada
* Integridade Referenciada
* Normalização de Dados
* Segurança
* Flexibilidade e extensibilidade
* Suporte a transações ACID

### ACID
* Atomicidade - todas as operações sejam executadas com sucesso ou nenhuma é.
* Consistência - garante que o DB saia de um estado consistente para outro estado consistente.
* Isolamento - cada transação é executada de maneira isolada, sem interferir nas ações concorrentes.
* Durabilidade - a alteração de informação é permanente e persiste no tempo. Alteração quando commitada não volta.


## Ogranização da SQL
Dividido em:

* DQL: linguagem de consulta de dados ex. SELECT
* DML: linguagem de manipulação de dados ex. INSERT, UPDATE, DELETE
* DDL: linguagem de definição de dados ex. CREATE, ALTER, DROP
* DCL: linguagem de controle de dados ex. GRANT, REVOKE
* DTL: linguagem de transformação de dados ex. BEGIN, COMMIT, ROLLBACK

## Sintaxe básica

* Os nomes devem começar com uma letra ou com um caractere de sublinhado (_);
* Os nomes podem conter letras, números e caracteres de sublinhado;
* Case sensitive (maiúsculas e minúsculas);

## Modelagem de bancos de dados relacionais (MER e DER)

O Modelo de Entidades e Relacionamento (MER) é representado através de diagramas denominados Diagramas Entidade Relacionamento (DER).

### Entidades

## Tabelas, colunas e linhas
As tabelas são usadas para armazenar dados de forma organizada. Cada tabela em um db relacional tem um nome único e é dividia em colunas e linhas.

* Coluna: estrutura dentro da tabela que representa umatributo específico. Cada coluna tem um nome único e armazena um tipo de dado.

* Registro: informação em si. Chamado também de linha ou tupla.

#### Comando CREATE TABLE
Definição de colunas, restrições de unique, not null etc.

#### Tipos de dados:
* Integer
* Decimal
* String
* etc...

# Operações CRUD: INSERT  e SELECT

# Chave primáriaé um atributo ou conjunto de que identifica de forma exclusiva cada registro da nossa tabela

# Atomicidade de dados - Formas Normais (1FN)
Estabelece que cada valor em uma tabela deve ser atômico, indivisível. Nenhum campo deve conter múltiplos valores ou listas.