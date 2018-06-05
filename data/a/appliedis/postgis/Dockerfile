FROM appliedis/postgres:9.5  
MAINTAINER Jonathan Meyer <jon@gisjedi.com>  
  
ENV POSTGIS_MAJOR 2.2  
RUN yum -y install https://dl.fedoraproject.org/pub/epel/epel-release-
latest-7.noarch.rpm \  
&& yum -y install postgis2_95 \  
&& yum clean all  
  
RUN mkdir -p /docker-entrypoint-initdb.d  
COPY ./initdb-postgis.sh /docker-entrypoint-initdb.d/postgis.sh  

