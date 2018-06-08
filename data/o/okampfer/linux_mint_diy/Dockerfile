FROM vcatechnology/base-linux-mint:18  
MAINTAINER Bruce Sun <okampfer@gmail.com>  
  
RUN apt-get update && \  
apt-get -y install sudo  
  
RUN adduser --disabled-password --gecos '' athrun && \  
adduser athrun sudo  
  
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers  
RUN mkdir /home/athrun/Downloads  
  
ENV USER=athrun  
USER athrun  
CMD /bin/bash  

