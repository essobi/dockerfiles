FROM webhippie/alpine:latest  
MAINTAINER Thomas Boerger <thomas@webhippie.de>  
  
VOLUME ["/var/lib/minio"]  
  
EXPOSE 9000  
WORKDIR /root  
ENTRYPOINT ["/usr/bin/entrypoint"]  
CMD ["/bin/s6-svscan", "/etc/s6"]  
  
ENV MINIO_PATH github.com/minio/minio  
ENV MINIO_REPO https://${MINIO_PATH}.git  
ENV MINIO_BRANCH RELEASE.2017-10-27T18-59-02Z  
  
ENV GOPATH /usr/local  
  
RUN apk update && \  
apk add \  
build-base \  
go \  
git && \  
git clone \  
-b ${MINIO_BRANCH} \  
${MINIO_REPO} \  
/usr/local/src/${MINIO_PATH} && \  
cd \  
/usr/local/src/${MINIO_PATH} && \  
go install \  
${MINIO_PATH}/... && \  
cp -f \  
/usr/local/bin/minio \  
/usr/bin/ && \  
apk del \  
build-base \  
go \  
git && \  
rm -rf \  
/var/cache/apk/* \  
/usr/local/*  
  
ADD rootfs /  

