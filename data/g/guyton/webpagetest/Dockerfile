FROM guyton/centos6  
# epel-release required for ExifTool  
RUN yum install -y epel-release; yum install -y wget tar zlib php php-gd perl-
Image-ExifTool httpd php-pecl-apc perl ImageMagick ImageMagick-devel
ImageMagick-perl libjpeg-turbo-devel libjpeg-turbo-static libjpeg-turbo
autoconf automake gcc gcc-c++ git libtool make nasm pkgconfig zlib-devel curl
bzip2; yum clean all  
RUN /usr/bin/perl -p -i -e 's/#ServerName www.example.com:80/ServerName
webpagetest/' /etc/httpd/conf/httpd.conf  
  
# Get WebPageTest code  
RUN cd /tmp; wget -q https://github.com/WPO-
Foundation/webpagetest/archive/WebPageTest-2.19.tar.gz ; cd /opt; tar zxf
/tmp/WebPageTest-2.19.tar.gz ; \rm /tmp/WebPageTest-2.19.tar.gz ; mv
webpagetest-WebPageTest-2.19/www/* /var/www/html/; \rm -fr webpagetest-
WebPageTest-2.19  
  
# Add patches for setting to allow non FQDN hostnames  
COPY settings.ini.sample /var/www/html/settings/settings.ini.sample  
COPY runtest.php /var/www/html/runtest.php  
  
RUN cd /var/www/html ; mkdir -p tmp dat results work/jobs work/video logs;
chown -R apache:apache tmp dat results work/jobs work/video logs  
RUN cd /var/www/html/settings; for i in locations settings; do cp
${i}.ini.sample ${i}.ini; done  
# Put Native speed at top  
RUN cd /var/www/html/settings; linenum=`grep -n '\\[Native\\]'
connectivity.ini.sample|cut -f1 -d:`; linenumoneback=`expr $linenum \- 1`;
tail -n +$linenum connectivity.ini.sample > connectivity.ini ; echo "" >>
connectivity.ini; head -$linenumoneback connectivity.ini.sample >>
connectivity.ini  
  
# fix php settings to webpagetest needs  
RUN /usr/bin/perl -p -i -e 's/upload_max_filesize = 2M/upload_max_filesize =
10M/' /etc/php.ini ; /usr/bin/perl -p -i -e 's/post_max_size =
8M/post_max_size = 10M/' /etc/php.ini ; /usr/bin/perl -p -i -e 's/memory_limit
= 128M/memory_limit = 256M/' /etc/php.ini  
  
# System Utilities  
# ffmpeg for video recording  
# based on docker image nowol/webpagetest  
# based on Julien Rottenberg <julien@rottenberg.info>  
# based on docker image rottenberg/ffmpeg  
# From https://trac.ffmpeg.org/wiki/CompilationGuide/Centos  
ENV FFMPEG_VERSION 2.8  
ENV MPLAYER_VERSION 1.1.1  
ENV YASM_VERSION 1.2.0  
ENV LAME_VERSION 3.99.5  
ENV FAAC_VERSION 1.28  
ENV XVID_VERSION 1.3.3  
ENV FDKAAC_VERSION 0.1.3  
ENV EXIFTOOL_VERSION 9.75  
# from https://github.com/WPO-Foundation/webpagetest base on pmeenan  
ENV SRC /usr/local  
ENV LD_LIBRARY_PATH ${SRC}/lib  
ENV PKG_CONFIG_PATH ${SRC}/lib/pkgconfig  
  
ENV PATH /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:  
  
RUN bash -c 'set -euo pipefail'  
  
# yasm  
RUN DIR=$(mktemp -d) && cd ${DIR} && \  
curl -Os
http://www.tortall.net/projects/yasm/releases/yasm-${YASM_VERSION}.tar.gz && \  
tar xzvf yasm-${YASM_VERSION}.tar.gz && \  
cd yasm-${YASM_VERSION} && \  
./configure --prefix="$SRC" \--bindir="${SRC}/bin" && \  
make && \  
make install && \  
make distclean && \  
rm -rf ${DIR}  
  
# x264  
RUN DIR=$(mktemp -d) && cd ${DIR} && \  
curl -Os ftp://ftp.videolan.org/pub/x264/snapshots/last_x264.tar.bz2 && \  
tar xvf last_x264.tar.bz2 && \  
cd x264* && \  
./configure --prefix="$SRC" \--bindir="${SRC}/bin" \--enable-static && \  
make && \  
make install && \  
make distclean&& \  
rm -rf ${DIR}  
  
# libmp3lame  
RUN DIR=$(mktemp -d) && cd ${DIR} && \  
curl -L -Os
http://downloads.sourceforge.net/project/lame/lame/${LAME_VERSION%.*}/lame-${LAME_VERSION}.tar.gz
&& \  
tar xzvf lame-${LAME_VERSION}.tar.gz && \  
cd lame-${LAME_VERSION} && \  
./configure --prefix="${SRC}" \--bindir="${SRC}/bin" \--disable-shared
--enable-nasm && \  
make && \  
make install && \  
make distclean&& \  
rm -rf ${DIR}  
  
# faac + http://stackoverflow.com/a/4320377  
RUN DIR=$(mktemp -d) && cd ${DIR} && \  
curl -L -Os http://downloads.sourceforge.net/faac/faac-${FAAC_VERSION}.tar.gz
&& \  
tar xzvf faac-${FAAC_VERSION}.tar.gz && \  
cd faac-${FAAC_VERSION} && \  
sed -i '126d' common/mp4v2/mpeg4ip.h && \  
./bootstrap && \  
./configure --prefix="${SRC}" \--bindir="${SRC}/bin" && \  
make && \  
make install && \  
rm -rf ${DIR}  
  
# xvid  
RUN DIR=$(mktemp -d) && cd ${DIR} && \  
curl -L -Os
http://downloads.xvid.org/downloads/xvidcore-${XVID_VERSION}.tar.gz && \  
tar xzvf xvidcore-${XVID_VERSION}.tar.gz && \  
cd xvidcore/build/generic && \  
./configure --prefix="${SRC}" \--bindir="${SRC}/bin" && \  
make && \  
make install&& \  
rm -rf ${DIR}  
  
# fdk-aac  
RUN DIR=$(mktemp -d) && cd ${DIR} && \  
curl -s https://codeload.github.com/mstorsjo/fdk-aac/tar.gz/v${FDKAAC_VERSION}
| tar zxvf - && \  
cd fdk-aac-${FDKAAC_VERSION} && \  
autoreconf -fiv && \  
./configure --prefix="${SRC}" \--disable-shared && \  
make && \  
make install && \  
make distclean && \  
rm -rf ${DIR}  
  
# ffmpeg  
RUN DIR=$(mktemp -d) && cd ${DIR} && \  
curl -Os http://ffmpeg.org/releases/ffmpeg-${FFMPEG_VERSION}.tar.gz && \  
tar xzvf ffmpeg-${FFMPEG_VERSION}.tar.gz && \  
cd ffmpeg-${FFMPEG_VERSION} && \  
./configure --prefix="${SRC}" \--extra-cflags="-I${SRC}/include" \--extra-
ldflags="-L${SRC}/lib" \--bindir="${SRC}/bin" \  
\--extra-libs=-ldl --enable-version3 --enable-libfaac --enable-libmp3lame
--enable-libx264 --enable-libxvid --enable-gpl \  
\--enable-postproc --enable-nonfree --enable-avresample --enable-libfdk_aac
--disable-debug --enable-small && \  
make && \  
make install && \  
make distclean && \  
hash -r && \  
rm -rf ${DIR}  
  
RUN echo "/usr/local/lib" > /etc/ld.so.conf.d/libc.conf  
  
EXPOSE 80 443  
VOLUME /var/www/html/tmp /var/www/html/dat /var/www/html/work/jobs
/var/www/html/work/video /var/www/html/results /var/www/html/logs
/var/log/httpd  
CMD /usr/sbin/httpd -DFOREGROUND  
  

