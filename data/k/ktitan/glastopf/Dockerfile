FROM gliderlabs/alpine:3.3  
  
MAINTAINER kTitan <alexander.schneider@gmail.com>  
  
## Install dependencies  
RUN apk add \--no-cache --update \  
autoconf \  
build-base \  
cython \  
git \  
libffi-dev \  
php-cli \  
php-dev \  
py-asn1 \  
py-cffi \  
py-chardet \  
py-chardet \  
py-cparser \  
py-cryptography \  
py-dateutil \  
py-enum34 \  
py-idna \  
py-ipaddress \  
py-jinja2 \  
py-lxml \  
py-lxml \  
py-mysqldb \  
py-openssl \  
py-openssl \  
py-pip \  
py-requests \  
py-setuptools \  
python \  
python-dev \  
&& apk add \--no-cache --repository
http://dl-3.alpinelinux.org/alpine/edge/testing/ \  
py-beautifulsoup \  
py-cssselect \  
py-gevent \  
py-greenlet \  
py-mongo \  
py-sqlalchemy \  
py-webob \  
&& rm -rf /var/cache/apk/*  
  
## Install and configure the PHP sandbox and glastopf from latest sources  
RUN git clone https://github.com/mushorg/BFR.git /opt/BFR \  
&& cd /opt/BFR \  
&& phpize \  
&& ./configure --enable-bfr \  
&& make \  
&& make install \  
&& echo "zend_extension = "$(find /usr -name bfr.so) >> /etc/php/php.ini \  
&& git clone https://github.com/mushorg/glastopf.git /opt/glastopf \  
&& cd /opt/glastopf \  
&& python setup.py install \  
&& rm -rf /opt/glastopf /opt/BFR /tmp/* /var/tmp/*  
  
## Configuration  
VOLUME ["/opt/myhoneypot"]  
  
EXPOSE 80  
WORKDIR /opt/myhoneypot  
CMD ["glastopf-runner"]  

