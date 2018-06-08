FROM python:3.5  
MAINTAINER abellee000 <lianbang@live.cn>  
  
# install phantomjs  
RUN mkdir -p /opt/phantomjs \  
&& cd /opt/phantomjs \  
&& wget -O phantomjs.tar.bz2
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
\  
&& tar xavf phantomjs.tar.bz2 --strip-components 1 \  
&& ln -s /opt/phantomjs/bin/phantomjs /usr/local/bin/phantomjs \  
&& rm phantomjs.tar.bz2  
ENV PYCURL_SSL_LIBRARY openssl  
  
# install requirements  
COPY requirements.txt /opt/pyspider/requirements.txt  
RUN pip install -r /opt/pyspider/requirements.txt  
  
# add all repo  
COPY ./ /opt/pyspider  
  
# run test  
WORKDIR /opt/pyspider  
RUN pip install pyspider  
  
VOLUME ["/opt/pyspider"]  
ENTRYPOINT ["pyspider"]  
  
EXPOSE 5000 23333 24444 25555  

