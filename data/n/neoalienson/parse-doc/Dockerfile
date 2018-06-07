FROM alpine:3.3  
MAINTAINER neo [at] orz [dot] hk  
  
ENV BUNDLER_VERSION 1.12.5  
ENV NODE_VERSION=v6.5.0 NPM_VERSION=3  
ENV GEM_HOME /usr/local/bundle  
ENV BUNDLE_PATH="$GEM_HOME" \  
BUNDLE_BIN="$GEM_HOME/bin" \  
BUNDLE_SILENCE_ROOT_WARNING=1 \  
BUNDLE_APP_CONFIG="$GEM_HOME"  
ENV PATH $BUNDLE_BIN:$PATH  
  
WORKDIR /src  
  
# clone parse doc  
RUN apk --no-cache add git \  
&& git clone https://github.com/ParsePlatform/docs.git \  
&& apk del git  
  
RUN \  
apk --no-cache add ruby && \  
build_pkgs="autoconf bison bzip2 bzip2-dev coreutils gcc make" && \  
ruby_build_pkgs="gdbm-dev glib-dev libc-dev libxml2-dev libxslt-dev linux-
headers ncurses-dev readline-dev ruby-dev ruby-rdoc ruby-irb libffi-dev
openssl-dev yaml-dev zlib-dev " && \  
ruby_runtime_pkgs="ruby bzip2 ca-certificates curl procps gmp ruby-io-console
" && \  
nodejs_build_pkgs="python paxctl gnupg g++" && \  
nodejs_runtime_pkgs="libgcc libstdc++" && \  
apk --no-cache add ${build_pkgs} ${ruby_build_pkgs} ${ruby_runtime_pkgs}
${nodejs_build_pkgs} ${nodejs_runtime_pkgs} && \  
mkdir -p /usr/local/etc && \  
{ \  
echo 'install: --no-document'; \  
echo 'update: --no-document'; \  
} >> /usr/local/etc/gemrc && \  
gem install bundler --version $BUNDLER_VERSION && \  
mkdir -p "$GEM_HOME" "$BUNDLE_BIN" && \  
chmod 777 "$GEM_HOME" "$BUNDLE_BIN" && \  
echo "Installing bundler" && \  
cd /src/docs && \  
bundle config build.nokogiri --use-system-libraries && \  
bundle install && \  
cd /src && \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys \  
9554F04D7259F04124DE6B476D5A82AC7E37093B \  
94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \  
0034A06D9D9B0064CE8ADF6BF1747F4AD2306D93 \  
FD3A5288F042B6850C66B31F09FE44734EB7990E \  
71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \  
DD8F2338BAE7501E3DD5AC78C273792F7D83545D \  
C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \  
B9AE9905FFD7803F25714661B63B535A4C206CA9 && \  
curl -o node-${NODE_VERSION}.tar.gz -sSL
https://nodejs.org/dist/${NODE_VERSION}/node-${NODE_VERSION}.tar.gz && \  
curl -o SHASUMS256.txt.asc -sSL
https://nodejs.org/dist/${NODE_VERSION}/SHASUMS256.txt.asc && \  
gpg --verify SHASUMS256.txt.asc && \  
grep node-${NODE_VERSION}.tar.gz SHASUMS256.txt.asc | sha256sum -c - && \  
tar -zxf node-${NODE_VERSION}.tar.gz && \  
cd node-${NODE_VERSION} && \  
export GYP_DEFINES="linux_use_gold_flags=0" && \  
./configure --prefix=/usr ${CONFIG_FLAGS} && \  
NPROC=$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) && \  
make -j${NPROC} -C out mksnapshot BUILDTYPE=Release && \  
paxctl -cm out/Release/mksnapshot && \  
make -j${NPROC} && \  
make install && \  
paxctl -cm /usr/bin/node && \  
if [ -x /usr/bin/npm ]; then \  
npm install -g npm@${NPM_VERSION} && \  
find /usr/lib/node_modules/npm -name test -o -name .bin -type d | xargs rm
-rf; \  
fi && \  
cd .. && \  
rm -rf /etc/ssl node-${NODE_VERSION}.tar.gz SHASUMS256.txt.asc
node-${NODE_VERSION} ${RM_DIRS} \  
/usr/share/man /tmp/* /var/cache/apk/* /root/.npm /root/.node-gyp /root/.gnupg
\  
/usr/lib/node_modules/npm/man /usr/lib/node_modules/npm/doc
/usr/lib/node_modules/npm/html \  
&& apk del ${build_pkgs} ${ruby_build_pkgs} ${nodejs_build_pkgs} && \  
cd /src/docs && \  
npm install && \  
npm run webpack && \  
rm -rf node_modules  
  
WORKDIR /src/docs  
  
EXPOSE 4000  
CMD ["/usr/local/bundle/bin/bundle","exec","jekyll","serve","-H","0.0.0.0"]  
  

