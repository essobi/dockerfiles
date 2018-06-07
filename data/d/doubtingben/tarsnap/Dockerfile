FROM debian:jessie  
MAINTAINER Ben Wilson [doubtingben@gmail.com]  
  
RUN apt-get update && \  
apt-get install -y wget lsb-release locales && \  
wget -qO- https://pkg.tarsnap.com/tarsnap-deb-packaging-key.asc | apt-key add
- && \  
sh -c 'echo "deb http://pkg.tarsnap.com/deb/$(lsb_release -s -c) ./" >>
/etc/apt/sources.list.d/tarsnap.list' && \  
apt-get update && \  
apt-get install -y tarsnap  
  
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \  
dpkg-reconfigure --frontend=noninteractive locales && \  
update-locale LANG=en_US.UTF-8  
  
RUN echo -n 'cachedir /tarsnap/cache\n\  
keyfile /tarsnap/key\n\  
nodump\n\  
print-stats\n\  
checkpoint-bytes 1G\n' > /etc/tarsnap.conf  
  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
VOLUME ["/tarsnap", "/volume"]]  
  
CMD ["/bin/bash", "-c", "echo 'Available commands: ' && compgen -ca | grep
tarsnap | sort"]  

