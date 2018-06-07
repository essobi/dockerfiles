FROM debian:latest  
MAINTAINER Linux-Fan, Ma_Sys.ma <Ma_Sys.ma@web.de>  
LABEL Description="Evaluate the possibility of using Docker with 3D graphics"  
RUN \  
if ping -w 1 -c 1 192.168.1.16; then \  
sed "s/httpredir.debian.org/192.168.1.16/g" \  
/etc/apt/sources.list > /tmp/list; \  
cp /tmp/list /etc/apt/sources.list && rm /tmp/list; \  
fi; \  
apt-get update && apt-get install -y mesa-utils  
ENTRYPOINT [ "/usr/bin/glxinfo" ]  

