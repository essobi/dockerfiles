# FROM docker/whalesay:latest  
#  
# RUN apt-get -y update && apt-get install -y fortunes  
#  
# RUN apt-get -y install sshfs  
# RUN apt-get -y install rsync  
# RUN apt-get -y install sshpass  
#  
# CMD echo "asdvef sd sdcsd f"  
  
FROM debian:stretch-slim  
MAINTAINER Jurgen Oldenburg <jurgen@pms72.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV LC_ALL en_US.UTF-8  
ENV LANGUAGE en_US:en  
  
RUN \  
apt-get update &&\  
apt-get -y \--no-install-recommends install locales apt-utils &&\  
echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen &&\  
locale-gen en_US.UTF-8 &&\  
/usr/sbin/update-locale LANG=en_US.UTF-8 &&\  
apt-get -y \--no-install-recommends install ca-certificates bzip2 tar gnupg
git php-apcu php-bcmath php-cli php-curl php-geoip php-gettext php-intl php-
json php-mbstring php-mcrypt php-xml php-xmlrpc php-zip openssh-client curl
software-properties-common gettext zip apt-transport-https ruby python python3
perl php7.0 &&\  
curl -sSL https://deb.nodesource.com/setup_6.x | bash - &&\  
apt-get -y \--no-install-recommends install nodejs &&\  
apt-get -y install sshfs &&\  
apt-get -y install rsync &&\  
apt-get -y install sshpass &&\  
apt-get autoclean && apt-get clean && apt-get autoremove  
  
RUN \  
sed -ri -e "s/^variables_order.*/variables_order=\"EGPCS\"/g"
/etc/php/7.0/cli/php.ini  
  
RUN \  
curl -sSL https://getcomposer.org/installer | php -- --filename=composer
--install-dir=/usr/bin &&\  
npm install --no-color --production --global gulp-cli webpack bower &&\  
rm -rf /root/.npm /root/.composer /tmp/* /var/lib/apt/lists/*  

