FROM debian:jessie  
  
MAINTAINER Potiguar Faga <potz@potz.me>  
  
# Install only the English version.  
ENV LINGUAS=en  
  
RUN apt-get update && \  
apt-get install -y git-core build-essential \  
autoconf intltool libtool guile-2.0-dev swig2.0 \  
libxml2-dev libxslt1-dev xsltproc \  
libdbi-dev libdbd-sqlite3 libgnomecanvas2-dev \  
libgoffice-0.8-dev libgnome-desktop-dev \  
libwebkit-dev && \  
git clone https://github.com/GnuCash/gnucash /tmp/build && \  
cd /tmp/build && git checkout 2.6.14 && \  
./autogen.sh && \  
./configure --enable-compile-warnings && \  
make && make install && ldconfig && \  
rm -rf /tmp/build && \  
apt-get remove \--purge -y git-core \  
build-essential autoconf intltool libtool && \  
rm -rf /var/lib/apt/lists  
  
CMD [ "/usr/local/bin/gnucash", "--logto", "stderr" ]  

