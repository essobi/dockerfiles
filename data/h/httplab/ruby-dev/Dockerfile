FROM buildpack-deps:xenial  
  
ENV RUBY_MAJOR 2.2  
ENV RUBY_VERSION 2.2.4  
ENV RUBY_DOWNLOAD_SHA256
b6eff568b48e0fda76e5a36333175df049b204e91217aa32a65153cc0cdcb761  
ENV RUBYGEMS_VERSION 2.6.3  
# some of ruby's build scripts are written in ruby  
# we purge this later to make sure our final image uses what we just built  
RUN apt-get update \  
&& apt-get install -y bison libgdbm-dev nodejs ruby \  
&& rm -rf /var/lib/apt/lists/* \  
&& mkdir -p /usr/src/ruby \  
&& curl -fSL -o ruby.tar.gz "http://cache.ruby-
lang.org/pub/ruby/$RUBY_MAJOR/ruby-$RUBY_VERSION.tar.gz" \  
&& echo "$RUBY_DOWNLOAD_SHA256 *ruby.tar.gz" | sha256sum -c - \  
&& tar -xzf ruby.tar.gz -C /usr/src/ruby --strip-components=1 \  
&& rm ruby.tar.gz \  
&& cd /usr/src/ruby \  
&& autoconf \  
&& ./configure \  
&& make -j"$(nproc)" \  
&& make install \  
&& apt-get purge -y --auto-remove bison libgdbm-dev ruby \  
&& gem update --system $RUBYGEMS_VERSION \  
&& rm -r /usr/src/ruby  

