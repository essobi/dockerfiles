FROM lsiobase/alpine:3.6  
MAINTAINER sparklyballs  
  
# set version label  
ARG BUILD_DATE  
ARG VERSION  
LABEL build_version="Linuxserver.io version:- ${VERSION} Build-date:-
${BUILD_DATE}"  
  
# package version  
ARG MEDIAINF_VER="0.7.94"  
ARG CURL_VER="7.54.1"  
  
# copy patches  
COPY patches/ /defaults/patches/  
  
  
# install build packages  
RUN \  
apk add --no-cache --virtual=build-dependencies \  
autoconf \  
automake \  
cppunit-dev \  
perl-dev \  
file \  
g++ \  
gcc \  
git \  
libressl-dev \  
libtool \  
make \  
ncurses-dev && \  
  
# install runtime packages  
apk add --no-cache \  
ca-certificates \  
fcgi \  
ffmpeg \  
geoip \  
gzip \  
logrotate \  
nginx \  
php7 \  
php7-cgi \  
php7-fpm \  
php7-json \  
php7-mbstring \  
php7-sockets \  
php7-pear \  
rtorrent \  
screen \  
dtach \  
tar \  
unrar \  
unzip \  
wget \  
irssi \  
irssi-perl \  
zlib \  
zlib-dev \  
libxml2-dev \  
git \  
perl-archive-zip \  
perl-net-ssleay \  
perl-digest-sha1 \  
zip && \  
  
# compile curl to fix tracker timeouts for rtorrent  
cd /tmp && \  
mkdir curl && \  
cd curl && \  
wget -qO- https://curl.haxx.se/download/curl-${CURL_VER}.tar.gz | tar xz
--strip 1 && \  
./configure --with-ssl && make -j ${NB_CORES} && make install && \  
ldconfig /usr/bin && ldconfig /usr/lib && \  
  
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
/defaults/rutorrent-conf/users && \  
  
# patch snoopy.inc for rss fix  
cd /usr/share/webapps/rutorrent/php && \  
patch < /defaults/patches/snoopy.patch && \  
  
# install autodl-irssi perl modules  
perl -MCPAN -e 'my $c = "CPAN::HandleConfig"; $c->load(doit => 1, autoconfig
=> 1); $c->edit(prerequisites_policy => "follow");
$c->edit(build_requires_install_policy => "yes"); $c->commit' && \  
curl -L http://cpanmin.us | perl - App::cpanminus && \  
cpanm HTML::Entities XML::LibXML JSON JSON::XS && \  
  
# get additional theme  
git clone git://github.com/phlooo/ruTorrent-MaterialDesign.git
/usr/share/webapps/rutorrent/plugins/theme/themes/MaterialDesign && \  
  
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
make install && \  
cd /tmp/libmediainfo/MediaInfoLib/Project/GNU/Library && \  
make install && \  
cd /tmp/mediainfo && \  
./CLI_Compile.sh && \  
cd /tmp/mediainfo/MediaInfo/Project/GNU/CLI && \  
make install && \  
  
# cleanup  
apk del --purge \  
build-dependencies && \  
rm -rf \  
/etc/nginx/conf.d/default.conf \  
/tmp/* && \  
  
# fix logrotate  
sed -i "s#/var/log/messages {}.*# #g" /etc/logrotate.conf  
  
# add local files  
COPY root/ /  
  
# ports and volumes  
EXPOSE 80  
VOLUME /config /downloads  

