FROM alpine:3.7  
MAINTAINER Andrey Sizov <andrey.sizov@jetbrains.com>  
  
# Versions: https://pypi.python.org/pypi/awscli#downloads  
ARG AWS_CLI_VERSION=1.11.131  
RUN apk --no-cache update && \  
apk --no-cache add python py-pip py-setuptools ca-certificates mysql-client
rsync && \  
update-ca-certificates && \  
pip --no-cache-dir install awscli==${AWS_CLI_VERSION} && \  
rm -rf /var/cache/apk/*  
  
COPY s3.sh mysqldump-to-s3.sh restore-mysql-rsync-s3.sh /  
RUN chmod a+x /*.sh  
  
WORKDIR /data  
ENTRYPOINT []  
CMD ["/bin/ash"]  

