FROM python:3.4-alpine  
  
ADD . /build  
  
RUN \  
cd /build && \  
apk add \--no-cache --virtual build-dependencies python-dev build-base && \  
python setup.py build && \  
python setup.py install && \  
apk del build-dependencies && \  
rm -fr /build  
  
ENTRYPOINT ["simpledns"]

