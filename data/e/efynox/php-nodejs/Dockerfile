FROM debian:stretch-slim  
  
MAINTAINER Efynox <efynox@protonmail.com>  
  
RUN apt-get update \  
&& apt-get install -y git-core php php7.0-mbstring php7.0-dom php7.0-zip wget
xz-utils git-ftp \  
&& wget https://nodejs.org/dist/v6.9.4/node-v6.9.4-linux-x64.tar.xz \  
&& tar -C /usr/local --strip-components 1 -xJf node-v6.9.4-linux-x64.tar.xz \  
&& rm node-v6.9.4-linux-x64.tar.xz \  
&& php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" \  
&& php -r "if (hash_file('SHA384', 'composer-setup.php') ===
'55d6ead61b29c7bdee5cccfb50076874187bd9f21f65d8991d46ec5cc90518f447387fb9f76ebae1fbbacf329e583e30')
{ echo 'Installer verified'; } else { echo 'Installer corrupt';
unlink('composer-setup.php'); } echo PHP_EOL;" \  
&& php composer-setup.php \  
&& php -r "unlink('composer-setup.php');" \  
&& mv composer.phar /usr/local/bin/composer

