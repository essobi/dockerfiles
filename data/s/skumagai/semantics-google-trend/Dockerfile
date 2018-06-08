FROM alpine:3.4  
RUN adduser -DH nc_semantics && \  
apk update && apk upgrade && \  
apk add --no-cache libxml2 libxslt py-lxml uwsgi-python && \  
apk add --no-cache --virtual .build-deps python-dev py-pip \  
libxml2-dev libxslt-dev g++ && \  
ln -s /usr/include/locale.h /usr/include/xlocale.h && \  
ln -s /usr/include/libxml2/libxml /usr/include/libxml && \  
pip install --no-cache-dir numpy && \  
pip install --no-cache-dir pandas && \  
pip install --no-cache-dir pytrends flask && \  
apk del .build-deps && \  
rm /var/cache/apk/*  
  
WORKDIR /etc/uwsgi  
COPY trend.py trend.ini /etc/uwsgi/  
  
ENTRYPOINT ["uwsgi", "--ini", "trend.ini"]  

