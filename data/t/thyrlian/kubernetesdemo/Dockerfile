# ====================================================================== #  
# Ruby Sinatra Docker Image for Kubernetes Demo Purpose  
# ====================================================================== #  
# Base image  
# ---------------------------------------------------------------------- #  
FROM ruby:2.5.1-alpine3.7  
# Author  
# ---------------------------------------------------------------------- #  
LABEL maintainer "thyrlian@gmail.com"  
  
# Install necessary packages  
RUN apk update && apk add git  
  
# Setup server project  
RUN git clone https://github.com/thyrlian/KubernetesDemo.git
/srv/KubernetesDemo && \  
cd /srv/KubernetesDemo/Server/ && \  
bundle install  
  
WORKDIR "/srv/KubernetesDemo/Server"  
  
EXPOSE 8080  
CMD ["rackup"]  

