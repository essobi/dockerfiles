FROM debian:wheezy  
MAINTAINER Thiago Avelino <avelino@filmow.com>  
  
# Used aptitude  
RUN apt-get update \  
&& apt-get install -y aptitude  
  
# make the "pt_BR.UTF-8" locale so postgres will be utf-8 enabled by default  
RUN aptitude update \  
&& aptitude install -y locales \  
&& rm -rf /var/lib/apt/lists/* \  
&& localedef -i pt_BR -c -f UTF-8 -A /usr/share/locale/locale.alias
pt_BR.UTF-8  
ENV LANG pt_BR.utf8  
  
# install packages  
RUN aptitude upgrade -yq \  
&& aptitude -yq install supervisor git-core build-essential libc6-dev
libexpat1-dev gettext libz-dev libssl-dev libevent-dev libcurl4-nss-dev
libcurl4-dev libfreetype6-dev postgresql-client libpq-dev sqlite3 libxslt1-dev
libxml2-dev libjpeg62-dev zlib1g-dev cron \  
&& aptitude -yq install python python-dev python-setuptools python-software-
properties python-psycopg2 python-numpy python-opencv python-pip python-lxml \  
&& rm -rf /var/lib/apt/lists/*  
  
# install ruby + lessc  
ENV RUBY_MAJOR 2.0  
ENV RUBY_VERSION 2.0.0-p647  
ENV RUBY_DOWNLOAD_SHA256
c88aaf5b4ec72e2cb7d290ff854f04d135939f6134f517002a9d65d5fc5e5bec  
ENV RUBYGEMS_VERSION 2.4.8  
RUN echo 'install: --no-document\nupdate: --no-document' > "$HOME/.gemrc"  
RUN apt-get update \  
&& apt-get install -y bison libgdbm-dev ruby curl make build-essential \  
&& rm -rf /var/lib/apt/lists/* \  
&& mkdir -p /usr/src/ruby \  
&& curl -fSL -o ruby.tar.gz "http://cache.ruby-
lang.org/pub/ruby/$RUBY_MAJOR/ruby-$RUBY_VERSION.tar.gz" \  
&& echo "$RUBY_DOWNLOAD_SHA256 *ruby.tar.gz" | sha256sum -c - \  
&& tar -xzf ruby.tar.gz -C /usr/src/ruby --strip-components=1 \  
&& rm ruby.tar.gz \  
&& cd /usr/src/ruby \  
&& ./configure --disable-install-doc \  
&& make -j"$(nproc)" \  
&& make install \  
&& apt-get purge -y --auto-remove bison libgdbm-dev ruby \  
&& gem update --system $RUBYGEMS_VERSION \  
&& /usr/local/bin/gem install therubyracer \  
&& /usr/local/bin/gem install less  

