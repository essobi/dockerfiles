FROM quay.io/letsencrypt/letsencrypt:latest  
  
MAINTAINER Michał Czeraszkiewicz <contact@czerasz.com>  
  
# Set the reset cache variable  
# Read more here: http://czerasz.com/2014/11/13/docker-tip-and-tricks/#use-
refreshedat-variable-for-better-cache-control  
ENV REFRESHED_AT 2016-05-16  
# Create the webroot directory which will be used by Let's Encrypt to store  
# temporary files. Let's Encrypt will use the following directory:  
# /etc/letsencrypt/webroot/.well-known/acme-challenge/  
RUN mkdir -p /etc/letsencrypt/webroot  
  
# Copy the renewal script  
COPY ./docker-entrypoint.sh /docker-entrypoint.sh  
# Copy the main Let's Encrypt configuration file template  
COPY ./cli.ini.example /etc/default/letsencrypt/cli.ini.example  
  
# Share /etc/letsencrypt  
VOLUME ["/etc/letsencrypt"]  
  
# /docker-entrypoint.sh should be executed by default  
ENTRYPOINT [ "/docker-entrypoint.sh" ]  

