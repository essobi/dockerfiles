# drummerroma/rails24  
FROM ruby:2.4-alpine3.6  
MAINTAINER Alex Drummer <drummerroma@gmail.com>  
  
ENV RAILS_VERSION="5.0.6" \  
BUILD_PACKAGES="curl-dev build-base openssh" \  
DEV_PACKAGES="tzdata libxml2 libxml2-dev libxslt libxslt-dev mysql-client \  
imagemagick imagemagick-dev mysql-dev sqlite-dev git nodejs bash syslog-ng \  
libstdc++ libjpeg-turbo libpng" \  
JPEGOPTIM_VERSION=1.4.3 \  
PNGCRUSH_VERSION=1.7.88 \  
ZOPFLI_VERSION=1.0.1 \  
ADVANCECOMP_VERSION=1.20 \  
JHEAD_VERSION=3.00 \  
GIFSICLE_VERSION=1.88 \  
OPTIPNG_VERSION=0.7.5 \  
PNGQUANT_VERSION=2.5.2 \  
JPEGARCHIVE_VERSION=2.1.1 \  
MOZJPEG_VERSION=3.1 \  
IJG_VERSION=9a \  
PNGOUT_VERSION=20150319 \  
SKIP_IMAGE_OPTIM_PACK=1  
  
RUN \  
apk --update --upgrade add --no-cache $BUILD_PACKAGES $DEV_PACKAGES && \  
rm /var/cache/apk/*  
  
WORKDIR /tmp  
  
RUN apk update && apk add \  
&& apk add --virtual build-dependencies \  
# jpegoptim  
libjpeg-turbo-dev \  
# advancecomp  
zlib-dev \  
# pngquant  
bash libpng-dev \  
# mozjpeg  
pkgconfig autoconf automake libtool nasm \  
# utils  
curl \  
  
# advancecomp  
&& curl -L -O
https://github.com/amadvance/advancecomp/releases/download/v$ADVANCECOMP_VERSION/advancecomp-$ADVANCECOMP_VERSION.tar.gz
\  
&& tar zxf advancecomp-$ADVANCECOMP_VERSION.tar.gz \  
&& cd advancecomp-$ADVANCECOMP_VERSION \  
&& ./configure && make && make install \  
&& cd .. \  
# gifsicle  
&& curl -O https://www.lcdf.org/gifsicle/gifsicle-$GIFSICLE_VERSION.tar.gz \  
&& tar zxf gifsicle-$GIFSICLE_VERSION.tar.gz \  
&& cd gifsicle-$GIFSICLE_VERSION \  
&& ./configure && make && make install \  
&& cd .. \  
# jhead  
&& curl -O http://www.sentex.net/~mwandel/jhead/jhead-$JHEAD_VERSION.tar.gz \  
&& tar zxf jhead-$JHEAD_VERSION.tar.gz \  
&& cd jhead-$JHEAD_VERSION \  
&& make && make install \  
&& cd .. \  
# jpegoptim  
&& curl -O
http://www.kokkonen.net/tjko/src/jpegoptim-$JPEGOPTIM_VERSION.tar.gz \  
&& tar zxf jpegoptim-$JPEGOPTIM_VERSION.tar.gz \  
&& cd jpegoptim-$JPEGOPTIM_VERSION \  
&& ./configure && make && make install \  
&& cd .. \  
# jpeg-recompress (from jpeg-archive along with mozjpeg dependency)  
&& curl -L -O
https://github.com/mozilla/mozjpeg/archive/v$MOZJPEG_VERSION.tar.gz \  
&& tar zxf v$MOZJPEG_VERSION.tar.gz \  
&& cd mozjpeg-$MOZJPEG_VERSION \  
&& autoreconf -fiv && ./configure && make && make install \  
&& cd .. \  
&& curl -L -O https://github.com/danielgtaylor/jpeg-
archive/archive/$JPEGARCHIVE_VERSION.tar.gz \  
&& tar zxf $JPEGARCHIVE_VERSION.tar.gz \  
&& cd jpeg-archive-$JPEGARCHIVE_VERSION \  
&& make && make install \  
&& cd .. \  
# jpegtran (from Independent JPEG Group)  
&& curl -O http://www.ijg.org/files/jpegsrc.v$IJG_VERSION.tar.gz \  
&& tar zxf jpegsrc.v$IJG_VERSION.tar.gz \  
&& cd jpeg-$IJG_VERSION \  
&& ./configure && make && make install \  
&& cd .. \  
# optipng  
&& curl -L -O
http://downloads.sourceforge.net/project/optipng/OptiPNG/optipng-$OPTIPNG_VERSION/optipng-$OPTIPNG_VERSION.tar.gz
\  
&& tar zxf optipng-$OPTIPNG_VERSION.tar.gz \  
&& cd optipng-$OPTIPNG_VERSION \  
&& ./configure && make && make install \  
&& cd .. \  
# pngcrush  
# && curl -O
http://iweb.dl.sourceforge.net/project/pmt/pngcrush/$PNGCRUSH_VERSION/pngcrush-$PNGCRUSH_VERSION.tar.gz
\  
# && tar zxf pngcrush-$PNGCRUSH_VERSION.tar.gz \  
# && cd pngcrush-$PNGCRUSH_VERSION \  
# && make && cp -f pngcrush /usr/local/bin \  
# && cd .. \  
# pngout (binary distrib)  
&& curl -O http://static.jonof.id.au/dl/kenutils/pngout-$PNGOUT_VERSION-linux-
static.tar.gz \  
&& tar zxf pngout-$PNGOUT_VERSION-linux-static.tar.gz \  
&& cd pngout-$PNGOUT_VERSION-linux-static \  
&& cp -f x86_64/pngout-static /usr/local/bin/pngout \  
&& cd .. \  
# pngquant  
&& curl -L -O http://pngquant.org/pngquant-$PNGQUANT_VERSION-src.tar.bz2 \  
&& tar xjf pngquant-$PNGQUANT_VERSION-src.tar.bz2 \  
&& cd pngquant-$PNGQUANT_VERSION \  
&& ./configure && make && make install \  
&& cd ..  
# \  
# svgo  
#&& npm install -g svgo  
  
  
  
RUN \  
gem install -N bundler  
  
  
RUN \  
rm -rf /tmp/* && \  
apk del build-dependencies  
#RUN \  
# gem install -N nokogiri  
#RUN \  
# gem install -N rails --version "$RAILS_VERSION" && \  
# echo 'gem: --no-document' >> ~/.gemrc && \  
# cp ~/.gemrc /etc/gemrc && \  
# chmod uog+r /etc/gemrc && \  
# rm -rf /usr/lib/lib/ruby/gems/*/cache/* && \  
# rm -rf ~/.gem  
#sudo apt-get install -y advancecomp gifsicle jhead jpegoptim libjpeg-progs
optipng pngcrush pngquant  
#CMD puma -C config/puma.rb  
#important!  
#https://nickjanetakis.com/blog/dockerize-a-rails-5-postgres-redis-sidekiq-
action-cable-app-with-docker-compose  

