FROM phusion/baseimage  
ENV DEBIAN_FRONTEND=noninteractive  
  
#add this for mustache templates in config files  
ADD https://raw.githubusercontent.com/tests-always-included/mo/master/mo
/usr/bin/  
RUN chmod +x /usr/bin/mo  
  
RUN apt-get update && apt-get install gosu && apt-get -y upgrade  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

