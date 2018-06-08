FROM debian:stretch  
MAINTAINER Jan Harsa <j.harsa@gmail.com>  
  
ENV TERM xterm  
ENV USER_UID 1000  
ENV USER_NAME dockuser  
ENV USER_HOME /home/dockuser  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get dist-upgrade -y && \  
apt-get clean -y && apt-get autoclean -y && apt-get autoremove -y && \  
rm -rf /var/lib/apt/lists/* /var/lib/log/* /tmp/* /var/tmp/* && \  
useradd -ms /bin/bash -u $USER_UID $USER_NAME  
  
CMD ["/bin/bash"]  

