FROM mysql:5.6  
MAINTAINER Dmitry Schegolikhin <d.shegolihin@gmail.com>  
  
# Let the conatiner know that there is no tty  
ENV DEBIAN_FRONTEND noninteractive  
  
ADD /config /config  
RUN cp /config/my.cnf /etc/my.cnf  

