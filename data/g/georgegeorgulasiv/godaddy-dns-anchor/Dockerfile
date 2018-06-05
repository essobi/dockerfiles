FROM georgegeorgulasiv/rpi-alpine-cross:latest  
LABEL maintainer georgegeorgulas@gmail.com  
  
# add files  
COPY crontab.txt /crontab.txt  
COPY env_secrets_expand.sh /env_secrets_expand.sh  
COPY godaddy-dns-anchor.sh /godaddy-dns-anchor.sh  
COPY entry.sh /entry.sh  
  
# Declare GoDaddy API environment variables as secrets  
ENV GODADDY_API_KEY DOCKER-SECRET->GODADDY_API_KEY  
ENV GODADDY_API_SECRET DOCKER-SECRET->GODADDY_API_SECRET  
  
# Declare other environment variables with default values to keep scripts
happy  
ENV DOMAIN example.org  
ENV HOST_TYPE A  
ENV HOST examplesubdomain  
  
# allow cross-compile for arm from x86 servers (such as docker hub)  
RUN [ "cross-build-start" ]  
  
# Make scripts executable  
RUN chmod 755 /godaddy-dns-anchor.sh && \  
chmod 755 /entry.sh && \  
chmod 755 env_secrets_expand.sh && \  
# Load crontab file into crontab  
/usr/bin/crontab /crontab.txt && \  
# Prepare apk  
apk update && \  
# Upgrade any underlying packages missed by our base image in the name of
security best practices  
apk upgrade && \  
# Install our required packages  
apk add \--update bash curl dcron && \  
# Clean up the chaff from apk for smaller final layer size  
rm -rf /var/cache/apk/*  
RUN [ "cross-build-end" ]  
  
# Launch the container with our shell script to both update once and launch
crontab  
ENTRYPOINT ["/entry.sh"]  

