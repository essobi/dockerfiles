FROM ubuntu:latest  
  
MAINTAINER Ivan Pushkin <imetalguardi+docker@gmail.com>  
  
ENV TERM xterm  
ENV GOLANG_VERSION 1.5.1  
ENV GOLANG_DOWNLOAD_URL https://golang.org/dl/go$GOLANG_VERSION.linux-
amd64.tar.gz  
ENV GOLANG_DOWNLOAD_SHA1 46eecd290d8803887dec718c691cc243f2175fe0  
  
RUN yes "" | adduser --uid=1000 --disabled-password docker  
RUN echo "docker ALL=(ALL:ALL) NOPASSWD: ALL" >> /etc/sudoers  
  
RUN apt-get update  
RUN DEBIAN_FRONTEND=noninteractive apt-get install --yes --quiet --no-install-
recommends \  
bash-completion \  
ca-certificates \  
curl \  
gcc \  
libc6-dev \  
make \  
nano \  
git  
  
RUN curl -fsSL "$GOLANG_DOWNLOAD_URL" -o golang.tar.gz  
RUN echo "$GOLANG_DOWNLOAD_SHA1 golang.tar.gz" | sha1sum -c -  
RUN tar -C /usr/local -xzf golang.tar.gz  
RUN rm golang.tar.gz  
  
# clean apt cache and temps  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV GOPATH /go  
ENV PATH $GOPATH/bin:/usr/local/go/bin:$PATH  
  
RUN mkdir -p "$GOPATH/src" "$GOPATH/bin" && chmod -R 777 "$GOPATH"  
WORKDIR $GOPATH  
  
COPY go-wrapper /usr/local/bin/  
  
VOLUME ["/go"]  
  
EXPOSE 8080  
COPY ./docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  

