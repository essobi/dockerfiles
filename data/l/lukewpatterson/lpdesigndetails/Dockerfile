FROM ubuntu:14.04  
#----------------------------------------------------------------------------------------------  
# buildpack-deps, adapted from:  
# https://github.com/docker-library/buildpack-
deps/blob/69f0b516b5515939bef6170f1e82362174143d13/wheezy/Dockerfile  
#----------------------------------------------------------------------------------------------  
#FROM debian:wheezy  
RUN apt-get update && apt-get install -y \  
autoconf \  
build-essential \  
imagemagick \  
libbz2-dev \  
libcurl4-openssl-dev \  
libevent-dev \  
libffi-dev \  
libglib2.0-dev \  
libjpeg-dev \  
libmagickcore-dev \  
libmagickwand-dev \  
libmysqlclient-dev \  
libncurses-dev \  
libpq-dev \  
libreadline-dev \  
libsqlite3-dev \  
libssl-dev \  
libxml2-dev \  
libxslt-dev \  
libyaml-dev \  
zlib1g-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN apt-get update && apt-get install -y \  
bzr \  
cvs \  
git \  
mercurial \  
subversion \  
&& rm -rf /var/lib/apt/lists/*  
#----------------------------------------------------------------------------------------------  
#----------------------------------------------------------------------------------------------  
# ruby, adapted from:  
# https://github.com/docker-
library/ruby/blob/d7fe6ada601c6b1e59ff0e228093ac518882f7d7/1.9/Dockerfile  
#----------------------------------------------------------------------------------------------  
#FROM buildpack-deps:wheezy  
RUN apt-get update && apt-get install -y curl procps && rm -rf
/var/lib/apt/lists/*  
  
ENV RUBY_MAJOR 2.0  
ENV RUBY_VERSION 2.0.0-p645  
  
# some of ruby's build scripts are written in ruby  
# we purge this later to make sure our final image uses what we just built  
RUN apt-get update \  
&& apt-get install -y bison ruby \  
&& rm -rf /var/lib/apt/lists/* \  
&& mkdir -p /usr/src/ruby \  
&& curl -SL "http://cache.ruby-
lang.org/pub/ruby/$RUBY_MAJOR/ruby-$RUBY_VERSION.tar.bz2" \  
| tar -xjC /usr/src/ruby --strip-components=1 \  
&& cd /usr/src/ruby \  
&& autoconf \  
&& ./configure --disable-install-doc \  
&& make \  
&& apt-get purge -y --auto-remove bison ruby \  
&& make install \  
&& rm -r /usr/src/ruby  
  
# skip installing gem documentation  
RUN echo 'gem: --no-rdoc --no-ri' >> "$HOME/.gemrc"  
  
# install things globally, for great justice  
ENV GEM_HOME /usr/local/bundle  
ENV PATH $GEM_HOME/bin:$PATH  
RUN gem install bundler \  
&& bundle config --global path "$GEM_HOME" \  
&& bundle config --global bin "$GEM_HOME/bin"  
  
# don't create ".bundle" in all our apps  
ENV BUNDLE_APP_CONFIG $GEM_HOME  
#----------------------------------------------------------------------------------------------  
#----------------------------------------------------------------------------------------------  
# node, adapted from:  
# https://github.com/docker-
library/node/blob/613915ab891cf4f204acad8d75a5184cc004142c/0.10/Dockerfile  
#----------------------------------------------------------------------------------------------  
#FROM buildpack-deps  
RUN apt-get update && apt-get install -y \  
ca-certificates \  
curl  
  
# verify gpg and sha256: http://nodejs.org/dist/v0.10.31/SHASUMS256.txt.asc  
# gpg: aka "Timothy J Fontaine (Work) <tj.fontaine@joyent.com>"  
RUN gpg --keyserver pgp.mit.edu --recv-keys
7937DFD2AB06298B2293C3187D33FF9D0246406D  
  
ENV NODE_VERSION 0.10.32  
ENV NPM_VERSION 2.1.4  
RUN curl -SLO "http://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.gz" \  
&& curl -SLO "http://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \  
&& gpg --verify SHASUMS256.txt.asc \  
&& grep " node-v$NODE_VERSION-linux-x64.tar.gz\$" SHASUMS256.txt.asc |
sha256sum -c - \  
&& tar -xzf "node-v$NODE_VERSION-linux-x64.tar.gz" -C /usr/local \--strip-
components=1 \  
&& rm "node-v$NODE_VERSION-linux-x64.tar.gz" SHASUMS256.txt.asc \  
&& npm install -g npm@"$NPM_VERSION" \  
&& npm cache clear  
#----------------------------------------------------------------------------------------------  
RUN gem install github-pages  
RUN npm install --global bower  
RUN apt-get install --yes exiftool  
  
EXPOSE 4000  
VOLUME /gh-pages  
WORKDIR /gh-pages  
  
COPY / /gh-pages  
  
CMD ["jekyll", "serve", "--host", "0.0.0.0"]  

