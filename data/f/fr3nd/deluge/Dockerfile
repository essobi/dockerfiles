FROM debian:jessie  
MAINTAINER Carles Amigó, fr3nd@fr3nd.net  
  
ENV DELUGE_VERSION 1.3.15  
RUN apt-get update && apt-get install -y \  
build-essential \  
geoip-database \  
intltool \  
librsvg2-common \  
python \  
python-chardet \  
python-glade2 \  
python-libtorrent \  
python-mako \  
python-notify \  
python-openssl \  
python-pygame \  
python-setuptools \  
python-twisted \  
python-xdg \  
supervisor \  
xdg-utils \  
&& rm -rf /usr/share/doc/* && \  
rm -rf /usr/share/info/* && \  
rm -rf /tmp/* && \  
rm -rf /var/tmp/*  
  
RUN mkdir -p /usr/src/deluge  
WORKDIR /usr/src/deluge  
RUN curl -L http://download.deluge-
torrent.org/source/deluge-${DELUGE_VERSION}.tar.xz | \  
tar xvJ --strip-components=1 && \  
python setup.py build && \  
python setup.py install --install-layout=deb && \  
rm -rf /usr/src/deluge  
WORKDIR /  
  
COPY supervisord.conf /etc/supervisor/supervisord.conf  
  
EXPOSE 8112 58846 58946 58946/udp  
  
CMD /usr/bin/supervisord -c /etc/supervisor/supervisord.conf  

