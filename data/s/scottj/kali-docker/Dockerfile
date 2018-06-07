FROM kalilinux/kali-linux-docker  
MAINTAINER scott.johnson+docker@gmail.com  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get -y update && apt-get -y dist-upgrade &&\  
apt-get -y install htop dirb kali-linux-top10 &&\  
apt-get clean  
  
CMD ["/bin/bash"]  

