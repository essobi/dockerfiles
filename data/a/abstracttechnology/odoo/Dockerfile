FROM abstracttechnology/webapp  
MAINTAINER Giacomo Spettoli <giacomo.spettoli@abstract.it>  
  
ENV ODOO_VERSION 8.0  
USER root  
  
# Install some deps, lessc and less-plugin-clean-css, and wkhtmltopdf  
RUN apt-key adv --keyserver ha.pool.sks-keyservers.net --recv-keys
B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8 && \  
echo 'deb http://apt.postgresql.org/pub/repos/apt/ jessie-pgdg main' $PG_MAJOR
> /etc/apt/sources.list.d/pgdg.list && \  
apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -y --no-install-recommends \  
ca-certificates curl node-less node-clean-css \  
python-pyinotify python-renderpm python-support \  
libxml2-dev libxslt1-dev libfreetype6-dev \  
libyaml-dev libevent-dev libldap2-dev libsasl2-dev libssl-dev \  
ttf-dejavu graphviz postgresql-client-9.5 ssh-client\  
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
  
# Clone Odoo Sources  
RUN git clone https://github.com/OCA/OCB.git -b ${ODOO_VERSION} \  
\--single-branch --depth 1 odoo && rm -rf odoo/.git  
  
# Odoo requirements  
RUN pip install -r odoo/requirements.txt  
  
# Odoo extra  
RUN pip install pyPdf unicodecsv erppeek pdbpp watchdog click  
  
# pgpass holds the credentials used to check if the postgres db is running  
COPY pgpass .pgpass  
RUN chmod 0600 .pgpass && \  
chown -R webapp:webapp .pgpass  
  
# Additional addon directory  
RUN /bin/bash -c "mkdir -p /srv/webapp/{data,etc,var}"  
ADD docker-entrypoint.sh /srv/webapp/docker-entrypoint.sh  
  
COPY scripts scripts  
  
COPY odoo.cfg.j2 odoo.cfg.j2  
COPY odoo_conf.yaml odoo_conf.yaml  
RUN python scripts/generate_odoo_conf.py --template='odoo.cfg.j2'
\--config='odoo_conf.yaml' > /srv/webapp/etc/odoo.cfg  
  
RUN chown webapp:webapp -R /srv/webapp && \  
chmod ugo+rX /srv/webapp  
  
USER webapp  
  
# Volumes and ports  
VOLUME ["/srv/webapp/var", "/srv/webapp/data"]  
EXPOSE 8069 8072  
# Set the default ENTRYPOINT and CMD  
ENTRYPOINT ["/srv/webapp/docker-entrypoint.sh"]  
CMD ["run"]  

