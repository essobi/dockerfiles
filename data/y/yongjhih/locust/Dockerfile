FROM python:alpine3.6  
RUN apk -U add ca-certificates build-base git openssh && \  
pip install locustio pipenv && \  
rm -r /var/cache/apk/* && \  
mkdir /app  
  
WORKDIR /app  
  
ADD docker-entrypoint.sh /docker-entrypoint.sh  
  
EXPOSE 8089 5557 5558  
ENTRYPOINT [ "/docker-entrypoint.sh" ]  

