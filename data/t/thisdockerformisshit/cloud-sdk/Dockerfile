FROM docker:17.12.0-ce as static-docker-source  
  
FROM debian:jessie  
ENV CLOUD_SDK_VERSION 200.0.0  
ENV PATH="/root/google-cloud-sdk/bin:${PATH}"  
COPY \--from=static-docker-source /usr/local/bin/docker /usr/local/bin/docker  
  
# Install prerequisites  
RUN apt-get update && apt-get install -y curl  
RUN apt-get install -y python  
  
RUN curl https://sdk.cloud.google.com | bash -s -- --disable-prompts  
RUN gcloud components install kubectl  
RUN gcloud components install beta  

