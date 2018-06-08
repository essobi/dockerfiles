FROM debian:jessie  
MAINTAINER Jordan Wesolowski <jrwesolo@gmail.com>  
  
# reduce footprint of package installs  
COPY minify /  
  
# ruby install  
ENV RUBY_VERSION 2.2.3  
RUN export DEBIAN_FRONTEND=noninteractive && \  
apt-get update && \  
apt-get install -y \  
curl \  
gcc \  
libffi-dev \  
libreadline-dev \  
libssl-dev \  
make \  
zlib1g-dev \  
&& \  
curl -L "http://cache.ruby-
lang.org/pub/ruby/${RUBY_VERSION%.*}/ruby-${RUBY_VERSION}.tar.gz" | \  
tar -C /usr/local/src -xz && \  
cd "/usr/local/src/ruby-${RUBY_VERSION}" && \  
./configure \  
\--disable-install-doc \  
\--enable-shared && \  
make && make install && \  
apt-get purge -y --auto-remove \  
curl \  
gcc \  
libffi-dev \  
libreadline-dev \  
libssl-dev \  
make \  
zlib1g-dev \  
&& \  
rm -rf "/usr/local/src/ruby-${RUBY_VERSION}" /var/lib/apt/lists/*  
  
# prerequisites  
RUN export DEBIAN_FRONTEND=noninteractive && \  
apt-get update && \  
apt-get install -y \  
ca-certificates \  
curl \  
openssl \  
&& \  
rm -rf /var/lib/apt/lists/*  
  
# gosu install  
ENV GOSU_VERSION 1.7  
RUN curl -o /usr/local/bin/gosu -sSL
"https://github.com/tianon/gosu/releases/download/${GOSU_VERSION}/gosu-amd64"
&& \  
curl -o /usr/local/bin/gosu.asc -sSL
"https://github.com/tianon/gosu/releases/download/${GOSU_VERSION}/gosu-
amd64.asc" && \  
gpg -q --keyserver pgp.mit.edu --recv-keys BF357DD4 && \  
gpg --verify /usr/local/bin/gosu.asc && \  
rm /usr/local/bin/gosu.asc && \  
chmod +x /usr/local/bin/gosu  
  
# geminabox install  
ENV GEMINABOX_VERSION=0.12.4 PUMA_VERSION=2.15.3  
RUN export DEBIAN_FRONTEND=noninteractive && \  
apt-get update && \  
apt-get install -y \  
make \  
gcc \  
g++ \  
&& \  
gem install --no-document "geminabox:${GEMINABOX_VERSION}"
"puma:${PUMA_VERSION}" && \  
apt-get purge -y --auto-remove \  
make \  
gcc \  
g++ \  
&& \  
rm -rf /var/lib/apt/lists/*  
  
ENV GEMINABOX_CONF=/etc/geminabox \  
GEMINABOX_DATA=/data/geminabox \  
GEMINABOX_USER=geminabox GEMINABOX_UID=543 \  
GEMINABOX_GROUP=geminabox GEMINABOX_GID=543  
RUN groupadd -g $GEMINABOX_GID $GEMINABOX_GROUP && \  
useradd -s /bin/bash -M -N -d $GEMINABOX_CONF -u $GEMINABOX_UID -g
$GEMINABOX_GROUP $GEMINABOX_USER && \  
mkdir -p $GEMINABOX_DATA $GEMINABOX_CONF && \  
chown $GEMINABOX_USER:$GEMINABOX_GROUP $GEMINABOX_CONF $GEMINABOX_DATA && \  
chmod 0755 $GEMINABOX_DATA $GEMINABOX_CONF  
  
COPY docker /docker  
  
EXPOSE 9292  
VOLUME $GEMINABOX_DATA  
ENTRYPOINT ["/docker/run"]  
CMD []  

