FROM debian:sid  
  
MAINTAINER Jakob Runge <sicarius@g4t3.de>  
  
LABEL version="1.0.0" \  
source="https://github.com/runjak/docker-signal"  
  
COPY confs/local.conf /etc/fonts/local.conf  
  
RUN apt-get update \  
&& apt-get install -y chromium libexif12 \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY entrypoint.sh /  
  
Run chmod a+x /entrypoint.sh  
  
ENTRYPOINT [ "/entrypoint.sh" ]  

