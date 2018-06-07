FROM golang:1.10 AS build-buildkit  
WORKDIR /go/src/github.com/moby/buildkit  
COPY . /go/src/github.com/moby/buildkit  
RUN go install -v ./cmd/buildctl ./cmd/buildkitd  
  
FROM fermayo/containerd:latest-debian  
RUN apt-get update -q && apt-get install -yq git  
VOLUME /var/lib  
COPY \--from=build-buildkit /go/bin/* /usr/local/bin/  
CMD ["buildctl"]  

