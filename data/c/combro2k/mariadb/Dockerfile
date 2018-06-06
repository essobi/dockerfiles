FROM combro2k/debian-debootstrap:8  
MAINTAINER Martijn van Maurik <docker@vmaurik.nl>  
  
# Environment variables  
ENV HOME=/root \  
INSTALL_LOG=/var/log/build.log \  
MARIA_DB_VERSION=10.1  
# Add first the scripts to the container  
ADD resources/bin/ /usr/local/bin/  
  
RUN chmod +x /usr/local/bin/* && touch ${INSTALL_LOG} && /bin/bash -l -c
'/usr/local/bin/setup.sh build'  
  
# Run the last bits and clean up  
RUN /bin/bash -l -c 'bash /usr/local/bin/setup.sh post_install' | tee -a
${INSTALL_LOG} > /dev/null 2>&1 || exit 1  
  
# Add VOLUMEs to allow backup of config and databases  
VOLUME ["/etc/mysql", "/var/lib/mysql"]  
  
EXPOSE 3306  
CMD ["/usr/local/bin/run"]  

