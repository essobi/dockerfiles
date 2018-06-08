FROM python:2.7.12-alpine  
  
ENV FLASK_PROXY_PORT 8080  
RUN mkdir -p /actionProxy  
ADD actionproxy.py /actionProxy/  
  
RUN mkdir -p /action  
ADD . /action  
ADD my_script.py /action/exec  
RUN chmod +x /action/exec  
  
# install dependencies  
# the lapack package is only in the community repository  
RUN echo "http://dl-4.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories  
RUN apk add --no-cache bash lapack-dev  
RUN apk add --no-cache --virtual .build-deps \  
gcc \  
freetype-dev \  
gfortran \  
musl-dev \  
g++ \  
&& ln -s /usr/include/locale.h /usr/include/xlocale.h \  
&& pip install --no-cache-dir gevent==1.1.2 flask==0.11.1 \  
&& pip install -r /action/requirements.txt \  
&& apk del .build-deps  
RUN apk add --no-cache libstdc++  
  
CMD ["/bin/bash", "-c", "cd actionProxy && python -u actionproxy.py"]  

