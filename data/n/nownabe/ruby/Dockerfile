FROM buildpack-deps:wheezy  
MAINTAINER nownabe  
  
ENV RUBY_MAJOR 2.2  
ENV RUBY_VERSION 2.2.0  
RUN apt-get update && apt-get install -y curl procps && rm -rf
/var/lib/apt/lists/*  
  
RUN apt-get update  
RUN apt-get install -y bison ruby  
RUN rm -rf /var/lib/apt/lists/*  
  
RUN mkdir -p /usr/src/jemalloc  
RUN curl -SL
"http://www.canonware.com/download/jemalloc/jemalloc-3.6.0.tar.bz2" \  
| tar -xjC /usr/src/jemalloc --strip-components=1  
WORKDIR /usr/src/jemalloc  
RUN ./configure  
RUN make -j"$(nproc)"  
RUN make install  
RUN rm -r /usr/src/jemalloc  
  
RUN mkdir -p /usr/src/ruby  
RUN curl -SL "http://cache.ruby-
lang.org/pub/ruby/$RUBY_MAJOR/ruby-$RUBY_VERSION.tar.bz2" \  
| tar -xjC /usr/src/ruby --strip-components=1  
  
WORKDIR /usr/src/ruby  
RUN autoconf  
RUN LDFLAGS='-Xlinker -R/usr/local/lib' ./configure --disable-install-doc
--with-jemalloc  
RUN make -j"$(nproc)"  
RUN apt-get purge -y --auto-remove bison ruby  
RUN make install  
RUN rm -r /usr/src/ruby  
  
RUN echo 'gem: --no-rdoc --no-ri' >> "$HOME/.gemrc"  
  
ENV GEM_HOME /usr/local/bundle  
ENV PATH $GEM_HOME/bin:$PATH  
RUN gem install bundler  
RUN bundle config --global path "$GEM_HOME"  
RUN bundle config --global bin "$GEM_HOME/bin"  
  
ENV BUNDLE_APP_CONFIG $GEM_HOME  
  
CMD [ "irb" ]  

