FROM python:2-alpine  
MAINTAINER Ilkka Laukkanen <ilkka@ilkka.io>  
  
RUN apk --no-cache add build-base python-dev && pip install fabric && mkdir -p
/work  
  
WORKDIR /work  
ENTRYPOINT ["fab"]  

