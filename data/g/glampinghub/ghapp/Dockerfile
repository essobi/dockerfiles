FROM ubuntu:xenial  
MAINTAINER José Luis Salvador Rufo <salvador.joseluis@gmail.com>  
  
ENV DEBIAN_FRONTEND=noninteractive \  
LANG=en_US.UTF-8 \  
LANGUAGE=en_US:en \  
LC_ALL=en_US.UTF-8 \  
TERM=${TERM:-xterm} \  
PORT=8000 \  
ENV=develop \  
DEBUG=True  
  
RUN apt-get update && \  
apt-get install locales && \  
locale-gen en_US.UTF-8  
  
ADD https://deb.nodesource.com/setup_6.x /tmp/setup-nodejs  
COPY ./requirements.txt /tmp/  
COPY ./sd_notify /usr/bin/  
  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections && \  
bash /tmp/setup-nodejs && \  
apt-get install --no-install-recommends -qy \  
nodejs openssh-client git \  
build-essential \  
virtualenv python-pip python-dev python-setuptools python-wheel \  
libpq-dev libmaxminddb0 libmaxminddb-dev libmemcached-dev \  
libjpeg8 libjpeg8-dev libopenjp2-7 libopenjp2-7-dev libtiff5 libtiff5-dev
libfreetype6 libfreetype6-dev libwebp5 libwebp-dev \  
libgeos-3.5.0 libgeos-dev gdal-bin libgdal-dev python-gdal binutils libproj-
dev gdal-bin \  
wkhtmltopdf xvfb \  
libffi-dev \  
vim less tmux && \  
ln -s /usr/include/freetype2 /usr/local/include/freetype && \  
echo -n '#!/bin/sh\nxvfb-run -a /usr/bin/wkhtmltopdf "$@" ||
/usr/bin/wkhtmltopdf "$@"\n' > /usr/local/bin/wkhtmltopdf && \  
chmod +x /usr/local/bin/wkhtmltopdf && \  
npm install --global --production bower gulp-cli && \  
pip install -r /tmp/requirements.txt && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && npm cache
clean  
  
COPY ./docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
WORKDIR /webapp  
CMD ["/bin/sleep","infinity"]  

