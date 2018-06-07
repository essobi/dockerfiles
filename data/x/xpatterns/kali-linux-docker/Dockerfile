FROM kalilinux/kali-linux-docker  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get -y update && apt-get -y dist-upgrade && apt-get clean &&\  
apt-get -y update && apt-cache search kali-linux &&\  
apt-get -y install kali-linux-full  
  
CMD ["/bin/bash"]  

