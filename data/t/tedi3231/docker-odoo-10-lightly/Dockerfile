FROM debian:jessie  
MAINTAINER Odoo S.A. <info@odoo.com>  
  
# Install some deps, lessc and less-plugin-clean-css, and wkhtmltopdf  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
ca-certificates \  
curl \  
unzip \  
node-less \  
python-gevent \  
python-pip \  
python-renderpm \  
python-support \  
python-watchdog \  
&& apt-get install -y --no-install-recommends build-essential libsasl2-dev
libldap2-dev libssl-dev libffi-dev python-dev \  
&& pip install psycogreen==1.0 \  
&& pip install -U pip \  
&& pip install psycogreen==1.0 \  
&& pip install cryptography \  
&& pip install wechatpy \  
&& pip install redis \  
&& pip install rabbitmq \  
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
RUN curl -o odoo.zip -SL
https://github.com/tedi3231/odoo_lightly/archive/master.zip \  
&& unzip -q odoo.zip  
  
RUN pip install wdb odoo_lightly-master/ \  
&& rm -rf odoo.zip  
# && rm -rf odoo_lightly-master  
# Copy entrypoint script and Odoo configuration file  
COPY ./entrypoint.sh /  
COPY ./odoo.conf /etc/odoo/  
  
RUN useradd -m -d /var/lib/odoo -s /bin/false -u 104 -g www-data odoo  
RUN mkdir -p /var/odoo \  
&& chown -R odoo:www-data /var/odoo \  
&& mv odoo_lightly-master/addons /var/odoo/ \  
&& chown -R odoo:www-data /var/odoo \  
&& chmod 0750 /var/odoo \  
&& rm -rf odoo_lightly-master  
  
RUN chown odoo:www-data /etc/odoo/odoo.conf \  
&& chown 0640 /etc/odoo/odoo.conf  
  
# Mount /var/lib/odoo to allow restoring filestore and /mnt/extra-addons for
users addons  
RUN mkdir -p /mnt/extra-addons \  
&& chown -R odoo:www-data /mnt/extra-addons  
VOLUME ["/var/lib/odoo", "/mnt/extra-addons"]  
  
# Expose Odoo services  
EXPOSE 8069 8071  
# Set the default config file  
ENV ODOO_RC /etc/odoo/odoo.conf  
  
# Set default user when running the container  
USER odoo  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["odoo"]  

