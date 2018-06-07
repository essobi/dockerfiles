FROM docker:latest  
  
RUN apk update && apk add --no-cache wget python \  
&& wget https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-
cloud-sdk-162.0.1-linux-x86_64.tar.gz \  
&& tar -xvzf google-cloud-sdk-162.0.1-linux-x86_64.tar.gz \  
&& rm google-cloud-sdk-162.0.1-linux-x86_64.tar.gz \  
&& ./google-cloud-sdk/install.sh -q \  
&& export PATH=/google-cloud-sdk/bin:$PATH \  
&& ln -s /google-cloud-sdk/bin /usr/local/sbin \  
&& gcloud config set disable_usage_reporting true \  
&& gcloud components install kubectl -q \  
&& gcloud components install docker-credential-gcr -q  

