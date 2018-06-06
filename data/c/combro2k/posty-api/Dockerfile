FROM combro2k/ruby-rvm:latest  
  
MAINTAINER Martijn van Maurik <docker@vmaurik.nl>  
  
# Environment variables  
ENV HOME "${APP_HOME}"  
ENV INSTALL_LOG "${APP_HOME}/build.log"  
ENV RACK_ENV "production"  
# Add first the scripts to the container  
ADD resources/bin/ /usr/local/bin/  
  
# Run the installer script  
RUN /bin/bash -l -c 'bash /usr/local/bin/setup.sh build'  
  
ADD resources/home/ /home/  
  
# Run the last bits and clean up  
RUN /bin/bash -l -c '/usr/local/bin/setup.sh post_install | tee -a
${INSTALL_LOG} > /dev/null 2>&1'  
  
WORKDIR /home/app/posty_api  
  
VOLUME /var/vmail  
  
EXPOSE 9292  
CMD ["/usr/local/bin/run"]  

