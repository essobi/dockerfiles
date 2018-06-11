## Tuleap All In One for development ##  
FROM centos:centos6  
  
MAINTAINER Manuel Vacelet, manuel.vacelet@enalean.com  
  
RUN yum install -y \  
epel-release \  
centos-release-scl \  
postfix \  
openssh-server \  
rsyslog \  
cronie && \  
yum install -y supervisor && \  
yum clean all  
  
# The later commend is meant to work around meld, distribute and supervisord  
# issues on centos6  
# http://stackoverflow.com/questions/7446187/no-module-named-pkg-resources  
  
COPY Tuleap.repo /etc/yum.repos.d/  
# Gitolite will not work out-of-the-box with an error like  
# "User gitolite not allowed because account is locked"  
# Given http://stackoverflow.com/a/15761971/1528413 you might want to trick  
# /etc/shadown but the following pam modification seems to do the trick too  
# It's better for as as it can be done before installing gitolite, hence  
# creating the user.  
# I still not understand why it's needed (just work without comment or tricks  
# on a fresh centos install)  
# Second sed is for cron  
# Cron: http://stackoverflow.com/a/21928878/1528413  
  
RUN sed -i '/session required pam_loginuid.so/c\\#session required
pam_loginuid.so' /etc/pam.d/sshd && \  
sed -i '/session required pam_loginuid.so/c\\#session required
pam_loginuid.so' /etc/pam.d/crond && \  
/sbin/service sshd start && \  
rpm --rebuilddb && \  
yum install -y \  
tuleap-install \  
tuleap-core-cvs \  
tuleap-core-subversion \  
tuleap-plugin-agiledashboard \  
tuleap-plugin-hudson \  
tuleap-plugin-git-gitolite3 \  
tuleap-plugin-graphontrackers \  
tuleap-theme-flamingparrot \  
tuleap-documentation \  
tuleap-customization-default \  
tuleap-api-explorer \  
java-1.8.0-openjdk \  
tuleap-plugin-ldap \  
tuleap-plugin-mediawiki \  
tuleap-core-mailman \  
tuleap-plugin-forumml \  
tuleap-plugin-fulltextsearch \  
tuleap-plugin-webdav \  
openldap-clients \  
php-markdown \  
php-ZendFramework2-Loader \  
php-jwt \  
php-paragonie-random-compat \  
vim \  
rh-php56-php-gd \  
rh-php56-php-pear \  
rh-php56-php-soap \  
rh-php56-php-mysqlnd \  
rh-php56-php-xml \  
rh-php56-php-mbstring \  
rh-php56-php-cli \  
rh-php56-php-opcache \  
rh-php56-php-process \  
rh-php56-php-pdo \  
rh-php56-php-fpm \  
rh-php56-php-ldap \  
rh-php56-php-pecl-xdebug \  
rh-php56-php-intl \  
rh-php56-php-bcmath php-amqplib-amqplib \  
nginx \  
php-mediawiki-tuleap-123 && \  
yum clean all && \  
rm -rf /usr/share/tuleap && \  
sed -i 's/inet_interfaces = localhost/inet_interfaces = all/'
/etc/postfix/main.cf  
  
# Add fr_FR.UTF-8 locale for translation using gettext  
RUN localedef -i fr_FR -c -f UTF-8 fr_FR.UTF-8  
  
COPY supervisord.conf /etc/supervisord.conf  
COPY xdebug-fpm.ini /etc/opt/rh/rh-php56/php.d/15-xdebug.ini  
  
COPY . /root/app  
  
## Run environement  
WORKDIR /root/app  
VOLUME [ "/data", "/usr/share/tuleap" ]  
EXPOSE 22 80 443  
CMD ["/root/app/run.sh"]  

