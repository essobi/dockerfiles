FROM openjdk:8-jdk  
  
RUN apt-get update && apt-get install -y git curl rsync && rm -rf
/var/lib/apt/lists/*  
  
# Install ANT  
RUN apt-get update && apt-get install -y \  
ant \  
apt-transport-https \  
build-essential \  
ca-certificates \  
curl \  
docker \  
git-core \  
gnupg2 \  
libssl-dev \  
mysql-client \  
openssl \  
rsync \  
software-properties-common \  
&& rm -rf /var/lib/apt/lists/*  
  
# PHP STUFF  
# Reference: https://www.cyberciti.biz/faq/installing-php-7-on-debian-
linux-8-jessie-wheezy-using-apt-get/  
#RUN echo 'deb http://packages.dotdeb.org stretch all' >>
/etc/apt/sources.list  
#RUN echo 'deb-src http://packages.dotdeb.org stretch all' >>
/etc/apt/sources.list  
#RUN curl -OL https://www.dotdeb.org/dotdeb.gpg \  
# && apt-key add dotdeb.gpg \  
# && rm dotdeb.gpg  
RUN apt-get update -y \  
&& apt-get install -y \  
php7.0 \  
php7.0-fpm \  
php7.0-gd \  
php7.0-mysql \  
php7.0-xsl \  
php7.0-xml \  
php7.0-bcmath \  
php7.0-bz2 \  
php7.0-intl \  
php7.0-mbstring \  
php7.0-mongodb \  
php7.0-pgsql \  
php7.0-redis \  
php7.0-curl \  
php7.0-xdebug \  
php7.0-zip \  
&& rm -rf /var/lib/apt/lists/*  
  
# RUN curl -OL "http://xdebug.org/files/xdebug-2.4.0.tgz"  
# RUN tar -xf xdebug-2.4.0.tgz  
# RUN cd xdebug-2.4.0/  
# RUN phpize  
# RUN ./configure  
# RUN make && make install  
# RUN echo "zend_extension=xdebug.so" > /etc/php/7.0/mods-available/xdebug.ini  
# RUN ln -sf /etc/php/7.0/mods-available/xdebug.ini
/etc/php/7.0/fpm/conf.d/20-xdebug.ini  
# RUN ln -sf /etc/php/7.0/mods-available/xdebug.ini
/etc/php/7.0/cli/conf.d/20-xdebug.ini  
# RUN cd ..  
RUN curl -OL https://phar.phpunit.de/phpunit-6.0.phar \  
&& chmod +x phpunit-6.0.phar \  
&& mv phpunit-6.0.phar /usr/local/bin/phpunit  
  
RUN curl -OL https://squizlabs.github.io/PHP_CodeSniffer/phpcs.phar \  
&& chmod +x phpcs.phar \  
&& mv phpcs.phar /usr/local/bin/phpcs  
  
RUN curl -OL https://squizlabs.github.io/PHP_CodeSniffer/phpcbf.phar \  
&& chmod +x phpcbf.phar \  
&& mv phpcbf.phar /usr/local/bin/phpcbf  
  
RUN curl -OL https://phar.phpunit.de/phploc.phar \  
&& chmod +x phploc.phar \  
&& mv phploc.phar /usr/local/bin/phploc  
  
RUN curl -OL http://static.pdepend.org/php/latest/pdepend.phar \  
&& chmod +x pdepend.phar \  
&& mv pdepend.phar /usr/local/bin/pdepend  
  
RUN curl -OL http://static.phpmd.org/php/latest/phpmd.phar \  
&& chmod +x phpmd.phar \  
&& mv phpmd.phar /usr/local/bin/phpmd  
  
RUN curl -OL https://phar.phpunit.de/phpcpd.phar \  
&& chmod +x phpcpd.phar \  
&& mv phpcpd.phar /usr/local/bin/phpcpd  
  
RUN curl -OL http://phpdox.de/releases/phpdox.phar \  
&& chmod +x phpdox.phar \  
&& mv phpdox.phar /usr/local/bin/phpdox  
  
RUN curl -OL https://getcomposer.org/composer.phar \  
&& chmod +x composer.phar \  
&& mv composer.phar /usr/local/bin/composer  
  
# Install Codeception  
RUN curl -o codecept.phar http://codeception.com/codecept.phar \  
&& chmod +x codecept.phar \  
&& mv codecept.phar /usr/local/bin/codecept  
  
#RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -  
  
RUN apt-get update -y \  
&& apt-get install -y nodejs \  
&& rm -rf /var/lib/apt/lists/*  
  
#RUN git clone https://github.com/nodejs/node.git \  
# && cd node \  
# && git checkout master \  
# && ./configure \  
# && make \  
# && make install \  
# && cd .. \  
# && rm -rf node  
#RUN curl https://www.npmjs.com/install.sh | sh  
# fix npm - not the latest version installed by apt-get  
#RUN npm install -g npm  
RUN npm install -g yo grunt-cli bower express  
  
# Angular CLI ( https://github.com/nodejs/node-gyp/issues/454 )  
RUN npm install -g node-gyp \  
&& npm install --unsafe-perm -g @angular/cli@latest  
  
# Bower  
RUN npm install bower -g  
  
# Gulp  
RUN npm install gulp-cli -g  
RUN npm install gulp -g  
  
# Grunt  
#RUN npm install grunt-cli -g  
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -  
RUN add-apt-repository \  
"deb [arch=amd64] https://download.docker.com/linux/debian \  
$(lsb_release -cs) \  
stable"  
RUN apt-get update && apt-get install -y \  
docker-ce && \  
rm -rf /var/lib/apt/lists/*  
  
ENV JENKINS_HOME /var/jenkins_home  
ENV JENKINS_SLAVE_AGENT_PORT 50000  
ARG user=jenkins  
ARG group=jenkins  
ARG uid=1000  
ARG gid=1000  
# Jenkins is run with user `jenkins`, uid = 1000  
# If you bind mount a volume from the host or a data container,  
# ensure you use the same uid  
RUN groupadd -g ${gid} ${group} \  
&& useradd -d "$JENKINS_HOME" -u ${uid} -g ${gid} -G docker -m -s /bin/bash
${user}  
  
# Jenkins home directory is a volume, so configuration and build history  
# can be persisted and survive image upgrades  
VOLUME /var/jenkins_home  
  
# `/usr/share/jenkins/ref/` contains all reference configuration we want  
# to set on a fresh new installation. Use it to bundle additional plugins  
# or config file with your custom jenkins Docker image.  
RUN mkdir -p /usr/share/jenkins/ref/init.groovy.d  
  
ENV TINI_VERSION 0.14.0  
ENV TINI_SHA 6c41ec7d33e857d4779f14d9c74924cab0c7973485d2972419a3b7c7620ff5fd  
  
# Use tini as subreaper in Docker container to adopt zombie processes  
RUN curl -fsSL
https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini-
static-amd64 -o \  
/bin/tini && chmod +x /bin/tini \  
&& echo "$TINI_SHA /bin/tini" | sha256sum -c -  
  
COPY init.groovy /usr/share/jenkins/ref/init.groovy.d/tcp-slave-agent-
port.groovy  
  
# jenkins version being bundled in this docker image  
ARG JENKINS_VERSION  
ENV JENKINS_VERSION ${JENKINS_VERSION:-2.103}  
  
# jenkins.war checksum, download will be validated using it  
ARG
JENKINS_SHA=0ad2e6b785f853380994f88f0a60ffba8a0f8d1c5f76039b3f514ad9090ee7b4  
  
# Can be used to customize where jenkins.war get downloaded from  
ARG JENKINS_URL=https://repo.jenkins-ci.org/public/org/jenkins-
ci/main/jenkins-war/${JENKINS_VERSION}/jenkins-war-${JENKINS_VERSION}.war  
  
# could use ADD but this one does not check Last-Modified header neither does
it allow to control checksum  
# see https://github.com/docker/docker/issues/8331  
RUN curl -fsSL ${JENKINS_URL} -o /usr/share/jenkins/jenkins.war \  
&& echo "${JENKINS_SHA} /usr/share/jenkins/jenkins.war" | sha256sum -c -  
  
ENV JENKINS_UC https://updates.jenkins.io  
RUN chown -R ${user} "$JENKINS_HOME" /usr/share/jenkins/ref  
  
# for main web interface:  
EXPOSE 8080  
# will be used by attached slave agents:  
EXPOSE 50000  
ENV COPY_REFERENCE_FILE_LOG $JENKINS_HOME/copy_reference_file.log  
  
USER ${user}  
  
COPY jenkins-support /usr/local/bin/jenkins-support  
COPY jenkins.sh /usr/local/bin/jenkins.sh  
ENTRYPOINT ["/bin/tini", "--", "/usr/local/bin/jenkins.sh"]  
  
# from a derived Dockerfile, can use `RUN plugins.sh active.txt` to setup
/usr/share/jenkins/ref/plugins from a support bundle  
COPY plugins.sh /usr/local/bin/plugins.sh  
COPY install-plugins.sh /usr/local/bin/install-plugins.sh  
  
RUN install-plugins.sh \  
ansicolor \  
checkstyle \  
cloverphp \  
crap4j \  
dry \  
htmlpublisher \  
jdepend \  
plot \  
pmd \  
violations \  
warnings \  
xunit \  
shared-workspace \  
envinject \  
bitbucket \  
build-timestamp \  
workflow-aggregator  
  

