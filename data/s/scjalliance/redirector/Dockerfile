# --------  
# Stage 1: Build  
# -------  
FROM golang:alpine as builder  
  
RUN apk --no-cache add git  
  
WORKDIR /go/src/github.com/scjalliance/redirection  
COPY . .  
  
WORKDIR /go/src/github.com/scjalliance/redirection/cmd/redirector  
  
# Disable CGO to make sure we don't rely on libc  
ENV CGO_ENABLED=0  
# Exclude debugging symbols and set the netgo tag for Go-based DNS resolution  
ENV BUILD_FLAGS="-v -a -ldflags '-d -s -w' -tags netgo"  
RUN go-wrapper download  
RUN go-wrapper install  
  
# --------  
# Stage 2: Release  
# --------  
FROM gcr.io/distroless/base  
  
VOLUME /data  
EXPOSE 80  
EXPOSE 443  
COPY \--from=builder /go/bin/redirector /  
  
WORKDIR /data  
CMD ["/redirector"]  

