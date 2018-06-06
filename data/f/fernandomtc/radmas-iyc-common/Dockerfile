FROM ubuntu:14.04.3  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# install build tools  
RUN \  
sed -i 's/# \\(.*multiverse$\\)/\1/g' /etc/apt/sources.list && \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y build-essential && \  
apt-get install -y software-properties-common && \  
apt-get install -y byobu \  
curl \  
git \  
htop \  
man \  
unzip \  
vim \  
wget  
  
RUN apt-get update && apt-get install -y \  
zlib1g-dev  
  
# install PHP common dependencies  
RUN apt-get update && apt-get install -y \  
php5-cli \  
php5-dev \  
php5-json \  
php5-curl \  
php5-mongo \  
php5-gd \  
php5-intl \  
php-apc \  
php5-gearman \  
gearman-job-server \  
php-pear \  
phpunit  
  
# WKHTMLtoPDF dependencies  
RUN apt-get update && apt-get install -y \  
fontconfig \  
libfontconfig1 \  
libfreetype6 \  
libpng12-0 \  
zlib1g \  
libjpeg-turbo8 \  
libssl1.0.0 \  
libx11-6 \  
libxext6 \  
libxrender1 \  
libstdc++6 \  
libc6  
  
# Update ext-mongo  
RUN pecl install mongo  
  
# WKHTMLtoPDF  
ADD wkhtmltox-0.12.1-trusty-amd64.deb /wkhtmltox-0.12.1-trusty-amd64.deb  
RUN dpkg -i /wkhtmltox-0.12.1-trusty-amd64.deb  
RUN ln -s /usr/local/bin/wkhtmltopdf /usr/bin/.  
  
# install Ruby  
RUN \  
apt-get update && \  
apt-get install -y ruby1.9.3  
  
RUN gem install premailer nokogiri  
  
RUN \  
rm -rf /var/lib/apt/lists/*  
  
CMD /bin/bash  

