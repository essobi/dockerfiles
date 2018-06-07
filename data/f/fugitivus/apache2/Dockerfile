#apache2 container for general purpose and teaching students:  
FROM fugitivus/debian:jessie  
MAINTAINER fugitivus <fugitivus@gmx.net>  
  
#environment-variables for non-interactive shell:  
#ENV DEBIAN_FRONTEND noninteractive  
#install updates, some packages and do cleanup:  
RUN apt-get update && apt-get upgrade -y\  
&& apt-get install apache2 php5 php5-mysql -y\  
&& apt-get clean autoclean\  
&& apt-get autoremove -y\  
&& rm -rf /var/lib/{apt,dpkg,cache,log}/  
  
#start apache2 as a service  
CMD ["/etc/init.d/apache2", "start"]  

