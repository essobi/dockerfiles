FROM debian:jessie  
  
MAINTAINER nicolas.bonaldi@gmail.com  
  
WORKDIR /root  
  
RUN apt-get update && apt-get upgrade -y \  
&& apt-get install -y \  
git \  
&& git clone https://github.com/letsencrypt/letsencrypt \  
&& apt-get purge -y \  
git \  
&& apt-get autoremove -y \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR /root/letsencrypt  
  
RUN ./letsencrypt-auto --help all \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
ENTRYPOINT ["/root/letsencrypt/letsencrypt-auto"]  

