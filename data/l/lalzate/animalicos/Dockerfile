#version 1  
FROM library/debian  
MAINTAINER Laura Alzate <gm.2012.laura.alzate@gmail.com>  
RUN apt-get update && apt-get install -y apache2 && \  
/etc/init.d/apache2 start  
EXPOSE 80  
CMD /usr/sbin/apache2ctl -D FOREGROUND  
  

