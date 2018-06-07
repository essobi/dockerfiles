FROM docker.io/ubuntu:latest  
MAINTAINER Yoshiaki Kawazu kawazzz@gmail.com  
  
RUN \  
apt-get update && \  
apt-get install -y vlc curl && \  
apt-get clean && \  
url="http://s3.amazonaws.com/AirVideoHD/Download/AirVideoServerHD-2.1.0-alpha1-u1.tar.bz2"
&& \  
dir="/opt/AirVideoServerHD" && \  
mkdir -p "$dir" && curl -L "$url" | tar xj -C "$dir"  
  
WORKDIR /opt/AirVideoServerHD  
  
EXPOSE 45601 45633  
VOLUME [ "/data" ]  
  

