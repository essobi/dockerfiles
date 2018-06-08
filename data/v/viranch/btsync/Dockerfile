FROM ubuntu:14.04  
RUN apt-get update && apt-get install -y --no-install-recommends curl ca-
certificates && rm -rf /var/lib/apt/lists/*  
  
RUN curl -sL https://download-cdn.getsync.com/stable/linux-x64/BitTorrent-
Sync_x64.tar.gz | tar zx -C /usr/local/bin  
  
EXPOSE 3369/udp  
  
RUN curl -sL
https://github.com/jwilder/dockerize/releases/download/v0.0.2/dockerize-linux-
amd64-v0.0.2.tar.gz | tar zx -C /usr/local/bin  
  
ADD btsync.tmpl /etc/templates/  
  
CMD ["dockerize", "-template", "/etc/templates/btsync.tmpl:/etc/btsync.conf",
"btsync", "--nodaemon", "--config", "/etc/btsync.conf"]  

