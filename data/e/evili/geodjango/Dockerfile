FROM centos:7  
ENV CENTOS_VERSION=7 \  
PG_VERSION=10 \  
PG_NODOT=10 \  
PG_REVISION=2 \  
POSTGIS_VERSION=24 \  
BASE_DIR=/src  
# https://download.postgresql.org/pub/repos/yum/10/redhat/rhel-7-x86_64/pgdg-
centos10-10-2.noarch.rpm  
RUN cd /tmp && \  
yum install -y epel-release && \  
curl -o pgdg.rpm
http://download.postgresql.org/pub/repos/yum/${PG_VERSION}/redhat/rhel-${CENTOS_VERSION}-x86_64/pgdg-
centos${PG_NODOT}-${PG_VERSION}-${PG_REVISION}.noarch.rpm && \  
yum localinstall -y pgdg.rpm && \  
yum upgrade -y && \  
yum install -y \  
GeoIP-devel \  
GeoIP-update \  
gdal \  
gdal-devel \  
geos \  
geos-devel \  
gcc \  
libxml2-devel \  
nginx \  
postgresql${PG_NODOT} \  
postgresql${PG_NODOT}-devel \  
postgis${POSTGIS_VERSION}_${PG_NODOT} \  
postgis${POSTGIS_VERSION}_${PG_NODOT}-client \  
postgis${POSTGIS_VERSION}_${PG_NODOT}-utils \  
proj-devel \  
pwgen \  
python \  
python-devel \  
python-libs \  
python-pip \  
python-urllib3 \  
python34-pip \  
uwsgi-plugin-python  
  
RUN mkdir -pv ${BASE_DIR}  
WORKDIR ${BASE_DIR}  
  
ENV PIP /usr/bin/pip install --no-cache-dir  
ENV PATH /usr/pgsql-${PG_VERSION}/bin:${PATH}  
RUN ${PIP} \--upgrade pip  
RUN ${PIP} Django psycopg2  

