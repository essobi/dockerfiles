FROM debian:stretch  
  
ENV DOCKER_VERSION 17.12.0~ce-0~debian  
ENV NODEJS_VERSION 10.x  
ENV GOLANG_VERSION 1.10  
ENV GOLANG_CHECKSUM
b5a64335f1490277b585832d1f6c7f8c6c11206cba5cd3f771dcb87b98ad1a33  
  
ENV GOPATH /go  
ENV PATH $GOPATH/bin:/usr/local/go/bin:$PATH  
  
ENV BUILD_PACKAGES "apt-transport-https python-pip python-setuptools gnupg2
software-properties-common"  
ENV RUNTIME_PACKAGES "git curl build-essential ca-certificates fontconfig
ruby-compass"  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends $BUILD_PACKAGES
$RUNTIME_PACKAGES \  
&& curl -fsSL https://download.docker.com/linux/$(. /etc/os-release; echo
"$ID")/gpg | apt-key add - \  
&& apt-key fingerprint 0EBFCD88 \  
&& add-apt-repository \  
"deb [arch=amd64] https://download.docker.com/linux/$(. /etc/os-release; echo
"$ID") \  
$(lsb_release -cs) \  
stable" \  
&& curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \  
&& echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends docker-ce=$DOCKER_VERSION \  
&& pip install docker-compose --force --upgrade \  
&& curl -sL https://deb.nodesource.com/setup_$NODEJS_VERSION | bash \  
&& apt-get install -y --no-install-recommends nodejs yarn \  
&& npm install -g --unsafe-perm bower gulp phantomjs-prebuilt \  
&& curl -fsSL "https://golang.org/dl/go$GOLANG_VERSION.linux-amd64.tar.gz" -o
golang.tar.gz \  
&& echo "$GOLANG_CHECKSUM golang.tar.gz" | sha256sum -c - \  
&& tar -C /usr/local -xzf golang.tar.gz \  
&& rm golang.tar.gz \  
&& mkdir -p "$GOPATH/src" "$GOPATH/bin" \  
&& chmod -R 777 "$GOPATH" \  
&& apt-get remove --purge -y $BUILD_PACKAGES \  
&& rm -rf /var/lib/apt/lists/*  
  
# Upgrade npm  
RUN npm -g install npm

