FROM ubuntu:xenial  
MAINTAINER Sander de Witte  
  
# prevent installers from opening dialog boxes and set software versions, gem
home & working directory  
ENV DEBIAN_FRONTEND=noninteractive \  
RUBY_MAJOR=2.4 \  
RUBY_VERSION=2.4.2 \  
RUBYGEMS_VERSION=2.7.2 \  
BUNDLER_VERSION=1.16.0 \  
NODE_VERSION=6.12.0 \  
GEM_HOME=/usr/local/gems \  
WORK_DIR=/data/src  
  
# set bundler variables and set log level for node.js package manager  
ENV BUNDLE_PATH="$GEM_HOME" \  
BUNDLE_BIN="$GEM_HOME/bin" \  
BUNDLE_APP_CONFIG="$GEM_HOME" \  
BUNDLE_SILENCE_ROOT_WARNING=1 \  
NPM_CONFIG_LOGLEVEL=error  
  
# update image and install tools  
RUN apt-get -qq update \  
&& apt-get -qq upgrade \  
&& essentialTools='apt-utils wget git' \  
&& buildTools='build-essential autoconf' \  
&& apt-get -qq install -y --no-install-recommends $essentialTools $buildTools  
  
# download, compile and install ruby  
RUN mkdir -p /usr/local/etc \  
&& { echo 'install: --no-document --no-prerelease'; echo 'update: --no-
document --no-prerelease'; } >> /usr/local/etc/gemrc  
RUN buildDeps='bison libgdbm-dev libssl-dev libreadline-dev zlib1g-dev ruby' \  
&& apt-get -qq install -y --no-install-recommends $buildDeps \  
&& rm -rf /var/lib/apt/lists/* \  
&& wget -nv -O ruby.tar.xz "https://cache.ruby-
lang.org/pub/ruby/${RUBY_MAJOR%-rc}/ruby-$RUBY_VERSION.tar.xz" \  
&& mkdir -p /usr/src/ruby \  
&& tar -xJf ruby.tar.xz -C /usr/src/ruby --strip-components=1 \  
&& rm ruby.tar.xz \  
&& cd /usr/src/ruby \  
&& { echo '#define ENABLE_PATH_CHECK 0'; echo; cat file.c; } > file.c.new \  
&& mv file.c.new file.c \  
&& autoconf \  
&& gnuArch="$(dpkg-architecture --query DEB_BUILD_GNU_TYPE)" \  
&& ./configure --build="$gnuArch" \--disable-install-doc --enable-shared \  
&& make -j "$(nproc)" \  
&& make install \  
&& make clean \  
&& apt-get -qq purge -y --auto-remove $buildDeps \  
&& apt-get clean \  
&& cd / \  
&& rm -r /usr/src/ruby \  
&& export LANG="C.UTF-8" \  
&& export LC_ALL="C.UTF-8" \  
&& gem update --system "$RUBYGEMS_VERSION" \--no-post-install-message  
  
# update path with gem binaries and install bundler and other gems  
ENV PATH="$BUNDLE_BIN:$PATH"  
COPY Gemfile /var/tmp/Gemfile  
RUN mkdir -p "$GEM_HOME" "$BUNDLE_BIN" \  
&& chmod 777 "$GEM_HOME" "$BUNDLE_BIN" \  
&& gem install bundler --version "$BUNDLER_VERSION" \  
&& cd /var/tmp \  
&& bundle install  
  
# download, compile and install libsass (C/C++ implementation of the sass
compiler) and sassc (libsass command line driver)  
RUN cd /usr/local/lib \  
&& git clone https://github.com/sass/libsass.git --depth 1 \  
&& git clone https://github.com/sass/sassc.git --depth 1  
RUN cd /usr/local/lib \  
&& export SASS_LIBSASS_PATH="/usr/local/lib/libsass" \  
&& make -C libsass \  
&& make -C libsass clean \  
&& make -C sassc \  
&& make -C sassc install \  
&& make -C sassc clean  
  
# download and install node.js (including node.js package manager npm) and the
fs-extra package  
# (for file system methods that are not included in the native fs module),
apply patch to rename.js  
RUN cd /var/tmp \  
&& wget -nv -O node.tar.gz
"https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-x64.tar.gz"
\  
&& tar -xzf "node.tar.gz" -C /usr/local --strip-components=1 \  
&& rm "node.tar.gz" \  
&& cd $(npm root --global) \  
&& npm install --global fs-extra \  
&& sed -i -e s/graceful-fs/fs-extra/ -e s/fs\\.rename/fs.move/
./npm/lib/utils/rename.js  
  
# install a package for parsing argument options and the smaller version of
the caniuse-db,  
# postcss, the node-sass library and the gulp toolkit (including gulp-postcss
and gulp-sass)  
RUN cd $(npm root --global) \  
&& npm install --global minimist \  
&& npm install --global caniuse-lite \  
&& npm install --global postcss \  
&& npm install --global \--unsafe-perm node-sass \  
&& npm install --global gulp \  
&& npm install --global gulp-cli \  
&& npm install --global gulp-util \  
&& npm install --global gulp-plumber \  
&& npm install --global gulp-postcss \  
&& npm install --global \--unsafe-perm gulp-sass  
  
# install postcss plugins via package.json file  
COPY package.json /usr/local/lib/package.json  
RUN cd /usr/local/lib \  
&& npm install  
  
# set NODE_PATH and add it at the end of PATH  
ENV NODE_PATH="/usr/local/lib/node_modules" \  
PATH="$PATH:/usr/local/lib/node_modules"  
# create externally mounted directory and set it as working directory  
VOLUME ["$WORK_DIR"]  
WORKDIR $WORK_DIR  
  
# link global gulp and start main executable using script  
COPY docker-entrypoint.sh /  
RUN chmod +x /docker-entrypoint.sh  
ENTRYPOINT ["/docker-entrypoint.sh"]  

