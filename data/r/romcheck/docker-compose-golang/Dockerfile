FROM docker  
  
FROM golang:1.9-alpine  
  
RUN apk add --no-cache make py2-pip bash \  
&& pip install --no-cache-dir docker-compose  
  
COPY \--from=0 /usr/local/bin/docker /usr/local/bin/  

