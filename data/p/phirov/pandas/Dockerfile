# consult: https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-
practices  
# Forked: https://hub.docker.com/r/amancevice/pandas  
FROM phirov/python:2  
MAINTAINER phirov@163.com  
  
RUN apk add \--no-cache --virtual .build-deps g++ && \  
pip install numpy==1.12.0 \  
cython==0.25.2 && \  
pip install pandas==0.19.2 && \  
apk del .build-deps  

