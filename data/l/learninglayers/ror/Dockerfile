FROM learninglayers/base  
MAINTAINER Jukka Purma <jukka.purma ÄT aalto.fi>  
  
# things needed to build ruby2.2, by trial and error from  
RUN apt-get update && apt-get install -y autoconf \  
bzip2 \  
libssl-dev \  
libreadline-dev \  
make \  
zlib1g-dev  
  
# -- this part comes from ruby2.2 -image --  
ENV RUBY_MAJOR 2.2  
ENV RUBY_VERSION 2.2.2  
ENV RUBYGEMS_VERSION 2.4.8  
RUN apt-get install -y bison libgdbm-dev ruby \  
&& rm -rf /var/lib/apt/lists/* \  
&& mkdir -p /usr/src/ruby \  
&& curl -fSL -o ruby.tar.gz "http://cache.ruby-
lang.org/pub/ruby/$RUBY_MAJOR/ruby-$RUBY_VERSION.tar.gz" \  
&& tar -xzf ruby.tar.gz -C /usr/src/ruby --strip-components=1 \  
&& rm ruby.tar.gz  
RUN cd /usr/src/ruby \  
&& autoconf \  
&& ./configure --disable-install-doc \  
&& make -j"$(nproc)" \  
&& make install \  
&& apt-get purge -y --auto-remove bison libgdbm-dev ruby \  
&& gem update --system $RUBYGEMS_VERSION \  
&& rm -r /usr/src/ruby  
  
RUN apt-get update -qq && apt-get install -y build-essential \  
libpq-dev  
ENV GEM_HOME /usr/local/bundle  
ENV PATH $GEM_HOME/bin:$PATH  
  
ENV BUNDLER_VERSION 1.10.6  
RUN gem install bundler --version "$BUNDLER_VERSION" \  
&& bundle config --global path "$GEM_HOME" \  
&& bundle config --global bin "$GEM_HOME/bin"  
  
# don't create ".bundle" in all our apps  
ENV BUNDLE_APP_CONFIG $GEM_HOME  
# -- part from ruby2.2 ends --  

