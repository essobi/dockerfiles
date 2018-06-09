FROM mlaccetti/docker-oracle-java8-ubuntu-16.04  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
wget python python2.7-dev fakeroot ca-certificates tar gzip zip \  
autoconf automake bzip2 file g++ gcc imagemagick libbz2-dev libc6-dev
libcurl4-openssl-dev \  
libdb-dev libevent-dev libffi-dev libgeoip-dev libglib2.0-dev libjpeg-dev
libkrb5-dev \  
liblzma-dev libmagickcore-dev libmagickwand-dev libmysqlclient-dev libncurses-
dev libpng-dev \  
libpq-dev libreadline-dev libsqlite3-dev libssl-dev libtool libwebp-dev
libxml2-dev libxslt-dev \  
libyaml-dev make patch xz-utils zlib1g-dev unzip curl \  
&& apt-get -y install git \  
&& apt-get -qy install libcurl4-openssl-dev git-man liberror-perl \  
&& apt-get clean  
  
RUN wget "https://bootstrap.pypa.io/get-pip.py" -O /tmp/get-pip.py \  
&& python /tmp/get-pip.py \  
&& pip install --upgrade awscli \  
&& rm -fr /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV RUBY_MAJOR="2.2" \  
RUBY_VERSION="2.2.3" \  
RUBYGEMS_VERSION="2.6.12" \  
BUNDLER_VERSION="1.14.6" \  
GEM_HOME="/usr/local/bundle"  
ENV BUNDLE_PATH="$GEM_HOME" \  
BUNDLE_BIN="$GEM_HOME/bin" \  
BUNDLE_SILENCE_ROOT_WARNING=1 \  
BUNDLE_APP_CONFIG="$GEM_HOME"  
ENV PATH $BUNDLE_BIN:$PATH  
  
RUN mkdir -p /usr/local/etc \  
&& { \  
echo 'install: --no-document'; \  
echo 'update: --no-document'; \  
} >> /usr/local/etc/gemrc \  
&& apt-get update && apt-get install -y --no-install-recommends \  
bison libgdbm-dev ruby \  
&& wget "https://cache.ruby-
lang.org/pub/ruby/$RUBY_MAJOR/ruby-$RUBY_VERSION.tar.gz" -O /tmp/ruby.tar.gz \  
&& mkdir -p /usr/src/ruby \  
&& tar -xzf /tmp/ruby.tar.gz -C /usr/src/ruby --strip-components=1 \  
&& cd /usr/src/ruby \  
&& { \  
echo '#define ENABLE_PATH_CHECK 0'; \  
echo; \  
cat file.c; \  
} > file.c.new \  
&& mv file.c.new file.c \  
&& autoconf \  
&& ./configure --disable-install-doc \  
&& make -j"$(nproc)" \  
&& make install \  
&& apt-get purge -y --auto-remove bison libgdbm-dev ruby \  
&& cd / \  
&& rm -r /usr/src/ruby \  
&& gem update --system "$RUBYGEMS_VERSION" \  
&& gem install bundler --version "$BUNDLER_VERSION" \  
&& mkdir -p "$GEM_HOME" "$BUNDLE_BIN" \  
&& chmod 777 "$GEM_HOME" "$BUNDLE_BIN" \  
&& rm -fr /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | apt-key
add -  
  
RUN apt-get update \  
&& apt-get install -y apt-transport-https  
  
RUN echo "deb https://artifacts.elastic.co/packages/5.x/apt stable main" | tee
-a /etc/apt/sources.list.d/elastic-5.x.list  
  
RUN apt-get update \  
&& apt-get install -y logstash  
  
RUN ln -s /usr/share/logstash/bin/logstash /bin/logstash  
  
RUN /usr/share/logstash/bin/logstash-plugin install logstash-output-amazon_es  
  
RUN pip install xlsx2csv \  
&& pip install awscurl --upgrade  
  
RUN apt-get update \  
&& apt-get install -y telnet jq  
  
RUN apt-get update \  
&& apt-get install -y netcat lsof  
  
RUN apt-get update \  
&& apt-get install -y libgtk2.0-0 libgconf-2-4 libasound2 libxtst6 libxss1
libnss3 xvfb  
  
RUN apt-get update \  
&& apt-get install -y nginx  
  
RUN apt-get update \  
&& apt-get install -y php7.0 php7.0-fpm php7.0-cli php7.0-common
php7.0-mbstring php7.0-gd php7.0-intl php7.0-xml php7.0-mysql php7.0-mcrypt
php7.0-zip  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
CMD ["bash"]  

