FROM alpine:3.7  
RUN apk add --no-cache groff less python py-pip && \  
pip install awscli && \  
apk del py-pip py-setuptools  
ENTRYPOINT ["/usr/bin/aws"]  

