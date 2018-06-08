FROM alpine:latest  
LABEL maintainer="jesse@weisner.ca"  
  
ENV RUNUSER none  
ENV HOME /  
  
RUN apk add --no-cache \  
tini  
  
# Add docker-entrypoint script base  
ENV DE_VERSION v1.1  
ADD https://github.com/itsbcit/docker-
entrypoint/releases/download/${DE_VERSION}/docker-entrypoint.tar.gz /docker-
entrypoint.tar.gz  
RUN tar zxvf docker-entrypoint.tar.gz && rm -f docker-entrypoint.tar.gz  
RUN chmod -R 555 /docker-entrypoint.*  
  
# Allow resolve-userid.sh script to run  
RUN chmod 664 /etc/passwd /etc/group  
  
ENTRYPOINT ["/sbin/tini", "--", "/docker-entrypoint.sh"]  

