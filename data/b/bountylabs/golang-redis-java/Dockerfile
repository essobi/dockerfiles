FROM debian:jessie  
MAINTAINER Mohammad Almalkawi <moh@twitter.com>  
  
#gcc for cgo  
RUN apt-get update && apt-get install -y --no-install-recommends \  
g++ \  
gcc \  
libc6-dev \  
make \  
ca-certificates \  
curl \  
&& rm -rf /var/lib/apt/lists/*  
  
#install go 1.8  
ENV GOLANG_VERSION 1.10  
ENV GOLANG_DOWNLOAD_URL https://golang.org/dl/go$GOLANG_VERSION.linux-
amd64.tar.gz  
ENV GOLANG_DOWNLOAD_SHA256
b5a64335f1490277b585832d1f6c7f8c6c11206cba5cd3f771dcb87b98ad1a33  
RUN curl -fsSL "$GOLANG_DOWNLOAD_URL" -o golang.tar.gz \  
&& echo "$GOLANG_DOWNLOAD_SHA256 golang.tar.gz" | sha256sum -c - \  
&& tar -C /usr/local -xzf golang.tar.gz \  
&& rm golang.tar.gz  
ENV GOPATH /go  
ENV PATH $GOPATH/bin:/usr/local/go/bin:$PATH  
RUN mkdir -p "$GOPATH/src" "$GOPATH/bin" && chmod -R 777 "$GOPATH"  
WORKDIR $GOPATH  
  
#install redis  
ENV REDIS_VERSION 3.0.3  
ENV REDIS_DOWNLOAD_URL http://download.redis.io/releases/redis-3.0.3.tar.gz  
ENV REDIS_DOWNLOAD_SHA1 0e2d7707327986ae652df717059354b358b83358  
RUN set -x \  
&& mkdir -p /usr/src/redis \  
&& curl -sSL "$REDIS_DOWNLOAD_URL" -o redis.tar.gz \  
&& echo "$REDIS_DOWNLOAD_SHA1 *redis.tar.gz" | sha1sum -c - \  
&& tar -xzf redis.tar.gz -C /usr/src/redis --strip-components=1 \  
&& rm redis.tar.gz \  
&& make -C /usr/src/redis \  
&& make -C /usr/src/redis install \  
&& rm -r /usr/src/redis  
  
#set timezone  
RUN cp /usr/share/zoneinfo/America/Los_Angeles /etc/localtime  
  
#install java  
RUN apt-get update && apt-get install -y openjdk-7-jre && apt-get clean  
COPY dynamo/ /bin/dynamo  
  
#install python  
RUN apt-get update && apt-get install -y python && apt-get clean  

