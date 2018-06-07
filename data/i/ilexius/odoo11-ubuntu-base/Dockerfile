FROM ubuntu:16.04  
MAINTAINER ilexius GmbH <info@ilexius.de>  
  
# Setup python and java and base system  
ENV DEBIAN_FRONTEND noninteractive  
ENV LANG=C.UTF-8  
  
RUN apt-get update && apt-get install -q -y wget  
#build-essential libldap2-dev libsasl2-dev  
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ xenial-pgdg main" >
/etc/apt/sources.list.d/pgdg.list  
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc |
apt-key add -  
  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -q -y \--no-install-recommends \  
git \  
adduser ssh postgresql-client-9.6\  
python \  
python-babel \  
python-dateutil \  
python-decorator \  
python-docutils \  
python-feedparser \  
python-gevent \  
python-html2text \  
python-pil \  
python-ldap \  
python-jinja2 \  
python-lxml \  
python-mako \  
python-mock \  
python-ofxparse \  
python-passlib \  
python-psutil \  
python-psycopg2 \  
python-pydot \  
python-pyparsing \  
python-pypdf \  
python-reportlab \  
python-requests \  
python-serial \  
python-suds \  
python-tz \  
python-usb \  
python-vatnumber \  
python-werkzeug \  
python-xlsxwriter \  
python-yaml \  
ca-certificates \  
curl \  
node-less \  
python-pip \  
python-setuptools \  
python-renderpm \  
libssl-dev \  
xz-utils \  
&& curl -o wkhtmltox.tar.xz -SL
https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.4/wkhtmltox-0.12.4_linux-
generic-amd64.tar.xz \  
&& echo '3f923f425d345940089e44c1466f6408b9619562 wkhtmltox.tar.xz' | sha1sum
-c \- \  
&& tar xvf wkhtmltox.tar.xz \  
&& cp wkhtmltox/lib/* /usr/local/lib/ \  
&& cp wkhtmltox/bin/* /usr/local/bin/ \  
&& cp -r wkhtmltox/share/man/man1 /usr/local/share/man/  
  
COPY requirements.txt /root/  
  
RUN pip install --upgrade pip requests  
RUN pip install -r /root/requirements.txt  
  
#missing  
#python3-vobject

