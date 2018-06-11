FROM docker:dind  
  
RUN apk add --no-cache make bash git python openssh-client 'py-pip' \  
&& pip install 'docker-compose'  
  
CMD ["--insecure-registry", "10.10.2.111:5000"]  

