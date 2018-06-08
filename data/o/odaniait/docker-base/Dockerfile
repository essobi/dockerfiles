FROM phusion/baseimage:latest  
MAINTAINER Mike Petersen <mike@odania-it.de>  
  
# Set correct environment variables.  
ENV DEBIAN_FRONTEND noninteractive  
ENV HOME /root  
  
RUN apt-get update  
RUN apt-get -y dist-upgrade  
RUN apt-get install -y vim curl nginx bison libgdbm-dev ruby build-essential
autoconf zlib1g-dev unzip \  
bzip2 ca-certificates libffi-dev libgdbm3 libssl-dev libyaml-dev procps git
vim apt-transport-https \  
unattended-upgrades logcheck logcheck-database make htop vim wget zip
software-properties-common \  
libxml2-dev libxslt1-dev imagemagick libmagickwand-dev libmysqlclient-dev
libsqlite3-dev libpq-dev \  
libcurl4-openssl-dev net-tools  
  
# Ruby environment vars  
ENV RUBY_MAJOR 2.3  
ENV RUBY_VERSION 2.3.0  
ENV RUBY_DOWNLOAD_SHA256
ba5ba60e5f1aa21b4ef8e9bf35b9ddb57286cb546aac4b5a28c71f459467e507  
ENV RUBYGEMS_VERSION 2.5.1  
RUN rm -rf /var/lib/apt/lists/* \  
&& mkdir -p /usr/src/ruby \  
&& curl -fSL -o ruby.tar.gz "http://cache.ruby-
lang.org/pub/ruby/$RUBY_MAJOR/ruby-$RUBY_VERSION.tar.gz" \  
&& echo "$RUBY_DOWNLOAD_SHA256 *ruby.tar.gz" | sha256sum -c - \  
&& tar -xzf ruby.tar.gz -C /usr/src/ruby --strip-components=1 \  
&& rm ruby.tar.gz \  
&& cd /usr/src/ruby \  
&& autoconf \  
&& ./configure --disable-install-doc \  
&& make -j"$(nproc)" \  
&& make install \  
&& apt-get purge -y --auto-remove bison libgdbm-dev ruby \  
&& gem update --system $RUBYGEMS_VERSION \  
&& rm -r /usr/src/ruby  
  
# install things globally, for great justice  
ENV GEM_HOME /usr/local/bundle  
ENV PATH $GEM_HOME/bin:$PATH  
  
ENV BUNDLER_VERSION 1.11.2  
RUN gem install bundler --version "$BUNDLER_VERSION" \  
&& bundle config --global path "$GEM_HOME" \  
&& bundle config --global bin "$GEM_HOME/bin"  
  
# Setup cron  
RUN chmod 600 /etc/crontab  
COPY 20auto-upgrades /etc/apt/apt.conf.d/20auto-upgrades  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

