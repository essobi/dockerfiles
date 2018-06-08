FROM alpine  
  
ENV VERSION=2.5.1  
RUN cd /tmp && \  
apk add --no-cache curl && \  
curl https://storage.googleapis.com/kubernetes-helm/helm-v$VERSION-linux-
amd64.tar.gz -o helm.tar.gz && \  
tar xvf helm.tar.gz && \  
cp linux-amd64/helm /usr/bin/helm && \  
rm -rf /tmp/*  

