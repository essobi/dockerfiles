FROM golang:1.9.2-alpine3.6 AS build  
ARG version=devel  
  
# Install build tools.  
RUN apk add --no-cache git  
RUN go get github.com/golang/dep/cmd/dep  
  
# Copy and build squirrelbot.  
COPY . /go/src/github.com/xordspar0/squirrelbot/  
WORKDIR /go/src/github.com/xordspar0/squirrelbot/  
RUN dep ensure -vendor-only  
RUN env CGO_ENABLED=0 go build -ldflags "-X main.version=${version}" -o
"/bin/squirrelbot.docker" ./cmd/squirrelbot  
  
FROM alpine:latest  
# Install runtime dependencies.  
RUN apk --update --no-cache add \  
ca-certificates \  
youtube-dl  
  
COPY \--from=build /bin/squirrelbot.docker /bin/squirrelbot  
CMD ["/bin/squirrelbot"]  

