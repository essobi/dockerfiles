FROM alpine:3.5  
LABEL name="outguess"  
LABEL version=0.2  
LABEL maintainer="Stephane Jourdan <fasten@fastmail.fm>"  
MAINTAINER Stephane Jourdan <fasten@fastmail.fm>  
RUN apk --update add --virtual wget &&\  
wget -q --no-check-certificate https://github.com/sjourdan/outguess-
docker/releases/download/0.2/outguess-0.2_alpine.tar.gz && \  
tar xvfz outguess-0.2_alpine.tar.gz && \  
rm -rf outguess-0.2_alpine.tar.gz && \  
apk del wget && \  
rm -rf /var/cache/apk  
VOLUME ["/data"]  
WORKDIR /data  
ENTRYPOINT ["/outguess"]  

