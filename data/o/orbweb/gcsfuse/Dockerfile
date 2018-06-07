FROM golang:1.6-alpine  
MAINTAINER Orbweb Inc. <engineering@orbweb.com>  
  
RUN export GO15VENDOREXPERIMENT=1 && \  
apk --no-cache add --virtual .builddeps \  
git && \  
go get -u github.com/googlecloudplatform/gcsfuse && \  
ln -s bin/gcsfuse /usr/local/bin && \  
rm -rf /go/pkg/ /go/src/ && \  
apk --no-cache add --virtual .rundeps \  
fuse && \  
apk del .builddeps  
  
ENV GOOGLE_APPLICATION_CREDENTIALS=/.gcloud.json  
ENV GCSFUSE_USER=gcsfuse  
ENV GCSFUSE_MOUNTPOINT=/mnt/gcs  
ENV GCSFUSE_DEBUG=  
ENV GCSFUSE_DEBUG_FUSE=  
ENV GCSFUSE_DEBUG_GCS=1  
ENV GCSFUSE_DEBUG_HTTP=  
ENV GCSFUSE_DEBUG_INVARIANTS=  
ENV GCSFUSE_DIR_MODE=  
ENV GCSFUSE_FILE_MODE=  
ENV GCSFUSE_LIMIT_BPS=  
ENV GCSFUSE_LIMIT_OPS=  
ENV GCSFUSE_CACHE_STAT_TTL=  
ENV GCSFUSE_CACHE_TYPE_TTL=  
  
WORKDIR /  
COPY entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["gcsfuse", "-h"]  

