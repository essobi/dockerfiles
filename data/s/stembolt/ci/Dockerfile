FROM ubuntu:trusty  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# We need to update-locale first so that postgres will generate  
# the cluster with UTF-8  
# We also want curl as soon as possible  
RUN apt-get update && \  
apt-get install --no-install-recommends -y locales curl ca-certificates && \  
locale-gen "en_US.UTF-8" && \  
update-locale LANG=en_US.UTF-8 \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV LANG en_US.utf8  
  
RUN \  
echo "deb http://deb.nodesource.com/node_8.x $(lsb_release -sc) main" >>
/etc/apt/sources.list && \  
curl -sS -L https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add
- && \  
echo "deb http://dl.yarnpkg.com/debian/ stable main" >>
/etc/apt/sources.list.d/yarn.list && \  
curl -sS -L https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add - && \  
echo "deb http://packages.erlang-solutions.com/ubuntu $(lsb_release -sc)
contrib" >> /etc/apt/sources.list && \  
curl -sS -L https://packages.erlang-solutions.com/ubuntu/erlang_solutions.asc
| apt-key add - && \  
echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu $(lsb_release -sc)
main" >> /etc/apt/sources.list && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C2518248EEA14886 && \  
apt-get update && \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
apt-get install --no-install-recommends -y \  
build-essential \  
git-core \  
curl libcurl4-openssl-dev libssl-dev \  
rsync \  
libmcrypt-dev \  
libreadline-dev \  
zlib1g zlib1g-dev \  
libyaml-dev libgdbm-dev libncurses5-dev libffi-dev libgmp3-dev \  
libxslt-dev libxml2-dev \  
python python-pip python-dev \  
nodejs yarn \  
postgresql libpq-dev postgresql-contrib \  
mysql-server libmysqlclient-dev \  
sqlite3 libsqlite3-dev \  
redis-server memcached libmemcache-dev \  
ruby ruby-dev \  
unzip zip \  
xvfb \  
erlang \  
parallel \  
ghostscript libgs-dev \  
libmagickcore-dev imagemagick libmagickwand-dev \  
qt5-default libqt5webkit5-dev \  
oracle-java8-installer \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
/var/cache/oracle-jdk8-installer  
  
RUN \  
curl -Lo elasticsearch.deb
https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-5.1.1.deb
&& \  
dpkg -i elasticsearch.deb  
  
RUN yarn global add svgo karma-cli bower  
  
RUN curl -Lo /tmp/phantomjs.tar.bz2
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
&& \  
tar -xjf /tmp/phantomjs.tar.bz2 -C /tmp && \  
mv /tmp/phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/local/bin/phantomjs  
  
  
RUN pip install awscli  
  
ADD install_rubies.sh /  
RUN bash install_rubies.sh  
  
RUN curl -Lo /usr/local/bin/gosu
https://github.com/tianon/gosu/releases/download/1.4/gosu-amd64 && \  
chmod a+x /usr/local/bin/gosu  
  
WORKDIR /workspace  
ENTRYPOINT ["bash", "/init.sh"]  
ADD init.sh run_test.sh /  

