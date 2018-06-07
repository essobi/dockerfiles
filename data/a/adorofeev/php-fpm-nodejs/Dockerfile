FROM adorofeev/php-fpm:php71  
  
# switch to root (parent image uses www-data user)  
USER root  
  
# install nodejs  
RUN curl -s https://deb.nodesource.com/setup_8.x | bash  
RUN install_packages nodejs make g++  
  
# install yarn  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \  
echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
RUN install_packages yarn  
  
# allow ports<1024 to nodejs  
RUN install_packages libcap2-bin  
RUN /sbin/setcap CAP_NET_BIND_SERVICE=+eip /usr/bin/node  
  
# switch back to www-data  
USER www-data  
  
# expose webpack dev server to other docker containers  
EXPOSE 8080  

