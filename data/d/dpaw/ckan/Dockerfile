#!/bin/bash  
FROM ubuntu:12.04  
MAINTAINER Department of Parks and Wildlife <asi@dpaw.wa.gov.au>  
  
# Apt setup  
RUN sed -i
s=http://.*archive.ubuntu.*ubuntu=mirror://mirrors.ubuntu.com/mirrors.txt=g
/etc/apt/sources.list; \  
sed -i "s/ main/ main universe/g" /etc/apt/sources.list; \  
apt-get update && apt-get install -y python-software-properties wget sudo curl
vim ssh  
RUN add-apt-repository -y 'deb http://apt.postgresql.org/pub/repos/apt/
precise-pgdg main'; \  
wget -O - http://apt.postgresql.org/pub/repos/apt/ACCC4CF8.asc | apt-key add -  
RUN apt-get update  
  
# Install packages
-----------------------------------------------------------#  
# CKAN requisites, CKAN  
RUN sudo apt-get -y install nginx apache2 libapache2-mod-wsgi libpq5
postgresql-9.3 \  
postgresql-9.3-postgis build-essential solr-jetty git-core \  
python-dev libxml2-dev libxslt-dev  
ADD python-ckan_2.2-0_amd64.deb /tmp/python-ckan_2.2-0_amd64.deb  
RUN dpkg -i /tmp/python-ckan_2.2-0_amd64.deb  
  
# Environment variables
------------------------------------------------------#  
ENV PGVERSION 9.3  
ENV PGHOST localhost  
ENV PGPORT 5432  
RUN /etc/init.d/postgresql start && \  
sudo -u postgres psql -c \  
"CREATE USER ckan_default WITH CREATEROLE SUPERUSER PASSWORD 'pass';" && \  
/etc/init.d/postgresql stop  
# CKAN db and user  
ENV PGDATABASE ckan_default  
ENV PGUSER ckan_default  
ENV PGPASS pass  
# Datastore db and user  
ENV DSDATABASE datastore_default  
ENV DSUSER datastore_default  
ENV DSPASS pass  
# Home dirs  
ENV CKAN_HOME /usr/lib/ckan  
ENV CKAN_INI /etc/ckan/default/production.ini  
ENV JAVA_HOME /usr/lib/jvm/java-6-openjdk-amd64/  
# Setup databases
------------------------------------------------------------#  
# CKAN main db & datastore db  
RUN /etc/init.d/postgresql start && \  
sudo -u postgres createdb $PGDATABASE -E utf8 -T template0 -O $PGUSER; \  
sudo -u postgres psql -c "CREATE EXTENSION postgis" -d $PGDATABASE && \  
sudo -u postgres psql -c "CREATE USER $DSUSER PASSWORD '$DSPASS';" && \  
sudo -u postgres createdb $DSDATABASE -E utf8 -T template0 -O $DSUSER && \  
sudo -u postgres psql -c "CREATE EXTENSION postgis" -d $DSDATABASE && \  
/etc/init.d/postgresql stop  
  
  
# Virtualenv, post CKAN install
----------------------------------------------#  
# Install CKAN and CKAN extension dependencies  
RUN . $CKAN_HOME/default/bin/activate && cd $CKAN_HOME/default/src/ckan && \  
pip install -e git+https://github.com/okfn/ckanext-spatial.git#egg=ckanext-
spatial && \  
pip install -r $CKAN_HOME/default/src/ckanext-spatial/pip-requirements.txt  
  
  
# Modify config files
--------------------------------------------------------#  
RUN sed 's/NO_START=1/NO_START=0/g' -i /etc/default/jetty && \  
sed "s=#JAVA_HOME\==JAVA_HOME\=$JAVA_HOME=g" -i /etc/default/jetty && \  
sed "s/#JETTY_PORT=8080/JETTY_PORT=8983/g" -i /etc/default/jetty && \  
ln -sf $CKAN_HOME/default/src/ckan/ckan/config/solr/schema-2.0.xml
/etc/solr/conf/schema.xml && \  
sed "s/#solr_url/solr_url/g" -i $CKAN_INI && \  
sed "s/#ckan.storage_path/ckan.storage_path/g" -i $CKAN_INI && \  
sed "s/#ckan.max_resource_size.*/ckan.max_resource_size = 1024/g" -i $CKAN_INI
&& \  
sed "s/#ckan.max_image_size.*/ckan.max_image_size = 128/g" -i $CKAN_INI && \  
sed "s/#ckan.datastore.write_url.*/ckan.datastore.write_url =
postgresql:\/\/$PGUSER:$PGPASS@$PGHOST:$PGPORT\/$DSDATABASE/g" -i $CKAN_INI &&
\  
sed "s/#ckan.datastore.read_url.*/ckan.datastore.read_url =
postgresql:\/\/$DSUSER:$DSPASS@$PGHOST:$PGPORT\/$DSDATABASE/g" -i $CKAN_INI &&
\  
sed "s/ckan.plugins =.*/ckan.plugins = stats text_preview recline_preview
pdf_preview resource_proxy datastore spatial_metadata \  
spatial_query geojson_preview wms_preview datapusher/g" -i $CKAN_INI && \  
echo "extra_template_paths = /var/lib/ckan/templates" >> $CKAN_INI && \  
echo "extra_public_paths = /var/lib/ckan/public" >> $CKAN_INI && \  
mkdir -p /var/lib/ckan/templates/package /var/lib/ckan/public && \  
chown -R www-data:www-data /var/lib/ckan && \  
cp $CKAN_HOME/default/src/ckan/ckan/templates/package/search.html
/var/lib/ckan/templates/package/search.html && \  
sed "s/{% block secondary_content %}/{% block secondary_content %} \  
{% snippet \"spatial\/snippets\/spatial_query.html\", default_extent=\"[[-35,
115], [-10, 130]]\" %}/g" -i /var/lib/ckan/templates/package/search.html  
# Init db for CKAN  
# Setting permissions for CKAN databases and users to minimum  
RUN . $CKAN_HOME/default/bin/activate && cd $CKAN_HOME/default/src/ckan && \  
/etc/init.d/postgresql start && \  
/etc/init.d/jetty start && \  
paster datastore set-permissions postgres -c $CKAN_INI && \  
paster db init -c $CKAN_INI  
  
EXPOSE 8080 8800  
  
ADD startup.sh /usr/local/bin/startup.sh  
ADD shell.sh /usr/local/bin/shell.sh  
ENTRYPOINT ["startup.sh"]

