FROM alpine:3.6  
  
# Versions: https://pypi.python.org/pypi/awscli#downloads  
ENV AWS_CLI_VERSION 1.14.17  
  
RUN apk --no-cache update && \  
apk --no-cache add python py-pip py-setuptools ca-certificates groff less
tzdata mysql-client && \  
pip --no-cache-dir install awscli==${AWS_CLI_VERSION} && \  
rm -rf /var/cache/apk/*  

