FROM alpine:3.6  
LABEL maintainer="mario.siegenthaler@linkyard.ch"  
  
RUN apk --no-cache add bash  
RUN apk --no-cache add --update curl ca-certificates  
RUN apk --no-cache add jq  
  
ENV KUBE_LATEST_VERSION="v1.9.3"  
RUN curl -L https://storage.googleapis.com/kubernetes-
release/release/${KUBE_LATEST_VERSION}/bin/linux/amd64/kubectl -o
/usr/local/bin/kubectl \  
&& chmod +x /usr/local/bin/kubectl  
  
COPY initK8s.sh /opt/  

