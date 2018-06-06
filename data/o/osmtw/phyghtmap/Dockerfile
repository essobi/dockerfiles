FROM osmtw/ubuntu:xenial  
MAINTAINER Rex Tsai "https://about.me/chihchun"  
RUN apt-get dist-upgrade -y \  
&& apt-get install -y wget  
RUN cd /tmp \  
&& wget http://katze.tfiu.de/projects/phyghtmap/phyghtmap_1.74-1_all.deb \  
&& ( dpkg -i phyghtmap_1.74-1_all.deb || true ) \  
&& apt-get install -f -y  
  
# Clean up APT when done  
RUN apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
WORKDIR /data  
CMD phyghtmap --version  

