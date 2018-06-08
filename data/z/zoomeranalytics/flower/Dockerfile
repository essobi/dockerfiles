# Flower  
FROM python:3.6.3-slim  
  
RUN apt-get update && apt-get install -y unzip wget  
  
RUN wget
https://releases.hashicorp.com/envconsul/0.7.2/envconsul_0.7.2_linux_amd64.zip\  
&& unzip envconsul_0.7.2_linux_amd64.zip\  
&& ln -sf $PWD/envconsul /usr/local/bin  
  
RUN pip install celery==4.0.2  
RUN pip install flower==0.9.2  
RUN pip install redis  
  
COPY ./start.sh /app/start.sh  
  
WORKDIR /app  
  
EXPOSE 5555  
CMD ["/bin/bash", "/app/start.sh"]  

