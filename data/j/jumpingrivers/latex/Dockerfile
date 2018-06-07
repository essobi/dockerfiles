FROM debian:stretch  
  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get update \  
&& apt-get install -y \  
texlive-full \  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR /src  
CMD sleep 1  

