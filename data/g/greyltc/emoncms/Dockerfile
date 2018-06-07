# Arch Linux container with emoncms  
FROM greyltc/lamp-aur  
MAINTAINER Grey Christoforo <grey@christoforo.net>  
  
# install emoncms  
ADD setupEmoncms.sh /usr/sbin/setup-emoncms  
RUN setup-emoncms  
  
CMD start-servers; sleep infinity  

