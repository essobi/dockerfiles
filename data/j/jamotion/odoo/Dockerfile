FROM ubuntu:xenial  
MAINTAINER Renzo Meister <rm@jamotion.ch>  
  
# Install some deps, lessc and less-plugin-clean-css, and wkhtmltopdf  
RUN apt-get update  
RUN apt-get install -y --no-install-recommends \  
ca-certificates curl nodejs npm software-properties-common dh-python python-
pyinotify python-pip wget git vim \  
&& npm install -g less less-plugin-clean-css \  
&& ln -s /usr/bin/nodejs /usr/bin/node \  
&& curl -o wkhtmltox.deb -SL
http://download.gna.org/wkhtmltopdf/0.12/0.12.1/wkhtmltox-0.12.1_linux-trusty-
amd64.deb \  
&& echo '7dd0e9be7e4fa2a58aa7066460927cdb8ba07492 wkhtmltox.deb' | sha1sum -c
- \  
&& dpkg --force-depends -i wkhtmltox.deb \  
&& apt-get -y install -f --no-install-recommends \  
&& apt-get purge -y --auto-remove -o
APT::AutoRemove::RecommendsImportant=false -o
APT::AutoRemove::SuggestsImportant=false npm \  
&& rm -rf /var/lib/apt/lists/* wkhtmltox.deb  
  
# Add PostgreSQL 9.6 source  
RUN add-apt-repository "deb http://apt.postgresql.org/pub/repos/apt/ xenial-
pgdg main" \  
&& wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-
key add - \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends postgresql-client-9.6  
  
# We set the odoo user and group fixed for compatibility with hosts  
RUN addgroup --gid=5000 odoo && adduser --system --uid=5000 --gid=5000 --home
/var/lib/odoo --shell /bin/bash odoo  
  
# Install Odoo  
ENV ODOO_VERSION 8.0  
ENV ODOO_RELEASE 20170201  
RUN set -x; \  
curl -o odoo.deb -SL
http://nightly.odoo.com/${ODOO_VERSION}/nightly/deb/odoo_${ODOO_VERSION}.${ODOO_RELEASE}_all.deb
\  
&& dpkg --force-depends -i odoo.deb \  
&& apt-get -y install -f --no-install-recommends \  
&& rm -rf /var/lib/apt/lists/* odoo.deb  
  
# Install gevent dependencies for running odoo with workers  
RUN apt-get update  
RUN apt-get install -y libevent-dev python-all-dev python-setuptools \  
python-gevent python-psycopg2 python-psycogreen python-webdav \  
&& pip install --upgrade pip \  
&& pip install gdata unidecode unirest ftputil xlrd docker-py phonenumbers  
  
# Install aeroolib for Aeroo Reports  
RUN pip install git+https://github.com/aeroo/aeroolib.git@master  
  
VOLUME ["/opt/odoo/data", "/usr/local/share/fonts", "/etc/odoo",
"/var/log/odoo"]  
  
# Expose Odoo services  
EXPOSE 8069 8071 8072  
# Set the default config file  
ENV OPENERP_SERVER /etc/odoo/odoo-server.conf  
  
USER odoo  
  
ENTRYPOINT ["/usr/bin/odoo.py"]  

