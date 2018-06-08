FROM offbyone/supervisord:1.1.0  
MAINTAINER Craig Kimerer <craig@offxone.com>  
  
# Install requirements  
RUN apt-get update && apt-get upgrade -y  
RUN apt-get install -y ssh wget vim less zip cron lsof git sendmail nodejs-
legacy npm python-pygments  
RUN npm install ws  
  
# Add users  
RUN echo "git:x:2000:2000:user for phabricator ssh:/srv/phabricator:/bin/bash"
>> /etc/passwd  
RUN echo "phab-daemon:x:2001:2000:user for phabricator
daemons:/srv/phabricator:/bin/bash" >> /etc/passwd  
RUN echo "wwwgrp-phabricator:!:2000:nginx" >> /etc/group  
  
# Set up the Phabricator code base  
RUN mkdir /srv/phabricator  
RUN chown git:wwwgrp-phabricator /srv/phabricator  
USER git  
WORKDIR /srv/phabricator  
RUN git clone git://github.com/facebook/libphutil.git  
RUN git clone git://github.com/facebook/arcanist.git  
RUN git clone git://github.com/facebook/phabricator.git  
USER root  
WORKDIR /  
  
# Install requirements  
RUN apt-get -y install nginx php5 php5-fpm php5-mcrypt php5-mysql php5-gd
php5-dev php5-curl php-apc php5-cli php5-json php5-ldap python-Pygments nodejs
sudo  
  
# Expose Nginx on port 80 and 443  
EXPOSE 80  
EXPOSE 443  
# Expose Aphlict (notification server) on 22280  
EXPOSE 22280  
# Expose SSH port 24 (Git SSH will be on 22, regular SSH on 24)  
EXPOSE 24  
# Helper scripts around running & upgrading phabricator  
ADD configure-instance.sh /srv/phabricator/  
ADD upgrade-phabricator.sh /srv/phabricator/  
ADD startup.sh /  
  
# Add service config files  
ADD nginx.conf.org /etc/nginx/  
ADD nginx-ssl.conf.org /etc/nginx/  
ADD fastcgi.conf /etc/nginx/  
ADD php-fpm.conf /etc/php5/fpm/  
ADD php.ini /etc/php5/fpm/  
  
# Add necessary git entries entries  
RUN echo "git ALL=(phab-daemon) SETENV: NOPASSWD: /usr/bin/git-upload-pack,
/usr/bin/git-receive-pack" > /etc/sudoers.d/git  
  
# Add Supervisord config files  
ADD cron.sv.conf /etc/supervisor/conf.d/  
ADD nginx.sv.conf /etc/supervisor/conf.d/  
ADD phab-sshd.sv.conf /etc/supervisor/conf.d/  
ADD php5-fpm.sv.conf /etc/supervisor/conf.d/  
ADD sshd.sv.conf /etc/supervisor/conf.d/  
  
# Add the cron for upgrading phabricator  
ADD upgrade-phabricator.cron /etc/cron.d/phabricator  
  
# Move the default SSH to port 24  
RUN echo "" >> /etc/ssh/sshd_config  
RUN echo "Port 24" >> /etc/ssh/sshd_config  
  
RUN mkdir -p /var/repo/  
RUN chown phab-daemon:2000 /var/repo/  
  
# Configure Phabricator SSH service  
RUN mkdir /etc/phabricator-ssh  
RUN mkdir /var/run/sshd/  
RUN chmod 0755 /var/run/sshd  
ADD sshd_config.phabricator /etc/phabricator-ssh/  
ADD phabricator-ssh-hook.sh /etc/phabricator-ssh/  
RUN chown root:root /etc/phabricator-ssh/*  
  
CMD ./startup.sh && supervisord  

