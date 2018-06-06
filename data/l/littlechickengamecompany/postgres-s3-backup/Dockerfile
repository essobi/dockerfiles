FROM alpine:3.3  
# Run every night by default  
ENV SCHEDULE="@daily" \  
PGUSER="postgres" \  
COMPRESSION_LEVEL=9 \  
NAME_PREFIX='database-archive' \  
AWS_ENDPOINT='s3.amazonaws.com'  
  
RUN echo "@edge http://dl-cdn.alpinelinux.org/alpine/edge/main" >>
/etc/apk/repositories && \  
apk update && \  
apk --no-cache add --virtual build-dependencies tar ca-certificates && \  
apk --no-cache add libpq postgresql@edge && \  
# s3gof3r for S3 uploads  
wget -qO-
https://github.com/rlmcpherson/s3gof3r/releases/download/v0.5.0/gof3r_0.5.0_linux_amd64.tar.gz
| tar xvz --strip 1 -C /usr/local/bin/ && \  
  
# Go based cron replacement  
wget -qO- https://github.com/odise/go-cron/releases/download/v0.0.7/go-cron-
linux.gz | zcat > /usr/local/bin/go-cron && \  
# Keep only pg_dump/pg_dumpall  
cp /usr/bin/pg_dump* /usr/local/bin/ && \  
  
chmod u+x /usr/local/bin/pg_dump* /usr/local/bin/go-cron /usr/local/bin/gof3r
&& \  
# Cleanup  
apk del postgresql && \  
apk del build-dependencies  
  
COPY backup.sh /app/backup.sh  
RUN chmod +x /app/backup.sh  
  
CMD ["sh", "-c", "go-cron -s \"${SCHEDULE}\" -- sh /app/backup.sh"]  

