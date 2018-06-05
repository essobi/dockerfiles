FROM assemblyline/buildpack_deps  
  
ENV RUBY_VERSION 2.2.0  
COPY ruby.md5 /usr/src/ruby/  
  
RUN apt-get update -q \  
&& apt-get install -qy bison ruby nodejs --no-install-recommends \  
&& rm -rf /var/lib/apt/lists/* \  
&& mkdir -p /usr/src/ruby \  
&& curl -o /usr/src/ruby/src.tar.bz2 --create-dirs http://cache.ruby-
lang.org/pub/ruby/ruby-2.2.0.tar.bz2 \  
&& cd /usr/src/ruby \  
&& md5sum -c ruby.md5 \  
&& tar xjf src.tar.bz2 --strip-components=1 \  
&& autoconf \  
&& ./configure --disable-install-doc \  
&& make -j"$(nproc)" \  
&& apt-get purge -y \--auto-remove bison ruby \  
&& make install \  
&& rm -r /usr/src/ruby  
  
RUN echo 'gem: --no-document' > /etc/gemrc  
  
ENV GEM_HOME /usr/local/bundle  
ENV PATH $GEM_HOME/bin:$PATH  
RUN gem update \--system \  
&& gem install bundler \  
&& bundle config --global path "$GEM_HOME" \  
&& bundle config --global bin "$GEM_HOME/bin"  
  
ENV BUNDLE_APP_CONFIG $GEM_HOME  

