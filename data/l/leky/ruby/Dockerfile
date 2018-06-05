FROM leky/alpine:latest  
MAINTAINER leky <lekyzsj@gmail.com>  
  
ENV RUBY_MAJOR=2.3 \  
RUBY_VERSION=2.3.1 \  
RUBY_DOWNLOAD_SHA256="b87c738cb2032bf4920fef8e3864dc5cf8eae9d89d8d523ce0236945c5797dcd"
\  
GEM_MIRROR="https://mirrors.ustc.edu.cn/rubygems/"  
  
# Gem config.  
# Use ruby-china mirror.  
RUN mkdir -p /usr/local/etc \  
&& { \  
echo ":sources:" ; \  
echo "- ${GEM_MIRROR}" ; \  
echo ":install: --no-document -V" ; \  
echo ":update: --no-document -V" ; \  
} >> /usr/local/etc/gemrc  
  
# Install dependencies.  
RUN apk add --no-cache --virtual .rubyBuildDeps \  
autoconf \  
bison \  
build-base \  
ca-certificates \  
coreutils \  
curl \  
linux-headers \  
bzip2-dev \  
gdbm-dev \  
glib-dev \  
libffi-dev \  
libxml2-dev \  
libxslt-dev \  
openssl-dev \  
procps \  
readline-dev \  
yaml-dev \  
zlib-dev \  
&& curl -o ruby.tar.gz -fSL "https://cache.ruby-
lang.org/pub/ruby/${RUBY_MAJOR}/ruby-${RUBY_VERSION}.tar.gz" \  
&& echo "${RUBY_DOWNLOAD_SHA256} *ruby.tar.gz" | sha256sum -c - \  
&& mkdir -p /usr/src \  
&& tar -xzf ruby.tar.gz -C /usr/src \  
&& mv "/usr/src/ruby-${RUBY_VERSION}" /usr/src/ruby \  
&& rm -rf ruby.tar.gz \  
&& cd /usr/src/ruby \  
&& ./configure --disable-install-doc \  
&& make -j$(grep 'cpu cores' /proc/cpuinfo | uniq | grep -Eo '\d+') \  
&& make install \  
&& gem update --system \  
# Use ustc mirror as bundler default mirror.  
&& gem install bundler && bundle config mirror.https://rubygems.org
${GEM_MIRROR} \  
&& rm -rf /usr/src/ruby \  
&& runDeps="$( \  
scanelf --needed --nobanner --recursive /usr/local \  
| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \  
| sort -u \  
| xargs -r apk info --installed \  
| sort -u \  
)" \  
&& apk add --no-cache --virtual .rubyRunDeps ${runDeps} \  
bzip2 \  
ca-certificates \  
curl \  
libffi-dev \  
libxml2-dev \  
libxslt-dev \  
yaml-dev \  
procps \  
&& apk del .rubyBuildDeps  
  
CMD [ "irb" ]  

