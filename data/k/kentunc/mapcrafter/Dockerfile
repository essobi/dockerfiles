FROM debian:jessie  
  
RUN apt-get update && apt-get install -y \  
wget \  
lsb-release \  
apt-transport-https  
  
RUN echo "deb http://packages.mapcrafter.org/debian $(lsb_release -sc) main" |
tee /etc/apt/sources.list.d/mapcrafter.list \  
&& wget -O /etc/apt/trusted.gpg.d/mapcrafter.gpg
http://packages.mapcrafter.org/debian/keyring.gpg \  
&& apt-get update \  
&& apt-get install -y mapcrafter \  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR /root/share  
  
CMD mapcrafter --config render.conf --jobs "$(nproc --all)"  

