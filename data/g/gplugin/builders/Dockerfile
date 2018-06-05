FROM debian:buster  
  
MAINTAINER Gary Kramlich <grim@reaperworld.com>  
  
COPY debian/localepurge.selections /  
  
RUN set -ex && \  
debconf-set-selections -v /localepurge.selections && \  
apt-get update && \  
apt-get install -y --no-install-recommends localepurge && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists  
  
RUN set -ex && \  
apt-get update && \  
apt-get install -y --no-install-recommends \  
ca-certificates unzip devscripts fakeroot debhelper \  
build-essential meson gettext help2man xsltproc mercurial \  
libglib2.0-dev gobject-introspection libgirepository1.0-dev libgtk-3-dev \  
python3-dev python-gi-dev python3-gi \  
liblua5.1-0-dev lua-lgi luarocks \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists  
  
RUN set -ex && \  
luarocks install moonscript  
  
CMD ["/build.sh"]  
  
ENV DISTRIBUTION=testing \  
ARCH=amd64  
  
COPY debian/build.sh /build.sh  
  

