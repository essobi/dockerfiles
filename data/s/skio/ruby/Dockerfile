FROM ubuntu:xenial  
  
MAINTAINER Cameron Mullen <cam@skio.io>  
  
ENV RUBY_VERSION=2.3.1 \  
RUBY_BASE_VERSION=2.3 \  
RUBY_SHA256=b87c738cb2032bf4920fef8e3864dc5cf8eae9d89d8d523ce0236945c5797dcd  
  
# Install base utilities  
RUN \  
apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y --no-install-recommends \  
wget \  
ca-certificates \  
tar \  
patch \  
bzip2 \  
gawk \  
g++ \  
gcc \  
make \  
libc6-dev \  
patch \  
libreadline6-dev \  
zlib1g-dev \  
libssl-dev \  
libyaml-dev \  
libsqlite3-dev \  
sqlite3 \  
autoconf \  
libgmp-dev \  
libgdbm-dev \  
libncurses5-dev \  
automake \  
libtool \  
bison \  
pkg-config \  
libffi-dev && \  
rm -rf /var/lib/apt/lists/*  
  
# Installing Ruby  
RUN \  
mkdir -p /usr/local/etc && \  
{ echo 'install: --no-document'; echo 'update: --no-document'; } >>
/usr/local/etc/gemrc && \  
wget -O ruby.tar.gz https://cache.ruby-
lang.org/pub/ruby/${RUBY_BASE_VERSION}/ruby-${RUBY_VERSION}.tar.gz && \  
echo "$RUBY_SHA256 *ruby.tar.gz" | sha256sum -c - && \  
mkdir -p /usr/src/ruby && \  
tar -xzf ruby.tar.gz -C /usr/src/ruby --strip-components=1 && \  
rm ruby.tar.gz && \  
cd /usr/src/ruby && \  
{ echo '#define ENABLE_PATH_CHECK 0'; echo; cat file.c; } > file.c.new && mv
file.c.new file.c && \  
autoconf && \  
./configure --disable-install-doc && \  
make -j"$(nproc)" && \  
make install && \  
gem update --system $RUBYGEMS_VERSION && \  
rm -r /usr/src/ruby  
  
RUN gem install bundler  
  
ENV GEM_HOME=/usr/local/bundle  
  
ENV BUNDLE_PATH="$GEM_HOME" \  
BUNDLE_BIN="$GEM_HOME/bin" \  
BUNDLE_SILENCE_ROOT_WARNING=1 \  
BUNDLE_APP_CONFIG="$GEM_HOME"  
ENV PATH=$PATH:$BUNDLE_BIN  
  
RUN \  
mkdir -p "$GEM_HOME" "$BUNDLE_BIN" && \  
chmod 777 "$GEM_HOME" "$BUNDLE_BIN"  
  
CMD ["irb"]

