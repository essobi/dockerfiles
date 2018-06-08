# Base docker image  
FROM ubuntu:17.04  
LABEL maintainer "Prasad Tengse <https://github.com/tprasadtp/minchu>"  
  
ENV DEBIAN_FRONTEND noninteractive  
ARG container-user=gnome-builder  
ENV HOME /home/gnome-builder  
# Install essentials  
RUN apt-get update && apt-get install -y libx11-dev libxext-dev libxrender-dev
libxtst-dev libxt-dev ccache make gcc g++ build-essential  
RUN apt-get update && apt-get install -y \  
git \  
make \  
dh-make \  
flatpak \  
ninja-build \  
gnome-builder \  
libxext-dev \  
libxrender-dev\  
libxtst-dev \  
sudo \  
libgtop-2.0 \  
gir1.2-glib-2.0 \  
gir1.2-gtk-3.0 \  
libgtk-3-0\  
glib-2.0 \  
libgcc1 \  
valac  
  
# Add gnome-builder user  
ENV HOME /home/gnome-builder  
RUN useradd --create-home --home-dir $HOME gnome-builder \  
&& gpasswd -a gnome-builder audio \  
&& chown -R gnome-builder:gnome-builder $HOME  
  
RUN sudo adduser gnome-builder sudo  
ENV HOME /home/gnome-builder  
  
# Run gnome-builder as non privileged user  
USER gnome-builder  
WORKDIR $HOME  
# Autorun  
ENTRYPOINT [ "gnome-builder" ]  

