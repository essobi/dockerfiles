FROM nginx:stable  
MAINTAINER Ceroic <ops@ceroic.com>  
  
# Add the backports repo so we can install certbot  
RUN echo "deb http://ftp.debian.org/debian jessie-backports main" >>
/etc/apt/sources.list.d/jessie-backports.list  
  
# Update and install certbot  
RUN apt-get update && apt-get install -y -t jessie-backports certbot  
  
# Add our generate command  
COPY generate-certs.sh /usr/bin/generate-certs  
RUN chmod +x /usr/bin/generate-certs  
  
# Add our working directories  
RUN mkdir -p /var/local/certbot/challenges  
RUN mkdir -p /var/local/certbot/in  
RUN mkdir -p /var/local/certbot/out  
  
CMD ["generate-certs"]

