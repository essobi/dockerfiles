FROM ubuntu:16.04  
  
RUN apt-get update -y \  
&& apt-get install -y \  
ruby-sass \  
build-essential \  
rpm \  
php \  
libfontconfig \  
git \  
cpio \  
gettext \  
expect \  
curl \  
apt-transport-https \  
&& curl --silent https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-
key add - \  
&& echo "deb https://deb.nodesource.com/node_6.x xenial main" >
/etc/apt/sources.list.d/nodesource.list \  
&& apt-get update -y \  
&& apt-get install -y nodejs \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& gem install scss_lint \  
&& npm install --global npm@5.5.1 grunt-cli gulp-cli bower \  
&& php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" \  
&& php -r "if (hash_file('SHA384', 'composer-setup.php') ===
'544e09ee996cdf60ece3804abc52599c22b1f40f4323403c44d44fdfdd586475ca9813a858088ffbc1f233e9b180f061')
{ echo 'Composer Installer verified'; } else { echo 'Composer Installer
corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;" \  
&& php composer-setup.php \  
&& php -r "unlink('composer-setup.php');" \  
&& mv composer.phar //usr/local/bin/composer  
  
# This is used by bower to disable interactive mode  
ENV CI true  
  
COPY run.sh /run.sh  
COPY npm-login.sh /npm-login.sh  
  
VOLUME ["/tuleap"]  
VOLUME ["/srpms"]  
  
ENTRYPOINT ["/run.sh"]  

