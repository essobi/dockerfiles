# vim:set ft=dockerfile:  
# VERSION 1.0  
# AUTHOR: Alexander Turcic <alex@zeitgeist.se>  
# DESCRIPTION: Nero Linux in a Docker container  
# TO_BUILD: docker build --rm -t zeitgeist/docker-nero .  
# SOURCE: https://github.com/alexzeitgeist/docker-nero  
# Pull base image.  
FROM debian:jessie  
MAINTAINER Alexander Turcic "alex@zeitgeist.se"  
# Install dependencies.  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
fonts-droid \  
libc6 \  
libcanberra-gtk-module \  
libglib2.0-0 \  
libgtk2.0-0 \  
libstdc++6 \  
mpg123 \  
xfonts-base && \  
rm -rf /var/lib/apt/lists/*  
  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
wget && \  
rm -rf /var/lib/apt/lists/*  
  
RUN \  
wget
http://ftp20.us.nero.com//software/NeroLINUX/nerolinux-4.0.0.0b-x86_64.deb  
#COPY nerolinux-4.0.0.0b-x86_64.deb nerolinux-4.0.0.0b-x86_64.deb  
# Install Nero  
RUN \  
apt-get update && \  
{ dpkg -i nerolinux-4.0.0.0b-x86_64.deb || true; } && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y -f && \  
rm -rf /var/lib/apt/lists/*  
# Nero-specific fixes  
RUN \  
mkdir /usr/lib64 && \  
ln -s /usr/lib/nero /usr/lib64 && \  
cp /usr/lib/nero/libISOFS.so /usr/lib/nero/libUDFImporter.so /usr/lib  
# Setup user environment. Replace 1000 with your user / group id.  
RUN \  
export uid=1000 gid=1000 && \  
groupadd --gid ${gid} user && \  
useradd --uid ${uid} --gid ${gid} --create-home user && \  
addgroup user cdrom  
  
USER user  
WORKDIR /home/user  
  
# Enable below if we want to supply a Nero Linux config file  
#COPY config /home/user/  
#RUN \  
# mkdir .nero && \  
# cp config /home/user/.nero  
  
CMD ["/usr/bin/nero"]  

