FROM golang:1.9.1-alpine3.6  
MAINTAINER Vadim Zharov  
  
RUN echo http://nl.alpinelinux.org/alpine/v3.4/community >>
/etc/apk/repositories  
RUN apk add --no-cache git openssh fuse curl wget  
  
RUN wget
https://github.com/openshift/origin/releases/download/v3.7.1/openshift-origin-
client-tools-v3.7.1-ab0f056-linux-64bit.tar.gz  
  
RUN tar -xvf openshift-origin-client-tools-v3.7.1-ab0f056-linux-64bit.tar.gz
&& mv openshift-origin-client-tools-v3.7.1-ab0f056-linux-64bit/oc
/usr/local/bin/  
  
RUN wget -q -O /etc/apk/keys/sgerrand.rsa.pub
https://raw.githubusercontent.com/sgerrand/alpine-pkg-
glibc/master/sgerrand.rsa.pub  
RUN wget https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/2.26-r0/glibc-2.26-r0.apk  
RUN apk add glibc-2.26-r0.apk  
  
RUN apk del git  
  
RUN mkdir /mnt/restic  
  
#backup type - metadata/files/databases  
ENV BACKUP_TYPE="metadata"  
#destination for backup - full path (server address for s3, path for NFS (NFS
was excluded))  
ENV RESTIC_REPOSITORY=""  
#name of openshift project (script will take it automatically)  
ENV PROJECT_NAME="default"  
#custom tag  
ENV RESTIC_TAG="default"  
#how many copies we should store  
ENV RESTIC_KEEP=3  
#which files we should exclude from backup (see restic docs for details)  
ENV RESTIC_EXCLUDE=".zfs"  
#destintation for backup - aws (AMAZON S3 storage) or s3 (generic S3 server -
like minio)  
#for aws restic repository will be s3:$RESTIC_HOST, i.e.
s3:s3.amazonaws.com/my_bucket, RESTIC_HOST=s3.amazonaws.com/my_bucket  
#for s3 restic repository will be s3:http://$RESTIC_HOST:$RESTIC_S3_PORT/  
ENV RESTIC_DESTINATION="s3"  
#S3 credentials  
ENV AWS_ACCESS_KEY_ID=""  
ENV AWS_SECRET_ACCESS_KEY=""  
#s3 host/port  
ENV RESTIC_HOST=localhost  
ENV RESTIC_S3_PORT="9000"  
#token to get project metadata from API  
ENV TOKEN=""  
#default snapshot (for restore)  
ENV RESTIC_SNAPSHOT="latest"  
# /data is the dir where you have to put the data to be backed up  
#VOLUME /data  
COPY entry.sh /entry.sh  
  
WORKDIR "/"  
  
ENTRYPOINT ["/entry.sh"]  

