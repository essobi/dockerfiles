FROM node:7-slim  
MAINTAINER rainu <rainu@raysha.de>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
ENV ATOM_LINK https://github.com/atom/atom/releases/download/v1.13.1/atom-
amd64.deb  
RUN apt-get update &&\  
apt-get install -y --no-install-recommends git libgtk2.0-0 libnotify4 libxtst6
gconf2 gconf-service libnss3 libasound2 gvfs-bin xdg-utils &&\  
wget -nv $ATOM_LINK -O /tmp/atom-amd64.deb &&\  
dpkg --install /tmp/atom-amd64.deb &&\  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
#make home directory for atom user  
RUN export uid=1000 gid=1000 && \  
mkdir -p /home/atom && \  
echo "atom:x:${uid}:${gid}:atom User,,,:/home/atom:/bin/bash" >> /etc/passwd
&& \  
echo "atom:x:${uid}:" >> /etc/group && \  
chown ${uid}:${gid} -R /home/atom  
  
COPY start.sh /home/atom/atom.sh  
  
ENTRYPOINT ["/home/atom/atom.sh", "-f"]  
CMD [""]  

