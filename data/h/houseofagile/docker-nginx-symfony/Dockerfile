FROM houseofagile/docker-nginx-php-fpm:php7  
  
MAINTAINER Meillaud Jean-Christophe (jc@houseofagile.com)  
  
#Node install  
RUN apt-get update \  
&& apt-get install -y nodejs npm \  
&& npm install less -g && npm install -g bower \  
&& curl -sS https://getcomposer.org/installer | php -- --version=1.3.2
--install-dir=/usr/bin/ \  
&& mv /usr/bin/composer.phar /usr/bin/composer \  
&& mkdir /root/projects && mkdir /root/ssh-keys \  
&& echo "StrictHostKeyChecking no" >> /etc/ssh/ssh_config \  
&& apt-get clean && rm -rf /tmp/* /var/tmp/*  
  
ADD ./config/projects /root/projects  
ADD ./config/ssh-keys /root/ssh-keys  
  
ADD ./config/sm-config /root/.symfony-manager/sm-config  
ADD .bowerrc /root/.bowerrc  
ADD ./default-symfony-nginx.conf /root/docker-config/default-symfony-
nginx.conf  
  
RUN chown www-data -R /usr/share/nginx/ && \  
mkdir -p /root/docker-config && \  
rm /etc/nginx/sites-enabled/default && \  
mkdir -p /etc/my_init.d && \  
sed -i 's#%%php_fpm_sock_file%%#/run/php/php7.0-fpm.sock#g' /root/docker-
config/default-symfony-nginx.conf  
  
ADD setup-projects.sh /etc/my_init.d/10_setup-projects.sh  
RUN chmod +x /etc/my_init.d/10_setup-projects.sh  
  
EXPOSE 80  
CMD ["/sbin/my_init"]  

