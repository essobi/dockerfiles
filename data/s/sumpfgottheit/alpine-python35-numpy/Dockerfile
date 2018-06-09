FROM python:3.5-alpine  
MAINTAINER florian.sachs@gmx.at  
  
# https://github.com/python-pillow/Pillow/issues/1763  
# Pillow mit Alpine braucht das  
ENV LIBRARY_PATH=/lib:/usr/lib  
ENV BASEDIR=/opt/hr  
ENV VIRTUALENV=/opt/virtualenv_hr  
  
# Install Development libraries needed for our system  
RUN apk update && \  
apk add git libjpeg-turbo-dev linux-headers musl-dev gcc curl-dev zeromq-dev
gpgme-dev attr-dev  
  
RUN apk add openblas openblas-dev --update-cache --repository http://dl-
cdn.alpinelinux.org/alpine/edge/community/ && \  
pip install cython setuptools nose  
  
RUN mkdir /build && \  
cd /build && \  
apk add ca-certificates && \  
update-ca-certificates && \  
apk add openssl && \  
wget https://github.com/numpy/numpy/archive/v1.11.0.tar.gz && \  
tar xvfz v1.11.0.tar.gz  
  
ADD numpy-1.11.0-musl.patch /tmp  
RUN cd /build/numpy-1.11.0 && \  
patch -p1 < /tmp/numpy-1.11.0-musl.patch  
  
RUN cd /build/numpy-1.11.0 && \  
export ATLAS=None && \  
export LDFLAGS="$LDFLAGS -shared" && \  
python setup.py build config_fc --fcompiler=gnu95  
  
RUN cd /build/numpy-1.11.0 && \  
export ATLAS=None && \  
export LDFLAGS="$LDFLAGS -shared" && \  
python setup.py install config_fc --fcompiler=gnu95  
  
RUN rm -fr /tmp/* /var/cache/apk/*  
  

