FROM debian:latest  
MAINTAINER Linux-Fan, Ma_Sys.ma <Ma_Sys.ma@web.de>  
RUN \  
if ping -w 1 -c 1 192.168.1.16; then \  
sed "s/httpredir.debian.org/192.168.1.16/g" \  
/etc/apt/sources.list > /tmp/list; \  
cp /tmp/list /etc/apt/sources.list && rm /tmp/list; \  
fi; \  
apt-get update && apt-get \--no-install-recommends install -y gnat make  
ADD . /opt/program  
RUN make -C /opt/program  
ENTRYPOINT [ "/opt/program/ra_interpreter" ]  

