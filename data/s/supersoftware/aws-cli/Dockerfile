FROM bash:4.1  
  
# Versions: https://pypi.python.org/pypi/awscli#downloads  
ENV AWS_CLI_VERSION 1.14.42  
  
RUN apk --no-cache update && \  
apk --no-cache add jq coreutils python py-pip py-setuptools ca-certificates
groff less && \  
pip --no-cache-dir install awscli==${AWS_CLI_VERSION} && \  
rm -rf /var/cache/apk/*  
  
ENTRYPOINT ["aws"]  

