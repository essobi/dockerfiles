FROM python:2.7  
MAINTAINER antonioj.mattos@gmail.com  
  
ENV DEBIAN_FRONTEND=noninteractive LANG=C.UTF-8  
  
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc |
apt-key add - \  
&& echo 'deb http://apt.postgresql.org/pub/repos/apt/ jessie-pgdg main' >
/etc/apt/sources.list.d/pgdg.list  
  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
libsasl2-dev libldap2-dev freetds-dev \  
libxslt1-dev libblas-dev liblapack-dev \  
libatlas-base-dev gfortran python-dev \  
python-psycopg2 postgresql-contrib locales \  
&& rm -rf /var/lib/apt/lists/* \  
&& localedef -i pt_BR -c -f UTF-8 -A /usr/share/locale/locale.alias
pt_BR.UTF-8  
  
ENV LANG=pt_BR.utf8  

