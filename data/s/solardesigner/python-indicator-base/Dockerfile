FROM python:3.6.5-alpine  
LABEL maintainer="samsongama@gmail.com"  
  
COPY ta-lib-0.4.0-src.tar.gz /tmp/ta-lib-0.4.0-src.tar.gz  
RUN mkdir build && cd build && apk update && apk add \--no-cache --virtual
.build-deps musl-dev wget git build-base && \  
pip install --no-cache-dir cython numpy && \  
pip install --no-cache-dir pandas --no-build-isolation && \  
pip install --no-cache-dir --upgrade
https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-1.8.0-cp36-cp36m-linux_x86_64.whl
&& \  
cd /tmp && tar -xvzf ta-lib-0.4.0-src.tar.gz && rm ta-lib-0.4.0-src.tar.gz &&
cd ta-lib/ && ./configure --prefix=/usr && make && make install && cd .. && rm
-rf ta-lib/ && \  
git clone https://github.com/mrjbq7/ta-lib.git && cd ta-lib && python setup.py
install && cd .. && rm -rf ta-lib \  
&& find /usr/local \  
\\( -type d -a -name test -o -name tests \\) \  
-o \\( -type f -a -name '*.pyc' -o -name '*.pyo' \\) \  
-exec rm -rf '{}' \+ \  
&& runDeps="$( \  
scanelf --needed --nobanner --recursive /usr/local \  
| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \  
| sort -u \  
| xargs -r apk info --installed \  
| sort -u \  
)" \  
&& apk add \--virtual .rundeps $runDeps \  
&& cd / && apk del .build-deps && rm -rf /build/ /tmp/ta-lib/  

