FROM alpine:3.6  
MAINTAINER Kouichi Machida <k-machida@aideo.co.jp>  
  
ENV LANG=C.UTF-8 \  
LC_ALL=C  
  
# jre  
ENV JAVA_VERSION=8u131 \  
JAVA_ALPINE_VERSION=8.131.11-r2 \  
JAVA_HOME=/usr/lib/jvm/java-1.8-openjdk/jre  
ENV PATH
$PATH:/usr/lib/jvm/java-1.8-openjdk/jre/bin:/usr/lib/jvm/java-1.8-openjdk/bin  
  
RUN apk add --no-cache \  
fontconfig \  
openjdk8-jre="${JAVA_ALPINE_VERSION}"  
  
# ruby  
ENV RUBY_MAJOR=2.4 \  
RUBY_VERSION=2.4.1 \  
RUBY_DOWNLOAD_SHA256=4fc8a9992de3e90191de369270ea4b6c1b171b7941743614cc50822ddc1fe654
\  
RUBYGEMS_VERSION=2.6.12  
  
RUN apk add --no-cache --virtual .ruby-builddeps \  
autoconf \  
bison \  
bzip2 \  
bzip2-dev \  
ca-certificates \  
coreutils \  
dpkg-dev \  
dpkg \  
gcc \  
gdbm-dev \  
glib-dev \  
libc-dev \  
libffi-dev \  
libressl \  
libressl-dev \  
libxml2-dev \  
libxslt-dev \  
linux-headers \  
make \  
ncurses-dev \  
procps \  
readline-dev \  
tar \  
xz \  
yaml-dev \  
zlib-dev \  
\  
&& wget -O /tmp/ruby.tar.xz "https://cache.ruby-
lang.org/pub/ruby/${RUBY_MAJOR%-rc}/ruby-${RUBY_VERSION}.tar.xz" \  
&& echo "${RUBY_DOWNLOAD_SHA256} */tmp/ruby.tar.xz" | sha256sum -c - \  
&& mkdir -p /tmp/ruby \  
&& tar -xJf /tmp/ruby.tar.xz -C /tmp/ruby --strip-components=1 \  
&& cd /tmp/ruby \  
&& { \  
echo '#define ENABLE_PATH_CHECK 0'; \  
echo; \  
cat file.c; \  
} > file.c.new \  
&& mv file.c.new file.c \  
&& autoconf \  
&& gnuArch="$(dpkg-architecture --query DEB_BUILD_GNU_TYPE)" \  
&& export ac_cv_func_isnan=yes ac_cv_func_isinf=yes \  
&& ./configure \  
\--build="${gnuArch}" \  
\--disable-install-doc \  
\--enable-shared \  
&& make -j "$(nproc)" \  
&& make install \  
\  
&& mkdir -p /usr/local/etc \  
&& { \  
echo 'install: --no-document'; \  
echo 'update: --no-document'; \  
} >> /usr/local/etc/gemrc \  
\  
&& runDeps="$( \  
scanelf --needed --nobanner --recursive /usr/local \  
| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \  
| sort -u \  
| xargs -r apk info --installed \  
| sort -u \  
)" \  
&& apk add --no-cache --virtual .ruby-rundeps ${runDeps} \  
bzip2 \  
libffi-dev \  
libressl \  
procps \  
yaml-dev \  
zlib-dev \  
\  
&& apk del .ruby-builddeps \  
&& rm -r /tmp/ruby \  
&& rm -rf /var/cache/apk/*  
  
# bundler  
ENV GEM_HOME /usr/local/bundle  
ENV BUNDLER_VERSION=1.15.3 \  
BUNDLE_PATH="$GEM_HOME" \  
BUNDLE_BIN="$GEM_HOME/bin" \  
BUNDLE_SILENCE_ROOT_WARNING=1 \  
BUNDLE_APP_CONFIG="$GEM_HOME"  
ENV PATH $BUNDLE_BIN:$PATH  
  
RUN gem update --system "${RUBYGEMS_VERSION}" \  
\  
&& gem install bundler --version "${BUNDLER_VERSION}" \  
&& mkdir -p "${GEM_HOME}" "${BUNDLE_BIN}" \  
&& chmod 777 "${GEM_HOME}" "${BUNDLE_BIN}" \  
\  
&& gem cleanup  
  
# node  
ENV NODE_VERSION 6.11.2  
ENV NPM_CONFIG_LOGLEVEL info  
  
RUN apk add --no-cache --virtual .node-builddeps \  
binutils-gold \  
curl \  
g++ \  
gcc \  
gnupg \  
libstdc++ \  
libgcc \  
linux-headers \  
make \  
python \  
\  
&& for key in \  
9554F04D7259F04124DE6B476D5A82AC7E37093B \  
94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \  
FD3A5288F042B6850C66B31F09FE44734EB7990E \  
71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \  
DD8F2338BAE7501E3DD5AC78C273792F7D83545D \  
B9AE9905FFD7803F25714661B63B535A4C206CA9 \  
C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \  
56730D5401028683275BD23C23EFEFE93C4CFFFE \  
; do \  
gpg --keyserver pgp.mit.edu --recv-keys "$key" || \  
gpg --keyserver keyserver.pgp.com --recv-keys "$key" || \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key" ; \  
done \  
\  
&& cd /tmp \  
&& curl -SLO
"https://nodejs.org/dist/v${NODE_VERSION}/node-v${NODE_VERSION}.tar.xz" \  
&& curl -SLO --compressed
"https://nodejs.org/dist/v${NODE_VERSION}/SHASUMS256.txt.asc" \  
&& gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc \  
&& grep " node-v${NODE_VERSION}.tar.xz\$" SHASUMS256.txt | sha256sum -c - \  
&& tar -xf "node-v${NODE_VERSION}.tar.xz" \  
&& cd "node-v${NODE_VERSION}" \  
&& ./configure \  
&& make -j$(getconf _NPROCESSORS_ONLN) \  
&& make install \  
\  
&& runDeps="$( \  
scanelf --needed --nobanner --recursive /usr/local \  
| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \  
| sort -u \  
| xargs -r apk info --installed \  
| sort -u \  
)" \  
&& apk add --no-cache --virtual .node-rundeps ${runDeps} \  
libstdc++ \  
\  
&& apk del .node-builddeps \  
&& rm -rf /tmp/* \  
&& rm -rf /var/cache/apk/*  
  
# npm, yarn  
ENV NPM_VERSION 5.0.3  
ENV YARN_VERSION 0.27.5  
  
RUN apk add --no-cache --virtual .build-deps-yarn \  
curl \  
gnupg \  
tar \  
&& for key in \  
6A010C5166006599AA17F08146C2130DFD2497F5 \  
; do \  
gpg --keyserver pgp.mit.edu --recv-keys "$key" || \  
gpg --keyserver keyserver.pgp.com --recv-keys "$key" || \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key" ; \  
done \  
\  
&& cd /tmp \  
&& curl -fSLO --compressed
"https://yarnpkg.com/downloads/${YARN_VERSION}/yarn-v${YARN_VERSION}.tar.gz" \  
&& curl -fSLO --compressed
"https://yarnpkg.com/downloads/${YARN_VERSION}/yarn-v${YARN_VERSION}.tar.gz.asc"
\  
&& gpg --batch --verify yarn-v${YARN_VERSION}.tar.gz.asc
yarn-v${YARN_VERSION}.tar.gz \  
&& mkdir -p /opt/yarn \  
&& tar -xzf yarn-v${YARN_VERSION}.tar.gz -C /opt/yarn --strip-components=1 \  
&& ln -s /opt/yarn/bin/yarn /usr/local/bin/yarn \  
&& ln -s /opt/yarn/bin/yarn /usr/local/bin/yarnpkg \  
\  
&& rm yarn-v${YARN_VERSION}.tar.gz.asc yarn-v${YARN_VERSION}.tar.gz \  
&& apk del .build-deps-yarn \  
\  
&& yarn global add npm@${NPM_VERSION} \  
\  
&& yarn cache clean  
  
# erd  
ENV ERD_URL=https://github.com/cosmicvelocity/erd-build/raw/master/dist/erd  
  
RUN apk add --no-cache --virtual .erd-builddeps \  
curl \  
\  
&& curl -L -o /tmp/erd "${ERD_URL}" \  
&& install -m755 /tmp/erd /usr/local/bin/erd \  
\  
&& apk del .erd-builddeps \  
&& rm -rf /tmp/*  
  
# fonts  
ENV IPA_EX_URL=http://dl.ipafont.ipa.go.jp/IPAexfont/IPAexfont00301.zip \  
IPA_EX_FOLDER=IPAexfont00301 \  
NOTO_CJK_JP_URL=https://noto-
website.storage.googleapis.com/pkgs/NotoSansCJKjp-hinted.zip  
  
RUN apk add --no-cache --virtual .fonts-builddeps \  
curl \  
\  
&& apk add --no-cache --repository
http://dl-4.alpinelinux.org/alpine/edge/testing/ --allow-untrusted \  
font-noto \  
\  
&& curl -L -o /tmp/ipaex.zip "${IPA_EX_URL}" \  
\  
&& cd /tmp \  
&& unzip /tmp/ipaex.zip \  
&& mkdir -p /usr/share/fonts/ipa \  
&& mv /tmp/${IPA_EX_FOLDER}/*.ttf /usr/share/fonts/ipa/ \  
&& mv /tmp/${IPA_EX_FOLDER}/IPA_Font_License_Agreement_v1.0.txt / \  
\  
&& curl -L -o /tmp/noto-cjk-jp.zip "${NOTO_CJK_JP_URL}" \  
\  
&& cd /tmp \  
&& unzip /tmp/noto-cjk-jp.zip \  
&& mkdir -p /usr/share/fonts/noto \  
&& mv /tmp/*.otf /usr/share/fonts/noto/ \  
&& mv /tmp/LICENSE_OFL.txt /noto-cjk-LICENSE_OFL.txt \  
\  
&& fc-cache -f -v \  
\  
&& apk del .fonts-builddeps \  
&& rm -rf /tmp/*  
  
# graphviz  
RUN apk add --no-cache \  
graphviz  
  
# asciidoctor  
RUN apk add --no-cache --virtual .asciidoctor-builddeps \  
bison \  
build-base \  
cmake \  
flex \  
gdk-pixbuf-dev \  
libxml2-dev \  
pango-dev \  
\  
&& gem install \  
asciidoctor \  
asciidoctor-diagram \  
asciidoctor-mathematical \  
asciidoctor-pdf-cjk \  
\  
&& runDeps="$( \  
scanelf --needed --nobanner --recursive /usr/local \  
| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \  
| sort -u \  
| xargs -r apk info --installed \  
| sort -u \  
)" \  
&& apk add --no-cache --virtual .asciidoctor-rundeps ${runDeps} \  
\  
&& apk del .asciidoctor-builddeps \  
&& rm -rf /tmp/* \  
&& gem cleanup  

