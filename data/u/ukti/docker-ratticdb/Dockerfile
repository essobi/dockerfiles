FROM python:2.7  
ARG RATTIC_RELEASE  
ENV RATTIC_RELEASE 1.3.1  
WORKDIR /srv/rattic  
  
RUN curl -Lfs
https://github.com/tildaslash/RatticWeb/archive/v$RATTIC_RELEASE.tar.gz | tar
xz --strip 1 -C /srv/rattic  
RUN apt-get update && apt-get install -y gettext libsasl2-dev python-dev
libldap2-dev libssl-dev  
RUN pip install -r /srv/rattic/requirements-pgsql.txt  
RUN pip install jinja2 uwsgi  
RUN apt-get autoremove -y && apt-get clean -y && rm -rf var/lib/apt/lists/*
/var/tmp/* /tmp/*  
  
ADD conf/local.tmpl.cfg /srv/rattic/conf/local.cfg  
ADD conf/uwsgi.ini /usr/local/etc/rattic/uwsgi.ini  
ADD scripts/entrypoint.sh /scripts/entrypoint.sh  
RUN chmod +x /scripts/entrypoint.sh  
  
EXPOSE 8000/tcp  
  
ENTRYPOINT ["bash", "/scripts/entrypoint.sh"]  

