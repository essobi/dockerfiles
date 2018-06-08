# Base image  
FROM alpine  
  
# Upgrade is mandatory to install incron and kafkacat  
RUN apk update  
RUN apk upgrade  
  
# Install bash because alpine's own sh is too simple  
# to run route_file.sh script (Array)  
RUN apk add bash  
  
# Install kafkacat  
RUN apk --no-cache add ca-certificates wget  
RUN wget --quiet --output-document=/etc/apk/keys/sgerrand.rsa.pub
https://alpine-pkgs.sgerrand.com/sgerrand.rsa.pub  
RUN wget https://github.com/sgerrand/alpine-pkg-
kafkacat/releases/download/1.3.1-r0/kafkacat-1.3.1-r0.apk  
RUN apk add --no-cache kafkacat-1.3.1-r0.apk  
  
# Install incron  
RUN apk add incron  
  
# Config monitoring  
ADD monitoring.conf /etc/incron.d  
  
# Install routing script  
RUN mkdir /opt  
ADD route_file.sh /opt/  
RUN chmod a+x /opt/route_file.sh  
  
# Create shared directory for config of file routes  
RUN mkdir -p /etc/routes  
  
# Create directory for FTP sharing  
RUN mkdir -p /var/monitored  
  
# Start container  
CMD ["/usr/sbin/incrond", "-n"]  

