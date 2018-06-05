FROM babim/ubuntubase:ssh  
  
COPY source.list/ /etc/apt/sources.list.d/  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV FREEFILESYNC 9.3_Ubuntu_16.04_64-bit  
ENV IPSCAN 3.5.1_amd64  
ENV CROSSOVER 16.2.5-1  
ENV WIMLIB 1.12.0  
RUN apt-get clean && dpkg --add-architecture i386 && \  
apt-get update && \  
apt-get install xubuntu-desktop --no-install-recommends -y --force-yes && \  
apt-get install nano filezilla mtr-tiny nload bmon iotop htop putty baobab
mousepad glogg file-roller firefox synaptic\  
regexxer fwbuilder font-manager gnome-subtitles mediainfo-gui gedit
qbittorrent inetutils-ping\  
gtkorphan screenruler zenmap nmap rsync mysql-client ristretto thunar-archive-
plugin\  
xfce4-taskmanager gnome-icon-theme-full tomboy p7zip-full mc pyrenamer\  
tightvncserver telnet\  
-y --force-yes && \  
apt-get purge sane* scan* transmission* abiword* gnumeric* parole* banshee*
totem* -y --force-yes  
# opera-stable google-chrome-stable  
# Wimlib  
RUN apt-get install -y libxml2-dev ntfs-3g-dev ntfs-3g libfuse-dev
libattr1-dev libssl-dev pkg-config build-essential automake && \  
cd /tmp && wget https://wimlib.net/downloads/wimlib-$WIMLIB.tar.gz && tar
xzvpf wimlib* && cd wimlib* && ./configure && make && make install && ldconfig
&& cd .. && \  
rm -rf /tmp/winlib*  
  
# crossover  
RUN apt-get install -y gcc-5-base:i386 gcc-6-base:i386 krb5-locales libavahi-
client3:i386 \  
libavahi-common-data:i386 libavahi-common3:i386 libbsd0:i386 libc6:i386 \  
libcomerr2:i386 libcups2:i386 libdbus-1-3:i386 libdrm-amdgpu1:i386 \  
libdrm-intel1:i386 libdrm-nouveau2:i386 libdrm-radeon1:i386 libdrm2:i386 \  
libedit2:i386 libelf1:i386 libexpat1:i386 libffi6:i386 libfreetype6:i386 \  
libgcc1:i386 libgcrypt20:i386 libgl1-mesa-dri:i386 libgl1-mesa-glx:i386 \  
libglapi-mesa:i386 libglu1-mesa:i386 libgmp10:i386 libgnutls30:i386 \  
libgpg-error0:i386 libgssapi-krb5-2:i386 libhogweed4:i386 libidn11:i386 \  
libk5crypto3:i386 libkeyutils1:i386 libkrb5-3:i386 libkrb5support0:i386 \  
liblcms2-2:i386 libllvm3.8:i386 liblzma5:i386 libnettle6:i386 \  
libp11-kit0:i386 libpciaccess0:i386 libpcre3:i386 libpng12-0:i386 \  
libselinux1:i386 libstdc++6:i386 libsystemd0:i386 libtasn1-6:i386 \  
libtinfo5:i386 libtxc-dxtn-s2tc0:i386 libudev1:i386 libx11-6:i386 \  
libx11-xcb1:i386 libxau6:i386 libxcb-dri2-0:i386 libxcb-dri3-0:i386 \  
libxcb-glx0:i386 libxcb-present0:i386 libxcb-sync1:i386 libxcb1:i386 \  
libxcursor1:i386 libxdamage1:i386 libxdmcp6:i386 libxext6:i386 \  
libxfixes3:i386 libxi6:i386 libxrandr2:i386 libxrender1:i386 \  
libxshmfence1:i386 libxxf86vm1:i386 zlib1g:i386 && \  
cd /tmp && wget http://media.matmagoc.com/crossover_$CROSSOVER.deb && dpkg -i
crossover*.deb && \  
rm -rf /opt/cxoffice/lib/wine/winewrapper.exe.so /tmp/crossover*  
COPY winewrapper.exe.so /opt/cxoffice/lib/wine/winewrapper.exe.so  
  
# freefile sync  
RUN wget http://media.matmagoc.com/FreeFileSync_$FREEFILESYNC.tar.gz && \  
tar -xzvpf FreeFileSync_$FREEFILESYNC.tar.gz -C /opt && rm -f
FreeFileSync_$FREEFILESYNC.tar.gz  
RUN mkdir -p /root/Desktop  
RUN cd /root/Desktop && wget http://media.matmagoc.com/FreeFileSync.desktop &&
\  
chmod +x /root/Desktop/FreeFileSync.desktop  
  
# navicat_premium  
RUN wget http://media.matmagoc.com/navicat_premium.tar.gz && \  
tar -xzvpf navicat_premium.tar.gz -C /opt && rm -f navicat_premium.tar.gz  
RUN cd /root/Desktop && wget http://media.matmagoc.com/navicat.desktop && \  
chmod +x /root/Desktop/navicat.desktop  
  
# razorsql  
RUN wget http://media.matmagoc.com/razorsql_linux_x64.tar.gz && \  
tar -xzvpf razorsql_linux_x64.tar.gz -C /opt && rm -f
razorsql_linux_x64.tar.gz && \  
wget http://media.matmagoc.com/razorsqlreg.tar.gz && \  
tar -xzvpf razorsqlreg.tar.gz -C /root && rm -f razorsqlreg.tar.gz  
RUN cd /root/Desktop && wget http://media.matmagoc.com/razorsql.desktop && \  
chmod +x /root/Desktop/razorsql.desktop  
  
# angry ip scanner  
RUN wget http://media.matmagoc.com/ipscan_$IPSCAN.deb && \  
apt-get install -y --force-yes \  
ca-certificates-java fonts-dejavu-extra java-common libbonobo2-0 \  
libbonobo2-common libgnome-2-0 libgnome2-common libgnomevfs2-0 \  
libgnomevfs2-common liborbit-2-0 openjdk-8-jre openjdk-8-jre-headless && \  
dpkg -i ipscan_$IPSCAN.deb && rm -f ipscan_$IPSCAN.deb  
  
# clean  
RUN apt-get purge build-essential automake -y && apt-get clean && \  
apt-get autoclean && \  
apt-get autoremove -y --purge  
#disable freerdp-x11 remmina virt-manager  
# Define default command.  
RUN echo '#!/bin/bash' > /startup.sh && \  
echo "service ssh start" >> /startup.sh && \  
echo "rm -rf /tmp/.X*" >> /startup.sh && \  
echo "USER=root" >> /startup.sh && \  
echo "HOME=/root" >> /startup.sh && \  
echo "export USER HOME" >> /startup.sh && \  
echo "vncserver :1" >> /startup.sh && \  
echo "bash" >> /startup.sh && chmod +x /startup.sh  
CMD ["/startup.sh"]  
  
# Expose ports.  
EXPOSE 5901 22  

