FROM buildpack-deps:jessie  
  
#  
# node <https://github.com/nodejs/docker-
node/blob/d798690bdae91174715ac083e31198674f044b68/0.10/Dockerfile>  
#  
# verify gpg and sha256: http://nodejs.org/dist/v0.10.31/SHASUMS256.txt.asc  
# gpg: aka "Timothy J Fontaine (Work) <tj.fontaine@joyent.com>"  
# gpg: aka "Julien Gilli <jgilli@fastmail.fm>"  
RUN set -ex \  
&& for key in \  
7937DFD2AB06298B2293C3187D33FF9D0246406D \  
114F43EE0176B71C7BC219DD50A3051F888C628D \  
; do \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \  
done  
  
ENV NODE_VERSION 0.10.40  
ENV NPM_VERSION 2.14.1  
RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.gz" \  
&& curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \  
&& gpg --verify SHASUMS256.txt.asc \  
&& grep " node-v$NODE_VERSION-linux-x64.tar.gz\$" SHASUMS256.txt.asc |
sha256sum -c - \  
&& tar -xzf "node-v$NODE_VERSION-linux-x64.tar.gz" -C /usr/local \--strip-
components=1 \  
&& rm "node-v$NODE_VERSION-linux-x64.tar.gz" SHASUMS256.txt.asc \  
&& npm install -g npm@"$NPM_VERSION" \  
&& npm cache clear  
  
#  
# ruby <https://github.com/docker-library/ruby/blob/master/2.2/Dockerfile>  
#  
ENV RUBY_MAJOR 2.2  
ENV RUBY_VERSION 2.2.3  
ENV RUBY_DOWNLOAD_SHA256
df795f2f99860745a416092a4004b016ccf77e8b82dec956b120f18bdc71edce  
ENV RUBYGEMS_VERSION 2.4.8  
# skip installing gem documentation  
RUN echo 'install: --no-document\nupdate: --no-document' >> "$HOME/.gemrc"  
  
# some of ruby's build scripts are written in ruby  
# we purge this later to make sure our final image uses what we just built  
RUN apt-get update \  
&& apt-get install -y bison libgdbm-dev ruby \  
&& rm -rf /var/lib/apt/lists/* \  
&& mkdir -p /usr/src/ruby \  
&& curl -fSL -o ruby.tar.gz "http://cache.ruby-
lang.org/pub/ruby/$RUBY_MAJOR/ruby-$RUBY_VERSION.tar.gz" \  
&& echo "$RUBY_DOWNLOAD_SHA256 *ruby.tar.gz" | sha256sum -c - \  
&& tar -xzf ruby.tar.gz -C /usr/src/ruby --strip-components=1 \  
&& rm ruby.tar.gz \  
&& cd /usr/src/ruby \  
&& autoconf \  
&& ./configure --disable-install-doc \  
&& make -j"$(nproc)" \  
&& make install \  
&& apt-get purge -y --auto-remove bison libgdbm-dev ruby \  
&& gem update --system $RUBYGEMS_VERSION \  
&& rm -r /usr/src/ruby  
  
# install things globally, for great justice  
ENV GEM_HOME /usr/local/bundle  
ENV PATH $GEM_HOME/bin:$PATH  
  
ENV BUNDLER_VERSION 1.10.6  
RUN gem install bundler --version "$BUNDLER_VERSION" \  
&& bundle config --global path "$GEM_HOME" \  
&& bundle config --global bin "$GEM_HOME/bin"  
  
# don't create ".bundle" in all our apps  
ENV BUNDLE_APP_CONFIG $GEM_HOME  
  
#  
# rsync  
#  
RUN apt-get update && \  
apt-get install -y rsync  
  

