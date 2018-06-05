FROM python:3-alpine  
  
RUN apk add git --no-cache  
  
RUN pip --no-cache-dir install bumpversion  
ENTRYPOINT ["/usr/local/bin/bumpversion"]  

