FROM python:3  
MAINTAINER Patrick Holl <patrick.holl@tum.de>  
  
ENV PHANTOMJS_VERSION 2.1.1  
ENV PHANTOMJS_PLATFORM linux-x86_64  
  
RUN wget -q -O /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-${PHANTOMJS_VERSION}-${PHANTOMJS_PLATFORM}.tar.bz2
&& \  
tar -xjf /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2 -C /tmp && \  
rm -f /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2 && \  
mv /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64/ /usr/local/share/phantomjs
&& \  
ln -s /usr/local/share/phantomjs/bin/phantomjs /usr/local/bin/phantomjs  
  
COPY requirements.txt /opt/app/requirements.txt  
WORKDIR /opt/app  
  
RUN pip install -U setuptools  
RUN pip install appdirs --upgrade  
RUN pip install -r requirements.txt --upgrade  
COPY . /opt/app  
  
CMD hug -f Classifier.py

