# Arch Linux container with node-red IoT wireer  
FROM greyltc/archlinux-aur  
MAINTAINER Grey Christoforo <grey@christoforo.net>  
# define a json flow file to load here  
ENV DEFAULT_FLOW ""  
# install node-red  
ADD setupNodeRed.sh /usr/sbin/setup-node-red  
RUN setup-node-red  
  
ADD runNodeRed.sh /usr/bin/run-node-red  
  
CMD run-node-red  

