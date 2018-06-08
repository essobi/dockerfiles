FROM python:2.7.12-alpine  
  
MAINTAINER Han Zhang <zhanghan.simon@gmail.com>  
  
RUN apk --update add --no-cache \  
bash \  
wget \  
vim \  
supervisor \  
# for paypal API  
libffi-dev \  
openssl-dev  
  
# create target folder  
RUN mkdir /app  
WORKDIR /app  
  
COPY requirements.txt requirements.txt  
  
RUN apk add --no-cache nginx  
  
RUN apk add --update python-dev build-base linux-headers \  
&& pip --no-cache-dir install
https://github.com/unbit/uwsgi/archive/uwsgi-2.0.zip#egg=uwsgi \  
&& pip --no-cache-dir install -r requirements.txt \  
&& apk del python-dev build-base linux-headers  
  
# setup supervisord  
RUN mkdir -p /var/log/supervisor  
  
# configure nginx  
COPY ./conf/nginx.conf /etc/nginx/nginx.conf  
COPY ./conf/stage.default.conf /etc/nginx/conf.d/default.conf  
  
# get credentials  
RUN wget http://www.stack360.io/my-weekly-status.json \  
&& mkdir ~/.credentials \  
&& cp -rf my-weekly-status.json ~/.credentials/ \  
&& chmod 755 -R ~/.credentials  
  
COPY . .  
  
ENTRYPOINT ["/usr/bin/supervisord", "-c", "conf/supervisord.conf"]  
  
EXPOSE 80 443  

