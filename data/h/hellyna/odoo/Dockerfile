FROM debian:jessie  
MAINTAINER Hellyna NG <hellyna@hellyna.com>  
  
# Install some deps, lessc and less-plugin-clean-css, and wkhtmltopdf  
RUN set -x; \  
apt-get update \  
&& apt-get install -y --no-install-recommends \  
ca-certificates \  
curl \  
node-less \  
node-clean-css \  
python-pyinotify \  
python-renderpm \  
python-support \  
&& curl -o wkhtmltox.deb -SL
http://nightly.odoo.com/extra/wkhtmltox-0.12.1.2_linux-jessie-amd64.deb \  
&& echo '40e8b906de658a2221b15e4e8cd82565a47d7ee8 wkhtmltox.deb' | sha1sum -c
- \  
&& dpkg --force-depends -i wkhtmltox.deb \  
&& apt-get -y install -f --no-install-recommends \  
&& apt-get purge -y --auto-remove -o
APT::AutoRemove::RecommendsImportant=false -o
APT::AutoRemove::SuggestsImportant=false npm \  
&& rm -rf /var/lib/apt/lists/* wkhtmltox.deb  
  
# Install Odoo  
ENV ODOO_VERSION 9.0  
ENV ODOO_RELEASE 20160301  
RUN set -x; \  
curl -o odoo.deb -SL
http://nightly.odoo.com/${ODOO_VERSION}/nightly/deb/odoo_${ODOO_VERSION}c.${ODOO_RELEASE}_all.deb
\  
&& dpkg --force-depends -i odoo.deb \  
&& apt-get update \  
&& apt-get -y install -f --no-install-recommends \  
&& rm -rf /var/lib/apt/lists/* odoo.deb  
  
# Copy Odoo configuration file and entrypoint  
COPY ./openerp-server.conf /etc/odoo/  
COPY ./entrypoint.py /  
  
# Mkdir and define volumes, as well as fix permissions.  
RUN mkdir -p /mnt/extra-addons \  
&& chown -R odoo /mnt/extra-addons \  
&& chmod 0755 /entrypoint.py  
VOLUME ["/var/lib/odoo", "/mnt/extra-addons"]  
  
# Set the default config file  
ENV OPENERP_SERVER /etc/odoo/openerp-server.conf  
  
# Set default user when running the container  
USER odoo  
  
ENTRYPOINT ["/entrypoint.py"]  

