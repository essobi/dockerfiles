FROM python:3.5.1-alpine  
MAINTAINER Orbweb Inc. <engineering@orbweb.com>  
  
ENV PYTHON_SETUPTOOLS_VERSION 21.0.0  
ENV PYTHON_WHEEL_VERSION 0.29.0  
ENV PYTHONUNBUFFERED True  
ENV PIP_NO_CACHE_DIR off  
ENV PIP_DISABLE_PIP_VERSION_CHECK on  
ENV LIBRARY_PATH /lib:/usr/lib  
  
RUN pip install setuptools==$PYTHON_SETUPTOOLS_VERSION
wheel==$PYTHON_WHEEL_VERSION && \  
mkdir -p /usr/src/app/  
WORKDIR /usr/src/app/  
  
ONBUILD COPY requirements.txt /usr/src/app/  
ONBUILD RUN apk --no-cache add --virtual .build-deps \  
build-base \  
openssl-dev \  
libffi-dev \  
zlib-dev && \  
cat requirements.txt | grep -oh -E "builddeps:(\w|,|-)*" | awk
'{split($0,a,":"); print a[2]}' | awk '{gsub(/,/, "\n", $0); print $0}' | sort
-u | xargs apk --no-cache add --virtual .build-deps && \  
cat requirements.txt | grep -oh -E "rundeps:(\w|,|-)*" | awk
'{split($0,a,":"); print a[2]}' | awk '{gsub(/,/, "\n", $0); print $0}' | sort
-u | xargs apk --no-cache add --virtual .run-deps && \  
apk --no-cache add --virtual .run-deps \  
zlib && \  
pip install \  
cython==0.24 \  
pyOpenSSL==16.0.0 \  
ndg-httpsclient==0.4.0 \  
pyasn1==0.1.9 \  
pyasn1-modules==0.0.8 \  
pycparser==2.14 \  
cryptography==1.3.1 \  
cffi==1.6.0 \  
certifi==2016.2.28 && \  
pip install -r requirements.txt && \  
pip uninstall -y cython && \  
apk del .build-deps && \  
find /usr/ \  
\\( -type d -a -name test -o -name tests \\) \  
-o \\( -type f -a -name '*.pyc' -o -name '*.pyo' \\) \  
-exec rm -rf '{}' \+ && \  
find . -type d -name "__pycache__" -exec rm -rf '{}' +  
ONBUILD COPY . /usr/src/app  

