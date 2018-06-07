FROM ubuntu:xenial  
MAINTAINER Andrey Arapov <andrey.arapov@nixaid.com>  
  
# To avoid problems with Dialog and curses wizards  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get -y install build-essential libgtk-3-dev libindicator3-dev git-core \  
fakeroot dpkg-dev  
  
ENV USER user  
ENV UID 1000  
ENV HOME /home/$USER  
RUN useradd -u $UID -m -d $HOME -s /usr/sbin/nologin $USER  
  
USER $USER  
WORKDIR $HOME  
  
ENV REPO indicator-systemtray-unity  
ENV REL master  
CMD curl -L -o arch.tar.gz https://github.com/GGleb/$REPO/archive/$REL.tar.gz
&& \  
tar xpzf arch.tar.gz && \  
rm -f arch.tar.gz && \  
cd $REPO-$REL && \  
sed -i 's;glib-compile-schemas $(DESTDIR)/usr/share/glib-2.0/schemas/;;g'
Makefile && \  
dpkg-buildpackage -rfakeroot -b && \  
find $HOME/ -xdev -type f -name "*.deb" -exec cp -v '{}' /out \;  

