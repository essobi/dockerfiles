FROM debian:stretch  
LABEL maintainer="e-COSI <odoo@e-cosi.com>"  
  
# db_filter is added to odoo.conf  
ARG ODOO_DB_FILTER=^%d_*  
# Image is built from Odoo branch given by VERSION AND WITH EXACT COMMIT HASH  
# IMPORTANT! This script contains extra libraries that are specifically needed
for Odoo 10.0  
ARG ODOO_VERSION=11.0  
ARG ODOO_COMMIT_HASH  
# VERSION_DATE is used as meta info in version.txt file generated at /odoo  
# and to limit cloning depth via shallow-since  
# VERSION_DATE must be equal to commit selected date  
ARG VERSION_DATE  
# Odoo need specific extra version for wkhtmltopdf provided by Odoo from
nightly builds server  
ARG
WKHTMLTOPDF_SRC=https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.4/wkhtmltox-0.12.4_linux-
generic-amd64.tar.xz  
ARG WKHTMLTOPDF_SHA=3f923f425d345940089e44c1466f6408b9619562  
# PostgreSQL Version used for bakcup/restore operations  
ARG POSTGRES_VERSION=9.6  
# Choosing default conf file, eg. to create dev container  
ARG DEFAULT_CONF_FILE=odoo_default.conf  
  
ENV ODOO_VERSION=${ODOO_VERSION}  
ENV LC_ALL=C.UTF-8  
ENV LANG=C.UTF-8  
ENV DEBIAN_FRONTEND=noninteractive  
  
#--------------------------------------------------  
# Install Dependencies  
#--------------------------------------------------  
# Install some deps, lessc and less-plugin-clean-css, wkhtmltopdf  
# and pgclient  
RUN set -x; \  
apt-get update \  
&& apt-get install -y apt-utils wget gnupg \  
#&& echo 'deb http://apt.postgresql.org/pub/repos/apt/ xenial-pgdg main' >>
/etc/apt/sources.list.d/pgdg.list  
&& echo "deb http://apt.postgresql.org/pub/repos/apt/ stretch-pgdg main" >>
/etc/apt/sources.list.d/pgdg.list \  
&& wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-
key add -  
  
RUN set -x; apt-get update \  
&& apt-get install -y --no-install-recommends --allow-unauthenticated \  
# Utils  
curl \  
git \  
vim \  
gcc \  
xz-utils \  
# Python 3 env  
python3 \  
python3-pip \  
python3-setuptools \  
python3-wheel \  
python3-dev \  
# Dev stuff for building python requirements  
cython \  
zlib1g-dev \  
libxml2-dev \  
libxslt-dev \  
libsasl2-dev \  
libldap2-dev \  
libssl1.0-dev \  
# PostgreSQL client (for DB backup/restore)  
postgresql-client-${POSTGRES_VERSION} \  
# Requierd from Odoo Deb package  
#node-clean-css \  
adduser \  
lsb-base \  
node-less \  
postgresql-client \  
python-vobject \  
python3-babel \  
python3-dateutil \  
python3-decorator \  
python3-docutils \  
python3-feedparser \  
python3-html2text \  
python3-pil \  
python3-jinja2 \  
python3-lxml \  
python3-mako \  
python3-mock \  
python3-openid \  
python3-passlib \  
python3-psutil \  
python3-psycopg2 \  
python3-pydot \  
python3-pyparsing \  
python3-pypdf2 \  
python3-reportlab \  
python3-requests \  
python3-renderpm \  
python3-suds \  
python3-tz \  
python3-vatnumber \  
python3-werkzeug \  
python3-xlsxwriter \  
python3-yaml \  
# Recommanded from Odoo Deb Package  
python-gevent \  
&& pip3 install --upgrade pip  
  
