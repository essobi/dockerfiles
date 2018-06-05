FROM eeacms/kgs:18.2.27  
MAINTAINER "EEA: IDM2 S-Team"  
RUN apt-get update && apt-get install -y --no-install-recommends apt-utils \  
&& apt-get install build-essential libmemcached-dev zlib1g-dev libmysqlclient-
dev \  
python-dev libldap2-dev libsasl2-dev libssl-dev libxml2-dev libxslt1-dev
zlib1g-dev -y  
  
ENV GRAYLOG_FACILITY=bise-plone  
  
RUN buildout  
  
COPY buildout.cfg /plone/instance/  
RUN buildout -N  

