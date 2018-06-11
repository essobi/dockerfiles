#  
#--------------------------------------------------------------------------  
# Image Setup  
#--------------------------------------------------------------------------  
#  
# To edit the 'workspace' base Image, visit its repository on Github  
# https://github.com/Laradock/workspace  
#  
# To change its version, see the available Tags on the Docker Hub:  
# https://hub.docker.com/r/laradock/workspace/tags/  
#  
# Note: Base Image name format {image-tag}-{php-version}  
#  
  
FROM laradock/workspace:1.9-71  
  
MAINTAINER Mahmoud Zalt <mahmoud@zalt.me>  
  
#  
#--------------------------------------------------------------------------  
# Mandatory Software's Installation  
#--------------------------------------------------------------------------  
#  
# Mandatory Software's such as ("php7.1-cli", "git", "vim", ....) are  
# installed on the base image 'laradock/workspace' image. If you want  
# to add more Software's or remove existing one, you need to edit the  
# base image (https://github.com/Laradock/workspace).  
#  
#  
#--------------------------------------------------------------------------  
# Optional Software's Installation  
#--------------------------------------------------------------------------  
#  
# Optional Software's will only be installed if you set them to `true`  
# in the `docker-compose.yml` before the build.  
# Example:  
# - INSTALL_NODE=false  
# - ...  
#  
#####################################  
# Non-Root User:  
#####################################  
# Add a non-root user to prevent files being created with root permissions on
host machine.  
ARG PUID=1000  
ARG PGID=1000  
  
ENV PUID ${PUID}  
ENV PGID ${PGID}  
  
RUN groupadd -g ${PGID} laradock && \  
useradd -u ${PUID} -g laradock -m laradock && \  
apt-get update -yqq  
  
#####################################  
# SOAP:  
#####################################  
USER root  
  
ARG INSTALL_SOAP=true  
ENV INSTALL_SOAP ${INSTALL_SOAP}  
  
RUN if [ ${INSTALL_SOAP} = true ]; then \  
# Install the PHP SOAP extension  
add-apt-repository -y ppa:ondrej/php && \  
apt-get update -yqq && \  
apt-get -y install libxml2-dev php7.1-soap \  
;fi  
  
#####################################  
# Set Timezone  
#####################################  
  
ARG TZ=Asia/Shanghai  
ENV TZ ${TZ}  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
  
#####################################  
# Composer:  
#####################################  
# Add the composer.json  
COPY ./composer.json /home/laradock/.composer/composer.json  
  
# Make sure that ~/.composer belongs to laradock  
RUN chown -R laradock:laradock /home/laradock/.composer  
USER laradock  
  
# Check if global install need to be ran  
ARG COMPOSER_GLOBAL_INSTALL=true  
ENV COMPOSER_GLOBAL_INSTALL ${COMPOSER_GLOBAL_INSTALL}  
RUN if [ ${COMPOSER_GLOBAL_INSTALL} = true ]; then \  
# run the install  
composer global install \  
;fi  
  
#####################################  
# Crontab  
#####################################  
USER root  
  
COPY ./crontab /etc/cron.d  
RUN chmod -R 644 /etc/cron.d  
  
#####################################  
# User Aliases  
#####################################  
  
USER laradock  
COPY ./aliases.sh /home/laradock/aliases.sh  
RUN echo "" >> ~/.bashrc && \  
echo "# Load Custom Aliases" >> ~/.bashrc && \  
echo "source /home/laradock/aliases.sh" >> ~/.bashrc && \  
echo "" >> ~/.bashrc && \  
sed -i 's/\r//' /home/laradock/aliases.sh && \  
sed -i 's/^#! \/bin\/sh/#! \/bin\/bash/' /home/laradock/aliases.sh  
  
USER root  
RUN echo "" >> ~/.bashrc && \  
echo "# Load Custom Aliases" >> ~/.bashrc && \  
echo "source /home/laradock/aliases.sh" >> ~/.bashrc && \  
echo "" >> ~/.bashrc && \  
sed -i 's/\r//' /home/laradock/aliases.sh && \  
sed -i 's/^#! \/bin\/sh/#! \/bin\/bash/' /home/laradock/aliases.sh  
  
