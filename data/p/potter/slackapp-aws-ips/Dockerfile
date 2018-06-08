FROM node:alpine  
MAINTAINER Potter Rafed <r.s.rafed@gmail.com>  
  
# Set working directory  
WORKDIR /var/www/html  
  
# Copy app and install dependencies  
ADD ./appcode /var/www/html  
  
#
-----------------------------------------------------------------------------  
# COPY SUPERVISOR CONF  
#
-----------------------------------------------------------------------------  
COPY supervisord/supervisord.conf /etc/  
COPY supervisord/conf.d /etc/supervisor/conf.d/  
  
#
-----------------------------------------------------------------------------  
# Copy Custom Run Command Script  
#
-----------------------------------------------------------------------------  
COPY /node/run.sh /usr/local/bin/  
  
#
-----------------------------------------------------------------------------  
# Install required packages & node modules  
#
-----------------------------------------------------------------------------  
RUN apk update && apk add supervisor \  
&& npm install --production \  
&& mkdir /etc/supervisord \  
&& chmod 755 /usr/local/bin/run.sh  
  
EXPOSE 80  
CMD ["/usr/local/bin/run.sh"]  

