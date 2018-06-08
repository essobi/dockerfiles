FROM galeone/archlinux-updated-aur  
MAINTAINER Paolo Galeone <nessuno@nerdz.eu>  
  
USER aur  
RUN pacaur -Su sudo base-devel nginx subversion libunistring git imagemagick
python2 python-virtualenv \  
nodejs libjpeg-turbo texlive-bin tidyhtml optipng \  
libtheora libvorbis libx264 libvpx redis python-pip wget ghostscript openexr
openjpeg2 libwmf \  
librsvg libxml2 libwebp ladspa libvdpau yasm hardening-wrapper yajl perl \  
libaacplus libsndfile libbs2b opencl-headers shine vo-aacenc vo-amrwbenc
--noconfirm  
  
RUN mkdir /tmp/deck  
  
COPY decklink-pkgbuild /tmp/deck/PKGBUILD  
COPY Blackmagic_DeckLink_SDK_10.3.zip /tmp/deck/  
  
RUN pacaur -S glu qt4 --noconfirm  
  
RUN cd /tmp/deck && makepkg && sudo pacman -U decklink-sdk*.xz --noconfirm  
  
RUN gpg --no-tty --keyserver pgp.mit.edu --recv-keys
FCF986EA15E6E293A5644F10B4322F04D67658D8  
RUN pacaur -S jdk8-openjdk jdk7-openjdk java-runtime-common --noconfirm  
RUN pacaur -S ffmpeg-full --noconfirm  
RUN pacaur -S python2-pip python2-celery python2-flask jhead librsvg npm
--noconfirm  
  
USER root  
RUN npm install -g coffee-script  
  
EXPOSE 9999  
VOLUME /home/mediacrush  
COPY startup.sh /opt/  
  
RUN useradd -m -s /bin/bash mediacrush  
USER mediacrush  
ENTRYPOINT bash /opt/startup.sh  

