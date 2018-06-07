FROM ubuntu:14.04  
MAINTAINER Luis Triana <luis.triana@jarsa.com.mx>  
  
RUN echo 'APT::Get::Assume-Yes "true";' >> /etc/apt/apt.conf \  
&& echo 'APT::Get::force-yes "true";' >> /etc/apt/apt.conf  
RUN locale-gen fr_FR \  
&& locale-gen en_US.UTF-8 \  
&& dpkg-reconfigure locales \  
&& update-locale LANG=en_US.UTF-8 \  
&& update-locale LC_ALL=en_US.UTF-8  
RUN ln -s /usr/share/i18n/SUPPORTED /var/lib/locales/supported.d/all \  
&& locale-gen  
ENV PYTHONIOENCODING utf-8  
ENV TERM xterm  
#Install OpenERP dependencies  
RUN apt-get update -q && apt-get upgrade -q && \  
apt-get install --allow-unauthenticated -q \  
antiword \  
gcc \  
ghostscript \  
graphviz \  
lptools \  
make \  
mc \  
nano \  
poppler-utils \  
python-babel \  
python-dateutil \  
python-dev \  
python-docutils \  
python-egenix-mxdatetime \  
python-feedparser \  
python-feedparser \  
python-imaging \  
python-jinja2 \  
python-ldap \  
python-libxslt1 \  
python-lxml \  
python-mako \  
python-matplotlib \  
python-mock \  
python-openid \  
python-openssl \  
python-paramiko \  
python-pdftools \  
python-pip \  
python-psutil \  
python-psycopg2 \  
python-pybabel \  
python-pychart \  
python-pydot \  
python-pyparsing \  
python-reportlab \  
python-reportlab-accel \  
python-setuptools \  
python-simplejson \  
python-soappy \  
python-tz \  
python-unittest2 \  
python-vatnumber \  
python-vobject \  
python-webdav \  
python-werkzeug \  
python-xlwt \  
python-yaml \  
python-zbar \  
python-zsi \  
qrencode \  
wget \  
xmlstarlet \  
xsltproc \  
zbar-tools  
  
#Install gdata dependency  
RUN wget http://gdata-python-client.googlecode.com/files/gdata-2.0.17.tar.gz
&& \  
tar zxvf gdata-2.0.17.tar.gz && \  
cd gdata-2.0.17 && \  
python setup.py install  
  
#Install QR tools  
RUN wget https://launchpad.net/qr-tools/trunk/1.2/+download/python-
qrtools_1.2_all.deb && \  
dpkg -i python-qrtools_1.2_all.deb  
  
#Install some python dependencies  
RUN pip install pyopenssl && pip install pyyaml && pip install xmltodict  
  
# Install wkhtmltopdf  
RUN cd /tmp && \  
wget http://wkhtmltopdf.googlecode.com/files/wkhtmltopdf-0.9.9-static-
amd64.tar.bz2 && \  
tar xvjf wkhtmltopdf-0.9.9-static-amd64.tar.bz2 && \  
mv wkhtmltopdf-amd64 /usr/bin/wkhtmltopdf && \  
chmod +x /usr/bin/wkhtmltopdf  
  
# Install pip  
RUN cd /tmp && \  
wget -q https://bootstrap.pypa.io/get-pip.py && \  
python get-pip.py  
  
# Add user  
RUN adduser --home=/opt/odoo --disabled-password --gecos "" \--shell=/bin/bash
odoo  
RUN echo 'root:odoo' | chpasswd  
  
#Add log folder  
RUN mkdir /var/log/odoo && \  
chown odoo:root /var/log/odoo  
  
#Permission  
RUN echo $'#!/bin/bash\nchown -R odoo:odoo /opt/odoo && chmod 640
/opt/odoo/odoo-server.conf' > /permission.sh && \  
chmod +x /permission.sh  
CMD /permission.sh  
  
# Add entrypoint file and give execute permission  
ADD files/entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
  
CMD /entrypoint.sh  
  
VOLUME ["/opt/odoo/", "/var/log/odoo" ]  
  
USER odoo  
  
EXPOSE 8069  
EXPOSE 22

