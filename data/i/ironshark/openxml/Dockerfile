FROM phusion/baseimage:latest  
MAINTAINER Daniel Korger <korger@ironshark.de>  
  
WORKDIR /root  
  
# install requirements  
ENV DEBIAN_FRONTEND noninteractive  
RUN dpkg --add-architecture i386 \  
&& add-apt-repository -y ppa:ubuntu-wine/ppa \  
&& apt-get update -y \  
&& apt-get install -y --no-install-recommends \  
libcups2 \  
unoconv \  
imagemagick \  
ghostscript \  
supervisor \  
wine1.7 \  
winetricks \  
xvfb \  
wget \  
curl  
ENV DEBIAN_FRONTEND text  
  
# set wine ENV vars  
ENV WINEPREFIX /root/.wine  
ENV WINEARCH win32  
  
# Install .NET Framework 4.0  
RUN wine wineboot && xvfb-run winetricks --unattended dotnet40 corefonts  
  
# LibreOffice  
ADD .config .config  
RUN wget
"http://mirror3.layerjet.com/tdf/libreoffice/stable/4.3.7/deb/x86_64/LibreOffice_4.3.7_Linux_x86-64_deb.tar.gz"  
RUN tar xvf LibreOffice_*.tar.gz  
WORKDIR LibreOffice_4.3.7.2_Linux_x86-64_deb/DEBS  
RUN dpkg -i *.deb  
WORKDIR ../..  
RUN rm -Rf LibreOffice*  
  
# update unoconv LibreOffice  
RUN rm -R /usr/lib/libreoffice  
RUN ln -s /opt/libreoffice4.3 /usr/lib/libreoffice  
  
# clean up  
RUN apt-get clean \  
&& apt-get clean autoclean \  
&& apt-get autoremove -y \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

