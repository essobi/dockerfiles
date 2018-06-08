FROM alpine  
LABEL maintainer="extrawurst"  
RUN apk --no-cache update && \  
apk --no-cache add python py-pip py-setuptools ca-certificates groff less && \  
pip --no-cache-dir install awscli && \  
rm -rf /var/cache/apk/*  
RUN aws --version

