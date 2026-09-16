import requests
import logging
import azure.functions as func

app = func.FunctionApp()

# FUNCTION 1
# timertrigger que impri um log
@app.timer_trigger(schedule="*/2 * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False) 
def timer_trigger_log(myTimer: func.TimerRequest) -> None:
    if myTimer.past_due:
        logging.info('Imprimiu atrasado.')

    logging.info('Log imprimido.')


# FUNCTION 2 
# trigger http que recebe um parametro e o imprimi.
@app.route(route="parametro", methods=["GET"])
def http_parametro(req: func.HttpRequest) -> func.HttpResponse:

    parametro = req.params.get("parametro")

    logging.info(f"Parâmetro recebido: {parametro}")

    return func.HttpResponse("Parâmetro recebido.")


# FUNCTION 3
# trigger http get, que vai ser chamado pelo trigger 4 
@app.route(route="resposta", methods=["GET"])
def http_resposta(req: func.HttpRequest) -> func.HttpResponse:

    mensagem = req.params.get("mensagem")

    return func.HttpResponse(f"{mensagem} - resposta da Function 3")


# FUNCTION 4
# timer trigger que chama a function 3
@app.timer_trigger(schedule="0 */2 * * * *", arg_name="myTimer", run_on_startup=False,
                use_monitor=False)
def timer_http(myTimer: func.TimerRequest) -> None:

    url = "http://localhost:7071/api/resposta" # pra rodar localmente

    resposta = requests.get(
        url,
        params={"mensagem": "Olá da Function 4"}
    )

    logging.info(f"Resposta da Function 3: {resposta.text}")