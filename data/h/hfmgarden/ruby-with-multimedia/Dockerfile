FROM ruby:2.5.1  
  
RUN echo 'deb http://www.deb-multimedia.org stretch main non-free' >>
/etc/apt/sources.list \  
&& echo 'deb-src http://www.deb-multimedia.org stretch main non-free' >>
/etc/apt/sources.list \  
&& apt-get -qq update \  
&& apt-get -qq -y --allow-unauthenticated install deb-multimedia-keyring \  
&& apt-get -qq update \  
&& curl -sL https://deb.nodesource.com/setup_8.x | bash - \  
&& apt-get -qq -y install --no-install-recommends build-essential libmp3lame-
dev libvorbis-dev libtheora-dev libspeex-dev yasm pkg-config libfaac-dev
libopenjp2-7-dev libx264-dev ffmpeg libimlib2-dev libcurl4-openssl-dev
default-libmysqlclient-dev libmagick++-dev libimage-exiftool-perl zip deb-
multimedia-keyring mysql-client nodejs \  
&& rm -rf /var/lib/apt/lists/*  

