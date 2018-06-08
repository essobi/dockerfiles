##  
# Medin Portal Base Image  
#  
# This creates an Ubuntu derived base image that installs the latest  
# tagged version of the Medin Portal code along with the relevant  
# dependencies. The environment includes an Apache 2 setup that is  
# ready configuring by derived images.  
#  
# Ubuntu Trusty  
FROM ubuntu:14.04  
MAINTAINER Homme Zwaagstra <hrz@geodata.soton.ac.uk>  
  
# Ensure the package repository is up to date  
RUN apt-get update  
  
# Install dependencies provided by Ubuntu repositories  
RUN apt-get install -y \  
git \  
apache2 \  
python-libxml2 \  
python-gdal \  
python-mapnik2 \  
python-pip \  
libapache2-mod-xsendfile \  
libapache2-mod-wsgi \  
python-dev \  
python-docutils  
  
# Install dependencies provided by PIP  
RUN pip install docutils \  
SQLAlchemy==0.9.7 \  
iso8601==0.1.10 \  
rdfextras==0.4 \  
rdflib==4.1.2 \  
Mako==1.0.0 \  
TileCache==2.11 \  
Paste==1.7.5.1 \  
suds==0.4 \  
selector==0.10.1  
  
# Patch SUDS to properly handle invalid service responses  
ADD suds-client.py.patch /tmp/  
RUN patch -p0 /usr/local/lib/python2.7/dist-packages/suds/client.py /tmp/suds-
client.py.patch  
  
# The epsg module needs to be installed separately to SQLAlchemy to avoid
problems  
RUN pip install python-epsg==0.1.4 python-skos==0.1.1  
  
# Clone the git repository  
RUN git clone https://github.com/geo-data/medin-portal.git /usr/src/medin-
portal  
RUN cd /usr/src/medin-portal && git checkout new-dws  
RUN cd /usr/src/medin-portal && git submodule init && git submodule update  
  
# Update the EPSG registry cache. This may take a while...  
RUN cd /usr/src/medin-portal && PYTHONPATH=./python python ./bin/epsg-
update.py ./data/epsg-registry.sqlite  
  
# Update the SKOS based vocabulary cache  
RUN cd /usr/src/medin-portal && PYTHONPATH=./python python ./bin/vocab-
update.py --vocabularies ./data/vocabularies/vocab-list.txt
./data/vocabularies.sqlite  
  
# Set up the web root and link in the relevant static portal files.  
RUN mkdir -p /var/medin-portal/html  
RUN ln -s /usr/src/medin-portal/html/* /var/medin-portal/html/  
RUN ln -s /usr/src/medin-portal/templates /var/medin-portal/templates  
# The data directory has to be hard linked rather than symlinked so  
# that relative links within `data/raster/background-wms.vrt` work  
# correctly.  
RUN cp --archive --link /usr/src/medin-portal/data /var/medin-portal/data  
  
# Set up a temporary directory not under union fs control  
VOLUME ["/tmp"]  
#RUN chmod a+rwxt /tmp # This doesn't seem to work  
RUN ln -s /tmp /var/medin-portal/tmp  
  
# Install the portal configuration file. This includes setting the  
# `local_port` variable.  
RUN mkdir /var/medin-portal/etc  
RUN sed -e 's/;local_port/local_port/g' /usr/src/medin-
portal/etc/portal.ini.example > /var/medin-portal/etc/portal.ini  

