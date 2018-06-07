FROM alpine:latest  
  
ARG USER=node  
ARG APP_PATH="/opt/react-vr-pano-switch"  
ENV APP_PATH="${APP_PATH}"  
RUN adduser -D -G users -u 1000 ${USER} -s /bin/false  
  
EXPOSE 8080  
RUN apk upgrade --no-cache  
  
# https://github.com/tianon/gosu/blob/master/INSTALL.md  
ENV GOSU_VERSION 1.10  
RUN set -ex; \  
\  
apk add --no-cache --virtual .gosu-deps \  
dpkg \  
gnupg \  
openssl \  
; \  
\  
dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')"; \  
wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch";
\  
wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch.asc";
\  
\  
# verify the signature  
export GNUPGHOME="$(mktemp -d)"; \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4; \  
gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu; \  
rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc; \  
\  
chmod +x /usr/local/bin/gosu; \  
# verify that the binary works  
gosu nobody true; \  
\  
apk del .gosu-deps  
  
RUN apk --no-cache add darkhttpd \  
&& apk add --no-cache --virtual .build-app-deps \  
bash \  
git \  
nodejs \  
nodejs-npm \  
&& mkdir -p "${APP_PATH}" \  
&& export SRC_REPO="/tmp/react-vr-pano-switch" \  
&& git clone https://github.com/hankei6km/react-vr-pano-switch.git
"${SRC_REPO}" \  
&& cd "${SRC_REPO}" \  
# && npm uninstall --save-dev babel-jest jest react-devtools react-test-
renderer xopen \  
&& npm install --production && npm install --only=dev babel-preset-react-
native \  
&& npm run bundle \  
&& cp "${SRC_REPO}"/vr/index.html "${SRC_REPO}"/vr/build/* "${APP_PATH}/" \  
&& cp -r "${SRC_REPO}"/static_assets "${APP_PATH}/" \  
&& sed -i "${APP_PATH}/index.html" -e
's/\\.\/client.bundle?platform=vr/.\/client.bundle.js?platform=vr/' \  
&& sed -i "${APP_PATH}/index.html" -e
's/\\.\\.\/index.vr.bundle?platform=vr&dev=true/.\/index.bundle.js?platform=vr/'
\  
&& npm cache verify \  
&& npm cache clean --force \  
&& apk del .build-app-deps \  
&& cd \  
&& rm -rf "${SRC_REPO}" /tmp/react-native-packager-cache-* \  
&& rm /tmp/haste-map* \  
&& rm -rf /tmp/npm* \  
&& rm -rf /var/lib/apt/*  
  
# ENTRYPOINT ["gosu", "1000", "/usr/bin/darkhttpd", "${APP_PATH}", "--port",
"8080"]  
ENTRYPOINT gosu 1000 /usr/bin/darkhttpd "${APP_PATH}" \--port 8080  

