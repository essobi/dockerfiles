FROM golang:1.9.1-alpine3.6  
MAINTAINER Vadim Zharov  
  
RUN echo http://nl.alpinelinux.org/alpine/v3.4/community >>
/etc/apk/repositories  
RUN apk add --no-cache git nfs-utils openssh fuse curl wget postgresql
mariadb-client  
RUN git clone https://github.com/restic/restic \  
&& cd restic \  
&& go run build.go \  
&& cp restic /usr/local/bin/  
  
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
  
#backup type - metadata/files/databases/all-pvc  
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
#DB type to perform backup (postgres/mysql)  
ENV DATABASE_TYPE="postgres"  
#PG username  
ENV DATABASE_USER="postgres"  
#DB Openshift service address  
ENV DATABASE_SVC="127.0.0.1"  
#DB password  
ENV DATABASE_PASSWORD=""  
#SNAPSHOT ID  
ENV RESTIC_SNAPSHOT="latest"  
#API endpoints - to restore  
ENV API_TO_RESTORE=""  
#Change namespace from original  
ENV CHANGE_NAMESPACE="yes"  
#New namespace name  
ENV NEW_PROJECT_NAME=""  
# /data is the dir to restore data  
# VOLUME /data  
COPY entry.sh /entry.sh  
COPY metadata-restore.sh /metadata-restore.sh  
COPY files-restore.sh /files-restore.sh  
COPY databases-restore.sh /databases-restore.sh  
COPY restore-all-pvc.sh /restore-all-pvc.sh  
COPY restic-openshift-api.cfg /restic-openshift-api.cfg  
COPY restic-openshift-oapi.cfg /restic-openshift-oapi.cfg  
  
USER root  
  
WORKDIR "/"  
  
ENTRYPOINT ["/entry.sh"]  

