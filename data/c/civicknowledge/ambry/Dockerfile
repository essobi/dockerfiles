#  
# docker build -t civick/ambry .  
FROM phusion/baseimage:0.9.17  
MAINTAINER Eric Busboom "eric@civicknowledge.org"  
RUN apt-get update && apt-get install -y \  
language-pack-en \  
build-essential make gcc \  
wget curl git \  
python python-pip python-dev libffi-dev \  
sqlite3 libpq-dev \  
libgdal-dev gdal-bin python-gdal python-numpy python-scipy \  
libsqlite3-dev libspatialite5 libspatialite-dev spatialite-bin
libspatialindex-dev  
  
RUN pip install --upgrade pip  
  
ENV LANGUAGE en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
RUN locale-gen en_US.UTF-8  
RUN dpkg-reconfigure locales  
  
# This package allows Sqlalchemy to load the spatialite shared object to
provide  
# Spatialite services.  
RUN pip install git+https://github.com/clarinova/pysqlite.git#egg=pysqlite  
  
# The pip installs allow the creation of a layer for each, so changes to the
main Ambry source  
# can be isolated, resulting in faster docker builds. The list is built from
the merge-requirements script  
# We probably don't want to do this long term, but it is expediant during
development.  
# Start pip installs  
RUN pip install 'pyasn1>=0.1.8'  
RUN pip install 'address-parser==0.0.1'  
RUN pip install 'boto>=2.38.0'  
RUN pip install 'beautifulsoup4==4.3.2'  
RUN pip install 'ckanapi==3.5'  
RUN pip install 'ckcache>=0.1.6'  
RUN pip install 'decorator>=4'  
RUN pip install 'Flask-Compress==1.2.1'  
RUN pip install 'Flask==0.10.1'  
RUN pip install 'Flask-Session==0.1.1'  
RUN pip install 'geoid>=0.1.1'  
RUN pip install 'ipython==3.1.0'  
RUN pip install 'isodate==0.5.1'  
RUN pip install 'itsdangerous==0.24'  
RUN pip install 'Jinja2==2.8'  
RUN pip install 'lockfile==0.10.2'  
RUN pip install 'Markdown==2.6.2'  
RUN pip install 'MarkupSafe==0.23'  
RUN pip install 'meta==0.2.4'  
RUN pip install 'nltk==3.0.2'  
RUN pip install 'numpy==1.9.2'  
RUN pip install 'oauth2client==1.4.12'  
RUN pip install 'pandas<=0.15.1'  
RUN pip install 'Pygments==2.0.2'  
RUN pip install 'python-dateutil==2.4.2'  
RUN pip install 'pytz==2015.4'  
RUN pip install 'PyYAML==3.11'  
RUN pip install 'requests>=2.6.0'  
RUN pip install 'semantic-version==2.4.1'  
RUN pip install 'sh==1.11'  
RUN pip install 'simplejson==3.6.5'  
RUN pip install 'six==1.9.0'  
RUN pip install 'SQLAlchemy==1.0.0'  
RUN pip install 'sqlparse==0.1.15'  
RUN pip install 'Werkzeug==0.10.4'  
RUN pip install 'whoosh==2.7.0'  
RUN pip install 'psycopg2==2.6'  
RUN pip install 'fs>=0.5.2'  
RUN pip install 'msgpack-python==0.4.6'  
RUN pip install 'livestats==1.0'  
RUN pip install 'tabulate==0.7.5'  
RUN pip install 'terminaltables==1.2.1'  
RUN pip install 'watchdog==0.8.3'  
RUN pip install 'filelock==2.0.4'  
RUN pip install 'ambry-sources>=0.1.1'  
RUN pip install 'unicodecsv==0.12.0 '  
# End pip installs  
COPY . /var/ambry/src  
WORKDIR /var/ambry/src  
  
RUN python setup.py install  
  
WORKDIR /var/ambry  
  
VOLUME /var/ambry  
  
ADD support/ambry-docker/ambry-init.sh /var/ambry/ambry-init.sh  
  
RUN mkdir -p /var/ambry/source  
  
#RUN ambry config install  
ADD ${AMBRY_CONFIG:-ambry/support/ambry-builder.yaml} /etc/ambry.yaml  
RUN echo 'source /usr/local/bin/ambry-aliases.sh' >> /root/.bashrc  
  
RUN ambry import /var/ambry/src/test/bundle_tests/  
  
CMD bash ambry-init.sh

