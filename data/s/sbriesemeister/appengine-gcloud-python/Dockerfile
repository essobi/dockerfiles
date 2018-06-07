FROM alpine:latest as clean  
  
ARG GCLOUD_SDK_VERSION  
ENV GCLOUD_SDK_VERSION=${GCLOUD_SDK_VERSION:-202.0.0}  
ENV PATH /opt/google-cloud-sdk/bin:/usr/local/bin:$PATH  
  
COPY scripts/*.sh /opt/  
RUN ln -s /opt/env_secure.sh /usr/local/bin/ && chmod +x /opt/env_secure.sh  
  
# Dependencies for Google AppEngine Python  
RUN sh /opt/setup_alpine.sh  
  
# Install Google Cloud SDK  
RUN sh /opt/setup_appengine.sh /opt/google-cloud-sdk  
  

