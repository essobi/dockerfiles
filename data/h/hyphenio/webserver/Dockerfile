FROM hyphenio/ssh  
MAINTAINER Hyphen IO <services@hyphenio.com.au>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN echo "deb http://ppa.launchpad.net/ondrej/php/ubuntu xenial main" >>
/etc/apt/sources.list  
RUN echo "deb-src http://ppa.launchpad.net/nginx/stable/ubuntu xenial main "
>> /etc/apt/sources.list  
  
RUN apt-key adv --recv-keys --keyserver keyserver.ubuntu.com --recv
14AA40EC0831756756D7F66C4F4EA0AAE5267A6C  
RUN apt-key adv --recv-keys --keyserver keyserver.ubuntu.com --recv
8B3981E7A6852F782CC4951600A6F0A3C300EE8C  
  
RUN apt-key update  
RUN apt-get update  
RUN apt-get -y dist-upgrade  
  
RUN apt-get install -y \  
nginx \  
openssl \  
xz-utils \  
php \  
php-fpm \  
php-cli \  
php-tidy \  
php-xml \  
php-bcmath \  
php-gd \  
php-mbstring \  
php-curl \  
php-mysql \  
php-zip \  
php-mcrypt \  
php-imagick  
  
RUN mkdir -p /opt/apps && \  
mkdir -p /root/.composer && \  
mkdir -p /opt/node && \  
mkdir -p /run/php && \  
chmod 777 /run/php  
  
ADD nginx.conf /etc/supervisor/conf.d/nginx.conf  
ADD phpfpm.conf /etc/supervisor/conf.d/phpfpm.conf  
ADD https://getcomposer.org/composer.phar /usr/local/bin/composer  
RUN chmod 755 /usr/local/bin/composer  
RUN F='9cd350c5d095d397b263' && S='6296e20a712bd34186b4' && echo
"{\"bitbucket-oauth\":{},\"github-oauth\":{\"github.com\":\"$F$S\"},\"gitlab-
oauth\":{},\"http-basic\":{}}" >> /root/.composer/auth.json  
  
ADD https://nodejs.org/dist/v6.3.0/node-v6.3.0-linux-x64.tar.xz
/tmp/node.tar.xz  
RUN tar xvf /tmp/node.tar.xz --strip-components=1 -C /opt/node  
RUN rm /tmp/node.tar.xz  
  
RUN sed -i \  
-e 's/.*# server_tokens off;/server_tokens off;/' \  
-e 's/^worker_connections 768;/worker_connections 1024;/' \  
-e 's/^worker_processes auto;/worker_processes 5;/' \  
/etc/nginx/nginx.conf  
  
RUN sed -i \  
's/try_files.*404;/return 404;/' \  
/etc/nginx/sites-available/default  
  
RUN sed -i \  
-e 's/^pm\\.start_servers \= 2/pm\\.start_servers \= 5/' \  
-e 's/^pm\\.min_spare_servers \= 1/pm\\.min_spare_servers \= 2/' \  
-e 's/^pm\\.max_spare_servers \= 3/pm\\.max_spare_servers \= 5/' \  
/etc/php/7.0/fpm/pool.d/www.conf  
  
RUN echo "export PATH=/opt/node/bin:$PATH" >> /root/.bashrc && \  
echo "export NODE_PATH=/opt/node/lib/node_modules" >> /root/.bashrc && \  
echo "alias fetch='GIT_SSH=~/.ssh/gitwrapper.sh git fetch origin'" >>
/root/.bashrc && \  
echo "alias gd='git diff'" >> /root/.bashrc && \  
echo "alias gl='git log'" >> /root/.bashrc && \  
echo "alias gs='git status'" >> /root/.bashrc && \  
echo "alias pull='GIT_SSH=~/.ssh/gitwrapper.sh git pull origin'" >>
/root/.bashrc && \  
echo "alias clone='GIT_SSH=~/.ssh/gitwrapper.sh git clone'" >> /root/.bashrc
&& \  
echo "alias push='GIT_SSH=~/.ssh/gitwrapper.sh git push'" >> /root/.bashrc &&
\  
echo "alias ga='git add -A'" >> /root/.bashrc && \  
echo "alias cont='git rebase --continue'" >> /root/.bashrc && \  
echo "alias rebase='git rebase'" >> /root/.bashrc && \  
echo "alias stash='git stash'" >> /root/.bashrc && \  
echo "alias sapply='git stash apply'" >> /root/.bashrc && \  
echo "alias gsa='cd /opt/apps/gsa'" >> /root/.bashrc && \  
echo "alias cal='cd /opt/apps/gfp_cal'" >> /root/.bashrc && \  
echo "alias sso='cd /opt/apps/gfp_sso'" >> /root/.bashrc && \  
echo "alias fcl='cd /opt/apps/gfp_fcl'" >> /root/.bashrc && \  
echo "alias stl='cd /opt/apps/gfp_stl'" >> /root/.bashrc && \  
echo "alias tinker='php artisan tinker'" >> /root/.bashrc  
  
RUN apt-get clean && apt-get autoclean && apt-get -y autoremove  
  
EXPOSE 80 443  

