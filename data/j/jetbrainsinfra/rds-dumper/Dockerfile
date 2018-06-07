FROM alpine:3.7  
MAINTAINER Andrey Sizov <andrey.sizov@jetbrains.com>  
  
# Versions: https://pypi.python.org/pypi/awscli#downloads  
ARG AWS_CLI_VERSION=1.11.131  
RUN apk --no-cache update && \  
apk --no-cache add python py-pip py-setuptools ca-certificates mysql-client &&
\  
update-ca-certificates && \  
pip --no-cache-dir install awscli==${AWS_CLI_VERSION} && \  
rm -rf /var/cache/apk/*  
  
COPY run.sh /  
RUN chmod a+x /run.sh  
  
WORKDIR /data  
  
CMD ["/run.sh"]

