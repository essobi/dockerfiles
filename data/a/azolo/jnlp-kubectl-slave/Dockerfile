FROM jenkins/jnlp-slave:alpine  
  
USER root  
  
RUN wget https://storage.googleapis.com/kubernetes-
release/release/v1.8.3/bin/linux/amd64/kubectl && \  
chmod +x ./kubectl && \  
mv ./kubectl /usr/local/bin/kubectl  
  
USER jenkins  

