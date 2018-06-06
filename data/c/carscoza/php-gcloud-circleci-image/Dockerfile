FROM php:7-cli-stretch  
MAINTAINER allan <allan@cars.co.za>  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && apt-get install -y -qq --no-install-recommends \  
wget unzip python openssh-client python-openssl libzip-dev \  
apt-transport-https ca-certificates curl gnupg2 \  
software-properties-common \  
&& apt-get clean  
  
# Install Docker...  
RUN curl -fsSL https://download.docker.com/linux/$(. /etc/os-release; echo
"$ID")/gpg | apt-key add -  
RUN add-apt-repository \  
"deb [arch=amd64] https://download.docker.com/linux/$(. /etc/os-release; echo
"$ID") \  
$(lsb_release -cs) \  
stable"  
RUN apt-get update && apt-get install -y -qq --no-install-recommends docker-ce  
  
# Install the Google Cloud SDK.  
ENV HOME /  
ENV CLOUDSDK_PYTHON_SITEPACKAGES 1  
RUN wget https://dl.google.com/dl/cloudsdk/channels/rapid/google-cloud-sdk.zip
&& unzip google-cloud-sdk.zip && rm google-cloud-sdk.zip  
RUN google-cloud-sdk/install.sh --usage-reporting=true \--path-update=true
\--bash-completion=true \--rc-path=/.bashrc --additional-components kubectl  
  
# Disable updater check for the whole installation.  
# Users won't be bugged with notifications to update to the latest version of
gcloud.  
RUN google-cloud-sdk/bin/gcloud config set \--installation
component_manager/disable_update_check true  
  
# Disable updater completely.  
# Running `gcloud components update` doesn't really do anything in a union FS.  
# Changes are lost on a subsequent run.  
RUN sed -i -- 's/\"disable_updater\": false/\"disable_updater\": true/g'
/google-cloud-sdk/lib/googlecloudsdk/core/config.json  
  
ENV PATH /google-cloud-sdk/bin:$PATH  
  
# Install required PHP extensions  
RUN docker-php-ext-install bcmath zip  
  
# Install composer... this is taken from the offical composer Dockerfile, look
there when looking to update the composer install  
ENV COMPOSER_ALLOW_SUPERUSER 1  
ENV COMPOSER_HOME /tmp  
ENV COMPOSER_VERSION 1.6.3  
RUN curl -s -f -L -o /tmp/installer.php
https://raw.githubusercontent.com/composer/getcomposer.org/b107d959a5924af895807021fcef4ffec5a76aa9/web/installer
\  
&& php -r " \  
\$signature =
'544e09ee996cdf60ece3804abc52599c22b1f40f4323403c44d44fdfdd586475ca9813a858088ffbc1f233e9b180f061';
\  
\$hash = hash('SHA384', file_get_contents('/tmp/installer.php')); \  
if (!hash_equals(\$signature, \$hash)) { \  
unlink('/tmp/installer.php'); \  
echo 'Integrity check failed, installer is either corrupt or worse.' .
PHP_EOL; \  
exit(1); \  
}" \  
&& php /tmp/installer.php --no-ansi --install-dir=/usr/bin --filename=composer
--version=${COMPOSER_VERSION} \  
&& composer --ansi --version --no-interaction \  
&& rm -rf /tmp/* /tmp/.htaccess  

