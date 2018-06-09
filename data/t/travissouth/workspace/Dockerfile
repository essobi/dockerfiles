FROM travissouth/baseimage  
  
USER root  
  
# Add the "PHP 7" ppa  
RUN install_clean -y software-properties-common && \  
add-apt-repository -y ppa:ondrej/php  
  
#  
#--------------------------------------------------------------------------  
# Software's Installation  
#--------------------------------------------------------------------------  
#  
# Install "PHP Extentions", "libraries", "Software's"  
RUN install_clean -y --allow-downgrades --allow-remove-essential \  
\--allow-change-held-packages \  
php7.2-cli \  
php7.2-common \  
php7.2-curl \  
php7.2-intl \  
php7.2-json \  
php7.2-xml \  
php7.2-mbstring \  
php7.2-mysql \  
php7.2-pgsql \  
php7.2-sqlite \  
php7.2-sqlite3 \  
php7.2-zip \  
php7.2-bcmath \  
php7.2-memcached \  
php7.2-gd \  
php7.2-dev \  
pkg-config \  
libcurl4-openssl-dev \  
libedit-dev \  
libssl-dev \  
libxml2-dev \  
xz-utils \  
libsqlite3-dev \  
sqlite3 \  
git \  
curl \  
vim \  
nano \  
postgresql-client \  
htop \  
libmcrypt-dev \  
openssh-client \  
libxml2-dev \  
libpng-dev \  
g++ \  
make \  
autoconf  
  
#####################################  
# Composer:  
#####################################  
# Install composer and add its bin to the PATH.  
RUN curl -s http://getcomposer.org/installer | php && \  
echo "export
PATH=${PATH}:/var/www/vendor/bin:/usr/local/bin:/home/daker/.composer/vendor/bin"
>> ~/.bashrc && \  
mv composer.phar /usr/local/bin/composer && \  
chmod +x /usr/local/bin/composer  
  
# Source the bash  
RUN . ~/.bashrc  
ENV PATH
${PATH}:/var/www/vendor/bin:/usr/local/bin:/home/daker/.composer/vendor/bin  
  
USER daker  
  
RUN mkdir -p /home/daker/.docker-workspace/.composer/cache  
RUN echo "export
PATH=${PATH}:/var/www/vendor/bin:/usr/local/bin:/home/daker/.composer/vendor/bin"
>> ~/.bashrc  
RUN echo "export COMPOSER_CACHE_DIR=/home/daker/.docker-
workspace/.composer/cache" >> ~/.bashrc  
RUN . ~/.bashrc  
ENV PATH
${PATH}:/var/www/vendor/bin:/usr/local/bin:/home/daker/.composer/vendor/bin  
ENV COMPOSER_CACHE_DIR /home/daker/.docker-workspace/.composer/cache  
RUN mkdir -p ~/.composer  
RUN composer global require hirak/prestissimo && composer --version  
  
# Install PHPQATools  
RUN composer global require symfony/config:^3 \  
symfony/console:^3 \  
symfony/event-dispatcher:^3 \  
symfony/finder:^3 \  
symfony/process:^3 \  
symfony/var-dumper:^3 \  
symfony/yaml:^3 \  
symfony/filesystem:^3 \  
travis-south/phpqatools:^3.0 \  
behat/mink-extension \  
behat/mink-goutte-driver \  
behat/mink-selenium2-driver \  
behat/mink-zombie-driver \  
drupal/coder \  
endouble/symfony3-custom-coding-standard \  
rregeer/phpunit-coverage-check  
RUN phpcs --config-set installed_paths \  
$HOME/.composer/vendor/endouble/symfony3-custom-coding-
standard,$HOME/.composer/vendor/drupal/coder/coder_sniffer  
  
# Install Drush  
USER daker  
RUN composer global require drush/drush:^9.0 && drush --version  
  
# Install Laravel artisan  
USER daker  
RUN composer global require laravel/installer && laravel --version  
  
