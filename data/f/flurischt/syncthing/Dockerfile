FROM ubuntu:xenial  
  
USER root  
  
RUN useradd -d "/home/syncthing" -u 1000 -m -s /bin/bash syncthing  
  
# need apt-transport to use syncthing repository  
RUN apt-get update && apt-get install -y apt-transport-https ca-certificates
curl  
  
# Install syncthing from repository  
RUN curl -s https://syncthing.net/release-key.txt | apt-key add -  
RUN echo "deb https://apt.syncthing.net/ syncthing stable" | tee
/etc/apt/sources.list.d/syncthing.list  
  
RUN apt-get update && apt-get install -y syncthing  
  
WORKDIR /home/syncthing  
  
VOLUME ["/home/syncthing/Sync", "/home/syncthing/.config"]  
  
EXPOSE 8384  
EXPOSE 22000  
EXPOSE 21027/udp  
  
USER syncthing  
CMD ["/usr/bin/syncthing"]  

