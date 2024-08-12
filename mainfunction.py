import logging
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    return func.HttpResponse("Hello, this is a simple Azure Function!", status_code=200)
