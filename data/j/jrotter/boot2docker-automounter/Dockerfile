#Based on jeffdh/docker-vboxguest  
FROM debian:latest  
RUN apt-get update && apt-get -y install --no-install-recommends \  
curl \  
bzip2 \  
p7zip-full \  
util-linux  
  
## Originally from boot2docker: Copyright 2014 Docker, Inc.  
ENV VBOX_VERSION 4.3.20  
ADD mounter.sh /mounter.sh  
RUN mkdir -p /vboxguest && \  
cd /vboxguest && \  
\  
curl -L -o vboxguest.iso
http://download.virtualbox.org/virtualbox/${VBOX_VERSION}/VBoxGuestAdditions_${VBOX_VERSION}.iso
&& \  
7z x vboxguest.iso -ir'!VBoxLinuxAdditions.run' && \  
rm vboxguest.iso && \  
\  
sh VBoxLinuxAdditions.run --noexec --target . && \  
mkdir amd64 && tar -C amd64 -xjf VBoxGuestAdditions-amd64.tar.bz2 && \  
rm VBoxGuestAdditions*.tar.bz2 && \  
\  
cp amd64/sbin/VBoxService /sbin && \  
rm -rf /vboxguest && \  
groupadd vboxsf && \  
sed -i 's/\r//' /mounter.sh && \  
chmod +x /mounter.sh  
  
CMD ["/mounter.sh"]  
  

