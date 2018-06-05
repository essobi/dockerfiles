# pyinstaller-alpine:  
# compiles pyinstaller from source  
# which depends on python:2.7-alpine  
# which in turn uses apline 3.4  
# https://github.com/six8/pyinstaller-alpine  
# https://github.com/docker-library/python/tree/master/2.7/alpine  
# TODO: move to natvie py-* packages rather than pip,  
# openblas-dev cannot be installed when virtual flag is invoked.  
  
FROM six8/pyinstaller-alpine  
  
RUN echo "@edge_community http://dl-cdn.alpinelinux.org/alpine/edge/community"
>> /etc/apk/repositories && \  
apk add --update --no-cache --virtual=build_deps \  
cmake \  
g++ \  
gfortran \  
python-dev && \  
apk add --no-cache \  
make \  
freetype-dev \  
libpng \  
libstdc++ \  
mariadb-dev \  
openblas-dev@edge_community \  
openssh && \  
ln -s /usr/include/locale.h /usr/include/xlocale.h && \  
pip install --upgrade pip && \  
pip install numpy==1.11.1 && \  
pip install pandas==0.19.1 && \  
pip install matplotlib==2.0.0 && \  
pip install scipy==0.19.1 && \  
apk del build_deps && \  
rm -rf /var/cache/apk/*  
  
RUN pip install \  
coverage \  
flake8 \  
pycrypto \  
pyminifier \  
pylint \  
pyflakes \  
pyminifier \  
radon  

