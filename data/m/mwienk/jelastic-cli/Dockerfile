FROM openjdk:8-jdk-alpine  
  
RUN apk add --update curl wget bash && \  
rm -rf /var/cache/apk/*  
  
WORKDIR /root  
  
RUN curl -s ftp://ftp.jelastic.com/pub/cli/jelastic-cli-installer.sh | bash  
RUN export PATH=$PATH:/root/jelastic  
  
COPY ./jelastic.properties /root/.config/jelastic/jelastic.properties  
  
ENTRYPOINT []  

