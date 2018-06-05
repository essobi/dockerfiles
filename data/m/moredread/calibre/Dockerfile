# vim:set ft=dockerfile:  
# VERSION 1.0  
# AUTHORS: Alexander Turcic <alex@zeitgeist.se>  
# André-Patrick Bubel <code@andre-bubel.de>  
# DESCRIPTION: Latest version of calibre (with GUI) in a Docker container  
# TO_BUILD: docker build --rm -t moredread/docker-calibre .  
# SOURCE: https://github.com/moredread/docker-calibre  
# FORKED FROM: https://github.com/alexzeitgeist/docker-calibre  
# Pull base image.  
FROM debian:testing  
MAINTAINER André-Patrick Bubel "code@andre-bubel.de"  
  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get dist-upgrade -y && \  
rm -rf /var/lib/apt/lists/*  
  
# Install dependencies.  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
dbus-x11 \  
fonts-liberation \  
imagemagick \  
libjs-mathjax \  
locales \  
poppler-utils \  
python-apsw \  
python-beautifulsoup \  
python-chardet \  
python-cherrypy3 \  
python-cssselect \  
python-cssutils \  
python-dateutil \  
python-dbus \  
python-dnspython \  
python-feedparser \  
python-imaging \  
python-lxml \  
python-markdown \  
python-mechanize \  
python-netifaces \  
python-pil \  
python-pkg-resources \  
python-psutil \  
python-pygments \  
python-pyparsing \  
# python-qt4 \  
python-pyqt5 \  
python-pyqt5.qtsvg \  
python-pyqt5.qtwebkit \  
python-routes \  
python2.7 \  
wget \  
xdg-utils \  
xz-utils && \  
rm -rf /var/lib/apt/lists/*  
  
# Install optional fonts (non-western). Can be commented out if not needed.  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
fonts-arphic-ukai \  
fonts-arphic-uming \  
fonts-gfs-artemisia \  
fonts-ipafont-gothic \  
fonts-ipafont-mincho \  
fonts-unfonts-core && \  
rm -rf /var/lib/apt/lists/*  
  
# Set locale.  
RUN \  
sed -i 's/^[^#].*$/# &/' /etc/locale.gen && \  
sed -i 's/^# \\(en_US.UTF-8 UTF-8\\).*$/\1/' /etc/locale.gen && \  
locale-gen && \  
update-locale LANGUAGE=en_US:en LANG=en_US.UTF-8  
  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
# Install calibre latest version.  
RUN \  
wget -nv -O-
https://raw.githubusercontent.com/kovidgoyal/calibre/master/setup/linux-
installer.py | \  
python -c "import sys; main=lambda:sys.stderr.write('Download failed\n');
exec(sys.stdin.read()); main()" && \  
rm -rf /tmp/*  
  
# Setup user environment. Replace 1000 with your user / group id.  
RUN \  
export uid=1000 gid=1000 && \  
groupadd --gid ${gid} user && \  
useradd --uid ${uid} --gid ${gid} --create-home user  
  
USER user  
WORKDIR /home/user  
VOLUME /home/user  
  
ENV QT_XKB_CONFIG_ROOT=/usr/share/X11/xkb  
  
# Expose port for calibre-server.  
EXPOSE 8080  
  
CMD ["/usr/bin/calibre"]  

