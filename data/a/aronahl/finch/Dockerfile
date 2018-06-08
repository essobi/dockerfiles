FROM ubuntu:14.04  
MAINTAINER https://github.com/aronahl  
WORKDIR /root/  
RUN apt-get update && apt-get install --no-install-recommends -fy \  
build-essential \  
gconf2 \  
intltool \  
libglib2.0-dev \  
libnss3-dev \  
libidn11-dev \  
libmeanwhile-dev \  
libncurses5-dev \  
libtool \  
libxml2-dev \  
mercurial \  
wget && \  
hg clone https://bitbucket.org/pidgin/main && \  
cd /root/main && \  
hg update v2.12.0 && \  
./autogen.sh --disable-gtkui --disable-gstreamer --disable-vv --disable-avahi
--disable-dbus --disable-perl --disable-tcl && \  
make install && \  
cd /root && \  
rm -fr main && \  
wget https://github.com/Yelp/dumb-init/releases/download/v1.1.3/dumb-
init_1.1.3_amd64.deb && \  
dpkg -i dumb-init_*.deb && \  
rm dumb-init_*.deb && \  
apt-get remove -y \  
build-essential \  
mercurial \  
intltool \  
libtool \  
wget && \  
apt-get autoclean -y && \  
apt-get clean -y && \  
apt-get autoremove -y && \  
rm -rf /var/lib/apt/lists/*  
VOLUME /root/.purple  
ENV LD_LIBRARY_PATH=/usr/local/lib:/usr/lib:/lib  
CMD /usr/bin/dumb-init /usr/local/bin/finch  

