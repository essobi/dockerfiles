FROM alpine  
MAINTAINER Ben Origas <borigas@gmail.com>  
  
# Add in SSL certificates for use with https, curl to call the update
endpoint,  
# bash used by the namecheap-ddns-update script, and gawk to parse the
response  
RUN apk add --update ca-certificates curl bash gawk  
  
# Copy files  
COPY docker /docker  
  
# Environment variables  
ENV DOMAIN_ARGS none  
ENV INTERVAL 60  
# Command  
CMD ["bash", "/docker/entrypoint.sh" ]  

