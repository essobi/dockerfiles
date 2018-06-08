FROM ubuntu  
MAINTAINER Alessandro Lattao <me@alessandrolattao.com>  
  
# Let the conatiner know that there is no tty  
ENV DEBIAN_FRONTEND noninteractive  
  
# Copio l'entrypoint.sh  
COPY bin/entrypoint.sh /entrypoint.sh  
  
# Copio lo script per notificare newrelic di ogni nuova build  
COPY bin/new_relic_deployment_record.sh
/usr/bin/new_relic_deployment_record.sh  
  
# Copio lo script per notificare newrelic di ogni nuova build  
COPY bin/cleanup_s3.sh /usr/bin/cleanup_s3.sh  
  
# Copio lo script per notificare newrelic di ogni nuova build  
COPY bin/getLastBitbucketSuccessfulHash.js
/usr/bin/getLastBitbucketSuccessfulHash.js  
  
# Set bash as default shell  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
RUN debconf-set-selections <<< 'mysql-server mysql-server/root_password
password pipelines'  
RUN debconf-set-selections <<< 'mysql-server mysql-server/root_password_again
password pipelines'  
  
RUN set -x && \  
apt-get update && \  
apt-get install -y software-properties-common wget && \  
nginx=stable && \  
add-apt-repository ppa:nginx/$nginx && \  
# Configure Elixir  
apt-get update && \  
apt-get install curl && \  
apt-get upgrade -y && \  
BUILD_PACKAGES="php7.0 locales awscli vim mysql-server nginx php7.0-fpm unzip
zip composer vim phpmyadmin php7.0-soap php7.0-gd php7.0-mbstring php7.0-intl
php7.0-bcmath php7.0-mysql php7.0-curl php7.0-dev php7.0-zip inkscape optipng
gphoto2 exiftool imagemagick webp gimp" && \  
apt-get -y install $BUILD_PACKAGES && \  
# Installo le dipendenze per il resize delle immagini (per www2)  
apt-get -y install python-pip libjpeg-dev && \  
CC="cc -mavx2" pip install -U --force-reinstall pillow-simd && \  
  
rm /etc/nginx/sites-enabled/default && \  
rm /etc/php/7.0/fpm/pool.d/www.conf && \  
# Avvio e spengo php-fpm cosi' crea le cartelle di configurazione (bugfix)  
service php7.0-fpm start && \  
service php7.0-fpm stop && \  
update-rc.d php7.0-fpm defaults && \  
chmod +x /entrypoint.sh && \  
chmod +x /usr/bin/new_relic_deployment_record.sh && \  
chmod +x /usr/bin/getLastBitbucketSuccessfulHash.js && \  
# Configuro il locale  
locale-gen it_IT.UTF-8 && \  
update-locale LC_ALL=it_IT.UTF-8 && \  
# Installo Phalcon  
curl -s
https://packagecloud.io/install/repositories/phalcon/stable/script.deb.sh |
bash && \  
apt-get install php7.0-phalcon && \  
  
# Installo node tramite nvm  
curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.8/install.sh |
bash && \  
export NVM_DIR="$HOME/.nvm" && \  
[ -s "$NVM_DIR/nvm.sh" ] && \\. "$NVM_DIR/nvm.sh" && \  
nvm install v8 && \  
nvm use v8 && \  
# Aggiorno NPM  
npm install npm@latest -g && \  
npm set progress=false && \  
npm config set registry http://registry.npmjs.org/ && \  
npm install -g yarn && \  
  
apt-get remove --purge -y software-properties-common && \  
apt-get autoremove -y && \  
apt-get clean && \  
apt-get autoclean  
  
# Installa Chrome Dev Package per Puppeteer  
RUN apt-get update && apt-get install -y wget --no-install-recommends \  
&& wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add - \  
&& sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable
main" >> /etc/apt/sources.list.d/google.list' \  
&& apt-get update \  
&& apt-get install -y google-chrome-unstable fonts-ipafont-gothic fonts-wqy-
zenhei fonts-thai-tlwg fonts-kacst ttf-freefont \  
\--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /src/*.deb  
  
  
# Configure Nginx  
ADD sites-enabled/default.conf /etc/nginx/sites-available/default.conf  
ADD sites-enabled/default.phalcon.conf /etc/nginx/sites-
available/default.phalcon.conf  
ADD sites-enabled/default.slim.conf /etc/nginx/sites-
available/default.slim.conf  
ADD sites-enabled/default.symfony.conf /etc/nginx/sites-
available/default.symfony.conf  
  
# Configure php-fpm  
ADD pool.d/www.conf /etc/php/7.0/fpm/pool.d/www.conf  
  
# Avvio l'entrypoint  
ENTRYPOINT ["/entrypoint.sh"]  

