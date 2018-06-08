FROM debian:jessie  
MAINTAINER Masato Shimizu <ma6ato@gmail.com>  
  
ENV HOME /root  
ENV WORKDIR /root  
ENV MOIN_VERSION 1.9.8  
ENV EURO_VERSION 3995afe116b0  
  
#-ENV LANG ja_JP.UTF-8  
#RUN locale-gen $LANG && update-locale $LANG && \  
# ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -qy \  
nginx uwsgi uwsgi-plugin-python python wget unzip  
  
RUN wget http://static.moinmo.in/files/moin-$MOIN_VERSION.tar.gz -P /tmp && \  
tar xzf /tmp/moin-$MOIN_VERSION.tar.gz -C /tmp && \  
cd /tmp/moin-$MOIN_VERSION && \  
python setup.py install --force --prefix=/usr/local  
  
RUN wget https://bitbucket.org/thesheep/moin-europython/get/$EURO_VERSION.zip
-P /tmp && \  
unzip /tmp/$EURO_VERSION.zip -d /tmp && \  
cd /tmp/thesheep* && \  
cp europython.py /usr/local/share/moin/data/plugin/theme && \  
cp -R /usr/local/lib/python2.7/dist-packages/MoinMoin/web/static/htdocs
/usr/local/share/moin/htdocs && \  
mkdir /usr/local/share/moin/htdocs/europython && \  
cp -R css img /usr/local/share/moin/htdocs/europython  
  
RUN wget https://github.com/mathjax/MathJax/archive/master.zip -P /tmp && \  
unzip /tmp/master.zip -d /tmp && \  
mv /tmp/MathJax-master /usr/local/share/moin/htdocs/common/MathJax  
  
RUN mkdir -p /data/moin/pages /data/moin/user  
  
COPY wikiconfig.py /usr/local/share/moin/wikiconfig.py  
COPY nginx.conf /etc/nginx/sites-available/default  
COPY run-moinmoin.sh /run-moinmoin.sh  
COPY run.sh /run.sh  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log  
RUN ln -sf /dev/stderr /var/log/nginx/error.log  
  
EXPOSE 80  
VOLUME ["/data"]  
ENTRYPOINT ["/run-moinmoin.sh"]  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

