ARG BASE_IMAGE  
FROM ${BASE_IMAGE:-library/alpine}:edge  
  
ARG QEMU_ARCH  
ENV QEMU_ARCH=${QEMU_ARCH:-x86_64} S6_KEEP_ENV=1  
COPY qemu/qemu-${QEMU_ARCH}-static /usr/bin/  
  
RUN set -x && apk add --no-cache libgcc libstdc++ curl curl-dev coreutils
tzdata shadow libstdc++ paxctl \  
&& case "${QEMU_ARCH}" in \  
x86_64) S6_ARCH='amd64';; \  
arm) S6_ARCH='armhf';; \  
aarch64) S6_ARCH='aarch64';; \  
*) echo "unsupported architecture"; exit 1 ;; \  
esac \  
&& curl -L -s https://github.com/just-
containers/s6-overlay/releases/download/v1.21.1.1/s6-overlay-${S6_ARCH}.tar.gz
| tar xvzf - -C / \  
&& groupmod -g 911 users && \  
useradd -u 911 -U -d /config -s /bin/false abc && \  
usermod -G users abc && \  
mkdir -p /app /config /defaults && \  
apk del --purge \  
rm -rf /tmp/*  
  
ENV NODE_VERSION 8.11.2  
RUN set -x && curl -fLO https://github.com/oznu/alpine-
node/releases/download/${NODE_VERSION}/node-v${NODE_VERSION}-linux-${QEMU_ARCH}-alpine.tar.gz
\  
&& tar -xzf node-v${NODE_VERSION}-linux-${QEMU_ARCH}-alpine.tar.gz -C /usr
--strip-components=1 --no-same-owner \  
&& rm -rf node-v${NODE_VERSION}-linux-${QEMU_ARCH}-alpine.tar.gz \  
&& paxctl -cm `which node` \  
&& npm set prefix /usr/local \  
&& npm config set unsafe-perm true  
  
ENV YARN_VERSION 1.6.0  
RUN set -ex \  
&& curl -fSLO
"https://yarnpkg.com/downloads/$YARN_VERSION/yarn-v$YARN_VERSION.tar.gz" \  
&& mkdir -p /opt/yarn \  
&& tar -xzf yarn-v$YARN_VERSION.tar.gz -C /opt/yarn --strip-components=1 \  
&& ln -s /opt/yarn/bin/yarn /usr/local/bin/yarn \  
&& ln -s /opt/yarn/bin/yarn /usr/local/bin/yarnpkg \  
&& rm yarn-v$YARN_VERSION.tar.gz  
  
COPY rootfs /  
  
ENTRYPOINT [ "/init" ]  

