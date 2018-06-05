FROM python:latest  
  
# Take care of Python dependencies  
RUN pip install awsebcli --upgrade  
RUN pip install boto3  
  
# Install Sonar Scanner  
ENV SONAR_VERSION 3.0.3.778  
RUN apt-get -y update && apt-get -y install curl unzip jq  
ARG
SONAR_SCANNER_DOWNLOAD_URL="https://sonarsource.bintray.com/Distribution/sonar-
scanner-cli/sonar-scanner-cli-$SONAR_VERSION-linux.zip"  
RUN curl -s -L "${SONAR_SCANNER_DOWNLOAD_URL}" > "/tmp/sonar-scanner-
cli-$SONAR_VERSION-linux.zip" \  
&& unzip -qq "/tmp/sonar-scanner-cli-$SONAR_VERSION-linux.zip" -d "/opt" \  
&& mv "/opt/sonar-scanner-$SONAR_VERSION-linux" "/opt/sonar-scanner" \  
&& rm -f "/tmp/sonar-scanner-cli-$SONAR_VERSION-linux.zip"  
ENV PATH="$PATH:/opt/sonar-scanner/bin"  
# Add Billfire Conan the Deployer  
ADD billfire-deployer billfire-deployer  
ENV PATH="$PATH:/billfire-deployer/bin"  
# Configure Sonar with our custom config  
RUN mv billfire-deployer/sonar-scanner.properties /opt/sonar-scanner/conf/  
  
# Install Node and Yarn  
ENV NODE_VERSION 9.3.0  
  
RUN ARCH= && dpkgArch="$(dpkg --print-architecture)" \  
&& case "${dpkgArch##*-}" in \  
amd64) ARCH='x64';; \  
ppc64el) ARCH='ppc64le';; \  
s390x) ARCH='s390x';; \  
arm64) ARCH='arm64';; \  
armhf) ARCH='armv7l';; \  
i386) ARCH='x86';; \  
*) echo "unsupported architecture"; exit 1 ;; \  
esac \  
&& curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-$ARCH.tar.xz" \  
&& tar -xJf "node-v$NODE_VERSION-linux-$ARCH.tar.xz" -C /usr/local \--strip-
components=1 --no-same-owner \  
&& rm "node-v$NODE_VERSION-linux-$ARCH.tar.xz" \  
&& ln -s /usr/local/bin/node /usr/local/bin/nodejs  
  
ENV YARN_VERSION 1.5.1  
  
RUN set -ex \  
&& curl -fSLO --compressed
"https://github.com/yarnpkg/yarn/releases/download/v$YARN_VERSION/yarn-v$YARN_VERSION.tar.gz"
\  
&& mkdir -p /opt/yarn \  
&& tar -xzf yarn-v$YARN_VERSION.tar.gz -C /opt/yarn \--strip-components=1 \  
&& ln -s /opt/yarn/bin/yarn /usr/local/bin/yarn \  
&& ln -s /opt/yarn/bin/yarn /usr/local/bin/yarnpkg \  
&& rm yarn-v$YARN_VERSION.tar.gz  
  
# Install Siege  
RUN set -ex \  
&& curl -fSLO --compressed "http://download.joedog.org/siege/siege-
latest.tar.gz" \  
&& mkdir -p /opt/siege \  
&& tar -xzvf siege-latest.tar.gz -C /opt/siege \--strip-components=1 \  
&& cd /opt/siege \  
&& ./configure \  
&& make \  
&& make install \  
&& cd - \  
&& rm siege-latest.tar.gz

