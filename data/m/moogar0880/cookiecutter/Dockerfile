FROM python:alpine  
  
VOLUME /mnt  
WORKDIR /mnt  
  
RUN apk add --no-cache git && \  
pip install cookiecutter  
  
ENTRYPOINT ["cookiecutter"]  

