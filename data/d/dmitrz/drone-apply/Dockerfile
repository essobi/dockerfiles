FROM alpine:3.7  
ARG K8S_VERSION=v1.8.6  
RUN set -x && \  
wget -O /usr/local/bin/kubectl https://storage.googleapis.com/kubernetes-
release/release/$K8S_VERSION/bin/linux/amd64/kubectl && \  
chmod +x /usr/local/bin/kubectl  
  
COPY entrypoint.sh /  
ENTRYPOINT [ "/entrypoint.sh" ]  

