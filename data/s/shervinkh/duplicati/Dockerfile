FROM shervinkh/my-archlinux  
MAINTAINER "Shervin Khastoo" <shervinkh145@gmail.com>  
ENV VERSION=2.0.1.22  
ENV FULL_VERSION=2.0.1.22_experimental_2016-09-12  
RUN /update.sh && \  
pacman -S --noconfirm mono gtk-sharp-2 unzip && \  
wget -P /opt
https://github.com/duplicati/duplicati/releases/download/v${VERSION}-${FULL_VERSION}/duplicati-${FULL_VERSION}.zip
&& \  
unzip -d /opt/duplicati /opt/duplicati-${FULL_VERSION}.zip && \  
pacman -Rs --noconfirm unzip && \  
rm /opt/duplicati-${FULL_VERSION}.zip && \  
mkdir -p /data /backup && \  
/cleanup.sh  
COPY configs /etc/  
COPY scripts /scripts/  
EXPOSE 8200 9001  

