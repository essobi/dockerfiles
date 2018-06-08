FROM alpine:3.7  
  
LABEL maintainer matt.s.giles@gmail.com  
  
ENV BUILD_PKGS="gcc musl-dev python3-dev libev-dev" \  
RUNTIME_PKGS="python3 libev" \  
PIP_PKGS="pip setuptools" \  
PIP_PKGS_COMPILE="bjoern"  
RUN \  
apk add \--no-cache --virtual .build-deps $BUILD_PKGS && \  
pip3 install --compile $PIP_PKGS_COMPILE && \  
apk del .build-deps && \  
apk add \--no-cache $RUNTIME_PKGS && \  
python3 -m ensurepip && rm -r /usr/lib/python*/ensurepip && \  
ln -s pip3 /usr/bin/pip && ln -sf /usr/bin/python3 /usr/bin/python && \  
pip install --upgrade $PIP_PKGS  

