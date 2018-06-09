FROM debian:latest  
MAINTAINER Tomas Effenberger <effik@effik.cz>  
ADD etc /etc  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y locales ca-certificates inotify-tools nano pwgen supervisor
unrar unzip wget && \  
apt-get clean && \  
echo -n > /var/lib/apt/extended_states && \  
mkdir /config /data && \  
useradd -u 500 core  
ADD config /config  
RUN chmod +x /config/loop  
CMD /config/loop  

