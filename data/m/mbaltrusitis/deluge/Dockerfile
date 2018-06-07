FROM mbaltrusitis/deb-base:wheezy  
  
ENV DELUGE_VERSION 1.3.11  
ENV BASE_URL http://download.deluge-torrent.org/source/  
ENV FILENAME deluge-$DELUGE_VERSION.tar.gz  
ENV LANG "C"  
RUN apt-get -q update && \  
apt-get install -qy --fix-missing \  
python-twisted \  
python-openssl \  
intltool \  
python-xdg \  
python-chardet \  
geoip-database \  
python-libtorrent \  
python-notify \  
python-pygame \  
python-glade2 \  
librsvg2-common \  
xdg-utils \  
python-mako \  
&& apt-get -y autoremove \  
&& apt-get -y clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /tmp/*  
  
RUN cd /tmp \  
&& curl -O $BASE_URL$FILENAME \  
&& tar -xvf $FILENAME \  
&& cd deluge-$DELUGE_VERSION \  
&& python setup.py build \  
&& python setup.py install \  
&& python setup.py install_data \  
&& cd / \  
&& rm -fr tmp/deluge-*  
  
ADD start.sh /start.sh  
RUN chmod u+x /start.sh  
  
# Torrent  
EXPOSE 53160  
EXPOSE 53160/udp  
# WebUI  
EXPOSE 8112  
# Daemon  
EXPOSE 58846  
CMD ["/start.sh"]  

