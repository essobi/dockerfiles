FROM python:2-alpine  
  
LABEL maintainer "koopzington@gmail.com"  
  
COPY ./start.sh ./  
RUN chmod +x ./start.sh && \  
pip install dAbot  
  
ENTRYPOINT ./start.sh

