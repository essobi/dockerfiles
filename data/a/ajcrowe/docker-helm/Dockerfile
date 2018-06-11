FROM alpine:3.6  
ENV VERSION v2.7.0  
RUN apk add --no-cache --virtual build-dependencies curl && \  
mkdir -p /tmp/helm && \  
curl https://storage.googleapis.com/kubernetes-helm/helm-${VERSION}-linux-
amd64.tar.gz | \  
tar -xzv -C /tmp/helm && \  
mv /tmp/helm/linux-amd64/helm /usr/bin/helm && \  
rm -rf /tmp/helm && \  
apk del build-dependencies  
  
CMD ["/usr/bin/helm"]  

