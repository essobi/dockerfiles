FROM debian  
MAINTAINER Gabe Conradi <gummybearx@gmail.com>  
  
ENV RUBY_MAJOR_MINOR_VERSION 2.2  
ENV RUBY_VERSION 2.2.0  
RUN apt-get update && apt-get upgrade -y && rm -rf /var/lib/apt/lists/*  
RUN mkdir /app  
  
RUN mkdir -p /usr/src/ruby && \  
ls -la /usr/src/ruby && \  
apt-get update && apt-get install -y curl autoconf \  
build-essential imagemagick libbz2-dev libcurl4-openssl-dev \  
libevent-dev libffi-dev libglib2.0-dev libjpeg-dev libmagickcore-dev \  
libmagickwand-dev libmysqlclient-dev libncurses-dev libpq-dev libreadline-dev
\  
libsqlite3-dev libssl-dev libxml2-dev libxslt-dev libyaml-dev zlib1g-dev && \  
rm -rf /var/lib/apt/lists/* && \  
curl -SL "http://cache.ruby-
lang.org/pub/ruby/$RUBY_MAJOR_MINOR_VERSION/ruby-$RUBY_VERSION.tar.xz" \  
| tar xJ -C /usr/src/ruby --strip-components=1 && \  
cd /usr/src/ruby && \  
autoconf && \  
./configure --disable-install-doc && \  
make -j"$(nproc)" && \  
apt-get purge -y --auto-remove curl autoconf \  
imagemagick libbz2-dev libcurl4-openssl-dev libevent-dev libffi-dev
libglib2.0-dev libjpeg-dev \  
libmagickcore-dev libmagickwand-dev libmysqlclient-dev libncurses-dev libpq-
dev libreadline-dev \  
libsqlite3-dev libssl-dev && \  
make install && \  
rm -r /usr/src/ruby  
RUN gem install bundler  
WORKDIR /app  
CMD ["irb"]  

