FROM docker:latest  
RUN apk add --no-cache python2 bash curl openssl py-setuptools  
RUN curl https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-
cloud-sdk-197.0.0-linux-x86_64.tar.gz | tar -xzf -  
RUN /google-cloud-sdk/install.sh  
ENV PATH=/google-cloud-sdk/bin:$PATH  
RUN gcloud components install kubectl gsutil beta  
ADD docker-config.json /root/.docker/config.json  
#RUN gcloud auth configure-docker  
RUN curl https://raw.githubusercontent.com/kubernetes/helm/master/scripts/get
| bash  
RUN helm init --client-only  
RUN easy_install-2.7 pip  
RUN pip install awscli --upgrade  

