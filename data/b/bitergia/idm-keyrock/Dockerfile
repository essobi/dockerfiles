# Copyright (C) 2015 Bitergia  
# GPLv3 License  
FROM ubuntu:14.04  
MAINTAINER Bitergia <fiware-testing@bitergia.com>  
  
ENV WORKON_HOME /opt/virtualenvs  
ENV KEYROCK_HOME /opt/fiware-idm  
ENV GIT_URL_KEYSTONE https://github.com/ging/keystone  
ENV GIT_URL_HORIZON https://github.com/ging/horizon  
ENV GIT_REV_KEYSTONE keyrock-5.1.0  
ENV GIT_REV_HORIZON keyrock-5.1.0  
ENV DEBIAN_FRONTEND noninteractive  
ENV INITRD no  
  
WORKDIR ${KEYROCK_HOME}  
RUN mkdir -p ${WORKON_HOME}  
  
# install dependencies  
RUN apt-get update && \  
apt-get -y install --no-install-recommends\  
autoconf \  
bash-completion \  
build-essential \  
ca-certificates \  
curl \  
gcc \  
git \  
libffi-dev \  
libjpeg8-dev \  
libldap2-dev \  
libmysqlclient-dev \  
libsasl2-dev \  
libsqlite3-dev \  
libssl-dev \  
libxml2-dev \  
libxslt1-dev \  
python-dev \  
python-mysqldb \  
python-setuptools \  
python-virtualenv \  
sqlite3 \  
virtualenvwrapper \  
&& \  
  
# install keystone  
git clone --depth 1 \--branch ${GIT_REV_KEYSTONE} ${GIT_URL_KEYSTONE}
${KEYROCK_HOME}/keystone && \  
cd ${KEYROCK_HOME}/keystone && \  
cp etc/keystone.conf.sample etc/keystone.conf && \  
python tools/install_venv.py && \  
  
# install horizon  
git clone --depth 1 \--branch ${GIT_REV_HORIZON} ${GIT_URL_HORIZON}
${KEYROCK_HOME}/horizon && \  
cd ${KEYROCK_HOME}/horizon && \  
cp openstack_dashboard/local/local_settings.py.example
openstack_dashboard/local/local_settings.py && \  
sed -e 's/$$IDM_PASS/idm/g' \  
-i openstack_dashboard/local/local_settings.py && \  
python tools/install_venv.py && \  
tools/with_venv.sh python manage.py collectstatic --noinput && \  
tools/with_venv.sh python manage.py compress --force && \  
apt-get -y install --no-install-recommends apache2 libapache2-mod-wsgi ssl-
cert && \  
  
# cleanup image  
apt-get clean && \  
apt-get autoremove --purge -y && \  
find /var/lib/apt/lists -type f -delete && \  
rm -rf /root/.cache /root/.distlib  
  
# configure apache  
COPY idm.conf /opt/idm.conf  
RUN mv /opt/idm.conf /etc/apache2/sites-available/idm.conf && \  
a2enmod wsgi ssl && \  
a2dissite 000-default && \  
a2ensite idm && \  
chown www-data:www-data ${KEYROCK_HOME}/horizon/openstack_dashboard/local && \  
mkdir -p ${KEYROCK_HOME}/horizon/static && \  
chown www-data:www-data ${KEYROCK_HOME}/horizon/static && \  
chown -R www-data:www-data ${KEYROCK_HOME}/horizon/media  
  
# TODO: remove fabric from provisioning and authzforce sync  
COPY default_provision.py /config/default_provision.py  
COPY settings.py /config/settings.py  
COPY params-config.py ${KEYROCK_HOME}/keystone/params-config.py  
COPY access_control_xacml.py ${KEYROCK_HOME}/horizon/access_control_xacml.py  
  
RUN touch /initialize-provision && \  
touch /initialize-domain-request  
  
COPY docker-entrypoint.sh /  
ADD https://raw.githubusercontent.com/Bitergia/docker/master/utils/entrypoint-
common.sh /  
RUN chmod 755 /docker-entrypoint.sh  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
### Exposed ports  
# - Keystone  
EXPOSE 5000  
# - Horizon (HTTPS)  
EXPOSE 443  

