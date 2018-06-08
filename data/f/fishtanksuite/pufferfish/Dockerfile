FROM python:2.7-alpine  
RUN apk update && apk upgrade && \  
apk add --no-cache bash git openssh  
  
RUN git clone https://github.com/fishtanksuite/pufferfish-logger.git  
RUN pip install -r pufferfish-logger/requirements.txt  
CMD [ "python", "./pufferfish-logger/__main__.py" ]  

