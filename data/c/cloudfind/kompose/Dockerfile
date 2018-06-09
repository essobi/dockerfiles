FROM alpine  
MAINTAINER Rob Haswell <rob@cloudfindhq.com>  
  
ENV KOMPOSE_VERSION=v0.1.2  
RUN apk add --no-cache curl  
RUN curl -L https://github.com/kubernetes-
incubator/kompose/releases/download/${KOMPOSE_VERSION}/kompose_linux-
amd64.tar.gz | tar zxO kompose_linux-amd64/kompose > /usr/local/bin/kompose  
RUN chmod +x /usr/local/bin/kompose  
  
RUN adduser -S kompose  
USER kompose  
  
CMD kompose  

