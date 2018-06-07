FROM sumpfgottheit/centos7  
MAINTAINER Florian Sachs "florian.sachs@gmx.at"  
# libffi-devel openssl-devel und pyopenssl ndg-httpsclient pyasn1  
# are necessary to remove urllib3's inscure platform warning  
# see:
https://urllib3.readthedocs.org/en/latest/security.html#insecureplatformwarning  
RUN yum -y install python-pip gcc python-devel libffi-devel openssl-devel  
RUN pip install gunicorn logstash_formatter pyopenssl ndg-httpsclient pyasn1  
RUN yum clean all  
  
RUN mkdir /pub  
  
ADD logstash.conf /etc/logstash.conf  
ADD gunicorn.logging.conf /gunicorn.logging.conf  
ADD inject-logging-into-gunicorn.sh /docker-entrypoint.d/inject-logging-into-
gunicorn.sh  
ADD create_working_gunicorn_config.sh /docker-
entrypoint.d/create_working_gunicorn_config.sh  
ADD pip-install-requirements.sh /docker-entrypoint.d/pip-install-
requirements.sh  
  
EXPOSE 5000  
CMD /usr/bin/gunicorn --config /docker-entrypoint-ext.d/working.gunicorn.ini
$(</docker-entrypoint-ext.d/working.gunicorn.app)  
  

