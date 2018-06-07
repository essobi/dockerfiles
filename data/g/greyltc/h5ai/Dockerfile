FROM greyltc/lamp-aur  
MAINTAINER Grey Christoforo <grey@christoforo.net>  
  
# remove info.php  
RUN rm /srv/http/info.php  
  
# uncomment this to update the container's mirrorlist  
RUN get-new-mirrors  
  
# install h5ai  
ADD setup-h5ai.sh /usr/sbin/setup-h5ai  
RUN setup-h5ai  
  
# set some default variables for the startup script  
ENV REGENERATE_SSL_CERT false  
ENV START_APACHE true  
ENV START_MYSQL false  
EXPOSE 80  
ENV APACHE_ENABLE_PORT_80 true  
  
# start the servers, then wait forever  
CMD start-servers; sleep infinity  

