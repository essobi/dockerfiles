FROM ctarwater/docker-texlive  
MAINTAINER chrisanthropic <ctarwater@gmail.com>  
  
# Build command: docker build -t open-publisher-base .  
###########################################################################################  
### BEGIN CUSTOM Open-Publisher Stuff ###  
###########################################################################################  
RUN export DEBIAN_FRONTEND=noninteractive && \  
apt-get clean && \  
apt-get update -y && \  
apt-get upgrade -y && \  
apt-get install -y --fix-missing autoconf build-essential curl git fonts-
linuxlibertine tex-gyre abcm2ps fontconfig graphviz imagemagick libmagickcore-
dev libmagickwand-dev inotify-tools make python3 python-pygraphviz  
  
# Install Ruby (code stolen from official Ruby docker)  
# skip installing gem documentation  
RUN mkdir -p /usr/local/etc \  
&& { \  
echo 'install: --no-document'; \  
echo 'update: --no-document'; \  
} >> /usr/local/etc/gemrc  
  
ENV RUBY_MAJOR 2.1  
ENV RUBY_VERSION 2.1.9  
ENV RUBY_DOWNLOAD_SHA256
034cb9c50676d2c09b3b6cf5c8003585acea05008d9a29fa737c54d52c1eb70c  
ENV RUBYGEMS_VERSION 2.6.3  
# some of ruby's build scripts are written in ruby  
# we purge this later to make sure our final image uses what we just built  
RUN set -ex \  
&& buildDeps=' \  
bison \  
libgdbm-dev \  
ruby \  
' \  
&& apt-get install -y libssl-dev \  
&& apt-get install -y --no-install-recommends $buildDeps \  
&& rm -rf /var/lib/apt/lists/* \  
&& curl -fSL -o ruby.tar.gz "http://cache.ruby-
lang.org/pub/ruby/$RUBY_MAJOR/ruby-$RUBY_VERSION.tar.gz" \  
&& echo "$RUBY_DOWNLOAD_SHA256 *ruby.tar.gz" | sha256sum -c - \  
&& mkdir -p /usr/src/ruby \  
&& tar -xzf ruby.tar.gz -C /usr/src/ruby --strip-components=1 \  
&& rm ruby.tar.gz \  
&& cd /usr/src/ruby \  
&& { echo '#define ENABLE_PATH_CHECK 0'; echo; cat file.c; } > file.c.new &&
mv file.c.new file.c \  
&& autoconf \  
&& ./configure --disable-install-doc \  
&& make -j"$(nproc)" \  
&& make install \  
&& apt-get purge -y --auto-remove $buildDeps \  
&& gem update --system $RUBYGEMS_VERSION \  
&& rm -r /usr/src/ruby  
  
# Git clone the Open-Publisher repo  
ADD Gemfile .  
  
ENV BUNDLER_VERSION 1.11.2  
RUN gem install bundler --version "$BUNDLER_VERSION"  
  
# install things globally, for great justice  
# and don't create ".bundle" in all our apps  
ENV GEM_HOME /usr/local/bundle  
ENV BUNDLE_PATH="$GEM_HOME" \  
BUNDLE_BIN="$GEM_HOME/bin" \  
BUNDLE_SILENCE_ROOT_WARNING=1 \  
BUNDLE_APP_CONFIG="$GEM_HOME"  
ENV PATH $BUNDLE_BIN:$PATH  
RUN mkdir -p "$GEM_HOME" "$BUNDLE_BIN" \  
&& chmod 777 "$GEM_HOME" "$BUNDLE_BIN"  
  
# Install jekyll  
RUN bundle install --binstubs --path=vendor  
  
# Install Pandoc  
ENV PKGREL 1  
ENV VERSION 1.17.0.2  
ADD
https://github.com/jgm/pandoc/releases/download/${VERSION}/pandoc-${VERSION}-${PKGREL}-amd64.deb
/pandoc.deb  
RUN export DEBIAN_FRONTEND=noninteractive && \  
dpkg -i /pandoc.deb && \  
rm /pandoc.deb  
  
# download kindlegen and install it to /usr/bin  
RUN wget
http://kindlegen.s3.amazonaws.com/kindlegen_linux_2.6_i386_v2_9.tar.gz -O
/tmp/kindlegen_linux_2.6_i386_v2_9.tar.gz  
RUN tar -xzf /tmp/kindlegen_linux_2.6_i386_v2_9.tar.gz -C /tmp  
RUN mv /tmp/kindlegen /usr/bin  
RUN rm -r /tmp/*  
  
# Basic cleanup  
RUN export DEBIAN_FRONTEND=noninteractive && \  
apt-get remove -y autoconf build-essential make && \  
apt-get autoremove -y && \  
apt-get clean -y && \  
rm -rf /var/lib/apt/lists/*  

