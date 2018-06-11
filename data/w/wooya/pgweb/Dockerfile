FROM ubuntu:14.04  
MAINTAINER Wu Young <doomsplayer@gmail.com>  
  
RUN apt-get update && \  
apt-get install -y wget unzip && \  
rm -rf /var/lib/apt/lists/*  
  
ENV PGWEB_VERSION 0.9.6  
RUN \  
cd /tmp && \  
wget
https://github.com/sosedoff/pgweb/releases/download/v$PGWEB_VERSION/pgweb_linux_amd64.zip
&& \  
unzip pgweb_linux_amd64.zip -d /app && \  
rm -f pgweb_linux_amd64.zip  
  
RUN useradd -ms /bin/bash pgweb  
  
USER pgweb  
WORKDIR /app  
  
EXPOSE 8081  
CMD ["sh", "-c", "/app/pgweb_linux_amd64 -s --bind=0.0.0.0 --url=${PGURL:-''}
\--ssl ${PGSSL:-require}"]  

