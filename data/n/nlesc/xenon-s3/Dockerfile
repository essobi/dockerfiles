# FROM golang:1.8-alpine  
FROM golang:1.9.4-alpine3.6  
MAINTAINER Atze van der Ploeg (a.vanderploeg@esciencecenter.nl)  
  
  
  
ENV MINIO_ACCESS_KEY xenon  
ENV MINIO_SECRET_KEY javagat01  
  
WORKDIR /go/src/app  
  
# We use mc (minio client) to create files, because creating file on the
filesytem caused  
# minio to give errors (when accessing via rest), presumably because some
minio  
# meta-info was not present that is generate when using the s3 protocol.  
RUN \  
apk add --no-cache git && \  
git clone https://github.com/minio/mc && \  
cd mc && \  
go-wrapper download && \  
go-wrapper install -ldflags "$(go run buildscripts/gen-ldflags.go)" && \  
cd .. && \  
rm -rf mc && \  
apk del git  
  
RUN \  
apk add --no-cache ca-certificates && \  
apk add --no-cache --virtual .build-deps git go musl-dev && \  
echo 'hosts: files mdns4_minimal [NOTFOUND=return] dns mdns4' >>
/etc/nsswitch.conf && \  
go get -v -d github.com/minio/minio && \  
cd /go/src/github.com/minio/minio && \  
go install -v -ldflags "$(go run buildscripts/gen-ldflags.go)" && \  
rm -rf /go/pkg /go/src /usr/local/go && apk del .build-deps  
  
RUN mkdir /var/s3 && \  
chmod a+rx /var/s3  
  
RUN \  
minio server /var/s3 & \  
sleep 1s && \  
mc config host add hier "http://localhost:9000" xenon javagat01 && \  
mc mb hier/filesystem-test-fixture && \  
echo "Hello World" | mc pipe hier/filesystem-test-fixture/links/file0 && \  
echo "" | mc pipe hier/filesystem-test-fixture/links/file1 && \  
mc mb hier/filesystem-test-fixture2 && \  
echo "Hello World" | mc pipe hier/filesystem-test-fixture2/links/file0 && \  
echo "" | mc pipe hier/filesystem-test-fixture2/links/file1 && \  
mc policy public hier/filesystem-test-fixture2 && \  
sleep 1s && \  
killall minio  
  
EXPOSE 9000  
CMD ["minio","server","/var/s3"]  
  
HEALTHCHECK \--interval=1s CMD mc ls hier || exit 1  

