FROM ubuntu:trusty  
MAINTAINER Cyril PERROT <cperrot@genedys.com>  
  
# Set user jenkins to the image  
RUN useradd -m -d /home/jenkins -s /bin/sh jenkins &&\  
echo "jenkins:jenkins" | chpasswd  
  
RUN apt-key adv \--keyserver keys.gnupg.net \--recv-keys
14AA40EC0831756756D7F66C4F4EA0AAE5267A6C; \  
echo "deb http://ppa.launchpad.net/ondrej/php/ubuntu trusty main" >>
/etc/apt/sources.list; \  
echo "deb-src http://ppa.launchpad.net/ondrej/php/ubuntu trusty main" >>
/etc/apt/sources.list  
  
RUN export DEBIAN_FRONTEND=noninteractive; \  
apt-get -q update; \  
apt-get -qq install php7.1 php7.1-cli php7.1-xsl php7.1-json php7.1-curl
php7.1-sqlite php7.1-mysqlnd php7.1-xdebug php7.1-intl php7.1-mcrypt
php7.1-mbstring php7.1-zip php-pear curl git ant sudo apt-transport-https ca-
certificates curl software-properties-common python python-pip  
  
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -  
  
RUN add-apt-repository "deb [arch=amd64]
https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"  
  
RUN export DEBIAN_FRONTEND=noninteractive; \  
apt-get -q update; \  
apt-get -qq install docker-ce  
  
RUN pip install docker-compose  
  
RUN sed -i 's|disable_functions.*=|;disable_functions=|'
/etc/php/7.1/cli/php.ini; \  
sed -i 's/^error_reporting = .*/error_reporting = E_ALL \& ~E_STRICT/'
/etc/php/7.1/cli/php.ini; \  
sed -i 's/^display_errors = .*/display_errors = On/' /etc/php/7.1/cli/php.ini;
\  
echo "xdebug.max_nesting_level = 500" >> /etc/php/7.1/mods-
available/xdebug.ini  
  
RUN mkdir -p /usr/share/jenkins/composer/bin && chown -R jenkins:jenkins
/usr/share/jenkins/composer; \  
sudo -H -u jenkins bash -c ' \  
curl -sS https://getcomposer.org/installer | php -- \--install-
dir=/usr/share/jenkins/composer/bin \--filename=composer;'; \  
ln -s /usr/share/jenkins/composer/bin/composer /usr/local/bin/; \  
sudo -H -u jenkins bash -c ' \  
export COMPOSER_BIN_DIR=/usr/share/jenkins/composer/bin; \  
export COMPOSER_HOME=/usr/share/jenkins/composer; \  
composer global require "phpunit/phpunit=*" \--prefer-source \--no-
interaction; \  
composer global require "squizlabs/php_codesniffer=*" \--prefer-source \--no-
interaction; \  
composer global require "phploc/phploc=*" \--prefer-source \--no-interaction;
\  
composer global require "pdepend/pdepend=*" \--prefer-source \--no-
interaction; \  
composer global require "phpmd/phpmd=*" \--prefer-source \--no-interaction; \  
composer global require "sebastian/phpcpd=*" \--prefer-source \--no-
interaction; \  
composer global require "theseer/phpdox=*" \--prefer-source \--no-interaction;
'; \  
ln -s /usr/share/jenkins/composer/bin/pdepend /usr/local/bin/; \  
ln -s /usr/share/jenkins/composer/bin/phpcpd /usr/local/bin/; \  
ln -s /usr/share/jenkins/composer/bin/phpcs /usr/local/bin/; \  
ln -s /usr/share/jenkins/composer/bin/phpdox /usr/local/bin/; \  
ln -s /usr/share/jenkins/composer/bin/phploc /usr/local/bin/; \  
ln -s /usr/share/jenkins/composer/bin/phpmd /usr/local/bin/; \  
ln -s /usr/share/jenkins/composer/bin/phpunit /usr/local/bin/  
  
RUN locale-gen en_US.UTF-8 &&\  
DEBIAN_FRONTEND="noninteractive" apt-get -q upgrade -y -o Dpkg::Options::="--
force-confnew" \--no-install-recommends &&\  
DEBIAN_FRONTEND="noninteractive" apt-get -q install -y -o Dpkg::Options::="--
force-confnew" \--no-install-recommends openssh-server &&\  
apt-get -q autoremove &&\  
apt-get -q clean -y && rm -rf /var/lib/apt/lists/* && rm -f
/var/cache/apt/*.bin &&\  
sed -i 's|session required pam_loginuid.so|session optional pam_loginuid.so|g'
/etc/pam.d/sshd &&\  
mkdir -p /var/run/sshd  
  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
  
# Install JDK 7 (latest edition)  
RUN apt-get -q update &&\  
DEBIAN_FRONTEND="noninteractive" apt-get -q install -y -o Dpkg::Options::="--
force-confnew" \--no-install-recommends openjdk-7-jre-headless &&\  
apt-get -q clean -y && rm -rf /var/lib/apt/lists/* && rm -f
/var/cache/apt/*.bin  
# Standard SSH port  
EXPOSE 22  
  
# Default command  
CMD ["/usr/sbin/sshd", "-D"]  

