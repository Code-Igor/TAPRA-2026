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
# timer http que recebe um parametro e o imprimi.
@app.route(route="parametro", methods=["GET"])
def http_parametro(req: func.HttpRequest) -> func.HttpResponse:

    parametro = req.params.get("parametro")

    logging.info(f"Parâmetro recebido: {parametro}")

    return func.HttpResponse("Parâmetro recebido.")


# FUNCTION 3
#

# FUNCTION 4
#