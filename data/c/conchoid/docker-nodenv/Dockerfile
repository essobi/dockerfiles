FROM node:8.9.4-alpine  
  
RUN set -x \  
&& GLIBC_PKG_VERSION="${GLIBC_PKG_VERSION:-2.26-r0}" \  
&& GLIBC_URL="https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/$GLIBC_PKG_VERSION" \  
&& GLIBC_SSH_KEY="/etc/apk/keys/sgerrand.rsa.pub" \  
&& GLIBC_PKG_FILE="glibc-$GLIBC_PKG_VERSION.apk" \  
&& GLIBC_BIN_PKG_FILE="glibc-bin-$GLIBC_PKG_VERSION.apk" \  
&& apk add --no-cache --virtual=.fetchdeps wget ca-certificates \  
&& wget -q -O "$GLIBC_SSH_KEY"
"https://raw.githubusercontent.com/sgerrand/alpine-pkg-
glibc/master/sgerrand.rsa.pub" \  
&& wget -q "$GLIBC_URL/$GLIBC_PKG_FILE" "$GLIBC_URL/$GLIBC_BIN_PKG_FILE" \  
&& apk add --no-cache "$GLIBC_PKG_FILE" "$GLIBC_BIN_PKG_FILE" \  
&& apk del .fetchdeps \  
&& rm "$GLIBC_SSH_KEY" \  
&& rm ~/.wget-hsts \  
&& rm "$GLIBC_PKG_FILE" "$GLIBC_BIN_PKG_FILE"  
  
RUN mkdir -p /var/cache/apk \  
&& ln -s /var/cache/apk /etc/apk/cache  
  
RUN apk add --no-cache \  
bash="4.3.48-r1" \  
build-base="0.5-r0" \  
binutils-gold="2.28-r3" \  
git="2.13.5-r0" \  
linux-headers="4.4.6-r2" \  
openssl="1.0.2o-r0" \  
openssl-dev="1.0.2o-r0" \  
python="2.7.14-r0" \  
wget="1.19.2-r0"  
  
RUN rm /etc/apk/cache  
  
ENV NODENV_ROOT /opt/nodenv  
ENV PATH "$NODENV_ROOT/shims:$NODENV_ROOT/bin:$PATH"  
RUN set -x \  
&& nodenv_version="v1.1.2" \  
&& git clone https://github.com/nodenv/nodenv.git ${NODENV_ROOT} \  
&& cd ${NODENV_ROOT} && git checkout ${nodenv_version} \  
&& src/configure \  
&& make -C src \  
&& node_build_version="v3.0.0" \  
&& git clone https://github.com/nodenv/node-build.git
${NODENV_ROOT}/plugins/node-build \  
&& cd ${NODENV_ROOT}/plugins/node-build && git checkout ${node_build_version}
\  
&& npm_migrate_version="0.1.0" \  
&& git clone https://github.com/nodenv/nodenv-npm-migrate.git
${NODENV_ROOT}/plugins/nodenv-npm-migrate \  
&& cd ${NODENV_ROOT}/plugins/nodenv-npm-migrate && git checkout
${npm_migrate_version} \  
&& rm -rf ${NODENV_ROOT}/.git ${NODENV_ROOT}/plugins/node-build/.git
${NODENV_ROOT}/plugins/nodenv-npm-migrate/.git  

