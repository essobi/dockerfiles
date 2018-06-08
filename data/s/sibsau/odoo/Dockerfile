FROM debian:jessie  
MAINTAINER Anton Goroshkin <neobht@sibsau.ru>  
  
# Install some deps, lessc and less-plugin-clean-css, and wkhtmltopdf  
RUN set -x; \  
apt-get update \  
&& apt-get install -y --no-install-recommends \  
ca-certificates \  
curl \  
node-less \  
python-gevent \  
python-pip \  
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
&& rm -rf /var/lib/apt/lists/* wkhtmltox.deb \  
&& pip install psycogreen==1.0  
  
# Install Odoo  
ENV ODOO_VERSION 9.0  
ENV ODOO_RELEASE 20180604  
RUN set -x; \  
curl -o odoo.deb -SL
http://nightly.odoo.com/${ODOO_VERSION}/nightly/deb/odoo_${ODOO_VERSION}c.${ODOO_RELEASE}_all.deb
\  
&& echo 'aa91ce673832401a6305e6840673cc235fa5d0c7 odoo.deb' | sha1sum -c - \  
&& dpkg --force-depends -i odoo.deb \  
&& apt-get update \  
&& apt-get -y install -f --no-install-recommends \  
&& rm -rf /var/lib/apt/lists/* odoo.deb  
  
# Install Aeroo Reports support  
#RUN pip install git+https://github.com/aeroo/aeroolib.git@master  
ADD ./python-aeroolib_1.0_all.deb /  
RUN set -x; \  
apt-get update \  
&& dpkg --force-depends -i python-aeroolib_1.0_all.deb \  
&& apt-get -y install -f --no-install-recommends \  
&& apt-get purge -y --auto-remove -o
APT::AutoRemove::RecommendsImportant=false -o
APT::AutoRemove::SuggestsImportant=false npm \  
&& rm -rf /var/lib/apt/lists/* python-aeroolib_1.0_all.deb  
  
# Install some Python modules  
RUN set -x; \  
apt-get update \  
&& apt-get install -y --no-install-recommends \  
python-pip \  
python-numpy \  
python-qrcode \  
&& rm -rf /var/lib/apt/lists/* \  
&& pip install \  
bs4 PyPDF2 transliterate xlrd xlwt odfpy SQLAlchemy config openpyxl caldav
configs  
  
# Install Postgres to support pg_dump  
RUN set -ex; \  
# pub 4096R/ACCC4CF8 2011-10-13 [expires: 2019-07-02]  
# Key fingerprint = B97B 0AFC AA1A 47F0 44F2 44A0 7FCC 7D46 ACCC 4CF8  
# uid PostgreSQL Debian Repository  
key='B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8'; \  
export GNUPGHOME="$(mktemp -d)"; \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \  
gpg --export "$key" > /etc/apt/trusted.gpg.d/postgres.gpg; \  
rm -r "$GNUPGHOME"; \  
apt-key list  
  
ENV PG_MAJOR 9.6  
ENV PG_VERSION 9.6.9-2.pgdg80+1  
RUN echo 'deb http://apt.postgresql.org/pub/repos/apt/ jessie-pgdg main'
$PG_MAJOR > /etc/apt/sources.list.d/pgdg.list  
  
RUN apt-get update \  
&& apt-get install -y postgresql-common \  
&& sed -ri 's/#(create_main_cluster) .*$/\1 = false/' /etc/postgresql-
common/createcluster.conf \  
&& apt-get install -y \  
postgresql-$PG_MAJOR=$PG_VERSION \  
postgresql-contrib-$PG_MAJOR=$PG_VERSION \  
rlwrap pg-activity \  
&& rm -rf /var/lib/apt/lists/*  
  
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
  
# Set default user when running the container  
USER odoo  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["openerp-server"]  

