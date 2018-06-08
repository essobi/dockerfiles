FROM ubuntu:14.04  
MAINTAINER gooderp61001  
# make the "en_US.UTF-8" locale so postgres will be utf-8 enabled by default  
RUN locale-gen en_US.UTF-8  
RUN update-locale LANG=en_US.UTF-8  
  
#Install and setup postgresql  
RUN set -x; \  
apt-get update \  
&& apt-get install -y postgresql  
USER postgres  
  
RUN /etc/init.d/postgresql start && psql --command "CREATE USER admin WITH
SUPERUSER CREATEDB REPLICATION;"  
RUN /etc/init.d/postgresql start && psql --command "alter user admin with
password 'admin';"  
ENV PGDATA /var/lib/postgresql/data  
# Install some deps, lessc and less-plugin-clean-css  
# Cannot install wkhtmltopdf,default in ubuntu without header&footer  
USER root  
RUN set -x; \  
apt-get update \  
&& apt-get install -y --no-install-recommends --assume-yes \  
sudo \  
ca-certificates curl node-less npm python-gevent python-pyinotify \  
python-renderpm git-core git-gui git-doc python-dateutil python-docutils \  
python-feedparser python-gdata python-jinja2 python-ldap python-libxslt1
python-lxml \  
python-mako python-mock python-openid python-psycopg2 python-psutil python-
pybabel \  
python-pychart python-pydot python-pyparsing python-reportlab python-
simplejson \  
python-tz python-unittest2 python-vatnumber python-vobject python-webdav
python-werkzeug \  
python-xlwt python-yaml python-zsi python-pyPdf python-decorator python-
passlib python-requests\  
python-dev python-pip python-setuptools libffi-dev libxml2-dev libxslt1-dev
postgresql-client \  
postgresql-contrib libtiff4-dev libjpeg8-dev zlib1g-dev libfreetype6-dev
python-imaging\  
liblcms2-dev libwebp-dev tcl8.5-dev tk8.5-dev python-tk python-psycopg2  
  
# Usage: WORKDIR /pathdocker  
WORKDIR ~/  
MAINTAINER CLONE 相应的项目  
RUN set -x; \  
pip install ebaysdk greenlet jcconv httplib2 pdfkit MarkupSafe ofxparse
psycogreen \  
pyserial pyusb qrcode six suds-jurko wsgiref XlsxWriter xlrd xlutils docxtpl
python-ooxml&&\  
git clone https://github.com/osbzr/base.git&&\  
git clone https://github.com/osbzr/gooderp_addons.git  
#Install wkhtmltopdf 在线编译失败... 这段注释  
RUN set -x; \  
curl -o wkhtmltox.deb -SL
http://nightly.odoo.com/extra/wkhtmltox-0.12.1.2_linux-jessie-amd64.deb \  
&& echo '40e8b906de658a2221b15e4e8cd82565a47d7ee8 wkhtmltox.deb' | sha1sum -c
- \  
&& dpkg --force-depends -i wkhtmltox.deb \  
&& apt-get -y install -f --no-install-recommends \  
&& apt-get purge -y --auto-remove -o
APT::AutoRemove::RecommendsImportant=false -o
APT::AutoRemove::SuggestsImportant=false npm \  
&& rm -rf /var/lib/apt/lists/* wkhtmltox.deb  
  
# Set the default config file  
COPY ./oe.conf /~/base/  
#RUN mkdir /extra-addons && mkdir /data  
RUN mkdir /~/extra-addons  
  
#开放端口  
EXPOSE 8888 8071  
# Copy startup script  
#不使用root用户创建  
RUN useradd noroot -u 1000 -s /bin/bash  
USER noroot  
COPY ./startup.sh /  
ENTRYPOINT ["/bin/bash","/startup.sh"]  
  

