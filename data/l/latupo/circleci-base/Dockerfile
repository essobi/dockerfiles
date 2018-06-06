FROM openjdk:8u131-jdk-alpine  
  
RUN apk --update add --no-cache \  
bash git docker rsync openssh openssl py-pip tar gzip && \  
pip install --upgrade pip && \  
pip install awscli docker-compose docker-squash docker && \  
rm /var/cache/apk/*  

