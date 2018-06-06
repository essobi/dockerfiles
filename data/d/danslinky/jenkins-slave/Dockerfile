FROM jenkinsci/jnlp-slave  
  
ENV CLOUDSDK_CORE_DISABLE_PROMPTS 1  
ENV PATH /opt/google-cloud-sdk/bin:$PATH  
  
USER root  
  
RUN apt-get update -y  
RUN apt-get install -y jq  
RUN curl https://sdk.cloud.google.com | bash && mv google-cloud-sdk /opt  
RUN gcloud components install kubectl  
  
RUN curl -L https://github.com/docker/compose/releases/download/1.11.0/docker-
compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose && chmod +x
/usr/local/bin/docker-compose  

