FROM debian:jessie  
MAINTAINER Odoo S.A. <info@odoo.com>  
  
# Install some deps, lessc and less-plugin-clean-css, and wkhtmltopdf  
RUN set -x; \  
apt-get update \  
&& apt-get install -y --no-install-recommends \  
ca-certificates \  
curl \  
sudo \  
git \  
ssh \  
node-less \  
node-clean-css \  
python-pyinotify \  
python-renderpm \  
python-support \  
python-coverage \  
python-pip \  
postgresql \  
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
ENV ODOO_VERSION 8.0  
ENV ODOO_RELEASE 20160923  
RUN set -x; \  
curl -o odoo.deb -SL
http://nightly.odoo.com/${ODOO_VERSION}/nightly/deb/odoo_${ODOO_VERSION}.${ODOO_RELEASE}_all.deb
\  
&& dpkg --force-depends -i odoo.deb \  
&& apt-get update \  
&& apt-get -y install -f --no-install-recommends \  
&& rm -rf /var/lib/apt/lists/* odoo.deb  
  
# Install aeroolib for Aeroo Reports  
RUN pip install git+https://github.com/aeroo/aeroolib.git@master  
  
# Install additional Python Packages  
RUN pip install gdata unidecode unirest ftputil xlrd  
  
# Copy entrypoint script and Odoo configuration file  
COPY ./entrypoint.sh /  
COPY ./openerp-server.conf /etc/odoo/  
COPY ./ci-start-psql.sh /  
COPY ./ci-init-env.sh /  
RUN chown odoo /etc/odoo/openerp-server.conf \  
&& chown odoo /usr/lib/python2.7/dist-packages/openerp  
  
# Mount /var/lib/odoo to allow restoring filestore and /mnt/extra-addons for
users addons  
RUN mkdir -p /mnt/extra-addons \  
&& chown -R odoo /mnt/extra-addons  
VOLUME ["/var/lib/odoo", "/mnt/extra-addons"]  
  
# Expose Odoo services  
EXPOSE 8069 8071 5432  
# Set the default config file  
ENV OPENERP_SERVER /etc/odoo/openerp-server.conf  
  
USER postgres  
RUN /etc/init.d/postgresql start &&\  
createuser -l -s odoo &&\  
createdb -E UTF8 -T template0 -O odoo odoo  
  
# Set default user when running the container  
USER root  
  
RUN echo 'odoo ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers  
RUN mkdir -p /opt/odoo/custom_addons &&\  
chown -R odoo.odoo /opt/odoo/custom_addons  
  
USER odoo  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["openerp-server"]  

