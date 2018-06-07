FROM labengine/ubuntu  
LABEL maintainer="Fusengine <info@fusengine.ch>"  
  
# Add and fix permissions => install-deluge.sh  
ADD scripts/install-deluge.sh /root/install-deluge.sh  
RUN chmod 775 /root/install-deluge.sh  
  
# Add and fix permissions => start.sh  
ADD scripts/start.sh /start.sh  
RUN chmod 775 /start.sh  
  
# Start install package  
RUN ./root/install-deluge.sh  
  
# Volume  
VOLUME ["/data", "/root/Downloads"]  
  
# Expose port  
EXPOSE 8112 53160 53160/udp 5884  
ENTRYPOINT ["/bin/bash", "/start.sh"]  

