import requests
import logging
import azure.functions as func

app = func.FunctionApp()

# FUNCTION 1
# timertrigger que impri um log
@app.timer_trigger(schedule="*/2 * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False) 
def timer_imprimir_log(myTimer: func.TimerRequest) -> None:
    if myTimer.past_due:
        logging.info('Imprimiu atrasado.')

    logging.info('Log imprimido.')


# FUNCTION 2 
# trigger http que recebe um parametro e o imprimi.
@app.route(route="parametro", methods=["GET"])
def http_imprimir_parametro(req: func.HttpRequest) -> func.HttpResponse:

    parametro = req.params.get("parametro")

    logging.info(f"Log do parâmetro recebido: {parametro}")

    return func.HttpResponse(f"Parâmetro recebido: {parametro}")


# FUNCTION 3
# trigger http get, que vai ser chamado pelo timer trigger(function 4) 
@app.route(route="resposta", methods=["GET"])
def http_mensagem(req: func.HttpRequest) -> func.HttpResponse:

    mensagem_timer = req.params.get("mensagem")

    return func.HttpResponse(f"{mensagem_timer} - mensagem da Function 3 (httptrigger)")


# FUNCTION 4
# timer trigger que chama (chamada HTTP) a function 3 
@app.timer_trigger(schedule="0 */2 * * * *", arg_name="myTimer", run_on_startup=False,
                use_monitor=False)
def timer_chamar_http(myTimer: func.TimerRequest) -> None:

    url = "http://localhost:7071/api/" # pra rodar localmente


    resposta_http_mensagem = requests.get(
        url,
        params={"mensagem": "Olá da Function 4 (timertrigger)"}
    )

    #aqui precisa ser .text para mostrar como string
    logging.info(f"Resposta da Function 3: {resposta_http_mensagem.text}")