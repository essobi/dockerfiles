# Compiling application  
FROM golang:1.10-alpine as builder  
  
RUN apk update; apk add git; apk add gcc musl-dev curl  
RUN curl https://glide.sh/get | sh  
  
ENV PROJ github.com/networld-to/homecontrol  
ENV PROJ_DIR /go/src/${PROJ}  
ENV CGO_ENABLED 1  
  
WORKDIR ${PROJ_DIR}  
COPY . .  
  
RUN glide install  
  
RUN go build -o /tmp/server -buildmode=pie \  
-ldflags "-s -w -X ${PROJ}/version.Version=$(git describe --always) -X '${PROJ}/version.Build=$(date -u '+%Y-%m-%dT%H:%M:%SZ')'" server/main.go  
  
RUN go build -o /tmp/client -buildmode=pie \  
-ldflags "-s -w -X ${PROJ}/version.Version=$(git describe --always) -X '${PROJ}/version.Build=$(date -u '+%Y-%m-%dT%H:%M:%SZ')'" client/main.go  
  
RUN mv /tmp/server /go/bin && \  
mv /tmp/client /go/bin  
  
#####################################################  
# Final, minimized docker image usable in production  
#####################################################  
FROM alpine:3.7  
  
RUN apk add --no-cache ca-certificates  
  
WORKDIR /  
COPY --from=builder /go/bin/ /  
  
EXPOSE 50051  

