# Pull base image.  
FROM ubuntu:16.04  
# MAINTAINER  
LABEL ZomNex (Tyler Burr)  
  
# ENV  
ENV DEBIAN_FRONTEND noninteractive \  
HOME /var/www/html  
  
# Define working directory.  
WORKDIR /var/www/html  
  
# Install Requirements  
RUN \  
sed -i 's/# \\(.*multiverse$\\)/\1/g' /etc/apt/sources.list \  
&& apt -y update \  
&& apt -y upgrade \  
&& apt -y install software-properties-common \  
&& LC_ALL=C.UTF-8 add-apt-repository ppa:ondrej/php \  
&& LC_ALL=C.UTF-8 add-apt-repository -y ppa:chris-lea/redis-server \  
&& apt -y update \  
&& apt -y upgrade \  
&& apt-get install -y php7.2 php7.2-cli php7.2-gd php7.2-mysql php7.2-pdo
php7.2-mbstring php7.2-tokenizer php7.2-bcmath php7.2-xml php7.2-fpm
php7.2-curl php7.2-zip nginx curl tar unzip git redis-server \  
&& useradd -m -d /home/container container \  
&& mkdir -p /var/www/html /run/nginx \  
# Pterodactyl Install  
&& curl -Lo panel.tar.gz
https://github.com/pterodactyl/panel/releases/download/v0.7.6/panel.tar.gz \  
&& tar --strip-components=1 -xzvf panel.tar.gz \  
&& rm -rf panel.tar.gz \  
&& chmod -R 755 storage/* bootstrap/cache \  
# Composer Install  
&& curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer \  
&& cp .env.example .env \  
&& composer install --ansi --no-dev  
# Set environment variables.  
USER container  
  
# Define default command.  
CMD ["/bin/bash"]  
  
COPY ./manifest /  
  
EXPOSE 80 443  
ENTRYPOINT [ "/bin/ash", "/entrypoint.sh" ]

