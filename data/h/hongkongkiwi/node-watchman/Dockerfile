FROM node:9-alpine  
LABEL maintainer "Andy Savage"  
  
ENV TZ 'Asia/Hong_Kong'  
ENV WATCHMAN_VERSION '4.9.0'  
ENV WATCHMAN_REPO 'https://github.com/facebook/watchman.git'  
  
RUN apk update \  
&& apk add --no-cache \  
git build-base automake autoconf libtool openssl-dev \  
linux-headers ca-certificates tzdata curl pcre-dev \  
file \  
libc6-compat \  
tini \  
bash \  
&& cp "/usr/share/zoneinfo/${TZ}" /etc/localtime \  
&& echo "${TZ}" > /etc/timezone \  
# Install Watchman  
&& git clone "$WATCHMAN_REPO" /tmp/watchman-src \  
&& cd /tmp/watchman-src \  
&& git checkout -q "v${WATCHMAN_VERSION}"  
  
RUN cd /tmp/watchman-src \  
&& ./autogen.sh \  
&& ./configure --enable-statedir=/tmp \  
\--without-python --with-pcre="/usr/bin/pcre-config" \  
\--with-buildinfo="Built in Alpine Dockerfile" \  
&& make \  
&& make install  
# clean up dependencies  
  
RUN apk del --purge \  
git build-base automake autoconf \  
linux-headers ca-certificates \  
tzdata curl file \  
&& rm -rf /var/cache/apk/ \  
&& mkdir -p /var/cache/apk/ \  
&& rm -r /tmp/watchman-src  
  
ENTRYPOINT [ "/sbin/tini", "--" ]  

