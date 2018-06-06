FROM debian:latest  
MAINTAINER Colin Rymer <colin.rymer@gmail.com>  
  
ENV GEM_HOME /usr/local/bundle  
ENV PATH $GEM_HOME/bin:$PATH  
ENV BUNDLE_APP_CONFIG $GEM_HOME  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
wget \  
ca-certificates \  
curl \  
git \  
&& apt-get install -y \  
autoconf \  
bison \  
build-essential \  
imagemagick \  
libbz2-dev \  
libcurl4-openssl-dev \  
libevent-dev \  
libffi-dev \  
libgdbm-dev \  
libglib2.0-dev \  
libjpeg-dev \  
liblzma-dev \  
libmagickcore-dev \  
libmagickwand-dev \  
libmysqlclient-dev \  
libncurses5-dev \  
libreadline-dev \  
libssl-dev \  
libxml2-dev \  
libxslt-dev \  
libyaml-dev \  
zlib1g-dev \  
&& mkdir -p /usr/src/ruby \  
&& curl -SL "http://cache.ruby-lang.org/pub/ruby/2.2/ruby-2.2.2.tar.bz2" | tar
-xjC /usr/src/ruby --strip-components=1 \  
&& cd /usr/src/ruby \  
&& autoconf \  
&& ./configure --disable-install-doc \  
&& make -j"$(nproc)" \  
&& make install \  
&& curl -sL https://deb.nodesource.com/setup_0.12 | bash - \  
&& apt-get install -y nodejs \  
&& apt-get purge -y --auto-remove bison libgdbm-dev \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& rm -r /usr/src/ruby \  
&& echo 'gem: --no-rdoc --no-ri' >> "$HOME/.gemrc" \  
&& cd / \  
&& gem install bundler \  
&& bundle config --global path "$GEM_HOME" \  
&& bundle config --global bin "$GEM_HOME/bin" \  
&& mkdir /app  
  
WORKDIR /app/  
EXPOSE 3000  
ONBUILD ADD Gemfile* /app/  
ONBUILD RUN BUNDLE_JOBS=$(cat /proc/cpuinfo | grep cores | cut -d':' -f2 |
head -n1 | xargs expr -1 +) bundle install  
ONBUILD ADD . /app/  
ONBUILD RUN chmod 744 bin/start  
ONBUILD RUN RAILS_ENV=production bundle exec rake assets:precompile --trace  
ONBUILD CMD bin/start  

