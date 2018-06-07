FROM debian:jessie  
MAINTAINER Harsh Vakharia <harshjv@gmail.com>  
  
# mongoDB  
RUN groupadd -r mongodb && useradd -r -g mongodb mongodb  
  
# Postgres  
RUN groupadd -r postgres && useradd -r -g postgres postgres  
  
# GOSU  
ENV GOSU_VERSION 1.9  
RUN set -x && \  
apt-get update && \  
apt-get install -y --no-install-recommends ca-certificates wget && \  
dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')" && \  
wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch"
&& \  
wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch.asc"
&& \  
export GNUPGHOME="$(mktemp -d)" && \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 && \  
gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu && \  
rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc && \  
chmod +x /usr/local/bin/gosu && \  
gosu nobody true  
  
# UTF-8  
RUN apt-get install -y locales && \  
localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8  
ENV LANG en_US.utf8  
  
# install curl, git, nano, vim and supervisor.d  
RUN apt-get install -y --no-install-recommends git curl nano vim supervisor  
  
# RVM!!!  
RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys
409B6B1796C275462A1703113804BB82D39DC0E3  
  
# mongoDB, mongoDB, postgres and rvm  
ENV GPG_KEYS \  
DFFA3DCF326E302C4787673A01C4E7FAAAB2461C \  
42F3E95A2C4F08279C4960ADD68FA50FEA312927 \  
B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8  
  
# add keys  
RUN set -ex && \  
for key in $GPG_KEYS; do \  
apt-key adv --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \  
done  
  
# Install & enable rvm with ruby 2.2.2  
RUN echo "insecure" >> ~/.curlrc  
RUN echo "gem: --no-ri --no-rdoc" > ~/.gemrc  
  
RUN curl -L https://get.rvm.io | bash -s stable  
RUN /bin/bash -c "source /etc/profile.d/rvm.sh && \  
rvm requirements && \  
rvm install 2.2.2 && \  
gem install rake bundler && \  
bundle config mirror.https://rubygems.org http://104.155.147.226:9292 && \  
bundle config mirror.https://rubygems.org.fallback_timeout 3"  
  
# Add it to .bashrc  
RUN echo "source /etc/profile.d/rvm.sh" >> ~/.bashrc  
  
# Install nvm  
RUN curl -o-
https://raw.githubusercontent.com/creationix/nvm/v0.31.6/install.sh | bash  
  
# Enable nvm & install node >=6  
RUN export NVM_DIR="$HOME/.nvm" && [ -s "$NVM_DIR/nvm.sh" ] && .
"$NVM_DIR/nvm.sh" && nvm install 6  
  
# Prepare for mongoDB  
ENV MONGO_MAJOR 3.2  
ENV MONGO_VERSION 3.2.9  
RUN echo "deb http://repo.mongodb.org/apt/debian jessie/mongodb-
org/$MONGO_MAJOR main" > /etc/apt/sources.list.d/mongodb-org.list  
  
# Prepare for Postgres  
ENV PG_MAJOR 9.5  
ENV PG_VERSION 9.5.4-1.pgdg80+1  
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ jessie-pgdg main"
$PG_MAJOR > /etc/apt/sources.list.d/pgdg.list  
  
# Install mongoDB  
RUN set -x && \  
apt-get update && \  
apt-get install -y --no-install-recommends \  
mongodb-org=$MONGO_VERSION \  
mongodb-org-server=$MONGO_VERSION \  
mongodb-org-shell=$MONGO_VERSION \  
mongodb-org-mongos=$MONGO_VERSION \  
mongodb-org-tools=$MONGO_VERSION && \  
rm -rf /var/lib/mongodb && \  
mv /etc/mongod.conf /etc/mongod.conf.orig  
  
RUN mkdir -p /data/db /data/configdb && \  
chown -R mongodb:mongodb /data/db /data/configdb  
  
# Install Postgres  
RUN set -x && \  
apt-get install -y --no-install-recommends postgresql-common && \  
sed -ri "s/#(create_main_cluster) .*$/\1 = false/" /etc/postgresql-
common/createcluster.conf && \  
apt-get install -y \  
postgresql-$PG_MAJOR=$PG_VERSION \  
postgresql-contrib-$PG_MAJOR=$PG_VERSION  
  
# Install AdWyze dependencies  
RUN apt-get install -y --no-install-recommends build-essential \  
libpq-dev libxml2-dev cmake \  
libxslt1-dev libmagickwand-dev libjpeg-dev \  
libpng-dev libgmp3-dev libqtwebkit-dev \  
qt4-qmake libqt4-webkit libqt4-dev xvfb \  
advancecomp gifsicle jhead jpegoptim libjpeg-progs \  
optipng pngcrush pngquant \  
libcurl4-openssl-dev \  
libedit-dev libssl-dev libxml2-dev \  
libsqlite3-dev sqlite3 \  
git curl vim nano \  
postgresql-client redis-tools  
  
# clean  
RUN apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN mv -v /usr/share/postgresql/$PG_MAJOR/postgresql.conf.sample
/usr/share/postgresql/ && \  
ln -sv ../postgresql.conf.sample /usr/share/postgresql/$PG_MAJOR/ && \  
sed -ri "s!^#?(listen_addresses)\s*=\s*\S+.*!\1 = '*'!"
/usr/share/postgresql/postgresql.conf.sample  
  
RUN mkdir -p /var/run/postgresql && chown -R postgres:postgres
/var/run/postgresql  
  
ENV PATH /usr/lib/postgresql/$PG_MAJOR/bin:$PATH  
ENV PGDATA /var/lib/postgresql/data  
  
COPY start_postgres /start_postgres  
RUN chmod +x /start_postgres  
  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
RUN mkdir /adwyze  
WORKDIR /adwyze  
  
# start supervisord  
CMD ["/usr/bin/supervisord"]  

