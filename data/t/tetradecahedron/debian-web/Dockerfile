FROM debian:stable-slim  
LABEL maintainer="tetradecahedron"  
# Copy local files to container  
COPY files/ /  
  
# Environment variables  
ENV PS1="$(whoami)@$(hostname):$(pwd)$ " \  
HOME="/root" \  
TERM="xterm"  
# Install and configure base utilities  
RUN apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -y \  
vim \  
curl \  
unzip \  
sqlite3 \  
apache2 \  
php7.0 \  
php7.0-curl \  
php7.0-gd \  
php7.0-intl \  
php7.0-mcrypt \  
php7.0-mbstring \  
php7.0-sqlite3 \  
php7.0-xml \  
&& groupmod -g 1000 users \  
&& useradd -u 911 -U -d /config -s /bin/false abc \  
&& usermod -G users abc \  
&& mkdir -p \  
/defaults \  
&& rm /var/www/html/* \  
&& tar xzf /s6-overlay-amd64.tar.gz -C / \  
&& rm /s6-overlay-amd64.tar.gz \  
&& apt-get autoremove -y \  
&& apt-get clean -y  
  
WORKDIR /var/www/html  
VOLUME /var/www/html  
  
EXPOSE 80  
  
ENTRYPOINT ["/init"]  

