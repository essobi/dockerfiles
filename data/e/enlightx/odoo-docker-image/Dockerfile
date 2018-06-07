FROM debian:stretch  
MAINTAINER Davide Corio <me@davidecorio.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN \  
apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y build-essential \  
git vim libpq-dev zlib1g-dev \  
libgif-dev libjpeg-dev libtiff-dev \  
python-dev python-pip python-virtualenv && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Add odoo user  
RUN \  
useradd -u 1000 --home-dir=/opt/odoo --shell=/usr/sbin/nologin odoo && \  
mkdir /opt/odoo  
  
WORKDIR /opt/odoo  
  
RUN chown odoo:odoo /opt/odoo && \  
chmod ugo+rX /opt/odoo  
  
ENV ODOO_VERSION 10.0  
USER root  
  
# Install some deps, lessc and less-plugin-clean-css, and wkhtmltopdf  
RUN apt-key adv --keyserver ha.pool.sks-keyservers.net --recv-keys
B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8 && \  
echo 'deb http://apt.postgresql.org/pub/repos/apt/ stretch-pgdg main'
$PG_MAJOR > /etc/apt/sources.list.d/pgdg.list && \  
apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -y --no-install-recommends \  
ca-certificates curl \  
python-pyinotify python-renderpm \  
libxml2-dev libxslt1-dev libfreetype6-dev \  
libyaml-dev libevent-dev libldap2-dev libsasl2-dev libssl-dev \  
ttf-dejavu graphviz postgresql-client-9.6 ssh-client  
  
RUN curl -o wkhtmltox-0.12.4_linux-generic-amd64.tar.xz -SL
https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.4/wkhtmltox-0.12.4_linux-
generic-amd64.tar.xz \  
&& echo '3f923f425d345940089e44c1466f6408b9619562 *wkhtmltox-0.12.4_linux-
generic-amd64.tar.xz' | sha1sum -c - \  
&& tar xvf wkhtmltox-0.12.4_linux-generic-amd64.tar.xz
wkhtmltox/bin/wkhtmltopdf \  
&& cp wkhtmltox/bin/wkhtmltopdf /usr/local/bin/ \  
&& rm -rf wkhtmltox  
RUN curl -o setup_8.x -sL https://deb.nodesource.com/setup_8.x \  
&& chmod +x setup_8.x \  
&& ./setup_8.x \  
&& rm setup_8.x \  
&& apt-get install -y nodejs \  
&& npm install npm@latest -g \  
&& npm install less -g \  
&& npm install -g less-plugin-clean-css  
  
RUN apt-get -y install -f --no-install-recommends \  
&& apt-get purge -y --auto-remove -o
APT::AutoRemove::RecommendsImportant=false -o
APT::AutoRemove::SuggestsImportant=false npm  
  
# Clone Odoo Sources  
RUN git clone https://github.com/odoo/odoo.git -b ${ODOO_VERSION} \  
\--single-branch --depth 1 odoo && rm -rf odoo/.git  
  
# Setuptools Upgrade  
RUN pip install --upgrade setuptools pip wheel virtualenv  
  
# Odoo requirements  
RUN pip install -r odoo/requirements.txt  
  
# Odoo extra  
RUN pip install pyPdf unicodecsv odoorpc pdbpp watchdog click 'ipython<6.0'
pip  
  
# pgpass holds the credentials used to check if the postgres db is running  
COPY pgpass .pgpass  
RUN chmod 0600 .pgpass && \  
chown -R odoo:odoo .pgpass  
  
# Additional addon directory  
RUN /bin/bash -c "mkdir -p /opt/odoo/{data,etc,var}"  
ADD docker-entrypoint.sh /opt/odoo/docker-entrypoint.sh  
  
COPY scripts scripts  
  
COPY odoo.cfg.j2 odoo.cfg.j2  
COPY odoo_conf.yaml odoo_conf.yaml  
RUN python scripts/generate_odoo_conf.py --template='odoo.cfg.j2'
\--config='odoo_conf.yaml' > /opt/odoo/etc/odoo.cfg  
  
RUN chown odoo:odoo -R /opt/odoo && \  
chmod ugo+rX /opt/odoo  
  
USER odoo  
  
# Volumes and ports  
VOLUME ["/opt/odoo/var", "/opt/odoo/data"]  
EXPOSE 8069 8072  
# Set the default ENTRYPOINT and CMD  
ENTRYPOINT ["/opt/odoo/docker-entrypoint.sh"]  
CMD ["run"]  

