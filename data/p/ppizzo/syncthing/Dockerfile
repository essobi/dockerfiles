FROM debian  
  
MAINTAINER pietro.pizzo@gmail.com  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get -y install curl gnupg && \  
curl -s https://syncthing.net/release-key.txt | apt-key add - && \  
echo "deb http://apt.syncthing.net/ syncthing release" | tee
/etc/apt/sources.list.d/syncthing.list && \  
apt-get update && apt-get -y install syncthing && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /usr/share/doc* /usr/share/man/*
/usr/share/info/* && \  
useradd -m -g 100 -u 1000 user  
  
EXPOSE 8384/tcp 22000/tcp 21027/udp  
  
USER user  
ENTRYPOINT ["syncthing", "-no-browser"]  

