import logging
import azure.functions as func

app = func.FunctionApp()

@app.timer_trigger(schedule="*/2 * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False) 
def timer_trigger_log(myTimer: func.TimerRequest) -> None:
    if myTimer.past_due:
        logging.info('Imprimiu atrasado.')

    logging.info('Imprimi log.')