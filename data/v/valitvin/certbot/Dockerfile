FROM alpine:3.7  
RUN apk add -U certbot coreutils  
  
# Install requirements  
RUN apk add -U openssl curl tar gzip bash ca-certificates && \  
wget -q -O /etc/apk/keys/sgerrand.rsa.pub
https://raw.githubusercontent.com/sgerrand/alpine-pkg-
glibc/master/sgerrand.rsa.pub && \  
wget https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/2.23-r3/glibc-2.23-r3.apk && \  
apk add glibc-2.23-r3.apk && \  
rm glibc-2.23-r3.apk  
  
# Install kubectl  
RUN curl -L -o /usr/bin/kubectl https://storage.googleapis.com/kubernetes-
release/release/$(curl -s https://storage.googleapis.com/kubernetes-
release/release/latest.txt)/bin/linux/amd64/kubectl && \  
chmod +x /usr/bin/kubectl && \  
kubectl version --client  
  
RUN mkdir /le  
  
COPY ./*.sh /  
  
CMD [ '/bin/sh', '/run.sh' ]  

