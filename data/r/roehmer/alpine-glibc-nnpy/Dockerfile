FROM roehmer/alpine-glibc:latest  
  
LABEL maintainer matt.s.giles@gmail.com  
  
ENV BUILD_PKGS="gcc musl-dev python3-dev nanomsg-dev libffi-dev" \  
RUNTIME_PKGS="python3 nanomsg" \  
PIP_PKGS="pip setuptools" \  
PIP_PKGS_COMPILE="nnpy"  
RUN \  
echo "http://dl-4.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories && \  
apk add \--no-cache --virtual .build-deps $BUILD_PKGS && \  
pip3 install --compile $PIP_PKGS_COMPILE && \  
apk del .build-deps && \  
apk add \--no-cache $RUNTIME_PKGS && \  
python3 -m ensurepip && rm -r /usr/lib/python*/ensurepip && \  
ln -s pip3 /usr/bin/pip && ln -sf /usr/bin/python3 /usr/bin/python && \  
pip install $PIP_PKGS  

