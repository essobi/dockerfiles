FROM alpine:3.5  
  
# Build node  
  
ENV NODE_VERSION 7.9.0  
  
RUN addgroup -g 1000 node \  
&& adduser -u 1000 -G node -s /bin/sh -D node \  
&& apk add --no-cache \  
libstdc++ \  
&& apk add --no-cache --virtual .build-deps \  
binutils-gold \  
curl \  
g++ \  
gcc \  
gnupg \  
libgcc \  
linux-headers \  
make \  
python \  
# gpg keys listed at https://github.com/nodejs/node#release-team  
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
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key" || \  
gpg --keyserver pgp.mit.edu --recv-keys "$key" || \  
gpg --keyserver keyserver.pgp.com --recv-keys "$key" ; \  
done \  
&& curl -SLO
"https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION.tar.xz" \  
&& curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \  
&& gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc \  
&& grep " node-v$NODE_VERSION.tar.xz\$" SHASUMS256.txt | sha256sum -c - \  
&& tar -xf "node-v$NODE_VERSION.tar.xz" \  
&& cd "node-v$NODE_VERSION" \  
&& ./configure \  
&& make -j$(getconf _NPROCESSORS_ONLN) \  
&& make install \  
&& apk del .build-deps \  
&& cd .. \  
&& rm -Rf "node-v$NODE_VERSION" \  
&& rm "node-v$NODE_VERSION.tar.xz" SHASUMS256.txt.asc SHASUMS256.txt  
  
ENV YARN_VERSION 0.23.2  
  
RUN apk add --no-cache --virtual .build-deps-yarn curl gnupg \  
&& for key in \  
6A010C5166006599AA17F08146C2130DFD2497F5 \  
; do \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key" || \  
gpg --keyserver pgp.mit.edu --recv-keys "$key" || \  
gpg --keyserver keyserver.pgp.com --recv-keys "$key" ; \  
done \  
&& curl -fSL -o yarn.js "https://yarnpkg.com/downloads/$YARN_VERSION/yarn-
legacy-$YARN_VERSION.js" \  
&& curl -fSL -o yarn.js.asc "https://yarnpkg.com/downloads/$YARN_VERSION/yarn-
legacy-$YARN_VERSION.js.asc" \  
&& gpg --batch --verify yarn.js.asc yarn.js \  
&& rm yarn.js.asc \  
&& mv yarn.js /usr/local/bin/yarn \  
&& chmod +x /usr/local/bin/yarn \  
&& apk del .build-deps-yarn  
  
# Build nginx  
  
ENV NGINX_VERSION 1.11.13  
  
RUN CONFIG="\  
\--prefix=/home/node/nginx \  
\--sbin-path=/usr/sbin/nginx \  
\--modules-path=/usr/lib/nginx/modules \  
\--conf-path=/home/node/nginx/nginx.conf \  
\--error-log-path=/home/node/nginx/log/error.log \  
\--http-log-path=/home/node/nginx/log/access.log \  
\--pid-path=/home/node/nginx/nginx.pid \  
\--lock-path=/home/node/nginx/nginx.lock \  
\--http-client-body-temp-path=/home/node/nginx/cache/client_temp \  
\--http-proxy-temp-path=/home/node/nginx/cache/proxy_temp \  
\--http-fastcgi-temp-path=/home/node/nginx/cache/fastcgi_temp \  
\--http-uwsgi-temp-path=/home/node/nginx/cache/uwsgi_temp \  
\--http-scgi-temp-path=/home/node/nginx/cache/scgi_temp \  
\--user=node \  
\--group=node \  
\--with-http_ssl_module \  
\--with-http_gunzip_module \  
\--with-http_gzip_static_module \  
\--with-threads \  
\--with-stream \  
\--with-compat \  
\--with-file-aio \  
\--with-http_v2_module \  
" \  
&& apk add --no-cache --virtual .build-deps \  
gcc \  
libc-dev \  
make \  
openssl-dev \  
pcre-dev \  
zlib-dev \  
linux-headers \  
curl \  
gnupg \  
&& curl -fSL https://github.com/rdngr/nginx-
background/archive/v$NGINX_VERSION-bgpatch.tar.gz -o nginx.tar.gz \  
&& mkdir -p /usr/src \  
&& tar -zxC /usr/src -f nginx.tar.gz \  
&& rm nginx.tar.gz \  
&& ls -al /usr/src \  
&& cd /usr/src/nginx-background-$NGINX_VERSION-bgpatch \  
&& ls -al \  
&& ./configure $CONFIG --with-debug \  
&& make -j$(getconf _NPROCESSORS_ONLN) \  
&& mv objs/nginx objs/nginx-debug \  
&& ./configure $CONFIG \  
&& make -j$(getconf _NPROCESSORS_ONLN) \  
&& make install \  
&& rm -rf /home/node/nginx/html/ \  
&& mkdir /home/node/nginx/conf.d/ \  
&& mkdir -p /usr/share/nginx/html/ \  
&& install -m644 html/index.html /usr/share/nginx/html/ \  
&& install -m644 html/50x.html /usr/share/nginx/html/ \  
&& install -m755 objs/nginx-debug /usr/sbin/nginx-debug \  
&& strip /usr/sbin/nginx* \  
&& rm -rf /usr/src/nginx-background-$NGINX_VERSION-bgpatch \  
\  
# Bring in gettext so we can get `envsubst`, then throw  
# the rest away. To do this, we need to install `gettext`  
# then move `envsubst` out of the way so `gettext` can  
# be deleted completely, then move `envsubst` back.  
&& apk add --no-cache --virtual .gettext gettext \  
&& mv /usr/bin/envsubst /tmp/ \  
\  
&& runDeps="$( \  
scanelf --needed --nobanner /usr/sbin/nginx /usr/lib/nginx/modules/*.so
/tmp/envsubst \  
| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \  
| sort -u \  
| xargs -r apk info --installed \  
| sort -u \  
)" \  
&& apk add --no-cache --virtual .nginx-rundeps $runDeps \  
&& apk del .build-deps \  
&& apk del .gettext \  
&& mv /tmp/envsubst /usr/local/bin/ \  
\  
# forward request and error logs to docker log collector  
&& ln -sf /dev/stdout /home/node/nginx/log/access.log \  
&& ln -sf /dev/stderr /home/node/nginx/log/error.log  
  
RUN chown -R node:node /home/node/nginx  
  
ENV PORT 8080  
ENV NODE_PORT 8081  
  
COPY nginx.conf /home/node/nginx/  
COPY start.sh /home/node/  
  
ONBUILD WORKDIR /home/node/app  
ONBUILD COPY package.json yarn.lock ./  
ONBUILD RUN yarn install --production \  
&& yarn cache clean  
ONBUILD COPY . .  
ONBUILD USER node  
  
CMD ../start.sh  

