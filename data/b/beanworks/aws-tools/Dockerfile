FROM alpine:latest  
  
RUN apk --no-cache update && \  
apk --no-cache add python py-pip py-setuptools ca-certificates groff less vim
bash && \  
pip --no-cache-dir install awscli && \  
rm -rf /var/cache/apk/*  
  
COPY describe-apis /usr/bin/  
COPY update-sftp-config /usr/bin/  
COPY update-api-parameters /usr/bin/  
COPY update-config /usr/bin/  
COPY .bashrc /root/.bashrc  
  
RUN mkdir /root/.aws/  
  
WORKDIR /tmp  
  
CMD update-config && bash

