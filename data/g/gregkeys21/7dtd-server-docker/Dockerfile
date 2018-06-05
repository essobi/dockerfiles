FROM debian:latest  
  
MAINTAINER mudfly  
  
# Install dependencies  
RUN dpkg --add-architecture i386 && apt-get update && apt-get install -y \  
lib32gcc1 \  
wget \  
xmlstarlet \  
&& rm -rf /var/lib/apt/lists/*  
  
# Creates 7dtd server as a service  
WORKDIR /home/livingdead  
COPY serverconfig.xml serverconfig.xml  
COPY 7dtd.sh bin/7dtd  
  
# Expose the default 7dtd server port  
EXPOSE 26900-26902 26900-26902/udp 8080-8081/tcp  
  
CMD ["/home/livingdead/bin/7dtd"]  

