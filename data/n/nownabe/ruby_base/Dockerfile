FROM phusion/baseimage  
MAINTAINER nownabe <nownabe@gmail.com>  
  
ENV RUBY_MAJOR 2.2  
ENV RUBY_VERSION 2.2.2  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN echo "Acquire::http {No-Cache=True;};" > /etc/apt/apt.conf.d/no-cache  
  
# Update  
RUN sed -i".org" -e 's/archive.ubuntu.com/ftp.jaist.ac.jp/'
/etc/apt/sources.list  
RUN apt-get update && apt-get upgrade -y -q && rm -rf /var/lib/apt/lists/*  
  
# Set Timezone  
RUN mv /etc/localtime /etc/localtime.org  
RUN ln -s /usr/share/zoneinfo/Asia/Tokyo /etc/localtime  
  
# Setup Japanese Language  
RUN apt-get update && \  
apt-get install -y -q language-pack-ja && \  
rm -rf /var/lib/apt/lists/*  
ENV LANG ja_JP.UTF-8  
ENV LANGUAGE ja_JP.UTF-8  
ENV LC_ALL ja_JP.UTF-8  
RUN update-locale LANG=ja_JP.UTF-8  
  
# Install Git  
RUN apt-get update && \  
apt-get install -y -q --no-install-recommends git && \  
rm -rf /var/lib/apt/lists/*  
  
# Install Ruby  
RUN apt-get update && \  
apt-get install -y -q --no-install-recommends \  
autoconf bison build-essential libssl-dev libyaml-dev \  
libreadline6-dev zlib1g-dev libncurses5-dev libffi-dev \  
libgdbm3 libgdbm-dev && \  
rm -rf /var/lib/apt/lists/*  
  
RUN mkdir -p /usr/src/ruby && \  
curl -SL "http://cache.ruby-
lang.org/pub/ruby/$RUBY_MAJOR/ruby-$RUBY_VERSION.tar.bz2" \  
| tar -xjC /usr/src/ruby --strip-components=1  
  
WORKDIR /usr/src/ruby  
RUN autoconf && \  
./configure --disable-install-doc && \  
make -j"$(nproc)" && \  
make install && \  
rm -rf /usr/src/ruby  
  
# Setup Bundler  
RUN echo 'gem: --no-rdoc --no-ri' >> "$HOME/.gemrc"  
  
ENV GEM_HOME /usr/local/bundle  
ENV PATH $GEM_HOME/bin:$PATH  
RUN gem install bundler && \  
bundle config --global path "$GEM_HOME" && \  
bundle config --global bin "$GEM_HOME/bin"  
  
ENV BUNDLE_APP_CONFIG $GEM_HOME  
  
CMD ["irb"]  

