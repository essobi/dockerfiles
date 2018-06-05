FROM php:7.1-fpm  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV WKHTMLTOPDF_URL
"https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download"  
ENV WKHTMLTOPDF_VERSION 0.12.4  
# -----------------------------  
# Updating package dependencies  
# -----------------------------  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - \  
&& curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \  
&& curl -sS https://download.newrelic.com/548C16BF.gpg | apt-key add - \  
&& echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list \  
&& echo "deb http://apt.newrelic.com/debian/ newrelic non-free" | tee
/etc/apt/sources.list.d/newrelic.list \  
&& apt-get update --fix-missing  
  
#&& sh -c 'echo "deb http://apt.newrelic.com/debian/ newrelic non-free" >
/etc/apt/sources.list.d/newrelic.list' \  
# && wget -O - https://download.newrelic.com/548C16BF.gpg | sudo apt-key add -
\  
# ---------------------  
# Generic installations  
# ---------------------  
RUN apt-get install -y \  
libicu-dev \  
zlib1g-dev \  
libpng-dev \  
exif \  
sudo \  
libxml2-dev \  
wget \  
git \  
emacs \  
nano \  
mlocate \  
postgresql-9.6  
  
# ------------------  
# Install wkhtml2pdf  
# ------------------  
RUN apt-get install -y \  
wget \  
build-essential \  
xorg \  
libssl-dev \  
libxrender-dev \  
gdebi \  
&& wget
${WKHTMLTOPDF_URL}/${WKHTMLTOPDF_VERSION}/wkhtmltox-${WKHTMLTOPDF_VERSION}_linux-
generic-amd64.tar.xz \  
&& tar -xJf wkhtmltox-${WKHTMLTOPDF_VERSION}_linux-generic-amd64.tar.xz \  
&& rm wkhtmltox-${WKHTMLTOPDF_VERSION}_linux-generic-amd64.tar.xz \  
&& cp wkhtmltox/bin/wkhtmltopdf /usr/local/bin/wkhtmltopdf  
  
# ---------------  
# Install rsyslog  
# ---------------  
RUN apt-get install -y rsyslog  
  
# -------------  
# Install unzip  
# -------------  
RUN apt-get install -y unzip  
  
# ---------------  
# Install aws cli  
# ---------------  
RUN apt-get install -y python-setuptools \  
&& easy_install pip \  
&& pip install awscli  
  
# -----------------  
# Node dependencies  
# -----------------  
RUN apt-get install -y \  
libpq-dev \  
vim \  
nodejs \  
yarn  
  
# -----------------------  
# S3FS installation layer  
# -----------------------  
RUN apt-get install -y build-essential \  
libfuse-dev \  
fuse \  
fusesmb \  
gvfs \  
gvfs-backends \  
gvfs-fuse \  
libcurl4-openssl-dev \  
mime-support \  
automake \  
libtool \  
pkg-config \  
libssl-dev \  
&& cd /usr/local/src/ \  
&& git clone https://github.com/s3fs-fuse/s3fs-fuse \  
&& cd s3fs-fuse/ \  
&& ./autogen.sh \  
&& ./configure --prefix=/usr --with-openssl \  
&& make \  
&& sudo make install  
  
# ---------  
# New Relic  
# ---------  
RUN apt-get install -y newrelic-php5  
RUN apt-get install -y newrelic-sysmond  
  
# -------------  
# Clean sources  
# -------------  
RUN apt-get clean  
  
# ---------------------  
# Docker php extensions  
# ---------------------  
RUN docker-php-ext-install \  
zip \  
soap \  
intl \  
pdo \  
pdo_pgsql \  
pgsql  
  
# -----------------  
# APCu installation  
# -----------------  
RUN pecl install apcu  
RUN echo "extension=apcu.so" > /usr/local/etc/php/conf.d/apcu.ini  
  
# -------------  
# Clear sources  
# -------------  
RUN docker-php-source delete  
  
# ----------------  
# Install composer  
# ----------------  
RUN php -r "readfile('https://getcomposer.org/installer');" | php --
--install-dir=/usr/local/bin --filename=composer  
RUN php /usr/local/bin/composer --version  
RUN chmod +x /usr/local/bin/composer  
  
# --------------------  
# Crontab installation  
# --------------------  
#COPY ./cron/crontab ./cron/crontab  
#RUN cat ./cron/crontab > /etc/cron.d/app_crontab \  
#&& chmod 644 /etc/cron.d/app_crontab \  
#&& service cron start  
# ------------------------  
# Entrypoint configuration  
# ------------------------  
ENTRYPOINT ["/bin/bash"]  
CMD ["./.docker/entrypoint.sh"]  

