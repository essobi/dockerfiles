FROM ubuntu:14.04.2  
MAINTAINER Vicinity Commerce <engineering@vicinitycommerce.com>  
  
# Dependencies  
RUN apt-get update && apt-get install -y \--no-install-recommends \  
curl \  
build-essential \  
libssl-dev \  
libyaml-dev \  
libreadline-dev \  
git-core \  
zlib1g-dev \  
libxml2-dev \  
libxslt1-dev \  
libffi-dev \  
  
# Install from source  
&& mkdir /tmp/ruby \  
&& cd /tmp/ruby \  
&& curl -OL http://cache.ruby-lang.org/pub/ruby/2.2/ruby-2.2.0.tar.gz \  
&& tar -xzf ruby-2.2.0.tar.gz \  
&& cd ruby-2.2.0 \  
&& ./configure --disable-install-doc \  
&& make -j"$(nproc)" \  
&& make install \  
&& cd / \  
&& rm -rf /tmp/* \  
&& apt-get clean && rm -rf /var/lib/apt/lists/*  
  
# Do not install documentation when installing gems  
RUN echo 'gem: --no-rdoc --no-ri' >> "$HOME/.gemrc"  
  
RUN gem install bundler  

