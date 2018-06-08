# latest possible stable go for bootstrapping new go (or just ":latest")  
FROM golang:latest  
  
# SHA of commit to build  
ENV GOLANG_BUILD_SHA a1110c39301b21471c27dad0e50cdbe499587fc8  
# Last stable version prior this commit  
ENV GOLANG_BASE_VERSION 1.7rc1  
  
ENV GOLANG_BUILD_VERSION $GOLANG_BASE_VERSION-nightly-$GOLANG_BUILD_SHA  
  
  
# gcc for cgo  
RUN apt-get update && apt-get install -y --no-install-recommends \  
g++ \  
gcc \  
libc6-dev \  
make \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV GOLANG_DOWNLOAD_URL
https://github.com/golang/go/archive/$GOLANG_BUILD_SHA.tar.gz  
ENV GOSRC /usr/local/go-$GOLANG_BUILD_SHA  
  
ENV GOROOT $GOSRC  
ENV GOPATH /go  
ENV GOROOT_BOOTSTRAP /usr/local/go  
  
ENV GOBUILD $GOSRC/src  
  
  
RUN curl -fsSL "$GOLANG_DOWNLOAD_URL" \  
| tar -C /usr/local -xz  
  
RUN echo $GOLANG_BUILD_VERSION > "$GOROOT/VERSION"  
  
WORKDIR $GOBUILD  
RUN ./make.bash  
  
# let new built go take precendence over old go used for bootstrapping it  
ENV PATH=$GOSRC/bin:$PATH  
  

