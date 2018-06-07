FROM debian:stretch  
  
MAINTAINER Nikolas Lada <nikolas.lada@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
ENV TERM xterm  
ENV USER_UID 1000  
ENV USER_NAME nikolas  
ENV USER_HOME /home/nikolas  
  
RUN apt-get update && \  
apt-get dist-upgrade -y && \  
useradd -ms /bin/bash -u $USER_UID $USER_NAME && \  
apt-get clean -y && apt-get autoclean -y && apt-get autoremove -y && \  
rm -rf /var/lib/apt/lists/* /var/lib/log/* /tmp/* /var/tmp/*  
  
CMD ["/bin/bash"]  

