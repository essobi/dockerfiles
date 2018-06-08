FROM schlothauer/d_apache2.4:0.3  
RUN echo "deb http://ftp.de.debian.org/debian jessie-backports main" >>
/etc/apt/sources.list && \  
apt-get update && \  
apt-get install -y --force-yes autoconf libtool libmapnik-dev apache2-dev
libmapnik2.2 libmapnik-dev mapnik-utils python-mapnik && \  
rm -rf /var/lib/apt/lists/* && \  
find /usr/share/doc -depth -type f ! -name copyright|xargs rm || true && \  
find /usr/share/doc -empty|xargs rmdir || true && \  
rm -rf /usr/share/man/* /usr/share/groff/* /usr/share/info/* && \  
rm -rf /usr/share/lintian/* /usr/share/linda/* /var/cache/man/*  
  
COPY mod_tile.tar.gz /opt/mod_tile/mod_tile.tar.gz  
RUN cd /opt/mod_tile && tar -xzf mod_tile.tar.gz && cd
mod_tile-6c2cb243e4c8b047950ab8062cd66245f20a5d2f && \  
./autogen.sh && ./configure && make && make install && make install-mod_tile  
  
RUN /sbin/ldconfig  
  
COPY boundaries.tbz /opt/boundaries.tbz  
RUN cd /opt && tar -xjf boundaries.tbz  
  
COPY startTileServer.sh /startTileServer.sh  
ADD test /opt/osm/test  
COPY mod_tile.conf /etc/apache2/conf-enabled  
  
COPY renderd.conf /etc/renderd.conf  
COPY mapnik.tgz /opt/mapnik.tgz  
  
RUN cd /opt && tar -xzf mapnik.tgz  
RUN rm -f /opt/*.tgz  
RUN rm -f /opt/*.tbz  
  
RUN a2dismod auth_openidc ssl  
  
CMD ["/startTileServer.sh"]  

