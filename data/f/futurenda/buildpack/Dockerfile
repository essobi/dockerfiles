FROM golang:1.9.2-stretch  
  
# Python 3, unzip, netcat  
RUN apt-get update && apt-get install -y --no-install-recommends \  
python3 \  
python3-dev \  
python3-pip \  
python3-setuptools \  
unzip \  
xz-utils \  
netcat-openbsd \  
mariadb-client \  
libdigest-hmac-perl \  
&& rm -rf /var/lib/apt/lists/*  
  
# Docker 17.03  
RUN curl -L -o /tmp/docker.tgz
https://download.docker.com/linux/static/stable/x86_64/docker-17.06.1-ce.tgz \  
&& tar -xz -C /tmp -f /tmp/docker.tgz \  
&& mv /tmp/docker/docker* /usr/bin/  
  
# docker-compose 1.11.2  
RUN curl -L
"https://github.com/docker/compose/releases/download/1.15.0/docker-
compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose  
RUN chmod +x /usr/local/bin/docker-compose  
  
# migrate  
RUN curl -L -o /tmp/migrate.tar.gz
https://github.com/mattes/migrate/releases/download/v3.0.1/migrate.linux-
amd64.tar.gz \  
&& tar -xz -C /tmp -f /tmp/migrate.tar.gz \  
&& mv /tmp/migrate.linux-amd64 /usr/bin/migrate  
  
# awscli  
RUN pip3 install awscli  
  
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
gpg --keyserver pgp.mit.edu --recv-keys "$key" || \  
gpg --keyserver keyserver.pgp.com --recv-keys "$key" || \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key" ; \  
done  
  
ENV NPM_CONFIG_LOGLEVEL info  
ENV NODE_VERSION 9.2.0  
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
&& curl -SLO --compressed
"https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \  
&& gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc \  
&& grep " node-v$NODE_VERSION-linux-$ARCH.tar.xz\$" SHASUMS256.txt | sha256sum
-c - \  
&& tar -xJf "node-v$NODE_VERSION-linux-$ARCH.tar.xz" -C /usr/local \--strip-
components=1 --no-same-owner \  
&& rm "node-v$NODE_VERSION-linux-$ARCH.tar.xz" SHASUMS256.txt.asc
SHASUMS256.txt \  
&& ln -s /usr/local/bin/node /usr/local/bin/nodejs  
  
RUN groupadd --gid 1000 builder \  
&& useradd --uid 1000 --gid builder --shell /bin/bash --create-home builder  
  
RUN mkdir -p /npm  
COPY package.json /npm/package.json  
  
RUN chown -R builder /go  
RUN chown -R builder /npm  
  
# protoc 3.3  
RUN mkdir -p /tmp/downloads/protoc \  
&& cd /tmp/downloads/protoc \  
&& wget
https://github.com/google/protobuf/releases/download/v3.3.0/protoc-3.3.0-linux-x86_64.zip
\  
&& unzip protoc-3.3.0-linux-x86_64.zip \  
&& cp bin/protoc /usr/bin \  
&& rm -rf /tmp/downloads/protoc  
  
USER builder  
  
RUN cd /npm && npm install protobufjs  
RUN cd /npm && npm install grpcc  
RUN cd /npm/node_modules/protobufjs/cli && mv package.standalone.json
package.json && npm install  
ENV PATH="${PATH}:/npm/node_modules/.bin"  
COPY test.proto /tmp/test.proto  
RUN pbjs -t json /tmp/test.proto  
  
RUN go get -u github.com/golang/protobuf/protoc-gen-go  
RUN go get -u github.com/golang/lint/golint  
RUN go get -u github.com/futurenda/fossil  

