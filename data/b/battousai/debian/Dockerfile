FROM debian:latest  
MAINTAINER Mauro Pinto <mauro.s.pinto@gmail.com>  
  
ADD etc /etc  
CMD /config/loop  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install --no-install-recommends -y ca-certificates inotify-tools nano
vim-tiny pwgen supervisor unrar unzip wget && \  
apt-get clean && \  
echo -n > /var/lib/apt/extended_states  
  
RUN mkdir /config /data  
ADD config /config  
RUN chmod +x /config/loop  

