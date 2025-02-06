# ✈️ Sistema de Gerenciamento de Viagens

| <img src="/static/img/vf.png" alt="Logo" width="300"> | Este projeto implementa um sistema CRUD (Create, Read, Update, Delete) para gerenciar reservas, clientes e pacotes de uma viagem. |
|------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|

---

## 📌 Visão Geral

O objetivo deste sistema é facilitar o gerenciamento e a visualização de todos os dados e informações relacionadas aos clientes, pacotes e reservas. Ele permite:

✅ **Criação** de novos registros de clientes, pacotes e reservas.  
🔍 **Leitura** das informações existentes e uma visualização mais detalhada.  
✏️ **Edição** de dados quando necessário.  
🗑️ **Exclusão** de registros que não são mais necessários.  

---

## 🌎 Acessibilidade  
Este sistema foi desenvolvido para ser totalmente responsivo e acessível em **qualquer dispositivo**, seja **PC, tablet ou smartphone**.  
Isso permite que os usuários gerenciem reservas e pacotes de viagem de qualquer lugar, sem a necessidade de um dispositivo específico.

---

## ⚙️ Funcionalidades

- **Gerenciamento de Clientes**: Adicionar, visualizar, editar e remover informações de clientes.
- **Gerenciamento de Pacotes**: Criar, consultar, modificar e excluir pacotes de viagens.
- **Controle de Reservas**: Sistema para gerenciar, visualizar, modificar ou cancelar reservas que conectam clientes aos pacotes.

---

## 🎨 Algumas Interfaces:

### 🏁 Interface de Login  
![Tela de Login](https://github.com/user-attachments/assets/21a54cd5-c708-4614-aec0-a4887536ff8b)

### 🛫 Tela de Gerenciamento e Busca de Pacotes  
![Image](https://github.com/user-attachments/assets/077bc555-c47c-44da-8f92-9ca4cf253057)

### 👥 Tela de Gerenciamento e Busca de Clientes  
![Image](https://github.com/user-attachments/assets/86eb5879-5ab5-4b5e-a7f8-2b043dbbd9c9)

### 📆 Tela de Controle das Reservas  
![Image](https://github.com/user-attachments/assets/4033b0d7-e6a9-4ef8-ad04-56ec5b6692e3)

---

## 🗂️ Diagrama ER  
![Diagrama ER](/docs/ER.png)

---

## 📄 Dicionário de Dados

Este projeto utiliza um banco de dados SQLite para gerenciar informações de clientes, pacotes de viagem, reservas e usuários. Abaixo está a estrutura das tabelas e seus respectivos campos.

### 🏷️ Tabela: Cliente
| Coluna        | Tipo de Dados | Descrição                                |
|--------------|--------------|------------------------------------------|
| `id`        | INTEGER      | Identificador único (Primary Key)       |
| `nome`      | VARCHAR      | Nome do cliente                         |
| `cpf`       | VARCHAR      | CPF do cliente, único                   |
| `telefone`  | VARCHAR      | Telefone do cliente                     |
| `email`     | VARCHAR      | E-mail do cliente, único                |
| `data_criacao` | DATETIME  | Data de criação do cliente              |

### 🎟️ Tabela: Pacote
| Coluna        | Tipo de Dados    | Descrição                                |
|--------------|-----------------|------------------------------------------|
| `id`        | INTEGER          | Identificador único (Primary Key)       |
| `nome`      | VARCHAR          | Nome do pacote                          |
| `descricao` | TEXT             | Descrição do pacote                     |
| `preco`     | DECIMAL(10,2)    | Preço do pacote                         |
| `data_inicio` | DATETIME       | Data de início do pacote                |
| `data_fim`  | DATETIME         | Data de fim do pacote                   |
| `data_criacao` | DATETIME      | Data de criação do pacote               |

### 📌 Tabela: Reserva
| Coluna        | Tipo de Dados | Descrição                                        |
|--------------|--------------|--------------------------------------------------|
| `id`        | INTEGER      | Identificador único (Primary Key)               |
| `cliente_id` | INTEGER     | Chave estrangeira para o cliente (Foreign Key)  |
| `pacote_id`  | INTEGER     | Chave estrangeira para o pacote (Foreign Key)   |
| `data_reserva` | DATETIME  | Data da reserva                                 |
| `status`     | VARCHAR     | Status da reserva                              |

### 👤 Tabela: Usuario
| Coluna        | Tipo de Dados | Descrição                                |
|--------------|--------------|------------------------------------------|
| `id`        | INTEGER      | Identificador único (Primary Key)       |
| `nome`      | VARCHAR      | Nome do usuário                         |
| `email`     | VARCHAR      | E-mail do usuário, único                |
| `password`  | VARCHAR      | Senha do usuário                        |

---

📌 **Observações:**
- As chaves estrangeiras `cliente_id` e `pacote_id` na tabela `Reserva` fazem referência às tabelas `Cliente` e `Pacote`, respectivamente.
- Os campos `data_criacao`, `data_reserva`, `data_inicio` e `data_fim` são armazenados no formato `DATETIME`.

---

## 📌 Diagrama de Classes  
<img src="docs/Diagrama_de_ classes.png" alt="Diagrama de classes">

---

## 🛠️ Tecnologias Utilizadas

- 🔹 **Python**
- 🔥 **Flask**
- 🔑 **Werkzeug.security**
- 🗄️ **Banco SQLite**
- 🏗️ **ORM Peewee**
- ⚡ **Cru.js**
- 🖥️ **Visual Studio Code**

---

## 
