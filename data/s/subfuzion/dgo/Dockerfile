# Go development environment with bells and whistles.  
#  
# docker build -f Dockerfile.dev -t godocker .  
#  
#============================  
FROM debian:stretch as build  
#============================  
# Add build and runtime deps.  
# Note: taking advantage of this being a multi-stage build. It's  
# slightly slower than a single RUN command, but has the advantage  
# that packages can be inserted and removed with less overall impact.  
# Note also that it's not necessary to clean up the cache afterwards.  
ARG DEBIAN_FRONTEND=noninteractive  
RUN apt-get update  
ARG APTARGS="-yq --no-install-recommends install"  
RUN apt-get ${APTARGS} apt-utils  
RUN apt-get ${APTARGS} autoconf  
RUN apt-get ${APTARGS} automake  
RUN apt-get ${APTARGS} build-essential  
RUN apt-get ${APTARGS} ca-certificates  
RUN apt-get ${APTARGS} curl  
RUN apt-get ${APTARGS} cmake  
RUN apt-get ${APTARGS} dnsutils  
RUN apt-get ${APTARGS} gcc  
RUN apt-get ${APTARGS} git  
RUN apt-get ${APTARGS} iptables  
RUN apt-get ${APTARGS} jq  
RUN apt-get ${APTARGS} procps  
RUN apt-get ${APTARGS} sudo  
RUN apt-get ${APTARGS} tar  
RUN apt-get ${APTARGS} unzip  
RUN apt-get ${APTARGS} vim-common  
RUN apt-get ${APTARGS} xfsprogs  
RUN apt-get ${APTARGS} xz-utils  
  
# Install Go  
ARG GO_VERSION=1.9.2  
RUN curl -fsSL "https://golang.org/dl/go${GO_VERSION}.linux-amd64.tar.gz" \  
| tar -xzC /usr/local  
ENV PATH /go/bin:/usr/local/go/bin:$PATH  
ENV GOPATH /go  
ENV CGO_LDFLAGS -L/lib  
  
# Install protoc  
ARG PROTOC_VERSION=3.5.1  
RUN curl -fsSLo /tmp/protoc.zip
"https://github.com/google/protobuf/releases/download/v${PROTOC_VERSION}/protoc-${PROTOC_VERSION}-linux-x86_64.zip"
&& \  
unzip /tmp/protoc.zip -d /tmp/protoc && \  
mv /tmp/protoc/bin/protoc /usr/local/bin  
RUN go get github.com/golang/protobuf/proto  
RUN go get github.com/golang/protobuf/protoc-gen-go  
RUN go get github.com/gogo/protobuf/protoc-gen-gofast  
RUN go get github.com/gogo/protobuf/protoc-gen-gogofast  
RUN go get github.com/gogo/protobuf/protoc-gen-gogofaster  
RUN go get github.com/gogo/protobuf/protoc-gen-gogoslick  
RUN go get google.golang.org/grpc  
RUN go get github.com/grpc-ecosystem/grpc-gateway/protoc-gen-grpc-gateway  
RUN go get github.com/grpc-ecosystem/grpc-gateway/protoc-gen-swagger  
  
# Install vendoring tool  
RUN go get github.com/golang/dep/cmd/dep  
  
# Go lint tools  
RUN go get github.com/alecthomas/gometalinter  
RUN gometalinter --install  
  
# Move generated Go binaries to /usr/local/bin because only /usr/local/bin  
# gets copied in the final stage. This ensures /go is pristine for the final
stage.  
RUN mv /go/bin/* /usr/local/bin  
  
#============================  
from debian:stretch  
#============================  
ENV GO_VERSION=1.9.2  
ENV PATH=/go/bin:/usr/local/go/bin:$PATH  
ENV GOPATH=/go  
ENV CGO_LDFLAGS=-L/lib  
ENV PROTOC_VERSION=3.5.1  
COPY \--from=build /usr/local/bin /usr/local/bin  
COPY \--from=build /usr/local/go /usr/local/go  
  
WORKDIR /go  
RUN mkdir -p /go/bin /go/pkg /go/src  
ENV IN_DOCKER 1  
CMD [ "bash" ]  
  

