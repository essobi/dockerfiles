FROM library/ubuntu:16.04  
LABEL maintainer="Gerardo Junior <me@gerardo-junior.com>"  
  
# set default build arguments  
ARG ANDROID_VERSION=25.2.3  
ENV NPM_CONFIG_LOGLEVEL warn  
ENV NODE_VERSION 6.12.2  
ENV YARN_VERSION 1.3.2  
# set default environment variables  
ENV ADB_INSTALL_TIMEOUT 10  
ENV ANDROID_HOME /opt/android  
ENV ANDROID_SDK_HOME ${ANDROID_HOME}  
ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-
tools:/opt/tools:/opt/buck/bin/  
  
# install system dependencies  
RUN apt-get update -y && \  
apt-get upgrade -y && \  
apt-get install -y autoconf \  
automake \  
expect \  
curl \  
g++ \  
gcc \  
git \  
libqt5widgets5 \  
lib32z1 \  
lib32stdc++6 \  
make \  
maven \  
openjdk-8-jdk \  
python-dev \  
python3-dev \  
qml-module-qtquick-controls \  
qtdeclarative5-dev \  
unzip \  
xz-utils && \  
rm -rf /var/lib/apt/lists/* && \  
apt-get autoremove -y && \  
apt-get clean  
  
# install nodejs  
RUN set -ex \  
&& for key in 94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \  
FD3A5288F042B6850C66B31F09FE44734EB7990E \  
71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \  
DD8F2338BAE7501E3DD5AC78C273792F7D83545D \  
C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \  
B9AE9905FFD7803F25714661B63B535A4C206CA9 \  
56730D5401028683275BD23C23EFEFE93C4CFFFE \  
77984A986EBC2AA786BC0F66B01FBB92821C587A; do \  
gpg --keyserver pgp.mit.edu --recv-keys "$key" || \  
gpg --keyserver keyserver.pgp.com --recv-keys "$key" || \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key" ; \  
done \  
&& ARCH= && dpkgArch="$(dpkg --print-architecture)" \  
&& case "${dpkgArch##*-}" in \  
amd64) ARCH='x64';; \  
ppc64el) ARCH='ppc64le';; \  
s390x) ARCH='s390x';; \  
arm64) ARCH='arm64';; \  
armhf) ARCH='armv7l';; \  
i386) ARCH='x86';; \  
*) echo "unsupported architecture"; exit 1 ;; \  
esac && \  
curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-$ARCH.tar.xz" && \  
curl -SLO --compressed
"https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" && \  
gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc && \  
grep " node-v$NODE_VERSION-linux-$ARCH.tar.xz\$" SHASUMS256.txt | sha256sum -c
- && \  
tar -xJf "node-v$NODE_VERSION-linux-$ARCH.tar.xz" -C /usr/local \--strip-
components=1 --no-same-owner && \  
rm "node-v$NODE_VERSION-linux-$ARCH.tar.xz" SHASUMS256.txt.asc SHASUMS256.txt
&& \  
ln -s /usr/local/bin/node /usr/local/bin/nodejs  
  
# install yarn  
RUN set -ex \  
&& for key in 6A010C5166006599AA17F08146C2130DFD2497F5; do \  
gpg --keyserver pgp.mit.edu --recv-keys "$key" || \  
gpg --keyserver keyserver.pgp.com --recv-keys "$key" || \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key" ; \  
done && \  
curl -fSLO --compressed
"https://yarnpkg.com/downloads/$YARN_VERSION/yarn-v$YARN_VERSION.tar.gz" && \  
curl -fSLO --compressed
"https://yarnpkg.com/downloads/$YARN_VERSION/yarn-v$YARN_VERSION.tar.gz.asc"
&& \  
gpg --batch --verify yarn-v$YARN_VERSION.tar.gz.asc yarn-v$YARN_VERSION.tar.gz
&& \  
mkdir -p /opt/yarn && \  
tar -xzf yarn-v$YARN_VERSION.tar.gz -C /opt/yarn --strip-components=1 && \  
ln -s /opt/yarn/bin/yarn /usr/local/bin/yarn && \  
ln -s /opt/yarn/bin/yarn /usr/local/bin/yarnpkg && \  
rm yarn-v$YARN_VERSION.tar.gz.asc yarn-v$YARN_VERSION.tar.gz  
  
# configure npm  
RUN /usr/local/bin/npm config set spin=false && \  
/usr/local/bin/npm config set progress=false && \  
/usr/local/bin/npm install -g react-native-cli exp && \  
/usr/local/bin/npm cache clean  
  
# configure yarn  
RUN /usr/local/bin/yarn config set no-progress && \  
/usr/local/bin/yarn config set no-spin  
  
# download and unpack android  
RUN mkdir -p $ANDROID_SDK_HOME && mkdir -p /opt/tools && \  
cd $ANDROID_SDK_HOME && \  
curl --silent
https://dl.google.com/android/repository/tools_r$ANDROID_VERSION-linux.zip >
android.zip && \  
unzip android.zip && \  
rm android.zip  
  
# copy scripts  
COPY ./tools/android-accept-licenses.sh /opt/tools/android-accept-licenses.sh  
COPY ./entrypoint.sh /opt/tools/entrypoint.sh  
RUN chmod +x /opt/tools/entrypoint.sh /opt/tools/android-accept-licenses.sh  
  
# adding licenses  
RUN mkdir -p $ANDROID_HOME/licenses/ && \  
echo "d56f5187479451eabf01fb78af6dfcb131a6481e" >
$ANDROID_HOME/licenses/android-sdk-license && \  
echo "84831b9409646a918e30573bab4c9c91346d8abd" >
$ANDROID_HOME/licenses/android-sdk-preview-license  
  
# updating sdk  
RUN /opt/tools/android-accept-licenses.sh "$ANDROID_HOME/tools/bin/sdkmanager
\  
tools \  
\"platform-tools\" \  
\"build-tools;23.0.1\" \  
\"build-tools;23.0.3\" \  
\"build-tools;25.0.1\" \  
\"build-tools;25.0.2\" \  
\"platforms;android-23\" \  
\"platforms;android-25\" \  
\"extras;android;m2repository\" \  
\"extras;google;m2repository\" \  
\"add-ons;addon-google_apis-google-24\" \  
\"extras;google;google_play_services\"" \  
&& $ANDROID_HOME/tools/bin/sdkmanager --update  
  
VOLUME ["/app"]  
WORKDIR /app  
ENTRYPOINT ["/bin/bash", "/opt/tools/entrypoint.sh"]

