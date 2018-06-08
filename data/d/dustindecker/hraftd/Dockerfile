# Build stage  
ARG GO_VERSION=1.9  
ARG PROJECT_PATH=/go/src/github.com/dustin-decker/hraftd  
FROM golang:${GO_VERSION}-alpine AS builder  
WORKDIR /go/src/github.com/dustin-decker/hraftd  
RUN apk --no-cache add git  
RUN go get -u github.com/golang/dep/cmd/dep  
COPY ./ ${PROJECT_PATH}  
RUN export PATH=$PATH:`go env GOHOSTOS`-`go env GOHOSTARCH` \  
&& dep ensure \  
&& CGO_ENABLED=0 GOOS=`go env GOHOSTOS` GOARCH=`go env GOHOSTARCH` go build -o
hraftd \  
&& go test $(go list ./... | grep -v /vendor/)  
  
# Production image*  
FROM scratch  
EXPOSE 11000  
EXPOSE 12000  
COPY \--from=builder /go/src/github.com/dustin-decker/hraftd/hraftd /hraftd  
ENTRYPOINT [ "/hraftd" ]

