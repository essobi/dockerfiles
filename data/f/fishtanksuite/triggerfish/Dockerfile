FROM python:2.7-alpine  
RUN apk update && apk upgrade && \  
apk add --no-cache bash git openssh  
  
RUN git clone https://github.com/fishtanksuite/triggerfish-agent.git  
RUN pip install -r triggerfish-agent/requirements.txt  
CMD [ "python", "./triggerfish-agent/__main__.py" ]  

