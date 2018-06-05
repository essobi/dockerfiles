FROM bytesized/base  
MAINTAINER maran@bytesized-hosting.com  
  
# package version  
ARG MEDIAINF_VER="0.7.88"  
# install runtime packages  
RUN \  
apk add --no-cache \  
ca-certificates \  
curl \  
fcgi \  
ffmpeg \  
geoip \  
gzip \  
nginx \  
rtorrent \  
screen \  
tar \  
unrar \  
unzip \  
wget \  
zip  
  
RUN \  
apk add --no-cache \  
\--repository http://nl.alpinelinux.org/alpine/edge/community \  
php7 \  
php7-cgi \  
php7-fpm \  
php7-json \  
php7-pear \  
php7-sockets  
RUN \  
apk add --no-cache \  
\--repository http://nl.alpinelinux.org/alpine/edge/main\  
perl \  
irssi irssi-perl libxml2-dev perl-dev perl-archive-zip perl-net-ssleay perl-
digest-sha1 perl-json perl-html-parser  
  
RUN apk add --no-cache \  
\--repository http://nl.alpinelinux.org/alpine/edge/community \  
perl-xml-libxml  
  
RUN apk add --no-cache --repository
http://nl.alpinelinux.org/alpine/edge/testing perl-json-xs  
  
RUN \  
# install build packages  
apk add --no-cache --virtual=build-dependencies \  
autoconf \  
automake \  
cppunit-dev \  
curl-dev \  
file \  
g++ \  
gcc \  
libtool \  
make \  
ncurses-dev \  
openssl-dev  
  
RUN \  
# install webui  
mkdir -p \  
/usr/share/webapps/rutorrent \  
/defaults/rutorrent-conf && \  
curl -o \  
/tmp/rutorrent.tar.gz -L \  
"https://github.com/Novik/ruTorrent/archive/master.tar.gz" && \  
tar xf \  
/tmp/rutorrent.tar.gz -C \  
/usr/share/webapps/rutorrent --strip-components=1 && \  
mv /usr/share/webapps/rutorrent/conf/* \  
/defaults/rutorrent-conf/ && \  
rm -rf \  
/defaults/rutorrent-conf/users  
  
RUN \  
# compile mediainfo packages  
curl -o \  
/tmp/libmediainfo.tar.gz -L \  
"http://mediaarea.net/download/binary/libmediainfo0/${MEDIAINF_VER}/MediaInfo_DLL_${MEDIAINF_VER}_GNU_FromSource.tar.gz"
&& \  
curl -o \  
/tmp/mediainfo.tar.gz -L \  
"http://mediaarea.net/download/binary/mediainfo/${MEDIAINF_VER}/MediaInfo_CLI_${MEDIAINF_VER}_GNU_FromSource.tar.gz"
&& \  
mkdir -p \  
/tmp/libmediainfo \  
/tmp/mediainfo && \  
tar xf /tmp/libmediainfo.tar.gz -C \  
/tmp/libmediainfo --strip-components=1 && \  
tar xf /tmp/mediainfo.tar.gz -C \  
/tmp/mediainfo --strip-components=1 && \  
  
cd /tmp/libmediainfo && \  
./SO_Compile.sh && \  
cd /tmp/libmediainfo/ZenLib/Project/GNU/Library && \  
make -j4 install && \  
cd /tmp/libmediainfo/MediaInfoLib/Project/GNU/Library && \  
make -j4 install && \  
cd /tmp/mediainfo && \  
./CLI_Compile.sh && \  
cd /tmp/mediainfo/MediaInfo/Project/GNU/CLI && \  
make -j4 install  
  
RUN apk add --no-cache git && cd /usr/share/webapps/rutorrent/plugins && git
clone https://github.com/autodl-community/autodl-rutorrent.git autodl-irssi  
RUN echo "export TERM=xterm" >> /etc/profile  
  
# ports and volumes  
EXPOSE 80 55555 6112  
# add local files  
ADD files/conf.php /usr/share/webapps/rutorrent/plugins/autodl-irssi  
  
COPY static/ /  
  
VOLUME /config /data /media  

