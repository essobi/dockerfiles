FROM python:2-alpine  
MAINTAINER Maple <maplevalley8@gmail.com>  
  
ENV APP_PATH /webapp  
ENV PHANTOMJS_ARCHIVE="phantomjs.tar.gz"  
  
RUN apk update && apk add build-base libevent-dev curl  
  
COPY requirements.txt requirements.txt  
RUN pip install -r requirements.txt  
  
RUN curl -Lk -o $PHANTOMJS_ARCHIVE https://github.com/fgrehm/docker-
phantomjs2/releases/download/v2.0.0-20150722/dockerized-phantomjs.tar.gz \  
&& tar -xf $PHANTOMJS_ARCHIVE -C /tmp/ \  
&& cp -R /tmp/etc/fonts /etc/ \  
&& cp -R /tmp/lib/* /lib/ \  
&& cp -R /tmp/lib64 / \  
&& cp -R /tmp/usr/lib/* /usr/lib/ \  
&& cp -R /tmp/usr/lib/x86_64-linux-gnu /usr/ \  
&& cp -R /tmp/usr/share/* /usr/share/ \  
&& cp /tmp/usr/local/bin/phantomjs /usr/bin/ \  
&& rm -fr $PHANTOMJS_ARCHIVE /tmp/*  
  
RUN mkdir -p $APP_PATH  
WORKDIR $APP_PATH  
  
COPY . .  
  
EXPOSE 5000  
  
CMD gunicorn -w 4 -k gevent -b 0.0.0.0:5000 \--log-level debug manage:app  