# Install NodeJS  
USER root  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - && \  
install_clean nodejs && \  
nodejs --version  
USER daker  
RUN echo "export NPM_CONFIG_USERCONFIG=/home/daker/.docker-workspace/.npmrc"
>> ~/.bashrc  
ENV NPM_CONFIG_USERCONFIG /home/daker/.docker-workspace/.npmrc  
RUN echo "cache=/home/daker/.docker-workspace/npm-cache" >> ~/.docker-
workspace/.npmrc  
RUN nodejs --version && \  
npm --version  
  
# Install Yarn  
USER root  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \  
echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list && \  
install_clean yarn && \  
yarn --version  
USER daker  
RUN yarn --version && \  
echo "export YARN_CACHE_FOLDER=/home/daker/.docker-workspace/.yarn/cache" >>
~/.bashrc && \  
echo "export PATH=${PATH}:/home/daker/.yarn/bin" >> ~/.bashrc && \  
. ~/.bashrc  
ENV YARN_CACHE_FOLDER /home/daker/.docker-workspace/.yarn/cache  
ENV PATH ${PATH}:/home/daker/.yarn/bin  
  
# Install Python/PIP  
USER root  
RUN install_clean python-pip && \  
python --version && \  
pip --version  
  
# Install Ansible  
USER root  
RUN pip install --upgrade setuptools && \  
pip install ansible && \  
ansible --version  
USER daker  
RUN ansible --version  
  
# Install AWS CLI  
USER root  
RUN install_clean groff  
USER daker  
RUN pip install awscli --upgrade --user  
ENV PATH ${PATH}:/home/daker/.local/bin  
RUN echo "export PATH=${PATH}:/home/daker/.local/bin" >> ~/.bashrc  
RUN echo "export AWS_CONFIG_FILE=/home/daker/.docker-workspace/.aws/config" >>
~/.bashrc  
RUN echo "export AWS_SHARED_CREDENTIALS_FILE=/home/daker/.docker-
workspace/.aws/credentials" >> ~/.bashrc  
ENV AWS_CONFIG_FILE /home/daker/.docker-workspace/.aws/config  
ENV AWS_SHARED_CREDENTIALS_FILE /home/daker/.docker-workspace/.aws/credentials  
RUN . ~/.bashrc && \  
aws --version  
  
# Install Wodby CLI  
USER root  
RUN install_clean wget && \  
export WODBY_CLI_LATEST_URL=$(curl -s
https://api.github.com/repos/wodby/wodby-cli/releases/latest | grep linux-
amd64 | grep browser_download_url | cut -d '"' -f 4) && \  
wget -qO- "${WODBY_CLI_LATEST_URL}" | tar xz -C /usr/local/bin  
USER daker  
RUN wodby --help  
  
# Install eslint and tslint  
USER daker  
RUN yarn global add babel-eslint eslint typescript tslint  
  
# Install sonarscanner  
USER root  
RUN install_clean unzip \  
xz-utils \  
openjdk-8-jre-headless  
RUN java -version  
WORKDIR /  
RUN curl -o sonar-scanner-cli.zip -L
https://sonarsource.bintray.com/Distribution/sonar-scanner-cli/sonar-scanner-
cli-3.2.0.1227.zip  
RUN unzip sonar-scanner-cli.zip  
RUN mv sonar-scanner-3.2.0.1227 sonar-scanner && \  
chmod 777 -R /sonar-scanner  
RUN cd /usr/local/bin && ln -s /sonar-scanner/bin/sonar-scanner sonar-scanner  
COPY sonar-scanner.properties /sonar-scanner/conf/sonar-scanner.properties  
RUN rm -rf /sonar-scanner-cli.zip  
WORKDIR /var/www/app  
USER daker  
RUN yarn global add tslint-sonarts  
ENV NODE_PATH /usr/lib/node_modules  
RUN echo "export NODE_PATH=/usr/lib/node_modules" >> ~/.bashrc  
ENV SONAR_USER_HOME /home/daker/.docker-workspace/.sonar  
RUN echo "export SONAR_USER_HOME=/home/daker/.docker-workspace/.sonar" >>
~/.bashrc  
RUN . ~/.bashrc  
  
