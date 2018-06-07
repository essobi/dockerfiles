# Thx to Equitania Software GmbH <info@myodoo.de> for publishing this file  
# we adjusted it for our environmant and usage  
FROM datenbetrieb/debian:jessie  
MAINTAINER datenbetrieb technologie UGh <info@datenbetrieb.de>  
# Version 1.0.2  
# Date 14.03.2016  
  
CMD "echo" "Building box for odoo now.."  
# Install basics  
RUN set -x; \  
apt-get update \  
&& apt-get install -y --no-install-recommends \  
ca-certificates \  
ghostscript \  
graphviz \  
antiword \  
poppler-utils \  
curl \  
postgresql-client-9.4 \  
build-essential \  
libfreetype6-dev \  
libjpeg-dev \  
wget \  
unzip \  
sqlite3 \  
nano \  
mc \  
geoip-bin \  
geoip-database \  
sudo \  
node-less \  
node-clean-css  
  
# Python packages..  
RUN set -x; \  
apt-get install -y --no-install-recommends \  
python-pip \  
python-magic \  
python-dateutil \  
python-pypdf \  
python-requests \  
python-feedparser \  
python-gdata \  
python-ldap \  
python-libxslt1 \  
python-lxml \  
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
python-unittest2 \  
python-mock \  
python-jinja2 \  
python-dev \  
python-pdftools \  
python-decorator \  
python-openssl \  
python-babel \  
python-imaging \  
python-reportlab-accel \  
python-paramiko \  
python-software-properties \  
python-matplotlib \  
python-support \  
python-passlib \  
python-pyinotify \  
python-gevent \  
python-renderpm  
  
# Pip install..  
RUN set -x; \  
pip install passlib \  
&& pip install beautifulsoup4 \  
&& pip install evdev \  
&& pip install reportlab \  
&& pip install qrcode \  
&& pip install polib \  
&& pip install unidecode \  
&& pip install validate_email \  
&& pip install pyDNS \  
&& pip install pysftp \  
&& pip install python-slugify \  
&& pip install six==1.4 \  
&& pip install paramiko==1.9.0 \  
&& pip install pycrypto==2.4 \  
&& pip install pyinotify \  
&& pip install ecdsa==0.11 \  
&& pip install sphinx \  
&& pip install babel==1.3 \  
&& pip install Pygments==2.0 \  
&& pip install docutils==0.11 \  
&& pip install markupsafe \  
&& pip install pytz \  
&& pip install Jinja2==2.3 \  
&& pip install gevent \  
&& pip install psycogreen\  
&& pip install egenix-mx-base \  
&& pip install pillow==2.6.0  
# OpenSans font will be install...  
RUN set -x; \  
wget https://release.myodoo.de/fonts/opensans.zip \  
&& unzip opensans.zip \  
&& mv opensans /usr/share/fonts/truetype/ \  
&& rm opensans.zip  
  
# Barcodes will be install...  
RUN set -x; \  
wget http://www.reportlab.com/ftp/pfbfer.zip \  
&& unzip pfbfer.zip -d fonts \  
&& mv fonts /usr/lib/python2.7/dist-packages/reportlab/ \  
&& rm pfbfer.zip \  
&& fc-cache -f -v  
  
# PDF export engine..  
RUN set -x; \  
curl -k -o wkhtmltox.deb -SL
https://release.myodoo.de/wkhtmltox-0.12.1.2_linux-jessie-amd64.deb \  
&& echo '40e8b906de658a2221b15e4e8cd82565a47d7ee8 wkhtmltox.deb' | sha1sum -c
- \  
&& dpkg --force-depends -i wkhtmltox.deb \  
&& apt-get -y install -f --no-install-recommends \  
&& apt-get purge -y --auto-remove -o
APT::AutoRemove::RecommendsImportant=false -o
APT::AutoRemove::SuggestsImportant=false npm \  
&& rm -rf /var/lib/apt/lists/* wkhtmltox.deb  

