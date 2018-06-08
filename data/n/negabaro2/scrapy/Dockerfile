FROM alpine:3.4  
MAINTAINER negabaro <negabaro@gmail.com>  
  
RUN apk add --update \  
openssl \  
bash \  
ca-certificates \  
python \  
libxslt \  
libxml2 \  
py-pip \  
build-base \  
libxslt-dev \  
libxml2-dev \  
libffi-dev \  
python-dev \  
openssl-dev && \  
  
pip install \  
scrapy \  
simplejson \  
service_identity \  
beautifulsoup && \  
  
apk del --purge *-dev build-base && \  
rm -rf /tmp/* /var/cache/apk/* /root/.cache/*  
  
#COPY nginx.conf /etc/nginx/nginx.conf  
#RUN rm -rf /etc/nginx/conf/default.conf && \  
# touch /etc/nginx/htpasswd  
VOLUME /opt/scrapy/app  
VOLUME /opt/scrapy/logs  
VOLUME /opt/scrapy/data  
  
WORKDIR /opt/scrapy/app  
  
CMD "tail -f /dev/stdout"  

