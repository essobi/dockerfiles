FROM selenium/standalone-chrome:2.45.0  
MAINTAINER Raphael Michel  
USER root  
  
RUN apt-get update && apt-get install -y wget python3 git python3-pip \  
libxml2-dev libxslt1-dev python-dev locales libffi-dev \  
build-essential python3-dev zlib1g-dev libssl-dev npm gettext git \  
libpq-dev libmysqlclient-dev libmemcached-dev curl libfreetype6 \  
libfontconfig libfreetype6-dev libjpeg-dev bzip2 libcups2-dev \  
\--no-install-recommends  
  
WORKDIR /  
RUN npm install -g less@2.5.0 cssmin  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
RUN ln -s /node_modules/.bin/lessc /usr/bin/lessc  
RUN ln -s /node_modules/.bin/cssmin /usr/bin/cssmin  
  
RUN locale-gen  
RUN update-locale LANG=C.UTF-8  
ENV LC_ALL C.UTF-8  
ENV LANG C.UTF-8  
# We want a current pip  
ADD get-pip.py /tmp/get-pip.py  
RUN python3 /tmp/get-pip.py  
RUN pip install virtualenv  
  
ENV PHANTOMJS_VERSION 1.9.7  
# Commands  
RUN \  
mkdir -p /srv/var && \  
wget -q -O /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-$PHANTOMJS_VERSION-
linux-x86_64.tar.bz2 && \  
tar -xjf /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2 -C /tmp && \  
rm -f /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2 && \  
mv /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64/ /srv/var/phantomjs && \  
ln -s /srv/var/phantomjs/bin/phantomjs /usr/bin/phantomjs  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/*  
  
CMD ["/bin/bash"]  

