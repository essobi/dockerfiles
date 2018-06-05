FROM golang:alpine as builder  
COPY src /go/src/docker-worker  
WORKDIR /go/src/docker-worker  
RUN apk add --no-cache git gcc libc-dev \  
&& go get  
RUN GO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -tags netgo
-installsuffix netgo -ldflags '-w' -o main .  
  
FROM scratch  
  
ARG BUILD_DATE="N/A"  
ARG VCS_REF="N/A"  
ARG VCS_URL="N/A"  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.vcs-url=$VCS_URL \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.schema-version="1.0.0-rc1" \  
maintainer="clement@le-corre.eu"  
  
ADD Go_Daddy_Class_2_CA.pem /etc/ssl/certs/  
COPY \--from=builder /go/src/docker-worker/main .  
CMD ["./main"]  