#####################################  
# xDebug:  
#####################################  
  
ARG INSTALL_XDEBUG=false  
RUN if [ ${INSTALL_XDEBUG} = true ]; then \  
# Load the xdebug extension only with phpunit commands  
apt-get update && \  
apt-get install -y --force-yes php7.1-xdebug && \  
sed -i 's/^;//g' /etc/php/7.1/cli/conf.d/20-xdebug.ini && \  
echo "alias phpunit='php -dzend_extension=xdebug.so
/var/www/vendor/bin/phpunit'" >> ~/.bashrc \  
;fi  
# ADD for REMOTE debugging  
COPY ./xdebug.ini /etc/php/7.1/cli/conf.d/xdebug.ini  
  
#####################################  
# ssh:  
#####################################  
ARG INSTALL_WORKSPACE_SSH=false  
ENV INSTALL_WORKSPACE_SSH ${INSTALL_WORKSPACE_SSH}  
  
ADD insecure_id_rsa /tmp/id_rsa  
ADD insecure_id_rsa.pub /tmp/id_rsa.pub  
  
RUN if [ ${INSTALL_WORKSPACE_SSH} = true ]; then \  
rm -f /etc/service/sshd/down && \  
cat /tmp/id_rsa.pub >> /root/.ssh/authorized_keys \  
&& cat /tmp/id_rsa.pub >> /root/.ssh/id_rsa.pub \  
&& cat /tmp/id_rsa >> /root/.ssh/id_rsa \  
&& rm -f /tmp/id_rsa* \  
&& chmod 644 /root/.ssh/authorized_keys /root/.ssh/id_rsa.pub \  
&& chmod 400 /root/.ssh/id_rsa \  
;fi  
  
#####################################  
# MongoDB:  
#####################################  
# Check if Mongo needs to be installed  
ARG INSTALL_MONGO=true  
ENV INSTALL_MONGO ${INSTALL_MONGO}  
RUN if [ ${INSTALL_MONGO} = true ]; then \  
# Install the mongodb extension  
pecl install mongodb && \  
echo "extension=mongodb.so" >> /etc/php/7.1/mods-available/mongodb.ini && \  
ln -s /etc/php/7.1/mods-available/mongodb.ini
/etc/php/7.1/cli/conf.d/30-mongodb.ini \  
;fi  
  
#####################################  
# PHP REDIS EXTENSION FOR PHP 7.1  
#####################################  
  
ARG INSTALL_PHPREDIS=true  
ENV INSTALL_PHPREDIS ${INSTALL_PHPREDIS}  
RUN if [ ${INSTALL_PHPREDIS} = true ]; then \  
# Install Php Redis extension  
printf "\n" | pecl -q install -o -f redis && \  
echo "extension=redis.so" >> /etc/php/7.1/mods-available/redis.ini && \  
phpenmod redis \  
;fi  
  
USER laradock  
  
#####################################  
# Node / NVM:  
#####################################  
# Check if NVM needs to be installed  
ARG NODE_VERSION=stable  
ENV NODE_VERSION ${NODE_VERSION}  
ARG INSTALL_NODE=true  
ENV INSTALL_NODE ${INSTALL_NODE}  
ENV NVM_DIR /home/laradock/.nvm  
RUN if [ ${INSTALL_NODE} = true ]; then \  
# Install nvm (A Node Version Manager)  
curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.1/install.sh |
bash && \  
. $NVM_DIR/nvm.sh && \  
nvm install ${NODE_VERSION} && \  
nvm use ${NODE_VERSION} && \  
nvm alias ${NODE_VERSION} && \  
npm install -g gulp bower vue-cli \  
;fi  
  
