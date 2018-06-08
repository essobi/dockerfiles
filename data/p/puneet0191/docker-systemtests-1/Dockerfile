# Joomla! System tests  
FROM ubuntu:xenial  
  
# Set correct environment variables.  
ENV HOME /root  
  
# update the package sources  
RUN apt-get update -qq  
  
RUN dpkg-divert --local \--rename --add /sbin/initctl && \  
ln -sf /bin/true /sbin/initctl && \  
mkdir /var/run/sshd && \  
mkdir /run/php && \  
  
apt-get update && \  
apt-get install -y --no-install-recommends apt-utils \  
software-properties-common \  
python-software-properties \  
language-pack-en-base && \  
  
LC_ALL=en_US.UTF-8 add-apt-repository ppa:ondrej/php && \  
  
apt-get update && apt-get upgrade -y  
  
# we use the enviroment variable to stop debconf from asking questions..  
RUN DEBIAN_FRONTEND='noninteractive' apt-get install -y zip mysql-server
apache2 mysql-client php7.1 \  
php7.1-fpm php7.1-cli php7.1-curl php7.1-gd php7.1-mysql php7.1-zip php7.1-xml
php7.1-intl php7.1-mbstring libapache2-mod-php7.1 curl \  
wget unzip git fluxbox libxss1 libappindicator1 libindicator7 openjdk-8-jre
xvfb gconf-service fonts-liberation \  
dbus xdg-utils libasound2 libqt4-dbus libqt4-network libqtcore4 libqtgui4
libpython2.7 libqt4-xml libaudio2 fontconfig nodejs npm  
  
# package install is finished, clean up  
RUN apt-get clean # && rm -rf /var/lib/apt/lists/*  
  
# Create testing directory  
RUN mkdir -p /tests/www  
  
# Disable remote database security requirements.  
ENV JOOMLA_INSTALLATION_DISABLE_LOCALHOST_CHECK=1  
# Apache site conf  
ADD config/000-default.conf /etc/apache2/sites-available/000-default.conf  
  
# clean up tmp files (we don't need them for the image)  
RUN rm -rf /tmp/* /var/tmp/*  
  
# Composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=bin
--filename=composer  
RUN composer self-update  
RUN git config --global http.postBuffer 524288000  
  
RUN wget https://dl.google.com/linux/direct/google-chrome-
stable_current_amd64.deb  
RUN dpkg -i google-chrome*.deb  
  
# Start Apache and MySQL  
CMD apache2ctl -D FOREGROUND  
EXPOSE 3306  

