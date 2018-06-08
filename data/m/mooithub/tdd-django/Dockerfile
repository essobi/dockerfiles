FROM ubuntu:14.04  
MAINTAINER mooithub <lab.moo@gmail.com>  
  
RUN apt-get update  
  
# Common  
RUN apt-get install -y vim  
RUN apt-get install -y screen  
RUN apt-get install -y wget  
  
# Python  
RUN apt-get install -y python-dev python-setuptools  
RUN easy_install pip  
RUN pip install virtualenv  
RUN pip install uwsgi  
  
# SCM  
RUN apt-get install -y git  
  
# PhantomJS  
RUN apt-get install -y build-essential chrpath libssl-dev libxft-dev  
RUN apt-get install -y libfreetype6 libfreetype6-dev  
RUN apt-get install -y libfontconfig1 libfontconfig1-dev  
RUN apt-get install -y firefox  
  
# -- Env  
ENV PHANTOMJS_VERSION 1.9.8  
# -- Install phantomjs  
RUN mkdir -p /srv/var && \  
wget -q --no-check-certificate -O /tmp/phantomjs-$PHANTOMJS_VERSION-
linux-x86_64.tar.bz2
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-$PHANTOMJS_VERSION-
linux-x86_64.tar.bz2 && \  
tar -xjf /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2 -C /tmp && \  
rm -f /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2 && \  
mv /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64/ /usr/local/share/phantomjs
&& \  
ln -s /usr/local/share/phantomjs/bin/phantomjs /usr/local/bin/phantomjs  
  
# Project  
WORKDIR /var/www  
ADD ./ ./tdd_django/  
  
WORKDIR /var/www/tdd_django  
RUN cp ./env/.screenrc ~/.screenrc  
RUN cp ./env/.vimrc ~/.vimrc  
RUN . ~/.vimrc  
RUN virtualenv --no-site-packages --distribute ~/.venv/tdd  
RUN . ~/.venv/tdd/bin/activate; pip install -r pip-requirements.txt  
  

