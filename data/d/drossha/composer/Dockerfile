FROM drossha/php  
  
ENV COMPOSER_ALLOW_SUPERUSER=1  
  
RUN apt-get update --allow-unauthenticated && apt-get install git --allow-
unauthenticated -y  
  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
\  
&& php -r "if (hash_file('SHA384', 'composer-setup.php') ===
'669656bab3166a7aff8a7506b8cb2d1c292f042046c5a994c43155c0be6190fa0355160742ab2e1c88d40d5be660b410')
{ echo 'Installer verified'; } else { echo 'Installer corrupt';
unlink('composer-setup.php'); } echo PHP_EOL;" \  
&& php composer-setup.php \--install-dir=/usr/local/bin \--filename=composer \  
&& php -r "unlink('composer-setup.php');"  
RUN composer global require "hirak/prestissimo:^0.3"  
RUN composer global require fxp/composer-asset-plugin  
RUN composer config \--global github-oauth.github.com
50d0f2d7993cd829c34f362b93400839088e4b49  
  
RUN mkdir /root/.ssh/  
ADD id_rsa /root/.ssh/id_rsa  
  
RUN chmod 400 /root/.ssh/id_rsa  
  
RUN touch /root/.ssh/known_hosts  
RUN ssh-keyscan bitbucket.org >> /root/.ssh/known_hosts  
  
RUN echo " IdentityFile ~/.ssh/id_rsa" >> /etc/ssh/ssh_config  
  
ENTRYPOINT ["/usr/local/bin/composer"]  

