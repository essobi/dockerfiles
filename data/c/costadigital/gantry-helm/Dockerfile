ARG GANTRY_VERSION=v0.1.1  
  
FROM alpine:latest as helm-installer  
RUN apk update && apk upgrade && \  
apk --no-cache add curl  
  
ARG HELM_VERSION=2.7.0  
  
RUN curl "https://storage.googleapis.com/kubernetes-helm/helm-v$HELM_VERSION-
linux-amd64.tar.gz" -o helm.tar.gz  
RUN tar -xf helm.tar.gz  
  
FROM costadigital/gantry:$GANTRY_VERSION  
RUN apk update \  
&& apk upgrade \  
&& apk add \--no-cache bash  
  
COPY \--from=helm-installer /linux-amd64/helm /usr/local/bin/helm  

