FROM node:latest  
# Add repo for php 7 stuff as it does not get php7 by default???  
RUN echo 'deb http://packages.dotdeb.org jessie all' >
/etc/apt/sources.list.d/dotdeb.list  
RUN curl http://www.dotdeb.org/dotdeb.gpg | apt-key add -  
  
# get the needed  
RUN apt-get update \  
&& apt-get install -y \  
php7.0 \  
zip \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN curl --silent --show-error https://getcomposer.org/installer | php  
  
CMD [ "node" ]  

