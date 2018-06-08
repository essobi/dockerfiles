FROM openjdk:jre-slim  
  
ENV WHITESOURCE_HOME=/opt/whitesource \  
NODE_VERSION=6.13.1 \  
YARN_VERSION=1.5.1 \  
CHROME_BIN=chromium \  
WHITESOURCE_VERSION=17.12.4 \  
SONAR_SCANNER_VERSION=3.1.0.1141  
RUN set -ex \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends \  
gnupg \  
dirmngr \  
curl \  
git-core \  
zip \  
unzip \  
chromium  
  
RUN groupadd --gid 1000 node \  
&& useradd --uid 1000 --gid node --shell /bin/bash --create-home node  
  
# gpg keys listed at https://github.com/nodejs/node#release-team  
RUN set -ex \  
&& for key in \  
94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \  
FD3A5288F042B6850C66B31F09FE44734EB7990E \  
71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \  
DD8F2338BAE7501E3DD5AC78C273792F7D83545D \  
C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \  
B9AE9905FFD7803F25714661B63B535A4C206CA9 \  
56730D5401028683275BD23C23EFEFE93C4CFFFE \  
77984A986EBC2AA786BC0F66B01FBB92821C587A \  
; do \  
gpg --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys "$key" || \  
gpg --keyserver hkp://ipv4.pool.sks-keyservers.net --recv-keys "$key" || \  
gpg --keyserver hkp://pgp.mit.edu:80 --recv-keys "$key" ; \  
done  
  
RUN buildDeps='xz-utils' \  
&& ARCH= && dpkgArch="$(dpkg --print-architecture)" \  
&& case "${dpkgArch##*-}" in \  
amd64) ARCH='x64';; \  
ppc64el) ARCH='ppc64le';; \  
s390x) ARCH='s390x';; \  
arm64) ARCH='arm64';; \  
armhf) ARCH='armv7l';; \  
i386) ARCH='x86';; \  
*) echo "unsupported architecture"; exit 1 ;; \  
esac \  
&& set -x \  
&& apt-get update && apt-get install -y $buildDeps \--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/* \  
&& curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-$ARCH.tar.xz" \  
&& curl -SLO --compressed
"https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \  
&& gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc \  
&& grep " node-v$NODE_VERSION-linux-$ARCH.tar.xz\$" SHASUMS256.txt | sha256sum
-c - \  
&& tar -xJf "node-v$NODE_VERSION-linux-$ARCH.tar.xz" -C /usr/local \--strip-
components=1 --no-same-owner \  
&& rm "node-v$NODE_VERSION-linux-$ARCH.tar.xz" SHASUMS256.txt.asc
SHASUMS256.txt \  
&& apt-get purge -y --auto-remove $buildDeps \  
&& ln -s /usr/local/bin/node /usr/local/bin/nodejs  
  
RUN set -ex \  
&& for key in \  
6A010C5166006599AA17F08146C2130DFD2497F5 \  
; do \  
gpg --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys "$key" || \  
gpg --keyserver hkp://ipv4.pool.sks-keyservers.net --recv-keys "$key" || \  
gpg --keyserver hkp://pgp.mit.edu:80 --recv-keys "$key" ; \  
done \  
&& curl -fSLO --compressed
"https://yarnpkg.com/downloads/$YARN_VERSION/yarn-v$YARN_VERSION.tar.gz" \  
&& curl -fSLO --compressed
"https://yarnpkg.com/downloads/$YARN_VERSION/yarn-v$YARN_VERSION.tar.gz.asc" \  
&& gpg --batch --verify yarn-v$YARN_VERSION.tar.gz.asc
yarn-v$YARN_VERSION.tar.gz \  
&& mkdir -p /opt \  
&& tar -xzf yarn-v$YARN_VERSION.tar.gz -C /opt/ \  
&& ln -s /opt/yarn-v$YARN_VERSION/bin/yarn /usr/local/bin/yarn \  
&& ln -s /opt/yarn-v$YARN_VERSION/bin/yarnpkg /usr/local/bin/yarnpkg \  
&& rm yarn-v$YARN_VERSION.tar.gz.asc yarn-v$YARN_VERSION.tar.gz  
  
RUN mkdir -p $WHITESOURCE_HOME  
ADD https://s3.amazonaws.com/file-system-agent/whitesource-fs-
agent-$WHITESOURCE_VERSION.jar $WHITESOURCE_HOME  
RUN chmod +x $WHITESOURCE_HOME/whitesource-fs-agent-$WHITESOURCE_VERSION.jar  
  
# Install Cloud Foundry cli  
ADD https://cli.run.pivotal.io/stable?release=linux64-binary&version=6.32.0
/tmp/cf-cli.tgz  
RUN mkdir -p /usr/local/bin && \  
tar -xzf /tmp/cf-cli.tgz -C /usr/local/bin && \  
cf --version && \  
rm -f /tmp/cf-cli.tgz  
  
# Install cf cli Autopilot plugin  
ADD https://github.com/contraband/autopilot/releases/download/0.0.3/autopilot-
linux /tmp/autopilot-linux  
RUN chmod +x /tmp/autopilot-linux && \  
cf install-plugin /tmp/autopilot-linux -f && \  
rm -f /tmp/autopilot-linux  
  
# Install yaml cli  
ADD https://github.com/mikefarah/yaml/releases/download/1.10/yaml_linux_amd64
/tmp/yaml_linux_amd64  
RUN install /tmp/yaml_linux_amd64 /usr/local/bin/yaml && \  
yaml --help && \  
rm -f /tmp/yaml_linux_amd64  
  
ADD https://sonarsource.bintray.com/Distribution/sonar-scanner-cli/sonar-
scanner-cli-$SONAR_SCANNER_VERSION.zip /tmp/sonarscanner.zip  
RUN unzip /tmp/sonarscanner.zip -d /opt/sonarscanner && \  
rm /tmp/sonarscanner.zip  
  
ENV SONAR_RUNNER_HOME=/opt/sonarscanner/sonar-scanner-$SONAR_SCANNER_VERSION \  
PATH=$PATH:/opt/sonarscanner/sonar-scanner-$SONAR_SCANNER_VERSION/bin  

