FROM debian:jessie  
  
RUN apt-get update \  
&& apt-get install -y dpkg-dev dpkg-sig apt-utils \  
&& rm -rf /var/lib/apt/lists/*  
  
ADD apt-repo-update /bin/apt-repo-update  

