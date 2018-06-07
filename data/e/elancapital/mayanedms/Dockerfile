FROM ubuntu:16.04  
MAINTAINER Roberto Rosario "roberto.rosario@mayan-edms.com"  
ENV MAYAN_VERSION 2.7.3  
ENV DEBIAN_FRONTEND noninteractive  
ENV PYTHONUNBUFFERED 1  
ENV LANG en_US.UTF-8  
ARG APT_PROXY  
# Package caching  
RUN if [ "${APT_PROXY}" ]; then echo "Acquire::http { Proxy
\"http://${APT_PROXY}\"; };" > /etc/apt/apt.conf.d/01proxy; fi  
  
# Install base Ubuntu libraries  
RUN apt-get update && \  
  
# Update system  
apt-get -o Dpkg::Options::="--force-confnew" dist-upgrade -y && \  
  
apt-get install -y --no-install-recommends \  
curl \  
gcc \  
gettext-base \  
ghostscript \  
git \  
gpgv \  
graphviz \  
libjpeg-dev \  
libmagic1 \  
libmysqlclient-dev \  
libpng-dev \  
libpq-dev \  
libreoffice \  
libtiff-dev \  
locales \  
nginx \  
netcat-openbsd \  
poppler-utils \  
python-dev \  
python-pip \  
python-setuptools \  
python-wheel \  
redis-server \  
supervisor \  
tesseract-ocr \  
vim \  
  
&& \  
  
apt-get clean autoclean && \  
  
apt-get autoremove --purge -y && \  
  
rm -rf /var/lib/apt/lists/* && \  
  
rm -f /var/cache/apt/archives/*.deb  
  
# Switch to UTF locale  
RUN echo "LC_ALL=\"en_US.UTF-8\"" >> /etc/default/locale  
RUN locale-gen en_US.UTF-8  
RUN update-locale LANG=en_US.UTF-8  
RUN export LC_ALL=en_US.UTF-8  
  
# Install apt-get-install  
ADD https://raw.githubusercontent.com/guilhem/apt-get-install/master/apt-get-
install /usr/bin/  
RUN chmod +x /usr/bin/apt-get-install  
  
ENV MAYAN_INSTALL_DIR=/usr/local/lib/python2.7/dist-packages/mayan  
ENV MAYAN_MEDIA=/usr/local/lib/python2.7/dist-packages/mayan/media  
  
# Update to latest version of pip  
RUN pip install -U pip  
  
# Install Mayan EDMS, latest production release  
RUN pip install git+git://github.com/elancapital/mayan-edms.git@disclaimer  
  
# Install Python clients for PostgreSQL, REDIS, librabbitmq and uWSGI  
RUN pip install psycopg2 redis uwsgi mysql-python librabbitmq  
  
# Install Django storages alternate file storages  
RUN pip install django-storages boto boto3  
  
# Collect static files  
RUN mayan-edms.py collectstatic --noinput  
  
# Setup uWSGI  
COPY etc/uwsgi/uwsgi.ini $MAYAN_INSTALL_DIR  
  
# Setup NGINX  
COPY /etc/nginx/mayan-edms.template /etc/nginx/sites-available/mayan-
edms.template  
RUN rm /etc/nginx/sites-enabled/default  
  
# Setup supervisor  
COPY /etc/supervisor/beat.conf /etc/supervisor/conf.d  
COPY /etc/supervisor/nginx.conf /etc/supervisor/conf.d  
COPY /etc/supervisor/uwsgi.conf /etc/supervisor/conf.d  
COPY /etc/supervisor/redis.conf /etc/supervisor/conf.d  
COPY /etc/supervisor/workers.conf /etc/supervisor/conf.d  
  
# Create the directory for the logs  
RUN mkdir /var/log/mayan  
  
RUN mkdir -p $MAYAN_INSTALL_DIR/media/document_storage/  
  
# Fix ownership  
RUN chown -R www-data:www-data $MAYAN_INSTALL_DIR  
  
# Make volume symlinks  
# Docker doesn't allow symlinks in volumes, recreate the settings structure in  
# the media volume which is now a media and settings volume.  
RUN touch $MAYAN_MEDIA/__init__.py  
RUN mkdir $MAYAN_MEDIA/settings  
RUN touch $MAYAN_MEDIA/settings/__init__.py  
RUN mkdir $MAYAN_MEDIA/pip_installs  
  
# Setup Mayan EDMS settings file overrides  
COPY etc/mayan/media/settings/base.py
$MAYAN_INSTALL_DIR/media/settings/base.py  
  
# Override the default settings/__init__.py to check for the Mayan Docker  
# environment settings and the import the user's local.py file.  
COPY etc/mayan/settings/__init__.py $MAYAN_INSTALL_DIR/settings/__init__.py  
COPY etc/mayan/settings/docker.py $MAYAN_INSTALL_DIR/settings/docker.py  
  
RUN ln -s $MAYAN_MEDIA /var/lib/mayan  
RUN chown www-data:www-data /var/lib/mayan  
VOLUME ["/var/lib/mayan"]  
  
COPY entrypoint.sh /usr/local/bin/  
RUN ln -s usr/local/bin/entrypoint.sh / # backwards compat  
ENTRYPOINT ["entrypoint.sh"]  
  
# Healthcheck setup  
HEALTHCHECK \--interval=30s --timeout=1s --retries=20 \  
CMD curl -s -f http://localhost/authentication/login/ | grep 'form' >
/dev/null || exit 1  
  
EXPOSE 80  
CMD ["mayan"]  

