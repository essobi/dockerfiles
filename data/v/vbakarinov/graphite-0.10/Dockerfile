FROM ubuntu:14.04  
MAINTAINER Valentin Bakarinov <vbakarinov@asdco.ru>  
  
RUN apt-get update && apt-get install -y python python-pip python-twisted
python-memcache python-pysqlite2 python-simplejson python-cairo python-django
python-django-tagging python-txamqp python-pyparsing python-zope.interface
python-dev libffi-dev git nginx curl vim mc --no-install-recommends  
RUN apt-get clean  
RUN apt-get autoremove  
RUN rm -rf /var/lib/apt/lists/*  
RUN pip install pytz mock nose  
  
WORKDIR /tmp  
RUN git clone https://github.com/graphite-project/ceres.git  
RUN git clone https://github.com/graphite-project/whisper.git  
RUN git clone https://github.com/graphite-project/carbon.git -b megacarbon  
RUN git clone https://github.com/graphite-project/graphite-web.git  
RUN CWD=$PWD; for dir in ceres whisper carbon graphite-web; do cd $CWD/$dir;
python setup.py install; done  
  
WORKDIR /tmp/carbon  
RUN cp -R plugins /opt/graphite/  
RUN rm -rf /tmp/* /var/tmp/*  
  
RUN mkdir /ceres  
RUN ceres-tree-create /ceres  
  
ADD source /  
RUN /usr/bin/django-admin syncdb --pythonpath /opt/graphite/webapp --settings
graphite.settings --noinput  
RUN chmod +x /init  
VOLUME /ceres  
WORKDIR /  
EXPOSE 2003 2004 2104 2204 7002 8080  
CMD /init &  

