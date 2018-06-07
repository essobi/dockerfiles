FROM python:2.7-alpine  
  
# Copies the entire Git repo into the container during automated build on
Docker Hub.  
COPY . /holeio  
WORKDIR "/holeio"  
RUN pip install --no-cache-dir virtualenv && \  
apk update && apk upgrade && \  
apk add --no-cache bash  
RUN /bin/bash -c "/holeio/install.sh"  
#EXPOSE is only a hint, ports must be specififed on the host when running this
container.  
EXPOSE 8080  
CMD ["venv/bin/bottle.py","-b","0.0.0.0:8080","holeio.app"]  

