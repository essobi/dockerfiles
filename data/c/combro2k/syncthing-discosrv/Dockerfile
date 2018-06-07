FROM combro2k/debian-debootstrap:8  
MAINTAINER Martijn van Maurik <docker@vmaurik.nl>  
  
ENV INSTALL_LOG=/var/log/build.log  
  
ADD resources/bin/ /usr/local/bin/  
  
WORKDIR /opt/stdiscosrv  
  
# Run the installer script  
RUN /bin/bash -l -c 'bash /usr/local/bin/setup.sh build'  
  
# Run the last bits and clean up  
RUN /bin/bash -l -c 'bash /usr/local/bin/setup.sh post_install' | tee -a
${INSTALL_LOG} > /dev/null 2>&1 || exit 1  
  
VOLUME ["/var/stdiscosrv"]  
  
EXPOSE 8443/tcp  
  
CMD ["/usr/local/bin/run"]  

