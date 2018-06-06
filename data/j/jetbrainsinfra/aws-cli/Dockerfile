FROM alpine:3.6  
# Versions: https://pypi.python.org/pypi/awscli#downloads  
ENV AWS_CLI_VERSION 1.15.3  
RUN apk --no-cache update && \  
apk --no-cache add python py-pip less bash jq && \  
pip --no-cache-dir install awscli==${AWS_CLI_VERSION} && \  
apk -v --purge del py-pip && \  
rm -rf /var/cache/apk/*  
  
RUN mkdir -p /var/run/aws  
COPY entrypoint.sh /entrypoint.sh  
WORKDIR /data  
  
ENTRYPOINT ["/entrypoint.sh"]  

