FROM alpine  
MAINTAINER Fabian Köster <mail@fabian-koester.com>  
  
# Install required packages  
RUN apk add --no-cache ssmtp trac  
  
USER tracd  
  
VOLUME /var/www/trac  
VOLUME /var/backups/trac  
  
COPY backup.sh /usr/local/bin/  
  
CMD /usr/bin/tracd -b 0.0.0.0 -p 8000 -s /var/www/trac/ --basic-
auth="trac,/var/www/trac/.htpass,Restricted"  
  
# The port(s) the server uses  
EXPOSE 8000  

