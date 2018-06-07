FROM python:3.5.4  
MAINTAINER ERP Ukraine <info@erp.co.ua>  
  
# Install some deps  
RUN apt-get update && apt-get install -y \  
apt-utils \  
libsqlite3-dev \  
locales \  
nodejs \  
sqlite3  
  
RUN locale-gen en_US.UTF-8 && \  
localedef -i en_US -f UTF-8 en_US.UTF-8  
  
RUN apt-get install -y \  
postgresql-9.4 \  
postgresql-client-9.4 \  
sudo  
  
RUN service postgresql start && \  
pg_dropcluster --stop 9.4 main && \  
pg_createcluster --locale en_US.UTF-8 --start 9.4 main && \  
sudo -u postgres sh -c 'createuser -s root & createdb root'  
  
RUN apt-get install -y \  
build-essential \  
curl \  
expect-dev \  
gcc \  
python-dev \  
libldap2-dev \  
libsasl2-dev \  
libssl-dev \  
python-lxml \  
python-paramiko \  
python-simplejson \  
python-serial \  
python-yaml  
  
RUN curl -sL https://deb.nodesource.com/setup_4.x | bash -  
  
RUN apt-get update && apt-get install -y \  
nodejs \  
node-less  
  
RUN pip install -q \  
ofxparse \  
unidecode \  
unicodecsv \  
lxml \  
xlsxwriter \  
googlemaps  

