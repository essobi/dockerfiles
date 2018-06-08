FROM jenkins:alpine  
  
USER root  
  
RUN apk --no-cache --update add make docker py-pip  
RUN pip install --no-cache-dir --upgrade pip && \  
pip install --no-cache-dir docker-compose  
  
USER jenkins  
  
COPY plugins.txt /usr/share/jenkins/ref/plugins.txt  
RUN /usr/local/bin/install-plugins.sh < /usr/share/jenkins/ref/plugins.txt  

