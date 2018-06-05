FROM golang:1.9.2-alpine as builder  
LABEL maintainer="<easylo@users.noreply.github.com>"  
  
ENV PATH /go/bin:/usr/local/go/bin:$PATH  
ENV GOPATH /go  
ENV CGO_ENABLED=0  
COPY . $GOPATH/src/github.com/easylo/screenshots-cron  
WORKDIR $GOPATH/src/github.com/easylo/screenshots-cron  
  
RUN apk add --update --no-cache \  
make \  
git \  
ca-certificates  
  
RUN make build  
  
FROM debian:stretch-slim  
  
COPY \--from=builder /go/src/github.com/easylo/screenshots-cron/screenshots-
cron /bin/screenshots-cron  
  
RUN apt-get update && apt-get install -y libfontconfig ca-certificates
imagemagick  
  
COPY ./lib/phantomjs /bin/phantomjs  
  
RUN mkdir -p /var/example  
  
COPY ./example/capture.html /var/example/capture.html  
  
RUN chmod a+x /bin/phantomjs  
  
CMD [ "/bin/screenshots-cron"]

