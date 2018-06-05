FROM php:7.1  
  
# The main goal of this image is to be able to rum composer under specific PHP
versions.  
  
ARG CONTAINER_USER='composer'  
  
ENV DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get -y update && \  
apt-get -y upgrade && \  
apt-get -y install \  
git \  
inotify-tools \  
zip \  
unzip && \  
  
docker-php-ext-install \  
sockets && \  
  
# creates composer user  
useradd -m -u 1000 -s /usr/bin/zsh "${CONTAINER_USER}" && \  
  
# installs composer  
php -r "copy('https://raw.githubusercontent.com/exadra37-docker-
images/php7-composer/6e6b2fe96e319275e7463b929ae74a6c94c95bca/src/installer/composer-
setup.php', 'composer-setup.php');" && \  
php -r "if (hash_file('SHA384', 'composer-setup.php') ===
'544e09ee996cdf60ece3804abc52599c22b1f40f4323403c44d44fdfdd586475ca9813a858088ffbc1f233e9b180f061')
{ echo 'Installer verified'; } else { echo 'Installer corrupt';
unlink('composer-setup.php'); } echo PHP_EOL;" && \  
php composer-setup.php && \  
php -r "unlink('composer-setup.php');" && \  
mv composer.phar /usr/local/bin/composer && \  
composer  
  
# Any file copied after USER directive will belong always to root... WTF
Docker still have this bug after so many years!!!  
# So need to handle this manually....  
COPY ./bash/entrypoint.sh "/home/${CONTAINER_USER}/.entrypoint.sh"  
RUN chown "${CONTAINER_USER}:${CONTAINER_USER}"
"/home/${CONTAINER_USER}/.entrypoint.sh"  
  
USER "${CONTAINER_USER}"  
# If we don't create manually the WORKDIR Docker will create it for us but
will belong to root...  
# One more example where the USER directive is not respected!!!  
RUN mkdir "${HOME}/app"  
WORKDIR "/home/${CONTAINER_USER}/app"  
# The entrypoint borrowed from the official composer image  
ENTRYPOINT ["/home/composer/.entrypoint.sh"]  
  
CMD ["composer"]  

