FROM hope/base-alpine:3.5  
  
ENV \  
AWSCLI_VERSION=1.11.63  
  
RUN \  
apk add \--no-cache \--virtual=build-dependencies py-pip && \  
apk add \--no-cache groff less python && \  
pip install awscli==$AWSCLI_VERSION && \  
apk del build-dependencies  
  
ENTRYPOINT ["aws"]  