# Wouldn't execute when added to the RUN statement in the above block  
# Source NVM when loading bash since ~/.profile isn't loaded on non-login
shell  
RUN if [ ${INSTALL_NODE} = true ]; then \  
echo "" >> ~/.bashrc && \  
echo 'export NVM_DIR="$HOME/.nvm"' >> ~/.bashrc && \  
echo '[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh" # This loads nvm' >>
~/.bashrc \  
;fi  
  
# Add NVM binaries to root's .bashrc  
USER root  
  
RUN if [ ${INSTALL_NODE} = true ]; then \  
echo "" >> ~/.bashrc && \  
echo 'export NVM_DIR="/home/laradock/.nvm"' >> ~/.bashrc && \  
echo '[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh" # This loads nvm' >>
~/.bashrc \  
;fi  
  
#####################################  
# YARN:  
#####################################  
  
USER laradock  
  
ARG INSTALL_YARN=true  
ENV INSTALL_YARN ${INSTALL_YARN}  
ARG YARN_VERSION=latest  
ENV YARN_VERSION ${YARN_VERSION}  
  
RUN if [ ${INSTALL_YARN} = true ]; then \  
[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh" && \  
if [ ${YARN_VERSION} = "latest" ]; then \  
curl -o- -L https://yarnpkg.com/install.sh | bash; \  
else \  
curl -o- -L https://yarnpkg.com/install.sh | bash -s -- --version
${YARN_VERSION}; \  
fi && \  
echo "" >> ~/.bashrc && \  
echo 'export PATH="$HOME/.yarn/bin:$PATH"' >> ~/.bashrc \  
;fi  
  
# Add YARN binaries to root's .bashrc  
USER root  
  
RUN if [ ${INSTALL_YARN} = true ]; then \  
echo "" >> ~/.bashrc && \  
echo 'export YARN_DIR="/home/laradock/.yarn"' >> ~/.bashrc && \  
echo 'export PATH="$YARN_DIR/bin:$PATH"' >> ~/.bashrc \  
;fi  
  
#####################################  
# Non-root user : PHPUnit path  
#####################################  
# add ./vendor/bin to non-root user's bashrc (needed for phpunit)  
USER laradock  
  
RUN echo "" >> ~/.bashrc && \  
echo 'export PATH="/var/www/vendor/bin:$PATH"' >> ~/.bashrc  
  
#####################################  
# Laravel Artisan Alias  
#####################################  
USER root  
  
RUN echo "" >> ~/.bashrc && \  
echo 'alias art="php artisan"' >> ~/.bashrc  
  
#####################################  
# Laravel Installer:  
#####################################  
USER root  
  
ARG INSTALL_LARAVEL_INSTALLER=false  
ENV INSTALL_LARAVEL_INSTALLER ${INSTALL_LARAVEL_INSTALLER}  
  
RUN if [ ${INSTALL_LARAVEL_INSTALLER} = true ]; then \  
# Install the Laravel Installer  
echo "" >> ~/.bashrc && \  
echo 'export PATH="~/.composer/vendor/bin:$PATH"' >> ~/.bashrc \  
&& composer global require "laravel/installer" \  
;fi  
  
#####################################  
# Install golang  
# from https://github.com/docker-library/golang  
#####################################  
USER root  
  
ENV GOLANG_VERSION 1.9  
  
RUN curl -O https://storage.googleapis.com/golang/go1.9.linux-amd64.tar.gz &&
\  
tar -C /usr/local -xzf go1.9.linux-amd64.tar.gz && \  
rm go1.9.linux-amd64.tar.gz; \  
export PATH="/usr/local/go/bin:$PATH"; \  
echo 'export PATH="/usr/local/go/bin:$PATH"' >> ~/.bashrc; \  
go version  
  
#####################################  
# Install extra commands  
#####################################  
USER root  
  
RUN apt-get -y install iputils-ping wget mysql-client dnsutils silversearcher-
ag enca nmap redis-tools  
  
#  
#--------------------------------------------------------------------------  
# Final Touch  
#--------------------------------------------------------------------------  
#  
# Clean up  
USER root  
RUN apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Set default work directory  
WORKDIR /var/www  

