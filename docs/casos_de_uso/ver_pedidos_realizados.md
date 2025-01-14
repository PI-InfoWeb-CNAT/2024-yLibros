# Projeto eLibros - Especificação de caso de uso

##  Ver pedidos realizados

### Histórico da Revisão 
|  Data  | Versão | Descrição | Autor |
|:-------|:-------|:----------|:------|
| 12/09/2024 | **1.00** | Primeira versão  | Gabriel Campos |
| 04/11/2024 | **1.10** | Adição de protótipo de interface  | Gabriel Campos |
| 09/12/2024 | **1.20** | Adição de diagrama de classe de domínio  | Gabriel Campos |


### 1. Resumo 
Esse caso de uso permite o usuário consultar os pedidos realizados.

### 2. Atores 
- Cliente

### 3. Pré-condições
São pré-condições para iniciar este caso de uso:
- O cliente estar logado no sistema
  
### 4. Pós-condições
Após a execução deste caso de uso, espera-se que o sistema:
- Apresente ao cliente os pedidos já realizados.

### 5. Fluxos de evento

#### 5.1. Fluxo Principal 
|  Ator  | Sistema |
|:-------|:------- |
|1. Na página do perfil do usuário, o usuário clica no botão para ver pedidos realizados| --- |
| --- |2. O sistema apresenta uma nova página com os pedidos realizados pelo cliente.  | 

### 6. Protótipos de Interface
![image](https://github.com/user-attachments/assets/7d18919c-7995-4f75-bd72-de19adf677e8)


### 7. Diagrama de classe de domínio usados neste caso de uso
![image](https://github.com/user-attachments/assets/d8355352-3e4d-486f-994d-626eade05da0)



### 8. Dicionário de dados

#### 8.1. Pedido
- Status - Booleano
- entregaEstimada - Data do calendário em modelo DD/MM/AAAA
- numero_Pedido - Atributo identificador do Pedido

### 9. Regras de negócio
