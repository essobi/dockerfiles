FROM ruby:2.2.0  
  
MAINTAINER Kristopher Doyen  
  
RUN apt-get update \  
&& apt-get install -y automake libass-dev libfreetype6-dev libgpac-dev \  
libtheora-dev libtool libvorbis-dev pkg-config texi2html zlib1g-dev \  
libx264-dev libmp3lame-dev yasm git \  
&& cd /usr/local/src \  
&& git clone \--depth 1 git://github.com/mstorsjo/fdk-aac.git \  
&& cd fdk-aac \  
&& autoreconf -fiv \  
&& ./configure \--disable-shared \  
&& make \  
&& make install \  
&& make distclean \  
&& mkdir -p /ffmpeg/bin \  
&& cd /usr/local/src \  
&& git clone \--depth 1 git://source.ffmpeg.org/ffmpeg \  
&& cd ffmpeg \  
&& ./configure \--extra-libs="-ldl" \--bindir="/ffmpeg/bin" \--enable-gpl \  
\--enable-libx264 \--enable-libfdk-aac \--enable-nonfree \--enable-libmp3lame
\  
\--enable-libass \--enable-libfreetype \  
&& make \  
&& make install \  
&& make distclean \  
&& hash -r \  
&& git clone -b docker \--single-branch git://github.com/kdoyen/wallop.git
/wallop \  
&& cd /wallop \  
&& bundle install \--standalone \--binstubs \--local \--path vendor/gems
\--quiet \  
&& rm -rf /usr/local/src \  
&& apt-mark unmarkauto libass5 \  
&& apt-get purge -y \--auto-remove automake libfreetype6-dev \  
libgpac-dev libtheora-dev libtool libvorbis-dev pkg-config texi2html \  
zlib1g-dev yasm git  
  
ADD scripts/start.sh /start.sh  
  
EXPOSE 8888  
CMD /start.sh  

