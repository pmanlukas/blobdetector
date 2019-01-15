import logging

import azure.functions as func


def main(myblob: func.InputStream):
    logging.info(f"Python blob trigger function processed blob \n"
                 f"Name: {myblob.name}\n"
                 f"Blob Size: {myblob.length} bytes")

def loadmodel():

def preprocessimg(img):
    return processedimg

def predict(img):
    return prediction