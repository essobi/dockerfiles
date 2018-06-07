FROM debian:stretch AS build  
# build dvdisaster  
ENV dvdisasterversion=dvdisaster-0.79.6  
RUN apt-get update -qq && \  
apt-get install -qq -y \  
build-essential \  
pkg-config \  
libgtk2.0-dev \  
libglib2.0-dev \  
wget \  
&& \  
wget -q -O /tmp/"$dvdisasterversion".tar.bz2
http://www.dvdisaster.com/downloads/"$dvdisasterversion".tar.bz2 \  
&& \  
tar xjf /tmp/"$dvdisasterversion".tar.bz2 -C /tmp \  
&& \  
rm /tmp/"$dvdisasterversion".tar.bz2 \  
&& \  
cd /tmp/"$dvdisasterversion" \  
&& \  
./configure \  
&& \  
make \  
&& \  
mv /tmp/"$dvdisasterversion"/dvdisaster /dvdisaster  
  
FROM jlesage/baseimage-gui:debian-8  
RUN apt-get update -qq \  
&& \  
apt-get install -qq -y \  
libgtk2.0-dev \  
lsscsi  
COPY \--from=build /dvdisaster /usr/local/bin/dvdisaster  
COPY rootfs/ /  
ENV APP_NAME="dvdisaster"  
# Generate and install favicons.  
RUN \  
APP_ICON_URL=https://upload.wikimedia.org/wikipedia/commons/8/81/Dvdisaster.png
&& \  
install_app_icon.sh "$APP_ICON_URL"  

