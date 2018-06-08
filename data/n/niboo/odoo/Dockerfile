FROM debian:stretch  
MAINTAINER Niboo SPRL <info@niboo.be>  
  
# Install some deps, lessc and less-plugin-clean-css, and wkhtmltopdf  
RUN set -x; \  
apt-get update \  
&& apt-get install -y --no-install-recommends \  
ca-certificates \  
curl \  
node-less \  
ssh-client \  
postgresql-client \  
python3-pip \  
python3-setuptools \  
python3-dev \  
build-essential \  
libffi-dev \  
libsasl2-dev \  
libldap2-dev \  
python3-lxml \  
libssl1.0-dev \  
xz-utils \  
git \  
&& curl -o wkhtmltox.tar.xz -SL
https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.4/wkhtmltox-0.12.4_linux-
generic-amd64.tar.xz \  
&& echo '3f923f425d345940089e44c1466f6408b9619562 wkhtmltox.tar.xz' | sha1sum
-c - \  
&& tar xvf wkhtmltox.tar.xz \  
&& cp wkhtmltox/lib/* /usr/local/lib/ \  
&& cp wkhtmltox/bin/* /usr/local/bin/ \  
&& cp -r wkhtmltox/share/man/man1 /usr/local/share/man/ \  
&& pip3 install werkzeug==0.11.11 \  
Babel==2.3.4 \  
decorator==4.0.10 \  
docutils==0.12 \  
feedparser==5.2.1 \  
gevent==1.1.2 \  
greenlet==0.4.10 \  
html2text==2016.9.19 \  
Jinja2==2.8 \  
Mako==1.0.4 \  
MarkupSafe==0.23 \  
mock==2.0.0 \  
num2words==0.5.4 \  
ofxparse==0.16 \  
passlib==1.6.5 \  
Pillow==3.4.1 \  
psutil==4.3.1 \  
psycogreen==1.0 \  
psycopg2==2.7.1 \  
pydot==1.2.3 \  
pyldap==2.4.28 \  
pyparsing==2.1.10 \  
PyPDF2==1.26.0 \  
pyserial==3.1.1 \  
python-dateutil==2.5.3 \  
python-openid==2.2.5 \  
pytz==2016.7 \  
pyusb==1.0.0 \  
PyYAML==3.12 \  
qrcode==5.3 \  
reportlab==3.3.0 \  
requests==2.11.1 \  
six==1.10.0 \  
suds-jurko==0.6 \  
vatnumber==1.2 \  
vobject==0.9.3 \  
Werkzeug==0.11.11 \  
XlsxWriter==0.9.3 \  
xlwt==1.3 \  
xlrd==1.0.0  
  
# Install Odoo  
ENV ODOO_ORIGINAL_TAG "v11.0.1.0"  
RUN set -x; \  
mkdir -p /opt/local/odoo \  
&& cd /opt/local/odoo \  
&& git clone -b ${ODOO_ORIGINAL_TAG} --single-branch --depth 1
https://github.com/Niboo/odoo.git odoo \  
&& ln -s /opt/local/odoo/odoo/odoo-bin /usr/bin/odoo \  
&& useradd odoo -d /opt/local/odoo -p odoo \  
&& chown -R odoo /opt/local/odoo  
  
# Copy entrypoint script and Odoo configuration file  
COPY ./entrypoint.sh /  
  
# Expose Odoo services  
EXPOSE 8069 8071  
  
# Set the default config file  
ENV ODOO_RC /etc/odoo/odoo.conf  
  
# Set default user when running the container  
USER odoo  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["odoo"]  

