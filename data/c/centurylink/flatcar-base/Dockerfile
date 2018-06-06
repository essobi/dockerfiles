FROM debian:jessie  
  
MAINTAINER CenturyLink Labs <ctl-labs-futuretech@centurylink.com>  
  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \  
build-essential \  
curl \  
libffi-dev \  
libgdbm-dev \  
libncurses-dev \  
libreadline6-dev \  
libsqlite3-dev \  
libssl-dev \  
libyaml-dev \  
make \  
zlib1g-dev \  
ruby-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV RUBY_MAJOR 2.2  
ENV RUBY_VERSION 2.2.2  
RUN echo 'gem: --no-document' >> /.gemrc  
  
RUN mkdir -p /tmp/ruby \  
&& curl -L "http://cache.ruby-
lang.org/pub/ruby/$RUBY_MAJOR/ruby-$RUBY_VERSION.tar.bz2" \  
| tar -xjC /tmp/ruby --strip-components=1 \  
&& cd /tmp/ruby \  
&& ./configure --disable-install-doc \  
&& make \  
&& make install \  
&& gem update --system \  
&& rm -r /tmp/ruby \  
&& curl --silent --location https://deb.nodesource.com/setup_0.12 | bash - \  
&& apt-get install -y nodejs  
  
RUN gem install --no-document bundler  
  
CMD [ "irb" ]  
  

