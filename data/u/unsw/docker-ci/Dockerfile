FROM ubuntu:16.04  
MAINTAINER Vincent Chalamon <vincentchalamon@gmail.com>  
  
RUN apt-get update  
  
RUN export LANG=C.UTF-8  
  
RUN apt-get install -y --no-install-recommends software-properties-common &&
LC_ALL=C.UTF-8 add-apt-repository ppa:ondrej/php  
  
# Install dependencies  
RUN apt-get update && apt-key update && apt-get install -y --no-install-
recommends --allow-unauthenticated \  
ca-certificates \  
git \  
curl \  
nginx \  
tar \  
sqlite3 \  
php5.6 \  
php5.6-curl \  
php5.6-fpm \  
php5.6-intl \  
php5.6-sqlite \  
php5.6-pgsql \  
php5.6-mysql \  
php5.6-memcache \  
php5.6-apcu \  
php-twig \  
supervisor \  
php5.6-ldap \  
php5.6-mbstring \  
php5.6-dom \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
RUN composer global require "hirak/prestissimo:^0.3"  
  
# Install Node pre-requisites  
RUN apt-get update && apt-key update && apt-get install -y --no-install-
recommends --allow-unauthenticated \  
build-essential \  
m4 \  
ruby \  
texinfo \  
libbz2-dev \  
libcurl4-openssl-dev \  
libexpat-dev \  
libncurses-dev \  
zlib1g-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install Node  
# see https://github.com/nodejs/node-v0.x-archive/issues/3911  
RUN apt-get update && apt-key update && apt-get install -y --no-install-
recommends --allow-unauthenticated \  
nodejs-legacy \  
npm \  
&& rm -rf /var/lib/apt/lists/*  
  
# Configure PHP-FPM & Nginx  
RUN sed -e 's/;daemonize = yes/daemonize = no/' -i /etc/php/5.6/fpm/php-
fpm.conf \  
&& sed -e 's/;listen\\.owner/listen.owner/' -i
/etc/php/5.6/fpm/pool.d/www.conf \  
&& sed -e 's/;listen\\.group/listen.group/' -i
/etc/php/5.6/fpm/pool.d/www.conf \  
&& echo "opcache.enable=1" >> /etc/php/5.6/mods-available/opcache.ini \  
&& echo "\ndaemon off;" >> /etc/nginx/nginx.conf  
  
COPY vhost.conf /etc/nginx/sites-available/default  
RUN usermod -u 1000 www-data  
  
VOLUME /var/www  
WORKDIR /var/www  
  
EXPOSE 80  
#===================  
# Timezone settings  
# Possible alternative:
https://github.com/docker/docker/issues/3359#issuecomment-32150214  
#===================  
ENV TZ "Australia/Sydney"  
RUN echo "${TZ}" > /etc/timezone \  
&& dpkg-reconfigure --frontend noninteractive tzdata  
  
#========================  
# Selenium Configuration  
#========================  
RUN echo "deb http://archive.ubuntu.com/ubuntu xenial main universe\n" >
/etc/apt/sources.list \  
&& echo "deb http://archive.ubuntu.com/ubuntu xenial-updates main universe\n"
>> /etc/apt/sources.list \  
&& echo "deb http://security.ubuntu.com/ubuntu xenial-security main
universe\n" >> /etc/apt/sources.list  
ENV ENV_SCREEN_GEOMETRY=1280x1024x24  
  
#========================  
# Miscellaneous packages  
# Includes minimal runtime used for executing non GUI Java programs  
#========================  
RUN apt-get update -qqy \  
&& apt-get -qqy --no-install-recommends install \  
bzip2 \  
ca-certificates \  
openjdk-8-jre-headless \  
sudo \  
unzip \  
wget \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/*  
# && sed -i
's/securerandom\\.source=file:\/dev\/random/securerandom\\.source=file:\/dev\/urandom/'
./usr/lib/jvm/java-8-openjdk-amd64/jre/lib/security/java.security  
# =======================  
# Install browsers  
# See https://github.com/SeleniumHQ/docker-
selenium/blob/master/NodeFirefox/Dockerfile  
# See https://github.com/SeleniumHQ/docker-
selenium/blob/master/NodeChrome/Dockerfile  
#========================  
ARG FIREFOX_VERSION=52.0  
RUN wget --no-verbose -O /tmp/firefox.tar.bz2 https://download-
installer.cdn.mozilla.net/pub/firefox/releases/$FIREFOX_VERSION/linux-x86_64/en-
US/firefox-$FIREFOX_VERSION.tar.bz2 \  
&& rm -rf /opt/firefox \  
&& tar -C /opt -xjf /tmp/firefox.tar.bz2 \  
&& rm /tmp/firefox.tar.bz2 \  
&& mv /opt/firefox /opt/firefox-$FIREFOX_VERSION \  
&& ln -fs /opt/firefox-$FIREFOX_VERSION/firefox /usr/bin/firefox  
  
ARG GECKODRIVER_VERSION=0.15.0  
RUN wget --no-verbose -O /tmp/geckodriver.tar.gz
https://github.com/mozilla/geckodriver/releases/download/v$GECKODRIVER_VERSION/geckodriver-v$GECKODRIVER_VERSION-
linux64.tar.gz \  
&& rm -rf /opt/geckodriver \  
&& tar -C /opt -zxf /tmp/geckodriver.tar.gz \  
&& rm /tmp/geckodriver.tar.gz \  
&& mv /opt/geckodriver /opt/geckodriver-$GECKODRIVER_VERSION \  
&& chmod 755 /opt/geckodriver-$GECKODRIVER_VERSION \  
&& ln -fs /opt/geckodriver-$GECKODRIVER_VERSION /usr/bin/geckodriver  
  
ARG CHROME_VERSION="google-chrome-stable"  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add - \  
&& echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google-chrome.list \  
&& apt-get update -qqy \  
&& apt-get -qqy install \  
${CHROME_VERSION:-google-chrome-stable} \  
&& rm /etc/apt/sources.list.d/google-chrome.list \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/*  
  
ARG CHROME_DRIVER_VERSION=2.28  
RUN wget --no-verbose -O /tmp/chromedriver_linux64.zip
https://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip
\  
&& rm -rf /opt/selenium/chromedriver \  
&& unzip /tmp/chromedriver_linux64.zip -d /opt/selenium \  
&& rm /tmp/chromedriver_linux64.zip \  
&& mv /opt/selenium/chromedriver
/opt/selenium/chromedriver-$CHROME_DRIVER_VERSION \  
&& chmod 755 /opt/selenium/chromedriver-$CHROME_DRIVER_VERSION \  
&& ln -fs /opt/selenium/chromedriver-$CHROME_DRIVER_VERSION
/usr/bin/chromedriver  
  
#==========  
# Selenium  
#==========  
RUN mkdir -p /opt/selenium \  
&& wget --no-verbose https://selenium-
release.storage.googleapis.com/3.3/selenium-server-standalone-3.3.1.jar -O
/opt/selenium/selenium-server-standalone.jar  
EXPOSE 4444  
EXPOSE 5555  
#========================================  
# Add normal user with passwordless  
#========================================  
RUN useradd seluser --shell /bin/bash --create-home \  
# && usermod -a -G seluser \  
&& echo 'ALL ALL = (ALL) NOPASSWD: ALL' >> /etc/sudoers \  
&& echo 'seluser:secret' | chpasswd  
  
#=======================================  
# Start up Selenium server  
#=======================================  
# USER seluser  
COPY selenium_node_config.json /tmp/selenium_node_config.json  
  
#=======================================  
# Supervisord  
#=======================================  
COPY supervisor.conf /etc/supervisor/conf.d/supervisor.conf  
CMD ["/usr/bin/supervisord"]  
  
#=======================================  
# JSHint  
#=======================================  
RUN npm install -g jshint  

