FROM debian:stretch  
MAINTAINER Jay Davé <jay.dave@datadoghq.com>  
  
RUN apt-get update -y  
RUN apt-get -y install wkhtmltopdf-dbg  
RUN apt-get -y install xvfb  
  
RUN chmod 755 /usr/bin/wkhtmltopdf  
RUN chmod 755 /usr/bin/wkhtmltoimage  
  
# Add start script  
ADD start.sh /usr/bin/start.sh  
RUN chmod 755 /usr/bin/start.sh

