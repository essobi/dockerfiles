FROM ubuntu:14.04  
  
RUN apt-get update && \  
apt-get -yq install \  
adduser \  
postgresql-client-9.3 \  
python \  
python-dateutil \  
python-decorator \  
python-docutils \  
python-feedparser \  
python-imaging \  
python-jinja2 \  
python-ldap \  
python-libxslt1 \  
python-lxml \  
python-mako \  
python-mock \  
python-openid \  
python-passlib \  
python-psutil \  
python-psycopg2 \  
python-pybabel \  
python-pychart \  
python-pydot \  
python-pyparsing \  
python-pypdf \  
python-reportlab \  
python-requests \  
python-simplejson \  
python-tz \  
python-unittest2 \  
python-vatnumber \  
python-vobject \  
python-werkzeug \  
python-xlwt \  
python-yaml && \  
apt-get clean && rm -rf /var/lib/apt/lists/*  
  
RUN mkdir -p /var/log/odoo && mkdir -p /opt/odoo/custom_addons && mkdir -p
/opt/odoo/data  
  
ADD ./odoo_8.0.20141205.tar.gz /opt/odoo  
ADD ./odoo_server.conf /etc/odoo/odoo_server.conf  
ADD ./docker-entrypoint.sh /docker-entrypoint.sh  
RUN chmod +x /docker-entrypoint.sh  
ADD ./wkhtmltox-0.12.1_linux-trusty-amd64.deb /tmp/wkhtmltox-0.12.1_linux-
trusty-amd64.deb  
  
RUN dpkg -i /tmp/wkhtmltox-0.12.1_linux-trusty-amd64.deb  
  
RUN adduser --system \--quiet --group odoo  
RUN chown -R odoo:odoo /etc/odoo && chown -R odoo:odoo /var/log/odoo && chown
-R odoo:odoo /opt/odoo  
  
VOLUME /opt/odoo/data  
  
USER odoo  
  
EXPOSE 8069  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["/usr/bin/python", "/opt/odoo/odoo-8.0-55fa508/openerp-server", "-c",
"/etc/odoo/odoo_server.conf", "--logfile=/var/log/odoo/odoo_server.log"]

