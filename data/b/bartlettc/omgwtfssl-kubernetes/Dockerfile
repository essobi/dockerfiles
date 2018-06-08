FROM alpine  
  
RUN apk --update add --no-cache curl bash openssl  
  
ENV KUBE_VERSION="1.6.2"  
# Install kubectl  
RUN curl -LO https://storage.googleapis.com/kubernetes-
release/release/v$KUBE_VERSION/bin/linux/amd64/kubectl \  
&& chmod +x ./kubectl \  
&& mv ./kubectl /usr/local/bin/kubectl \  
# Basic check it works.  
&& kubectl version --client  
  
WORKDIR /certs  
  
COPY generate-certs /usr/local/bin/generate-certs  
  
CMD /usr/local/bin/generate-certs  
  
VOLUME /certs  

