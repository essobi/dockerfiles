FROM nvidia/cuda:8.0-cudnn7-devel-ubuntu16.04  
MAINTAINER Abdul Dakkak <dakkak@illinois.edu>  
  
# caffe2 install with cpu support  
RUN apt-get update && apt-get install -y --no-install-recommends \  
build-essential \  
cmake \  
curl \  
git \  
libgoogle-glog-dev \  
libprotobuf-dev \  
protobuf-compiler \  
libgflags-dev \  
libgflags-dev \  
libgtest-dev \  
libiomp-dev \  
libleveldb-dev \  
liblmdb-dev \  
libopenmpi-dev \  
libsnappy-dev \  
libopenblas-dev \  
libopenblas-base \  
openmpi-bin \  
openmpi-doc \  
libeigen3-dev \  
wget \  
ca-certificates \  
&& rm -rf /var/lib/apt/lists/*  
  
########## INSTALLATION STEPS ###################  
RUN git clone \--single-branch --depth 1 --recursive
https://github.com/caffe2/caffe2.git && \  
cd caffe2 && \  
cd third_party/benchmark && \  
git checkout master && \  
git pull && \  
cd ../..  
RUN cd caffe2 && mkdir build && cd build \  
&& cmake .. \  
-DCUDA_ARCH_NAME=Manual \  
-DCUDA_ARCH_BIN="35 52 60 61" \  
-DCUDA_ARCH_PTX="61" \  
-DUSE_NNPACK=OFF \  
-DUSE_ROCKSDB=OFF \  
-DUSE_OPENCV=OFF \  
-DBUILD_PYTHON=OFF \  
&& make -j"$(nproc)" install \  
&& ldconfig \  
&& make clean \  
&& cd .. \  
&& rm -rf build  
  
#Install Go  
ENV GIMME_GO_VERSION "1.8.3"  
ENV GIMME_OS "linux"  
ENV GIMME_ARCH "amd64"  
ADD https://raw.githubusercontent.com/travis-ci/gimme/master/gimme
/usr/bin/gimme  
RUN chmod +x /usr/bin/gimme  
RUN gimme  
  
ENV GOROOT
"/root/.gimme/versions/go${GIMME_GO_VERSION}.${GIMME_OS}.${GIMME_ARCH}"  
ENV PATH ${GOROOT}/bin:${PATH}  
  
ENV GOPATH "/go"  
ENV PATH $GOPATH/bin:$PATH  
  
#Install Glide  
RUN go get github.com/Masterminds/glide  
  
# Get Go bindings  
ENV PKG github.com/rai-project/go-caffe2  
WORKDIR $GOPATH/src/$PKG  
  
RUN git clone \--depth=1 --branch=master https://${PKG}.git . && \  
glide install && \  
rm -fr vendor/github.com/Sirupsen && \  
find vendor -type f -exec sed -i 's/Sirupsen/sirupsen/g' {} + && \  
go build -a -installsuffix cgo -ldflags "-s -w -X ${PKG}/Version=${VERSION} -X
${PKG}/GitCommit=${VCS_REF} -X ${PKG}/BuildDate=${BUILD_DATE}"&& \  
go install && \  
rm -fr vendor  
  
# Build-time metadata as defined at http://label-schema.org  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
LABEL org.carml.go-caffe2.build-date=$BUILD_DATE \  
org.carml.go-caffe2.name="go-caffe2 bindings for go with cuda support" \  
org.carml.go-caffe2.description="" \  
org.carml.go-caffe2.url="https://www.carml.org/" \  
org.carml.go-caffe2.vcs-ref=$VCS_REF \  
org.carml.go-caffe2.vcs-url="https://github.com/rai-project/go-caffe2" \  
org.carml.go-caffe2.vendor="CarML" \  
org.carml.go-caffe2.version=$VERSION \  
org.carml.go-caffe2.schema-version="1.0"  

