FROM python:3  
WORKDIR /usr/src/hermes  
  
RUN curl https://get.docker.com | bash -  
RUN pip install docker-compose  
  
COPY . .  
  
RUN pip install .  
  
ENTRYPOINT [ "hermes" ]  

