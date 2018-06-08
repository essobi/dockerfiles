FROM alejandrofcarrera/phusion.node  
MAINTAINER Alejandro F. Carrera  
  
ADD ./files/config.json /home/config.json  
ADD ./files/swagger.json /home/swagger.json  
  
# Configure runit  
ADD ./my_init.d/ /etc/my_init.d/  
ONBUILD ADD ./my_init.d/ /etc/my_init.d/  
  
CMD ["/sbin/my_init"]  
  
WORKDIR /usr/lib  
  
EXPOSE 8080  

