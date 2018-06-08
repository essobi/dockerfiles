FROM ubuntu:16.04  
MAINTAINER <support@savoirfairelinux.com> Savoir-faire Linux Inc.  
  
ENV USER odoo  
ENV VERSION 10.0  
ENV dev_packages python-dev \  
libxml2-dev \  
libxslt1-dev \  
zlib1g-dev \  
libjpeg-dev \  
libpq-dev \  
libsasl2-dev \  
libldap2-dev \  
libyaml-dev \  
freetds-dev \  
libffi-dev \  
libgeoip-dev \  
libyaml-dev \  
libtiff5-dev \  
libjpeg8-dev \  
libfreetype6-dev \  
liblcms2-dev \  
libwebp-dev \  
gcc \  
make \  
file  
  
RUN set -x; \  
locale-gen en_US.UTF-8 && \  
update-locale && \  
echo 'LANG="en_US.UTF-8"' > /etc/default/locale  
  
ENV LANG en_US.UTF-8  
  
COPY buildout.cfg /fake_buildout/  
COPY requirements-extra.txt /tmp/  
  
RUN set -x; mkdir -p /root/.buildout && mkdir -p /opt/${USER}/.buildout  
  
COPY default.cfg /root/.buildout/  
  
RUN set -x; \  
apt-get update && \  
apt-get install -y --no-install-recommends \  
git \  
ca-certificates \  
xz-utils \  
postgresql-client-9.5 \  
fontconfig \  
libxrender1 \  
libxext6 \  
patch \  
curl \  
bzip2 \  
ssh \  
geoip-database \  
geoip-database-extra \  
${dev_packages} \  
npm && \  
ln -s /usr/bin/nodejs /usr/bin/node && \  
npm install -g less less-plugin-clean-css && \  
curl -o /tmp/requirements.txt -SL
https://github.com/odoo/odoo/raw/${VERSION}/requirements.txt && \  
cd /fake_buildout && \  
curl -o bootstrap-buildout.py -SL https://bootstrap.pypa.io/bootstrap-
buildout.py && \  
curl -o /tmp/requirements.txt -SL
https://github.com/odoo/odoo/raw/${VERSION}/requirements.txt && \  
awk -F== '{print " " $1}' /tmp/requirements.txt >> buildout.cfg && \  
awk -F== '{print " " $1}' /tmp/requirements-extra.txt >> buildout.cfg && \  
sed 's|==| = |' /tmp/requirements.txt > buildout-requirements.txt && \  
sed 's|==| = |' /tmp/requirements-extra.txt > buildout-requirements-extra.txt
&& \  
echo "\n[versions]\n" >> buildout.cfg && \  
cat buildout-requirements.txt >> buildout.cfg && \  
cat buildout-requirements-extra.txt >> buildout.cfg && \  
python2.7 bootstrap-buildout.py && \  
bin/buildout && \  
ls -la /opt/${USER}/.buildout/eggs && \  
curl -o get-pip.py -SL https://bootstrap.pypa.io/get-pip.py && \  
python get-pip.py && \  
pip install urllib3[secure] && \  
pip install -r /tmp/requirements.txt && \  
pip install -r /tmp/requirements-extra.txt && \  
cd .. && \  
rm -rf fake_buildout && \  
apt-get -y remove ${dev_packages} && \  
apt-get clean all  
  
RUN set -x; \  
curl -SL
http://download.gna.org/wkhtmltopdf/0.12/0.12.3/wkhtmltox-0.12.3_linux-
generic-amd64.tar.xz | \  
tar xJ --strip-components=2 -C /usr/local/bin/ wkhtmltox/bin/wkhtmltopdf  
  
RUN set -x; \  
curl -SL
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
| \  
tar xj --strip-components=2 -C /usr/local/bin/
phantomjs-2.1.1-linux-x86_64/bin/phantomjs  
  
RUN set -x; \  
mv /root/.buildout/default.cfg /opt/${USER}/.buildout/ && \  
mkdir /opt/${USER}/git && \  
useradd -d /opt/${USER} ${USER} && \  
chown -R ${USER}:${USER} /opt/${USER}  
  
USER ${USER}  
  
WORKDIR /opt/${USER}/  
  
EXPOSE 8069 8071  

