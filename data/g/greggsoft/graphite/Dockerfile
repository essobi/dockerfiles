FROM ubuntu:14.04  
MAINTAINER Mikhail Menshenin <greggsoft@gmail.com>  
  
RUN apt-get update && apt-get install -y apache2 libapache2-mod-wsgi curl
libffi-dev python-cairo python-dev  
  
RUN curl -s https://bootstrap.pypa.io/get-pip.py > /tmp/get-pip.py  
RUN python /tmp/get-pip.py  
  
RUN pip install Django>=1.4  
RUN pip install simplejson==2.1.6  
RUN pip install django-tagging==0.3.6  
RUN pip install pytz  
RUN pip install pyparsing==1.5.7  
RUN pip install cairocffi  
RUN pip install whitenoise  
RUN pip install https://github.com/graphite-project/ceres/tarball/master  
RUN pip install https://github.com/graphite-project/whisper/tarball/master  
RUN pip install https://github.com/graphite-project/carbon/tarball/master  
RUN pip install https://github.com/graphite-project/graphite-
web/tarball/master  
  
RUN cp /opt/graphite/conf/carbon.conf.example /opt/graphite/conf/carbon.conf  
RUN cp /opt/graphite/conf/storage-schemas.conf.example
/opt/graphite/conf/storage-schemas.conf  
RUN cp /opt/graphite/conf/graphite.wsgi.example
/opt/graphite/conf/graphite.wsgi  
RUN cp /opt/graphite/webapp/graphite/local_settings.py.example
/opt/graphite/conf/local_settings.py  
  
RUN adduser --system --quiet --home /opt/graphite --no-create-home --shell
/bin/false \--force-badname --group --gecos "Graphite User" graphite  
  
ADD apache-graphite.conf /etc/apache2/sites-available/graphite.conf  
RUN a2dissite 000-default  
RUN a2ensite graphite  
  
EXPOSE 80  
EXPOSE 2003  
VOLUME [ "/opt/graphite/conf", "/opt/graphite/storage/whisper" ]  
  
CMD ln -sf /opt/graphite/conf/local_settings.py
/opt/graphite/webapp/graphite/local_settings.py &&
PYTHONPATH=/opt/graphite/webapp django-admin.py syncdb
--settings=graphite.settings --noinput && PYTHONPATH=/opt/graphite/webapp
django-admin.py collectstatic --noinput --settings=graphite.settings && chown
-R graphite:graphite /opt/graphite && apache2ctl start &&
/opt/graphite/bin/carbon-cache.py --debug start

