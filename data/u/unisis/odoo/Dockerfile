##################################################  
#  
# Dockerfile for Odoo  
#  
###################################################  
FROM unisis/base  
MAINTAINER Unisis <contacto@unisis.com.ar>  
  
# Expose ports:  
# - 22 is used by BarMan to copy Odoo files  
# - 8069 is used by Odoo (http)  
# - 8072 is used by Odoo (https, not used by us since https is provided by
NginX)  
EXPOSE 22 8069 8072  
# Volumes:  
# /opt/odoo: Odoo code (Git repository)  
# /mnt/addons: Odoo addons (Extra repos)  
# /mnt/eggs: PyCharm debug egg  
# /var/lib/odoo: Odoo filestore  
# /var/log/odoo: Odoo logs  
VOLUME ["/opt/odoo", "/mnt/addons", "/mnt/eggs", "/var/lib/odoo",
"/var/log/odoo"]  
  
# Install some deps, lessc and less-plugin-clean-css, and wkhtmltopdf  
# SSH server is installed because it's a BarMan requirement (even local)  
# rsync also needs be installed on both ends (barman and odoo)  
RUN set -x; \  
apt-get update \  
&& apt-get install -y --no-install-recommends \  
ca-certificates \  
node-less \  
node-clean-css \  
openssh-client \  
openssh-server \  
postgresql-client \  
python-pip \  
python-pyinotify \  
python-renderpm \  
python-support  
  
# Install wkhtmltopdf  
RUN apt-get -y install libfontenc1 libxfont1 xfonts-75dpi xfonts-base xfonts-
encodings xfonts-utils libfontconfig1 fontconfig libjpeg-turbo8 libx11-6
libxext6 libxrender1  
RUN wget
http://download.gna.org/wkhtmltopdf/0.12/0.12.2.1/wkhtmltox-0.12.2.1_linux-
trusty-amd64.deb  
RUN dpkg -i wkhtmltox-0.12.2.1_linux-trusty-amd64.deb  
RUN rm -rf wkhtmltox-0.12.2.1_linux-trusty-amd64.deb  
RUN cp /usr/local/bin/wkhtmltopdf /usr/bin/  
  
# Cleanup  
RUN apt-get -y install -f --no-install-recommends \  
&& apt-get purge -y --auto-remove -o
APT::AutoRemove::RecommendsImportant=false -o
APT::AutoRemove::SuggestsImportant=false npm \  
&& rm -rf /var/lib/apt/lists/* wkhtmltox.deb  
  
# Create odoo user  
RUN adduser --system --quiet --shell=/bin/bash --home=/var/lib/odoo --gecos
'ODOO' \--group odoo  
  
# Grant to Odoo user sudo power so -if we want debug- PyCharm can upload their
files via SSH  
# TO-DO: This could be a security vulnerability! Check!  
RUN echo "odoo ALL = NOPASSWD: ALL" >> /etc/sudoers  
  
# Install all Python modules  
RUN apt-get update  
RUN apt-get -y install \  
python-dateutil \  
python-feedparser \  
python-ldap \  
python-libxslt1 \  
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
python-zsi \  
python-docutils \  
python-psutil \  
python-mock \  
python-unittest2 \  
python-jinja2 \  
python-pypdf \  
python-decorator \  
python-requests \  
python-passlib \  
python-suds \  
python-openssl \  
python-pil  
  
# Generate locale (es_AR for right odoo es_AR language config, and C.UTF-8 for
postgres and general locale data)  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update -qq && apt-get install -y locales -qq  
RUN echo 'es_AR.UTF-8 UTF-8' >> /etc/locale.gen && locale-gen  
RUN echo 'es_US.UTF-8 UTF-8' >> /etc/locale.gen && locale-gen  
RUN echo 'C.UTF-8 UTF-8' >> /etc/locale.gen && locale-gen  
RUN dpkg-reconfigure locales && /usr/sbin/update-locale LANG=C.UTF-8  
ENV LANG C.UTF-8  
ENV LANGUAGE C.UTF-8  
ENV LC_ALL C.UTF-8  
# Workers and longpolling dependencies  
RUN apt-get install -y python-gevent  
RUN pip install psycogreen  
  
## Install pip dependencies for adhoc used odoo repositories  
# used by many pip packages  
RUN apt-get install -y python-dev  
  
# odoo-extra  
RUN apt-get install -y python-matplotlib font-manager  
  
# adhoc-website  
RUN pip install mercadopago  
  
# odoo argentina (nuevo modulo de FE)  
RUN apt-get install -y swig libffi-dev libssl-dev python-m2crypto python-
httplib2 mercurial libxml2-dev  
RUN pip install geopy==0.95.1 BeautifulSoup pyOpenSSL suds  
# para pyafipws  
RUN pip install -r
https://raw.githubusercontent.com/reingart/pyafipws/master/requirements.txt  
RUN pip install git+https://github.com/reingart/pyafipws@master  
RUN chmod 777 -R /usr/local/lib/python2.7/dist-packages/pyafipws/  
  
# odoo etl, infra and others  
RUN pip install openerp-client-lib fabric erppeek fabtools  
  
# oca reports  
RUN pip install xlwt  
  
# odoo kineses  
RUN pip install xlrd  
  
# oca partner contacts  
RUN pip install unicodecsv  
  
# aeroo direct print  
RUN apt-get install -y libcups2-dev libxslt-dev  
RUN easy_install lxml  
RUN pip install git+https://github.com/aeroo/aeroolib.git@master  
RUN pip install pycups==1.9.68  
  
# akretion/odoo-usability  
RUN pip install BeautifulSoup4  
  
# OCA knowledge  
RUN pip install python-magic  
  
# odoo support  
RUN pip install erppeek  
  
## Clean apt-get (copied from odoo)  
RUN apt-get purge -y --auto-remove -o
APT::AutoRemove::RecommendsImportant=false -o
APT::AutoRemove::SuggestsImportant=false  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Copy config files  
ENV CONF_REFRESHED_AT 2016_07_01  
ADD config/ssh_config /root/ssh_config  
ADD config/openerp-server.conf /root/openerp-server.conf  
  
# Copy Odoo setup script  
ADD scripts/odoo-setup /usr/sbin/odoo-setup  
RUN chmod +x /usr/sbin/odoo-setup  
  
# Copy Odoo service script  
ADD scripts/odoo-service /etc/init.d/odoo  
RUN chmod +x /etc/init.d/odoo  
  
# Copy Container start script  
ADD scripts/start.sh /root/start.sh  
RUN chmod +x /root/start.sh  
  
# Odoo Init script  
CMD ["/root/start.sh"]  

