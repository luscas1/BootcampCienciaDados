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
A modelagem de dados no MongoDB deve ser orientada pelas consultas que serão realizadas com mais frequência.

**Inner Documents:**

Denormalizar dados para evitar junções custosas. Dados relacionados podem ser armazenados na mesma estrutura.

**Modelar usuário com estratégia desnormalizada**

**Quando utilizar inner documents:**
- Os dados aninhados são específicos para o documento pai.
- Os dados aninhados são sempre acessados juntamente com o documento pai.
- A cardinalidade do relacionamento é um para muitos (um usuário pode ter várias reservas).

**Quando não utilizar inner documents:**

Se os dados aninhados precisam ser consultados e atualizados independentemente do documento pai, é mais adequado utilizar coleções separadas.

#### Relacionamentos no MongoDB
No MongoDB, os relacionamentos entre documentos podem ser modelados de duas maneiras principais: **embutidos** e **referenciados**.

**1. Relacionamentos Embutidos:**
- Utiliza inner documents para armazenar dados relacionados dentro do mesmo documento.
- Ideal para dados que são frequentemente acessados juntos e têm uma relação forte.
- Exemplo: Um documento de usuário que contém uma lista de endereços.

**2. Relacionamentos Referenciados:**
- Armazena referências a outros documentos em coleções separadas.
- Útil quando os dados relacionados são grandes ou precisam ser acessados de forma independente.
- Exemplo: Um documento de usuário que contém um ID de referência para uma coleção de reservas.

**Considerações ao escolher o tipo de relacionamento:**
- **Desempenho:** Embutir documentos pode melhorar o desempenho em consultas, mas pode aumentar a complexidade na atualização de dados.
- **Flexibilidade:** Referenciar documentos permite uma estrutura mais flexível, mas pode resultar em consultas mais complexas.
- **Consistência:** Avaliar a necessidade de manter a consistência entre documentos relacionados.

Luiztools.com.br
A escolha entre embutir ou referenciar depende do caso de uso específico e das necessidades de consulta da aplicação.

#### Operações MongoDB

- Create database

    ``` use viagens ```
- Create collection
   
   ``` db.viagens.insertOne({}) ```

    ```db.createCollection("destinos")```

- Inserir um registro
    
    ``` 
    db.usuarios.insertOne({
    "nome": "Lucas Motta",
    "email": "lucas.motta09@gmail.com",
    "idade": 24,
    "data_nascimento": "2002-01-03",
    })
    ```

- Inserir muitos registros
    
    ``` 
    db.usuarios.insertMany([
    {
    "nome": "Lucas Motta",
    "email": "lucas.motta09@gmail.com",
    "idade": 24,
    "data_nascimento": "2002-01-03",
    },
    {
    "nome": "Lucas Motta",
    "email": "lucas.motta09@gmail.com",
    "idade": 24,
    "data_nascimento": "2002-01-03",
    },])
    ```

- consultando documentos

    ```db.usuarios.find({})```

    Retorna o primeiro


    ```db.usuarios.findOne({"nome": "Lucas Motta"})```

    Atualiza informação do primeiro que encontrar
    ```db.usuarios.findOneAndUpdate({"nome":"Lucas Motta"}, {$set:      {"nome":"Lucas Silva"}})```


    Deletar user pelo Id

    ```db.usuarios.deleteOne({"_id":ObjectId("69717fb7fa538ab58d50113b")})```

#### Consultas Simples

```
// Operadores Lógicos
db.usuarios.find({ $and: [{ idade: { $gte: 18 } }, { cidade: "São Paulo" }] });

db.usuarios.find({ $or: [{ idade: { $lt: 18 } }, { cidade: "Rio de Janeiro" }] });

db.usuarios.find({ idade: { $not: { $eq: 25 } } });

// Operadores de Comparação
db.usuarios.find({ idade: { $eq: 25 } });

db.usuarios.find({ idade: { $ne: 30 } });

db.usuarios.find({ idade: { $gt: 30 } });

db.usuarios.find({ idade: { $gte: 30 } });

db.usuarios.find({ idade: { $lt: 30 } });

db.usuarios.find({ idade: { $lte: 30 } });

db.usuarios.find({ cidade: { $in: ["São Paulo", "Rio de Janeiro"] } });

db.usuarios.find({ cidade: { $nin: ["São Paulo", "Rio de Janeiro"] } });


// Projeção
db.usuarios.find({}, { nome: 1, idade: 1 })

// Ordenação
db.usuarios.find().sort({ idade: 1 })
// Limitação
db.usuarios.find().limit(10)
// Paginação
db.usuarios.find().skip(10).limit(5)

```