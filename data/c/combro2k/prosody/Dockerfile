FROM combro2k/debian-debootstrap:8  
MAINTAINER Martijn van Maurik <docker@vmaurik.nl>  
  
# Environment variables  
ENV HOME=/root \  
INSTALL_LOG=/var/log/build.log  
  
# Add resources  
ADD resources/bin/ /usr/local/bin/  
  
RUN chmod +x /usr/local/bin/* && touch ${INSTALL_LOG} && /bin/bash -l -c
'/usr/local/bin/setup.sh build'  
  
# Add custom config  
ADD resources/etc/prosody/prosody.cfg.lua /etc/prosody/prosody.cfg.lua  
  
# Run the last bits and clean up  
RUN /bin/bash -l -c '/usr/local/bin/setup.sh post_install | tee -a
${INSTALL_LOG} > /dev/null 2>&1'  
  
EXPOSE 5000 5222 5223 5269 5280 5281 5347  
VOLUME /data  
  
CMD ["/usr/local/bin/run"]  
  