RUN set -x; \  
curl -o wkhtmltox.tar.xz -SL ${WKHTMLTOPDF_SRC} \  
&& echo "${WKHTMLTOPDF_SHA} wkhtmltox.tar.xz" | sha1sum -c - \  
&& tar xvf wkhtmltox.tar.xz \  
&& cp wkhtmltox/lib/* /usr/local/lib/ \  
&& cp wkhtmltox/bin/* /usr/local/bin/ \  
&& cp -r wkhtmltox/share/man/man1 /usr/local/share/man/ \  
&& rm -rf wkhtmltox  
  
#--------------------------------------------------  
# Prepare Env  
#--------------------------------------------------  
# Create Odoo system user  
RUN set -x; \  
adduser --system --home /odoo --quiet --group odoo \  
# Log  
&& mkdir -p /var/log/odoo \  
&& chown odoo:odoo /var/log/odoo \  
&& chmod 0750 /var/log/odoo \  
# Data dir  
&& mkdir -p /var/lib/odoo \  
&& chown odoo:odoo /var/lib/odoo \  
&& chmod 0750 /var/lib/odoo  
  
#--------------------------------------------------  
# Install ODOO  
#--------------------------------------------------  
# Clone git repo, using commit hash if given  
RUN set -x; \  
if [ ${ODOO_COMMIT_HASH} ]; \  
then git clone \--shallow-since=${VERSION_DATE} \--branch ${ODOO_VERSION}
https://github.com/odoo/odoo.git /odoo/odoo-server; \  
else git clone \--depth 1 --branch ${ODOO_VERSION}
https://github.com/odoo/odoo.git /odoo/odoo-server; \  
fi; \  
cd /odoo/odoo-server \  
if [ ${ODOO_COMMIT_HASH} ]; then git reset --hard ${ODOO_COMMIT_HASH}; fi \  
rm -rf /odoo/odoo-server/.git  
  
RUN pip3 install -r /odoo/odoo-server/requirements.txt  
  
# Install extra stuff  
RUN pip3 install wdb pudb watchdog newrelic  
  
# Cleaning image  
RUN set -x; \  
apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false
-o APT::AutoRemove::SuggestsImportant=false \  
&& rm -rf /var/lib/apt/lists/*  
  
# Writing metainfo file  
RUN echo "Version : ${ODOO_VERSION}\n" > /odoo/version.txt \  
&& echo "Date from : ${VERSION_DATE}\n" >> /odoo/version.txt \  
&& echo "Commit : ${ODOO_COMMIT_HASH}\n" >> /odoo/version.txt \  
&& echo "Built on :" >> /odoo/version.txt \  
&& date +"%Y-%m-%d" >> /odoo/version.txt && echo "\n"  
  
#echo -e "\n---- Setting permissions on home folder ----"  
RUN chown -R odoo:odoo /odoo/* \  
# Odoo configuration file  
&& mkdir -p /etc/odoo  
  
COPY ./${DEFAULT_CONF_FILE} /etc/odoo/odoo.conf  
  
RUN chown odoo /etc/odoo/odoo.conf \  
&& chmod 0640 /etc/odoo/odoo.conf \  
&& echo "dbfilter=${DB_FILTER}" >> /etc/odoo/odoo.conf  
  
# Copy entrypoint script  
COPY ./entrypoint.sh /odoo/  
RUN chmod +x /odoo/entrypoint.sh  
  
# Mount /var/lib/odoo to allow restoring filestore  
# and /mnt/extra-addons for users addons  
RUN set -x; \  
mkdir -p /mnt/extra-addons/{oca,community,commercial,specific} \  
&& chown -R odoo /mnt/extra-addons \  
&& mkdir -p /var/lib/odoo \  
&& chown -R odoo /var/lib/odoo \  
&& mkdir -p /var/log/odoo \  
&& chown -R odoo /var/log/odoo  
  
VOLUME ["/var/lib/odoo", "/mnt/extra-addons", "/var/log/odoo", "/etc/odoo"]  
  
# Expose Odoo services  
EXPOSE 8069 8071  
# Set the default config file  
ENV ODOO_RC /etc/odoo/odoo.conf  
  
# Set default user when running the container  
USER odoo  
  
ENTRYPOINT ["/odoo/entrypoint.sh"]  
  
CMD ["/odoo/odoo-server/odoo-bin", "-c", "/etc/odoo/odoo.conf"]  

