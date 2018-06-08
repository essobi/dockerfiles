FROM eclipse/ubuntu_jre  
  
MAINTAINER Brad Pinter <brad.pinter@gmail.com>  
  
# Metadata params  
ARG VCS_URL  
ARG VCS_REF  
ARG BUILD_DATE  
ARG VERSION  
  
# Metadata  
LABEL org.label-schema.name="A Codenvy-compatiable Golang" \  
org.label-schema.description="A Codenvy-compatiable container with more
current version of Golang" \  
org.label-schema.vendor="CDW" \  
org.label-schema.url="https://cdw.com" \  
org.label-schema.vcs-url=$VCS_URL \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.version=$VERSION \  
org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.schema-version="1.0.0-rc.1"  
  
RUN sudo apt-get update && sudo apt-get install -y --no-install-recommends \  
g++ \  
gcc \  
libc6-dev \  
make \  
&& sudo rm -rf /var/lib/apt/lists/*  
  
ENV GOLANG_VERSION 1.8.3  
ENV GOLANG_DOWNLOAD_URL https://golang.org/dl/go$GOLANG_VERSION.linux-
amd64.tar.gz  
#ENV GOLANG_DOWNLOAD_SHA256
e40c36ae71756198478624ed1bb4ce17597b3c19d243f3f0899bb5740d56212a  
ENV GOLANG_DOWNLOAD_SHA256
1862f4c3d3907e59b04a757cfda0ea7aa9ef39274af99a784f5be843c80c6772  
  
RUN sudo curl -fsSL "$GOLANG_DOWNLOAD_URL" -o golang.tar.gz \  
&& echo "$GOLANG_DOWNLOAD_SHA256 golang.tar.gz" | sha256sum -c - \  
&& sudo tar -C /usr/local -xzf golang.tar.gz \  
&& sudo rm golang.tar.gz  
  
ENV GOPATH /go  
ENV PATH $GOPATH/bin:/usr/local/go/bin:$PATH  
  
RUN sudo mkdir -p "$GOPATH/src" "$GOPATH/bin" && sudo chmod -R 777 "$GOPATH"  
  
EXPOSE 8080  
CMD tail -f /dev/null  

