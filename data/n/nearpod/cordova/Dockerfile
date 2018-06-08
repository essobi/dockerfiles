FROM nearpod/android:android-201803  
ARG NODE_VERSION=9.9.0  
ARG YARN_VERSION=1.5.1  
ARG CORDOVA_VERSION=8.0.0  
ENV NODE_VERSION=$NODE_VERSION  
ENV YARN_VERSION=$YARN_VERSION  
ENV CORDOVA_VERSION=$CORDOVA_VERSION  
ENV BUILD_USER=cordova  
ENV ARCH=x64  
  
# Import gpg keys of node signers from https://github.com/nodejs/node#release-
team  
RUN set -ex; \  
WORKDIR="$PWD"; \  
apt-get update; \  
apt-get install -y --no-install-recommends gnupg apt-transport-https dirmngr;
\  
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - ; \  
echo "deb https://dl.yarnpkg.com/debian/ stable main" >
/etc/apt/sources.list.d/yarn.list ; \  
apt-get update ; \  
for key in \  
94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \  
FD3A5288F042B6850C66B31F09FE44734EB7990E \  
71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \  
DD8F2338BAE7501E3DD5AC78C273792F7D83545D \  
C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \  
B9AE9905FFD7803F25714661B63B535A4C206CA9 \  
56730D5401028683275BD23C23EFEFE93C4CFFFE \  
77984A986EBC2AA786BC0F66B01FBB92821C587A \  
; do \  
gpg --keyserver pool.sks-keyservers.net --recv-keys $key || \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys $key || \  
gpg --keyserver hkp://ipv4.pool.sks-keyservers.net --recv-keys $key; \  
done; \  
curl -q -sSLO
"https://nodejs.org/download/release/v$NODE_VERSION/node-v$NODE_VERSION-
linux-$ARCH.tar.xz"; \  
curl -q -sSLO --compressed
"https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc"; \  
  
gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc; \  
tar -xf "node-v$NODE_VERSION-linux-$ARCH.tar.xz" \--xz -C /usr/local --strip-
components=1 \--no-same-owner; \  
apt-get install -y --no-install-recommends yarn git; \  
yarn global add cordova@"${CORDOVA_VERSION}" ; \  
cordova telemetry off; \  
rm SHASUMS256.txt SHASUMS256.txt.asc "node-v$NODE_VERSION-linux-$ARCH.tar.xz"
; \  
apt-get purge -y --auto-remove gnupg ; \  
apt-get autoremove --purge -y ; \  
apt-get clean -y ; \  
rm -rf /var/lib/apt/lists/* ;  
  
WORKDIR /app  
  
RUN set -ex; \  
mkdir -p /app; \  
WORKDIR="/app"; \  
groupadd --gid 1000 "$BUILD_USER"; \  
useradd -m -u 1000 -g "$BUILD_USER" "$BUILD_USER"; \  
[ `id -u "$BUILD_USER"` -eq 1000 ]; \  
[ `id -g "$BUILD_USER"` -eq 1000 ]; \  
mkdir -p "/home/$BUILD_USER/.android" ; \  
touch "/home/$BUILD_USER/.android/repositories.cfg" ; \  
chown "$BUILD_USER":"$BUILD_USER" -R "/home/$BUILD_USER/.android/";  
  
USER cordova:cordova  
  
RUN set -ex; \  
node -v; \  
yarn -v; \  
cordova -v; \  
cordova telemetry off  

