FROM ubuntu:trusty  
MAINTAINER Renzo Meister <rm@jamotion.ch>  
  
# Install some deps, lessc and less-plugin-clean-css, and wkhtmltopdf  
RUN apt-get update  
RUN apt-get install -y --no-install-recommends \  
ca-certificates curl nodejs npm python-support python-pyinotify python-pip
wget git \  
&& npm install -g less less-plugin-clean-css \  
&& ln -s /usr/bin/nodejs /usr/bin/node \  
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
  
# Add PostgreSQL 9.4 source  
RUN apt-get install -y --no-install-recommends wget && sh -c 'echo "deb
http://apt.postgresql.org/pub/repos/apt/ $(lsb_release -cs)-pgdg main" >
/etc/apt/sources.list.d/pgdg.list' \  
&& wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo
apt-key add - \  
&& apt-get update  
  
# We set the odoo user and group fixed for compatibility with hosts  
RUN addgroup --gid=5000 odoo && adduser --system --uid=5000 --gid=5000 --home
/var/lib/odoo --shell /bin/bash odoo  
  
# Install Odoo  
ENV ODOO_VERSION 8.0  
ENV ODOO_RELEASE 20151111  
RUN set -x; \  
curl -o odoo.deb -SL
http://nightly.odoo.com/${ODOO_VERSION}/nightly/deb/odoo_${ODOO_VERSION}.${ODOO_RELEASE}_all.deb
\  
&& dpkg --force-depends -i odoo.deb \  
&& apt-get -y install -f --no-install-recommends \  
&& rm -rf /var/lib/apt/lists/* odoo.deb  
  
# Install gevent dependencies for running odoo with workers  
RUN apt-get update  
RUN apt-get install -y libevent-dev python-all-dev python-gevent python-
psycopg2  
RUN wget
https://pypi.python.org/packages/source/p/psycogreen/psycogreen-1.0.tar.gz \  
&& tar xvvf psycogreen-1.0.tar.gz \  
&& cd psycogreen-1.0 \  
&& python setup.py install \  
&& easy_install greenlet \  
&& easy_install gevent-psycopg2 \  
&& pip install gdata \  
&& cd .. \  
&& rm -rf psycogreen-1.0*  
  
# Install aeroolib for Aeroo Reports  
RUN pip install git+https://github.com/aeroo/aeroolib.git@master  
  
RUN chown -R odoo.odoo /usr/lib/python2.7/dist-packages/openerp  
  
# Install and configure OpenSSH Server (for development mode only)  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get -y install
openssh-server pwgen  
RUN mkdir -p /var/run/sshd \  
&& sed -i "s/UsePrivilegeSeparation.*/UsePrivilegeSeparation no/g"
/etc/ssh/sshd_config \  
&& sed -i "s/UsePAM.*/UsePAM no/g" /etc/ssh/sshd_config \  
&& sed -i "s/PermitRootLogin.*/PermitRootLogin yes/g" /etc/ssh/sshd_config  
  
# Install Docker-Py  
RUN pip install docker-py  
RUN addgroup --gid=999 docker && adduser odoo docker  
  
ENV AUTHORIZED_KEYS **None**  
VOLUME ["/opt/odoo/custom_addons", "/opt/odoo/data", "/usr/local/share/fonts",
"/etc/odoo", "/var/log/odoo", "/opt/odoo/bin", "/var/run/docker.sock",
"/opt/servman"]  
  
# Expose Odoo services  
EXPOSE 2022 8069 8071 8072  
# Set the default config file  
ENV OPENERP_SERVER /etc/odoo/odoo-server.conf  
  
ENTRYPOINT ["/opt/odoo/bin/run.sh"]  

