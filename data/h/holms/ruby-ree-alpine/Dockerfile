FROM alpine:latest  
  
RUN mkdir -p /usr/local/lib/ruby/bin  
ENV RUBY_BUILD_TAG v20170405  
ENV PATH="/usr/local/lib/ruby/bin:${PATH}"  
RUN echo 'gem: --no-rdoc --no-ri' >> "$HOME/.gemrc"  
RUN apk update \  
&& apk add --update alpine-sdk bash ruby git openssh openssl zlib-dev openssl-
dev readline-dev wget \  
&& git clone https://github.com/rbenv/ruby-build.git ruby-build \  
&& cd ruby-build \  
&& git checkout tags/$RUBY_BUILD_TAG \  
&& ./install.sh && CFLAGS="-O2 -fno-tree-dce -fno-optimize-sibling-calls"
CONFIGURE_OPTS=--no-tcmalloc ruby-build --verbose ree-1.8.7-2012.02
/usr/local/lib/ruby \  
&& cd / && rm -rf /ruby-build \  
&& gem update --system 1.4.2 \  
&& apk del alpine-sdk zlib-dev openssl-dev readline-dev \  
&& rm -rf /var/lib/apt/lists/* \  
&& gem install bundler  
  
  
  
  
  