# Install JMeter  
USER root  
ENV JMETER_HOME=/opt/jmeter \  
JMETER_VERSION=3.3 \  
PATH=/opt/jmeter/bin/:$PATH \  
PLUGINS_PATH=/tmp/plugins  
RUN mkdir -p ${JMETER_HOME} \  
&& wget -O /tmp/jmeter.tgz
https://archive.apache.org/dist/jmeter/binaries/apache-
jmeter-${JMETER_VERSION}.tgz \  
&& tar -C /tmp -xvzf /tmp/jmeter.tgz \  
&& mv /tmp/apache-jmeter-${JMETER_VERSION}/* ${JMETER_HOME} \  
&& rm -rf /tmp/jmeter.tgz /tmp/apache-jmeter-${JMETER_VERSION}
/var/cache/apk/* \  
&& mkdir -p $PLUGINS_PATH \  
&& wget https://jmeter-plugins.org/files/packages/jpgc-cmd-2.1.zip \  
&& unzip -o -d $PLUGINS_PATH jpgc-cmd-2.1.zip \  
&& cp $PLUGINS_PATH/lib/*.jar $JMETER_HOME/lib/ \  
&& cp $PLUGINS_PATH/bin/* $JMETER_HOME/bin/ \  
&& cp $PLUGINS_PATH/lib/ext/*.jar $JMETER_HOME/lib/ext/ \  
&& rm -rf $PLUGINS_PATH  
RUN /opt/jmeter/bin/jmeter.sh -n -v \  
&& java -cp /opt/jmeter/lib/ext/jmeter-plugins-manager-0.20.jar
org.jmeterplugins.repository.PluginManagerCMDInstaller  
RUN /opt/jmeter/bin/PluginsManagerCMD.sh install jpgc-oauth,jpgc-json,jpgc-
casutg,jpgc-graphs-additional,jpgc-synthesis && \  
chmod -R 777 /opt/jmeter  
USER daker  
ENV JMETER_HOME /opt/jmeter  
RUN echo "export JMETER_HOME=/opt/jmeter" >> ~/.bashrc  
ENV PATH ${PATH}:/opt/jmeter/bin  
RUN echo "export PATH=${PATH}:/opt/jmeter/bin" >> ~/.bashrc  
RUN . ~/.bashrc  
RUN jmeter -n -v  
  
# Install Apache bench  
USER root  
RUN install_clean apache2-utils && \  
ab -V  
  
# Install siege  
USER root  
WORKDIR /  
RUN install_clean openssl libssl-dev zlib1g zlib1g-dev  
RUN curl -o siege.tar.gz -L
http://download.joedog.org/siege/siege-4.0.4.tar.gz  
RUN tar -zxf siege.tar.gz  
RUN mv siege-4.0.4 siege  
RUN chmod 777 -R siege  
RUN cd siege && \  
./configure && \  
make && \  
make install  
  
# Install Docker and Docker Compose  
USER root  
RUN install_clean \  
apt-transport-https \  
ca-certificates \  
curl \  
software-properties-common && \  
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add - && \  
apt-key fingerprint 0EBFCD88 && \  
add-apt-repository \  
"deb [arch=amd64] https://download.docker.com/linux/ubuntu \  
$(lsb_release -cs) \  
stable" && \  
install_clean docker-ce  
RUN curl -L https://github.com/docker/compose/releases/download/1.21.2/docker-
compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose && \  
chmod +x /usr/local/bin/docker-compose && \  
docker --version && \  
docker-compose --version  
RUN usermod -aG docker daker && \  
service docker start && \  
service docker status  
  
###  
USER root  
COPY workspace-list /usr/local/bin/workspace-list  
RUN chmod +x /usr/local/bin/workspace-list  
CMD ["/usr/local/bin/workspace-list"]  
  
# Clean up APT when done.  
USER root  
RUN apt-get update -y && apt-get upgrade -y && apt-get clean && rm -rf
/var/lib/apt/lists/* /tmp/* /var/tmp/*  

