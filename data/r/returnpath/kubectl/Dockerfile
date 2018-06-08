FROM alpine:3.3  
ENTRYPOINT ["/bin/kubectl"]  
  
RUN set -x && \  
apk --update upgrade && \  
apk add ca-certificates && \  
rm -rf /var/cache/apk/*  
  
ENV K8S_VERSION 1.2.3  
RUN set -x && \  
wget -O -
https://github.com/kubernetes/kubernetes/releases/download/v${K8S_VERSION}/kubernetes.tar.gz
| \  
tar zxOf - kubernetes/platforms/linux/amd64/kubectl > /bin/kubectl && \  
chmod +x /bin/kubectl  
  

