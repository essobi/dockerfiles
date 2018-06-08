FROM python:3.4  
MAINTAINER John Paul Alcala, jpalcala@ayannah.com  
  
# Install nodejs  
RUN gpg --keyserver pool.sks-keyservers.net --recv-keys
7937DFD2AB06298B2293C3187D33FF9D0246406D
114F43EE0176B71C7BC219DD50A3051F888C628D  
  
ENV NODE_VERSION 0.12.3  
ENV NPM_VERSION 2.10.0  
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
  
# Install Ruby  
ENV RUBY_MAJOR 2.2  
ENV RUBY_VERSION 2.2.2  
ENV RUBY_DOWNLOAD_SHA256
5ffc0f317e429e6b29d4a98ac521c3ce65481bfd22a8cf845fa02a7b113d9b44  
  
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
  
# grab gosu for easy step-down from root  
RUN gpg --keyserver pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4  
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/* \  
&& curl -o /usr/local/bin/gosu -SL
"https://github.com/tianon/gosu/releases/download/1.2/gosu-$(dpkg --print-
architecture)" \  
&& curl -o /usr/local/bin/gosu.asc -SL
"https://github.com/tianon/gosu/releases/download/1.2/gosu-$(dpkg --print-
architecture).asc" \  
&& gpg --verify /usr/local/bin/gosu.asc \  
&& rm /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu  
  
ENV FLASK_VERSION 0.10.1  
ENV FLASK_ASSETS_VERSION 0.10  
RUN gem install sass && \  
npm install -g coffee-script bower && \  
easy_install pip && \  
pip install Flask==$FLASK_VERSION Flask-Assets==$FLASK_ASSETS_VERSION  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
ONBUILD COPY requirements.txt /usr/src/app/  
ONBUILD RUN pip install -r requirements.txt  
  
ONBUILD COPY bower.json /usr/src/app/  
ONBUILD RUN bower --allow-root install && bower --allow-root cache clean  
  
ONBUILD COPY . /usr/src/app  

