FROM debian:jessie  
  
# Install dependencies.  
RUN apt-get update && apt-get install -y \  
build-essential \  
curl \  
git \  
libbison-dev \  
libffi-dev \  
libfreetype6 \  
libfontconfig1 \  
libgdbm-dev \  
libicu-dev \  
libmysqlclient-dev \  
libncurses5-dev \  
libpq-dev\  
libreadline6 \  
libreadline6-dev \  
libsqlite3-dev \  
libssl-dev \  
libxml2-dev \  
libxslt-dev \  
libyaml-dev \  
nodejs \  
openssl \  
postgresql-client \  
socat \  
zlib1g \  
zlib1g-dev  
  
# Download and install Ruby.  
RUN \  
cd /tmp && \  
curl -O http://cache.ruby-lang.org/pub/ruby/2.1/ruby-2.1.2.tar.gz && \  
echo 'f22a6447811a81f3c808d1c2a5ce3b5f5f0955c68c9a749182feb425589e6635
ruby-2.1.2.tar.gz' | sha256sum -c && \  
tar -xzf ruby-2.1.2.tar.gz && \  
cd ruby-2.1.2 && \  
./configure --prefix=/usr/local --disable-install-doc --without-win32
--without-win32ole --without-tk --without-tk-util && \  
make -j`nproc` install && \  
rm -rf /tmp/ruby-2.1.2*  
  
# Update gem.  
RUN /usr/local/bin/gem update --system --no-document  
  
# Install bundler.  
RUN /usr/local/bin/gem install bundler --no-document  

