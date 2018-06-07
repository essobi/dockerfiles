FROM alpine:latest  
MAINTAINER lambdalisue <lambdalisue@hashnote.net>  
  
# Install build dependencies and required packages  
# and Build Vim  
# 'diffutils' is required while busybox's diff supports  
# only unified diff style  
# https://busybox.net/downloads/BusyBox.html  
# iconv in alpine is a bit different from usual one so  
# replace it to support 'iconv()' correctly in Vim  
ARG OPTIONS  
RUN apk add --no-cache --virtual build-deps curl git make g++ ncurses-dev \  
&& apk add --no-cache ncurses diffutils \  
&& echo "Install official 'iconv'" \  
&& curl -SL http://ftp.gnu.org/pub/gnu/libiconv/libiconv-1.15.tar.gz | tar -xz
\  
&& cd libiconv-1.15 \  
&& ./configure \  
&& make \  
&& make install \  
&& cd ../ && rm -rf libiconv-1.15 \  
&& echo "Install Vim with $OPTIONS" \  
&& git clone \--depth 1 --single-branch $OPTIONS https://github.com/vim/vim \  
&& cd vim \  
&& git log -1 \  
&& ./configure --enable-fail-if-missing --with-features=huge \  
&& make \  
&& make install \  
&& cd ../ && rm -rf vim \  
&& apk del build-deps  
  
VOLUME /mnt/volume  
WORKDIR /mnt/volume  
ENTRYPOINT ["/usr/local/bin/vim"]  
CMD []  

