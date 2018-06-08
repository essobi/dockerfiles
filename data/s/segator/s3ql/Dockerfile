FROM ubuntu:16.04  
MAINTAINER isaac.aymerich@gmail.com  
  
COPY install.sh /install.sh  
RUN chmod +x /install.sh  
RUN /install.sh  
  
COPY entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
  
ENV STORAGE_URL="" \  
CACHE_S3QL_SIZE=50 \  
LOGIN_USER="" \  
LOGIN_PASSWORD="" \  
PASSPHRASE="" \  
COMPRESS_METHOD="none" \  
BACKEND_OPTIONS="" \  
S3QL_CACHE_PATH="/s3ql/cache" \  
S3QL_MOUNTPOINT="/s3ql/mountpoint" \  
S3QL_METADATA_UPLOAD_INTERVAL=1800 \  
S3QL_THREADS=15 \  
S3QL_PROMETHEUS_PORT=7950 \  
NFS_PATH="127.0.0.1:${S3QL_MOUNTPOINT}" \  
NFS_MOUNTPOINT="/nfs/mountpoint" \  
NFS_OPTIONS="async,hard,noatime,nodiratime,intr,nolock,rsize=524288,wsize=524288"  
EXPOSE ${S3QL_PROMETHEUS_PORT}  
  
VOLUME ${S3QL_CACHE_PATH}  
VOLUME /var/cache/fscache  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["mount"]

