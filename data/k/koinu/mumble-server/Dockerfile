FROM ubuntu:xenial  
  
ARG DEBIAN_FRONTEND=noninteractive  
  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys
22C54CD5AAE0971730875E0285DECED27F05CF9E \  
&& echo "deb http://ppa.launchpad.net/mumble/release/ubuntu xenial main" >
/etc/apt/sources.list.d/mumble.list \  
&& apt-get update \  
&& apt-get install -y mumble-server=1.2.19-1~ppa4~xenial1 \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
USER mumble-server  
  
EXPOSE 64738/tcp 64738/udp  
  
CMD ["murmurd", "-fg", "-ini", "/murmur/murmur.conf"]  

