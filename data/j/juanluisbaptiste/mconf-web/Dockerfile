FROM ubuntu:14.04  
MAINTAINER Juan Luis Baptiste juan.baptiste@gmail.com  
ENV DEBIAN_FRONTEND noninteractive  
ENV TERM linux  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
ENV MCONF_USER mconf  
ENV MCONF_GROUP www-data  
ENV MCONF_ROOT /var/www/mconf-web/  
ENV MCONF_DB_NAME mconf  
ENV MCONF_DATA_DIR "/data"  
ENV MCONF_BACKUP_DIR "${MCONF_DATA_DIR}/backups"  
#ENV MCONF_VERSION=708b09447a5e05a0d008a8520d31eb7c5a5c64d2  
ENV MCONF_VERSION=v2.1.0  
RUN apt-get -y update && \  
apt-get -y dist-upgrade && \  
apt-get install -y curl make git-core libruby aspell-es aspell-en \  
libxml2-dev libxslt1-dev libmagickcore-dev libmagickwand-dev \  
imagemagick libmysqlclient-dev zlib1g-dev build-essential nfs-common \  
libreadline-dev libffi-dev libcurl4-openssl-dev mysql-client \  
openjdk-7-jre apache2 libapache2-mod-xsendfile \  
apache2-dev monit supervisor wget  
COPY /etc/supervisor/conf.d/*.conf /etc/supervisor/conf.d/  
  
#Add apache2 configuration  
COPY etc/apache2/apache2.conf /etc/apache2/  
COPY etc/apache2/sites-available/mconf-web.conf /etc/apache2/sites-available/  
RUN a2enmod rewrite && \  
a2enmod xsendfile && \  
a2ensite mconf-web  
  
#Create mconf user, create backup scrpts directories and add to sudoers  
RUN useradd -ms /bin/bash ${MCONF_USER} && \  
adduser ${MCONF_USER} $MCONF_GROUP && \  
chown -R ${MCONF_USER}:$MCONF_GROUP /var/www/ && \  
mkdir -p /opt/mconf/{scripts,backups}/ && \  
mkdir -p /opt/mconf/var/tmp && \  
touch /opt/mconf/var/tmp/firsttime && \  
echo "${MCONF_USER} ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers  
  
#Configure monit  
RUN sed -i -re 's/(daemon)\s+\w+/\1 60/gi' /etc/monit/monitrc && \  
sed -i '/set httpd port 2812/s/^#//g' /etc/monit/monitrc && \  
sed -i '/use address localhost/s/^#//g' /etc/monit/monitrc && \  
sed -i '/allow localhost/s/^#//g' /etc/monit/monitrc && \  
wget https://raw.github.com/mconf/mconf-
web/master/config/monit/resque_workers.monitrc -O
/etc/monit/conf.d/resque_workers.monitrc && \  
sed -i -e "s/\/mconf-web\/current/\/mconf-web/g"
/etc/monit/conf.d/resque_workers.monitrc  
  
#configure logrotate  
RUN wget https://raw.github.com/mconf/mconf-web/master/config/logrotate/mconf-
web -O /etc/logrotate.d/mconf-web && \  
chown root:root /etc/logrotate.d/mconf-web && \  
chmod 644 /etc/logrotate.d/mconf-web && \  
logrotate -s /var/lib/logrotate/status /etc/logrotate.d/mconf-web  
  
#Mconf installation  
USER ${MCONF_USER}  
#Install renv  
RUN git clone git://github.com/rbenv/rbenv.git ~/.rbenv && \  
echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.bash_profile && \  
echo 'eval "$(rbenv init -)"' >> ~/.bash_profile && \  
bash -l -c "source ~/.bash_profile"  
  
# install ruby build and bundler  
RUN git clone git://github.com/rbenv/ruby-build.git ~/.rbenv/plugins/ruby-
build && \  
bash -l -c "rbenv install 2.2.0" && \  
bash -l -c "rbenv rehash" && \  
bash -l -c "rbenv global 2.2.0" && \  
bash -l -c "rbenv version" && \  
bash -l -c "gem install bundler -v '1.7.2'" && \  
bash -l -c "rbenv rehash"  
WORKDIR /var/www  
#Download mconf MCONF_VERSION  
RUN bash -l -c "git clone git://github.com/mconf/mconf-web.git" && \  
chown -R ${MCONF_USER}:$MCONF_GROUP ${MCONF_ROOT}  
WORKDIR ${MCONF_ROOT}  
RUN bash -l -c "git checkout ${MCONF_VERSION}"  
#Install mconf  
USER root  
#update gems before installing passenger as root  
RUN gem install rubygems-update && \  
update_rubygems  
USER mconf  
RUN bash -l -c "bundle install --path vendor/bundle --without=development test
--clean"  
COPY database.yml ${MCONF_ROOT}config/  
COPY setup_conf.yml ${MCONF_ROOT}config/  
RUN bash -l -c "gem install rack:1.5.5 passenger:4.0.59" && \  
bash -l -c "rbenv rehash" && \  
bash -l -c "passenger-install-apache2-module -a" && \  
bash -l -c "passenger-install-apache2-module --snippet | sudo tee
/etc/apache2/conf-available/mconf-passenger.conf" && \  
sudo a2enconf mconf-passenger  
  
USER root  
# Add run script  
COPY run.sh /  
COPY functions.sh /  
COPY mconf_backup.sh /  
COPY mconf_restore.sh /  
RUN chmod 755 /*.sh && \  
touch ${MCONF_ROOT}tmp/restart.txt && \  
mkdir -p ${MCONF_BACKUP_DIR} && chown -R ${MCONF_USER} ${MCONF_DATA_DIR}  
USER ${MCONF_USER}  
RUN bash -l -c "bundle clean"  
  
EXPOSE 80  
VOLUME ["/data"]  
CMD ["/run.sh"]

