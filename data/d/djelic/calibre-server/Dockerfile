#  
# build:  
# docker build -t calibre .  
#  
# run:  
# docker run -d -v /path/to/library:/opt/calibre/library --name calibre
calibre  
#  
FROM debian:testing  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update -y \  
&& apt-get dist-upgrade -y \  
&& apt-get install -y --no-install-recommends calibre \  
&& rm -rf /var/lib/apt/lists/*  
  
EXPOSE 8080  
RUN mkdir -p /opt/calibre/library  
VOLUME ["/opt/calibre/library"]  
  
ENTRYPOINT ["/usr/bin/calibre-server", "--with-library=/opt/calibre/library"]  

