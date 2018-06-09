FROM debian:buster-slim  
  
USER root  
  
ENV DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get update && \  
apt-get install -y wget && \  
wget https://raw.githubusercontent.com/hyperion-
project/hyperion/master/bin/install_hyperion.sh && \  
chmod a+x ./install_hyperion.sh && \  
./install_hyperion.sh  
  
VOLUME ["/etc/hyperion"]  
  
CMD ["/usr/bin/hyperiond","/etc/hyperion/hyperion.config.json"]  
  

