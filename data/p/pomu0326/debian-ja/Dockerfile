FROM debian:jessie  
  
RUN echo 'Asia/Tokyo' > /etc/timezone \  
&& dpkg-reconfigure -f noninteractive tzdata \  
&& sed -i.bak -e 's|deb.debian.org|ftp.jp.debian.org|g' /etc/apt/sources.list  

