FROM alpine:3.7  
ENV AWS_DEFAULT_REGION us-west-1  
ARG BUILD_AWSCLI_VERSION=1.15.4  
ENV AWSCLI_VERSION ${BUILD_AWSCLI_VERSION}  
  
RUN apk add --no-cache --update py-pip && \  
pip install awscli==${AWSCLI_VERSION} \--upgrade && \  
rm -rf /root/.cache && \  
find / -type f -regex '.*\\.py[co]' -delete  
  
ENTRYPOINT ["/usr/bin/aws"]  

