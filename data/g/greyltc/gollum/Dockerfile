# Arch Linux container with gollum wiki server  
FROM greyltc/archlinux  
MAINTAINER Grey Christoforo <grey@christoforo.net>  
  
# uncomment this to update the container's mirrorlist  
#RUN get-new-mirrors  
# install gollum  
ADD setup-gollum.sh /usr/sbin/setup-gollum  
RUN setup-gollum  
  
ADD start-gollum.sh /usr/bin/start-gollum  
  
VOLUME /root/wiki  
  
EXPOSE 4567  
CMD start-gollum && sleep infinity  

