FROM alpine:3.5  
MAINTAINER jn.germon@meuhmeuhconcept.com  
  
# Install packages  
RUN apk update && \  
apk add \  
bash \  
supervisor \  
postfix \  
opendkim \  
rsyslog \  
cyrus-sasl && \  
apk del --no-cache && \  
rm -rf /var/cache/apk/*  
  
# Add installation file  
ADD assets/* /opt/  
  
# Run  
CMD ["/opt/install.sh"]  

