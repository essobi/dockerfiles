FROM alpine:3.6  
LABEL Name="asdf"  
LABEL Version="asdf"  
  
LABEL build="Image-Version:- ${IMAGE_VERSION} Image-Build-Date:
${IMAGE_BUILD_DATE}"  
ARG IMAGE_BUILD_DATE  
ARG IMAGE_VERSION  
  
ENV IAM_ROLE=none  
ENV AWS_ACCESS_KEY_ID=value  
ENV AWS_SECRET_ACCESS_KEY=value  
ENV S3_BUCKET_ACL=private  
ENV S3_BUCKET_NAME=none  
  
VOLUME /mnt/s3-bucket  
  
ARG S3FS_VERSION=v1.82  
RUN apk --update add --virtual build-dependencies \  
build-base alpine-sdk \  
fuse fuse-dev \  
automake autoconf git \  
libressl-dev \  
curl-dev libxml2-dev \  
ca-certificates  
  
# RUN apk del .build-dependencies  
RUN git clone https://github.com/s3fs-fuse/s3fs-fuse.git && \  
cd s3fs-fuse \  
git checkout tags/${S3FS_VERSION} && \  
./autogen.sh && \  
./configure --prefix=/usr && \  
make && \  
make install  
  
RUN s3fs --version  
  
COPY docker-entrypoint.sh /  
  
ENTRYPOINT ["/docker-entrypoint.sh"]

