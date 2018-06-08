FROM ubuntu:16.04  
MAINTAINER Brandon Tomlinson ( thebwt@gmail.com )  
  
RUN apt-get update && apt-get install -y \  
mumble-server \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY mumble-server.ini /mumble/mumble-server.ini  
COPY mumble-server.sqlite /mumble/mumble-server.sqlite  
  
CMD chown -R mumble-server:mumble-server /mumble && murmurd -ini
/mumble/mumble-server.ini -fg  

