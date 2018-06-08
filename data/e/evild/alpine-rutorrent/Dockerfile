FROM evild/alpine-php:7.0.4  
  
MAINTAINER Dominique HAAS <contact@dominique-haas.fr>  
  
  
ENV MEDIAINFO_VER=0.7.82 \  
RTORRENT_VER=0.9.6 \  
LIBTORRENT_VER=0.13.6 \  
PKG_CONFIG_PATH=/usr/local/lib/pkgconfig  
  
RUN \  
build_pkgs="build-base git libtool automake autoconf wget subversion cppunit-
dev openssl-dev ncurses-dev curl-dev" \  
&& runtime_pkgs="ffmpeg ca-certificates curl gzip zip unrar supervisor geoip"
\  
&& apk --no-cache add ${build_pkgs} ${runtime_pkgs} \  
&& cd /tmp \  
&& git clone https://github.com/esmil/mktorrent \  
&& svn checkout http://svn.code.sf.net/p/xmlrpc-c/code/stable xmlrpc-c \  
&& git clone https://github.com/rakshasa/libtorrent.git \  
&& git clone https://github.com/rakshasa/rtorrent.git \  
&& wget
http://mediaarea.net/download/binary/mediainfo/${MEDIAINFO_VER}/MediaInfo_CLI_${MEDIAINFO_VER}_GNU_FromSource.tar.gz
\  
&& wget
http://mediaarea.net/download/binary/libmediainfo0/${MEDIAINFO_VER}/MediaInfo_DLL_${MEDIAINFO_VER}_GNU_FromSource.tar.gz
\  
&& tar xzf MediaInfo_DLL_${MEDIAINFO_VER}_GNU_FromSource.tar.gz \  
&& tar xzf MediaInfo_CLI_${MEDIAINFO_VER}_GNU_FromSource.tar.gz \  
&& cd /tmp/mktorrent \  
&& make -j $(getconf _NPROCESSORS_ONLN) \  
&& make install \  
&& cd /tmp/MediaInfo_DLL_GNU_FromSource \  
&& ./SO_Compile.sh \  
&& cd /tmp/MediaInfo_DLL_GNU_FromSource/ZenLib/Project/GNU/Library \  
&& make install \  
&& cd /tmp/MediaInfo_DLL_GNU_FromSource/MediaInfoLib/Project/GNU/Library \  
&& make install \  
&& cd /tmp/MediaInfo_CLI_GNU_FromSource \  
&& ./CLI_Compile.sh \  
&& cd /tmp/MediaInfo_CLI_GNU_FromSource/MediaInfo/Project/GNU/CLI \  
&& make install \  
&& cd /tmp/xmlrpc-c \  
&& ./configure \  
&& make -j $(getconf _NPROCESSORS_ONLN) \  
&& make install \  
&& cd /tmp/libtorrent \  
&& git checkout ${LIBTORRENT_VER} \  
&& ./autogen.sh \  
&& ./configure \  
&& make -j $(getconf _NPROCESSORS_ONLN) \  
&& make install \  
&& cd /tmp/rtorrent \  
&& git checkout ${RTORRENT_VER} \  
&& ./autogen.sh \  
&& ./configure --with-xmlrpc-c \  
&& make -j $(getconf _NPROCESSORS_ONLN) \  
&& make install \  
&& git clone https://github.com/Novik/ruTorrent.git /rutorrent \  
&& cd /rutorrent/plugins/ \  
&& svn co http://rutorrent-logoff.googlecode.com/svn/trunk logoff \  
&& cd /rutorrent/plugins/ \  
&& git clone https://github.com/xombiemp/rutorrentMobile.git mobile \  
&& cd /rutorrent/plugins/ \  
&& svn checkout http://rutorrent-pausewebui.googlecode.com/svn/trunk
pausewebui \  
&& cd /rutorrent/plugins/theme/themes \  
&& wget
https://raw.githubusercontent.com/Swizards/QuickBox/master/plugins/rutorrent-
quickbox-dark.zip \  
&& unzip rutorrent-quickbox-dark.zip \  
&& rm -rf rutorrent-quickbox-dark.zip \  
&& apk del ${build_pkgs} \  
&& rm -rf /var/cache/apk/* /tmp/* \  
&& deluser svn \  
&& delgroup svnusers  
  
COPY supervisord-rtorrent.ini /etc/supervisor.d/supervisord-rtorrent.ini  
  
COPY rtorrent.conf /.rtorrent.rc  
  
ADD root /  
  
EXPOSE 5000 6881 51413  

