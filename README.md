# TAPRA-2026

## Integrantes da equipe
- Igor dos Santos Lopes
- André Manoel de Santana
- Denis Sebastian Medina Crusado

## Linguagem de Programação Escolhida

A linguagem escolhida foi o Python 3.13.5 e utilizamos o modelo 'v2' de programação Python para o Azure, referência: [Azure Functions HTTP trigger](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-http-webhook-trigger?tabs=python-v2%2Cisolated-process%2Cnodejs-v4%2Cfunctionsv2&pivots=programming-language-python).

## Azure Functions
1. Timer trigger - Imprimi apenas um log no terminal;
2. Http trigger - Deve receber via URL (get) um parametro e imprimir esse parametro na tela;
3. Timer trigger - Deve fazer uma chamada HTTP para outra Azure Function (envia um texto como parâmetro); 
4. Http trigger - Deve receber o que foi enviado pelo timer trigger e retornar essa informação junto de um texto adicional de identificação.
