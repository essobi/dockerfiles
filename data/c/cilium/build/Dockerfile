# Stage: bazel  
FROM ubuntu:16.10 as bazel  
WORKDIR /tmp  
RUN apt-get update  
RUN apt-get install -y --no-install-recommends curl ca-certificates unzip  
RUN curl -sS -L
https://github.com/bazelbuild/bazel/releases/download/0.5.1/bazel-0.5.1-installer-
linux-x86_64.sh -o bazel.sh  
RUN chmod +x bazel.sh  
RUN ./bazel.sh  
  
# Stage: godeps  
FROM golang:1.9 as godeps  
WORKDIR /tmp  
RUN go get -u github.com/golang/protobuf/protoc-gen-go  
RUN go get -u github.com/jteeuwen/go-bindata/...  
  
# Final stage: build  
FROM ubuntu:16.10  
LABEL maintainer="maintainer@cilium.io"  
COPY \--from=bazel /usr/local/bin/bazel /usr/local/lib/bazel/bin/bazel-real
/usr/bin/  
COPY \--from=godeps /go/bin/protoc-gen-go /go/bin/go-bindata /usr/bin/  
WORKDIR /tmp  
RUN apt-get update && apt-get -y install protobuf-compiler libprotobuf-dev git
make wget libtool cmake realpath m4 automake pkg-config zip g++ zlib1g-dev
unzip python rsync curl  
RUN curl -Sslk -o go.linux-amd64.tar.gz
https://storage.googleapis.com/golang/go1.9.linux-amd64.tar.gz && \  
tar -C /usr/local -xzf go.linux-amd64.tar.gz && \  
rm go.linux-amd64.tar.gz  
ENV GOROOT /usr/local/go  
ENV GOPATH /go  
ENV PATH="${GOROOT}/bin:${PATH}"  
WORKDIR /go/src/github.com/cilium  
RUN git clone https://github.com/cilium/cilium.git && cd cilium &&
CILIUM_USE_ENVOY=1 make envoy && rm -rf .  

