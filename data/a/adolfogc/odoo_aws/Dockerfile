FROM ubuntu:16.04  
  
ENV LANG=en_US \  
LANGUAGE=en_US:en \  
LC_COLLATE=C \  
LC_CTYPE=en_US.UTF-8  
  
RUN set -x \  
&& apt-get update --fix-missing \  
&& apt-get install -y --no-install-recommends \  
ca-certificates \  
curl \  
postgresql-client \  
openssl \  
nfs-common \  
python-setuptools \  
python-zsi \  
python-ldap \  
python-pychart \  
python-libxslt1 \  
python-pyparsing \  
&& easy_install pip \  
&& pip install babel \  
python-dateutil==1.5 \  
vobject==0.8.2 \  
feedparser \  
gdata \  
lxml \  
mako \  
psycopg2 \  
pydot \  
python-openid \  
pytz \  
pywebdav \  
pyyaml \  
reportlab \  
simplejson \  
vatnumber \  
werkzeug \  
xlwt \  
pyopenssl \  
dumb-init \  
&& curl -o openerp.tar.gz -SL
https://nightly.odoo.com/old/openerp-6.1/6.1.0/openerp_6.1-1-1.tar.gz \  
&& echo '3c9b8f44d3f2228dc9c1892620478263bf632b47cba1aeeef6985f49efe5c717
openerp.tar.gz' | sha256sum -c - \  
&& tar -xf openerp.tar.gz \  
&& cd openerp-6.1-1 \  
&& python setup.py install \  
&& cd .. \  
&& curl -o dockerize.tar.gz -SL
https://github.com/jwilder/dockerize/releases/download/v0.6.1/dockerize-linux-
amd64-v0.6.1.tar.gz \  
&& echo '1fa29cd41a5854fd5423e242f3ea9737a50a8c3bcf852c9e62b9eb02c6ccd370
dockerize.tar.gz' | sha256sum -c - \  
&& tar -C /usr/local/bin -xf dockerize.tar.gz \  
&& chmod u+x /usr/local/bin/dockerize \  
&& rm -rf /var/lib/apt/lists/* openerp.tar.gz openerp-6.1-1 dockerize.tar.gz  
  
COPY ./entrypoint.sh /entrypoint.sh  
COPY ./openerp.conf.tmpl /etc/openerp/openerp.conf.tmpl  
  
RUN set -x \  
&& adduser --system --home=/opt/openerp --group openerp \  
&& chmod u+x /entrypoint.sh \  
&& chown openerp:openerp /entrypoint.sh \  
&& chown -R openerp:openerp /etc/openerp \  
&& mkdir -p /mnt/extra-addons \  
&& chown -R openerp:openerp /mnt/extra-addons \  
&& mkdir -p /mnt/filestore \  
&& chown -R openerp:openerp /mnt/filestore  
  
VOLUME ["/mnt/extra-addons"]  
EXPOSE 8069 8070  
USER openerp  
  
ENTRYPOINT ["dumb-init", "--"]  
CMD ["/entrypoint.sh", "openerp-server"]  

