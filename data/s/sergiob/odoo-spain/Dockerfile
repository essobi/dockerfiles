FROM debian:jessie  
MAINTAINER Sergio Bernal  
  
# Install some deps, lessc and less-plugin-clean-css, and wkhtmltopdf  
RUN set -x; \  
apt-get update \  
&& apt-get install -y --no-install-recommends \  
ca-certificates \  
curl \  
node-less \  
node-clean-css \  
python-gevent \  
python-pip \  
python-pyinotify \  
python-renderpm \  
python-support \  
git \  
graphviz \  
ghostscript \  
python-dateutil \  
python-feedparser \  
python-matplotlib \  
python-ofxparse \  
python-ldap \  
python-libxslt1 \  
python-lxml \  
python-mako \  
python-openid \  
python-psycopg2 \  
python-pybabel \  
python-pychart \  
python-pydot \  
python-pyparsing \  
python-reportlab \  
python-simplejson \  
python-tz \  
python-vatnumber \  
python-vobject \  
python-webdav \  
python-werkzeug \  
python-xlwt \  
python-yaml \  
python-imaging \  
gcc \  
python-dev \  
mc \  
bzr \  
python-setuptools \  
python-babel \  
libfreetype6 \  
python-feedparser \  
python-reportlab-accel \  
python-zsi \  
python-openssl \  
python-egenix-mxdatetime \  
python-jinja2 \  
python-unittest2 \  
python-mock \  
python-docutils \  
lptools \  
make \  
python-psutil \  
python-paramiko \  
poppler-utils \  
python-pdftools \  
python-scipy \  
python-decorator \  
python-requests \  
python-pypdf \  
antiword \  
postgresql \  
postgresql-client \  
libldb-dev \  
libldap2-dev \  
libxslt-dev \  
libxml2-dev \  
libfreetype6-dev \  
zlib1g-dev \  
libjpeg-dev \  
libpng12-dev \  
libpq-dev \  
&& curl -o wkhtmltox.deb -SL
http://nightly.odoo.com/extra/wkhtmltox-0.12.1.2_linux-jessie-amd64.deb \  
&& echo '40e8b906de658a2221b15e4e8cd82565a47d7ee8 wkhtmltox.deb' | sha1sum -c
- \  
&& dpkg --force-depends -i wkhtmltox.deb \  
&& apt-get -y install -f --no-install-recommends \  
&& apt-get purge -y --auto-remove -o
APT::AutoRemove::RecommendsImportant=false -o
APT::AutoRemove::SuggestsImportant=false npm \  
&& rm -rf /var/lib/apt/lists/* wkhtmltox.deb \  
&& pip install psycogreen==1.0  
  
  
# Install Odoo  
ENV ODOO_VERSION 8.0  
ENV ODOO_RELEASE 20170207  
RUN set -x; \  
curl -o odoo.deb -SL
http://nightly.odoo.com/${ODOO_VERSION}/nightly/deb/odoo_${ODOO_VERSION}.${ODOO_RELEASE}_all.deb
\  
&& echo 'cd8c1dc9d2ddf5a538381eed85871a2e343ec8ae odoo.deb' | sha1sum -c - \  
&& dpkg --force-depends -i odoo.deb \  
&& apt-get update \  
&& apt-get -y install -f --no-install-recommends \  
&& rm -rf /var/lib/apt/lists/* odoo.deb  
  
# Copy entrypoint script and Odoo configuration file  
COPY ./entrypoint.sh /  
COPY ./openerp-server.conf /etc/odoo/  
RUN chown odoo /etc/odoo/openerp-server.conf  
  
# Mount /var/lib/odoo to allow restoring filestore and /mnt/extra-addons for
users addons  
RUN mkdir -p /mnt/extra-addons \  
&& chown -R odoo /mnt/extra-addons  
VOLUME ["/var/lib/odoo", "/mnt/extra-addons"]  
  
# Expose Odoo services  
EXPOSE 8069 8071  
# Set the default config file  
ENV OPENERP_SERVER /etc/odoo/openerp-server.conf  
  
# Git clone repos  
RUN cd /mnt/extra-addons && git clone \  
https://github.com/OCA/l10n-spain.git -b 8.0 \  
https://github.com/OCA/reporting-engine.git -b 8.0 \  
https://github.com/OCA/account-financial-tools.git -b 8.0 \  
https://github.com/OCA/community-data-files.git -b 8.0 \  
https://github.com/OCA/server-tools.git -b 8.0 \  
https://github.com/OCA/connector.git -b 8.0 \  
https://github.com/OCA/bank-statement-import.git -b 8.0 \  
https://github.com/OCA/bank-payment.git -b 8.0 \  
https://github.com/OCA/pos -b 8.0 \  
https://github.com/OCA/partner-contact.git -b 8.0  
# Install pip requirements  
RUN find -name "requirements.txt" | xargs pip install -r  
  
# Set default user when running the container  
USER odoo  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["openerp-server"]  

