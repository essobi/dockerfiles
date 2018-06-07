FROM debian:latest  
  
RUN apt update && apt install -y build-essential python-pip && pip install
celery flower redis  
  
RUN groupadd user && useradd --create-home --home-dir /home/user -g user user  
  
WORKDIR /home/user  
  
USER user  
  
EXPOSE 5555  
  
CMD celery -A tasks flower  

