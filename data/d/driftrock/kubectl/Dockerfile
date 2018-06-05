FROM alpine:3.5  
ENV KUBECTL_VERSION=1.5.2  
RUN apk --update add \  
curl \  
ca-certificates \  
&& curl -LO https://storage.googleapis.com/kubernetes-
release/release/v$KUBECTL_VERSION/bin/linux/amd64/kubectl \  
&& mv kubectl /usr/bin/ \  
&& chmod +x /usr/bin/kubectl  

