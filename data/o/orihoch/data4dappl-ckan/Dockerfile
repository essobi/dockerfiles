FROM ubuntu:16.04  
  
RUN apt-get update  
RUN apt-get install -y python-dev libpq-dev python-pip python-virtualenv git-
core  
  
RUN mkdir -p /usr/lib/ckan/default  
RUN virtualenv --no-site-packages /usr/lib/ckan/default  
COPY requirement-setuptools.txt /requirement-setuptools.txt  
COPY requirements-ckan.txt /requirements-ckan.txt  
RUN /usr/lib/ckan/default/bin/pip install -r /requirement-setuptools.txt  
RUN /usr/lib/ckan/default/bin/pip install -r /requirements-ckan.txt  
RUN /usr/lib/ckan/default/bin/pip install -e
'git+https://github.com/OriHoch/ckan.git@ckan-2.7.2-fixing-odata-bug#egg=ckan'  
# psql is used to restore db from backup  
RUN apt-get update && apt-get install -y postgresql-client  
  
RUN mkdir -p /etc/ckan/default  
COPY development.ini /etc/ckan/default/development.ini  
COPY who.ini /etc/ckan/default/who.ini  
  
COPY ckanext-odata_org_il /ckanext-odata_org_il  
RUN /usr/lib/ckan/default/bin/pip install -e /ckanext-odata_org_il  
  
WORKDIR "/usr/lib/ckan/default/src/ckan"  
  
COPY entrypoint.sh /entrypoint.sh  
  
CMD ["serve", "/etc/ckan/default/development.ini"]  
  
ENTRYPOINT ["/entrypoint.sh"]  

