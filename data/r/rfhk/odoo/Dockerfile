FROM ubuntu:16.04  
MAINTAINER Quartile Limited <info@quartile.co>  
  
# Update source repository  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys
B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8 \  
&& echo "deb http://apt.postgresql.org/pub/repos/apt/ xenial-pgdg main" >
/etc/apt/sources.list.d/pgdg.list \  
&& apt-get update  
  
# Install dependencies and tools  
RUN set -x; \  
apt-get install -yq --no-install-recommends \  
curl \  
python3-pip \  
# Libraries needed to install the pip modules (libpq-dev for pg_config >
psycopg2)  
python3-dev \  
# to install portable C which is a distant dependency for pysftp  
libffi-dev \  
libxml2-dev \  
libxslt1-dev \  
libldap2-dev \  
libsasl2-dev \  
libssl-dev \  
python3-setuptools \  
build-essential \  
# For database management  
postgresql-client-9.6 \  
# GeoIP related  
geoip-database-contrib \  
libgeoip-dev \  
# For getting Odoo code  
git  
  
# Install Odoo Python dependencies.  
ADD requirements.txt /opt/requirements.txt  
RUN python3 -m pip install --upgrade pip \  
&& pip3 install -r /opt/requirements.txt  
  
# Install LESS  
RUN set -x; \  
apt-get install -y --no-install-recommends \  
node-less  
  
# Install wkhtmltox 0.12.1  
ADD https://downloads.wkhtmltopdf.org/0.12/0.12.1/wkhtmltox-0.12.1_linux-
trusty-amd64.deb /opt/sources/wkhtmltox.deb  
RUN set -x; \  
apt-get install -y --no-install-recommends \  
fontconfig \  
libx11-6 \  
libxext6 \  
libxrender1 \  
libjpeg-dev \  
&& dpkg -i /opt/sources/wkhtmltox.deb \  
&& rm -rf /opt/sources/wkhtmltox.deb  
  
# Add odoo user (apply the same in the host machine for compatibility)  
RUN addgroup --gid=300 odoo && adduser --system --uid=300 --gid=300 --home
/odoo --shell /bin/bash odoo  
  
# Add boot script  
COPY ./odooboot /  
RUN chmod +x /odooboot  
  
USER odoo  
  
# Create directories  
RUN bin/bash -c "mkdir /odoo/{custom,data,etc,log}"  
COPY ./odoo.conf /odoo/etc/  
  
# Get Odoo code  
WORKDIR /odoo  
RUN set -x; \  
git clone \--depth 1 https://github.com/odoo/odoo.git -b 11.0 \  
&& rm -rf odoo/.git  
  
USER 0  
# Install Supervisord.  
# For some reason the boot script does not work (container exits...) when it
is directly set to entrypoint.  
RUN apt-get install -y supervisor  
COPY ./supervisord.conf /etc/supervisor/conf.d/  
  
VOLUME ["/odoo/custom", "/odoo/data", "/odoo/etc", "/odoo/log",
"/usr/share/fonts"]  
  
EXPOSE 8069 8072  
ENTRYPOINT ["/usr/bin/supervisord"]  

