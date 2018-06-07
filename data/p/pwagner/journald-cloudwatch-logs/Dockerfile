FROM debian:jessie  
  
ENV GOLANG_VERSION 1.6  
ENV GOLANG_DOWNLOAD_URL https://golang.org/dl/go$GOLANG_VERSION.linux-
amd64.tar.gz  
ENV GOLANG_DOWNLOAD_SHA256
5470eac05d273c74ff8bac7bef5bad0b5abbd1c4052efbdbc8db45332e836b0b  
  
  
ENV GOPATH /go  
ENV GOBIN /go/bin  
ENV PATH $GOPATH/bin:/usr/local/go/bin:$PATH  
  
COPY . /go/src/journald-cloudwatch-logs  
WORKDIR /go/src/journald-cloudwatch-logs  
  
RUN apt-get update && \  
apt-get -y \--no-install-recommends install \  
ca-certificates \  
curl \  
gcc \  
git \  
libc6-dev \  
libsystemd-dev \  
pkg-config \  
&& \  
curl -fsSL $GOLANG_DOWNLOAD_URL -o golang.tar.gz \  
&& echo "$GOLANG_DOWNLOAD_SHA256 golang.tar.gz" | sha256sum -c \- \  
&& tar -C /usr/local -xzf golang.tar.gz \  
&& rm golang.tar.gz && \  
go get . && \  
apt-get -y purge \  
curl \  
gcc \  
git \  
pkg-config \  
&& \  
apt-get -y autoremove && \  
cp /go/src/journald-cloudwatch-logs/start.sh /go/bin/start.sh && \  
rm -Rf /usr/local/go /go/src/  
  
  
CMD ["/go/bin/start.sh"]  

