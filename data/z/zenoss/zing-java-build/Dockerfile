FROM maven:3-jdk-8-alpine  
  
RUN apk add --no-cache su-exec curl bash git openssh make ca-certificates
docker libc6-compat  
  
# Disable ssh host key checking  
RUN echo 'Host *' >> /etc/ssh/ssh_config  
RUN echo ' StrictHostKeyChecking no' >> /etc/ssh/ssh_config  
  
COPY settings.xml /etc  
COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh  
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]  

