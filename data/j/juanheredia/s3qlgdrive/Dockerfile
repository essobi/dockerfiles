FROM ubuntu:16.04  
LABEL maintainer="jchm@infoinnova.net"  
  
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
S3QL_CACHE_PATH="/mnt/cache" \  
S3QL_MOUNTPOINT="/mnt/mountpoint" \  
S3QL_METADATA_UPLOAD_INTERVAL=24 \  
S3QL_THREADS=15 \  
S3QL_PROMETHEUS_PORT=7950  
EXPOSE ${S3QL_PROMETHEUS_PORT}  
  
VOLUME ${S3QL_CACHE_PATH}  
VOLUME ${S3QL_MOUNTPOINT}  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["mount"]

