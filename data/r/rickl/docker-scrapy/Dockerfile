FROM frolvlad/alpine-python2  
  
RUN apk add --no-cache python-dev gcc musl-dev openssl-dev libxml2-dev
libxslt-dev libffi-dev libxml2 libxslt \  
&& pip install scrapy \  
&& apk del python-dev gcc musl-dev openssl-dev libxml2-dev libxslt-dev libffi-
dev  
  
ENTRYPOINT ["/usr/bin/scrapy"]  
  

