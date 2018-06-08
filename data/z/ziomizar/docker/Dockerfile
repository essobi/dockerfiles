FROM ubuntu:16.04  
# No interactive frontend during docker build  
ENV DEBIAN_FRONTEND=noninteractive \  
DEBCONF_NONINTERACTIVE_SEEN=true  
  
# Install sudo and apt-utils usefull to run administrative commands  
RUN apt-get update && apt-get install -y sudo && rm -rf /var/lib/apt/lists/*  
  
#========================================  
# Add normal user with passwordless  
#========================================  
# Layer size: tiny: 0.3 MB  
RUN useradd pipelineuser \  
\--shell /bin/bash \  
\--create-home \  
&& usermod -aG sudo pipelineuser \  
&& echo 'pipelineuser:secret' | chpasswd \  
&& echo 'ALL ALL = (ALL) NOPASSWD: ALL' >> /etc/sudoers  
  
#==============================  
# Locale and encoding settings  
#==============================  
# TODO: Allow to change instance language OS and Browser level  
# see if this helps: https://github.com/rogaha/docker-
desktop/blob/68d7ca9df47b98f3ba58184c951e49098024dc24/Dockerfile#L57  
ENV LANG_WHICH en  
ENV LANG_WHERE US  
ENV ENCODING UTF-8  
ENV LANGUAGE ${LANG_WHICH}_${LANG_WHERE}.${ENCODING}  
ENV LANG ${LANGUAGE}  
# Layer size: small: ~9 MB  
# Layer size: small: ~9 MB MB (with --no-install-recommends)  
RUN apt-get -qqy update \  
&& apt-get -qqy --no-install-recommends install \  
language-pack-en \  
tzdata \  
locales \  
&& locale-gen ${LANGUAGE} \  
&& dpkg-reconfigure --frontend noninteractive locales \  
&& apt-get -qyy autoremove \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get -qyy clean  
  
RUN apt-get update -y  
RUN apt-get -qq -y install software-properties-common \  
python-software-properties \  
# net-tools are useul to debugging like netstat  
net-tools \  
# node npm and apache2  
nodejs \  
npm \  
apache2  
  
# mysql is not needed and is moved to the services section of pipeline  
RUN apt-get -qqy install mariadb-server  
# see https://confluence.atlassian.com/bitbucket/use-services-and-databases-
in-bitbucket-pipelines-874786688.html  
# install git, ssh and wget (useful to dpwnload packages and test pipeline)  
RUN apt-get -qqy install git openssh-client wget  
  
# To install php7.1 is needed this specific repo  
RUN add-apt-repository ppa:ondrej/php  
RUN apt-get update -y  
  
# install php  
RUN apt-get -qqy install php \  
php-mbstring \  
php-mcrypt \  
php-curl \  
php-xml \  
php-mysql \  
php-gd \  
php-imagick \  
libapache2-mod-php  
  
RUN sudo a2enmod rewrite  
  
#  
# COMPOSER + PHPUNIT  
#  
# This is needed to install drush properly  
# Is drupal specific and can be removed or changed  
# with the CLI used for other CMS  
RUN apt-get -qq -y install curl  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/local/bin/composer  
RUN ln -s /usr/local/bin/composer /usr/bin/composer  
RUN cd ~  
RUN wget https://phar.phpunit.de/phpunit-6.0.phar  
RUN chmod +x phpunit-6.0.phar  
RUN mv phpunit-6.0.phar /usr/local/bin/phpunit  
RUN phpunit --version  
  
#  
# DRUSH  
#  
# Drush 9 is installed locally in each site using composer, at global level
just  
# the launcher of drush will be installed to not write everytime the full
path.  
RUN wget -O drush.phar https://github.com/drush-ops/drush-
launcher/releases/download/0.6.0/drush.phar  
RUN chmod +x drush.phar  
RUN mv drush.phar /usr/local/bin/drush  
#  
# Selenium with chrome driver require a specific combination of versions  
# require: chrome, chromedrivers and xvfb  
RUN apt-get -qqy install xvfb zip  
# install crhome dependencies  
RUN apt-get -qqy install libgconf2-4 \  
libnss3-1d \  
libxss1 \  
libasound2 \  
libatk1.0-0 \  
libcairo2 \  
libcups2 \  
ibgdk-pixbuf2.0-0 \  
libgtk-3-0 \  
libpango-1.0-0 \  
libpangocairo-1.0-0 \  
libxcomposite1 \  
fonts-liberation \  
libappindicator1 \  
xdg-utils  
  
RUN wget http://selenium-release.storage.googleapis.com/2.53/selenium-server-
standalone-2.53.0.jar  
RUN wget
http://chromedriver.storage.googleapis.com/2.33/chromedriver_linux64.zip  
RUN unzip chromedriver_linux64.zip  
# force a crhome update to the latest version  
RUN wget -N https://dl.google.com/linux/direct/google-chrome-
stable_current_amd64.deb -P ~/  
RUN dpkg -i --force-depends ~/google-chrome-stable_current_amd64.deb  
RUN apt-get -f install -y  
RUN dpkg -i --force-depends ~/google-chrome-stable_current_amd64.deb  
  
# java  
RUN add-apt-repository -y ppa:openjdk-r/ppa  
RUN apt-get install -y -q openjdk-8-jre-headless  
  
# add all script files into the home dir  
COPY scripts /home/pipelineuser/scripts/  
  
USER pipelineuser  
ENV HOME /home/pipelineuser  
  

