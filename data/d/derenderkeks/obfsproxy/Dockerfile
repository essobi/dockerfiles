FROM alpine:3.5  
LABEL maintainer="DerEnderKeks <admin@derenderkeks.me>" version="0.0.1"
description="Docker image for obfsproxy"  
  
RUN apk add --update --no-cache bash build-base gmp-dev python python-dev py-
pip && \  
rm -rf /tmp/* /var/tmp/* /var/cache/apk/* /var/cache/distfiles/*  
  
RUN pip install --upgrade pip  
RUN pip install incremental  
RUN pip install obfsproxy  
  
CMD ["obfsproxy", "-h"]

