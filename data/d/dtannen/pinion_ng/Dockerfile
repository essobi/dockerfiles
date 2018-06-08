FROM ubuntu:14.04  
MAINTAINER David Tannenbaum <david@api.pinionate.com>  
  
# set some environment variables  
ENV APP_NAME pinionate-cms  
ENV APP_EMAIL app@pinionate.com  
ENV APP_DOMAIN cms.pinionate.com  
ENV APP_PATH /var/www/html/app  
ENV DEBIAN_FRONTEND noninteractive  
  
# upgrade the container  
RUN apt-get update && \  
apt-get upgrade -y  
  
# install some prerequisites  
RUN apt-get install -y software-properties-common curl build-essential \  
dos2unix gcc git libmcrypt4 libpcre3-dev memcached make python2.7-dev \  
python-pip re2c unattended-upgrades whois vim libnotify-bin nano wget \  
debconf-utils  
  
RUN apt-get update  
RUN apt-get install software-properties-common -y  
RUN apt-get install -y language-pack-en-base  
RUN LC_ALL=en_US.UTF-8 add-apt-repository ppa:ondrej/php -y  
RUN LC_ALL=en_US.UTF-8 apt-add-repository ppa:chris-lea/redis-server -y  
# add some repositories  
RUN apt-add-repository ppa:nginx/stable -y && \  
apt-get update  
  
# set the locale  
RUN echo "LC_ALL=en_US.UTF-8" >> /etc/default/locale && \  
locale-gen en_US.UTF-8 && \  
ln -sf /usr/share/zoneinfo/UTC /etc/localtime  
  
# setup bash  
COPY .bash_aliases /root  
  
# install nginx  
RUN apt-get install -y --force-yes nginx  
COPY nginx-site-conf /etc/nginx/sites-available/  
RUN rm -rf /etc/nginx/sites-available/default && \  
rm -rf /etc/nginx/sites-enabled/default && \  
ln -fs "/etc/nginx/sites-available/nginx-site-conf" "/etc/nginx/sites-
enabled/nginx-site-conf" && \  
sed -i -e"s/keepalive_timeout\s*65/keepalive_timeout 2/" /etc/nginx/nginx.conf
&& \  
sed -i -e"s/keepalive_timeout 2/keepalive_timeout 2;\n\tclient_max_body_size
100m/" /etc/nginx/nginx.conf && \  
echo "daemon off;" >> /etc/nginx/nginx.conf && \  
usermod -u 1000 www-data && \  
chown -Rf www-data.www-data /var/www/html/ && \  
sed -i -e"s/worker_processes 1/worker_processes 5/" /etc/nginx/nginx.conf  
VOLUME ["/var/cache/nginx"]  
VOLUME ["/var/log/nginx"]  
  
# install nodejs  
RUN apt-get install -y nodejs  
  
# upgrade node  
RUN curl -sL https://deb.nodesource.com/setup_7.x | sudo -E bash -  
RUN sudo apt-get install -y nodejs  
  
# install gulp  
RUN /usr/bin/npm install -g gulp  
  
# install bower  
RUN /usr/bin/npm install -g bower  
  
# install supervisor  
RUN apt-get install -y supervisor && \  
mkdir -p /var/log/supervisor  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
VOLUME ["/var/log/supervisor"]  
  
# clean up our mess  
RUN apt-get remove --purge -y software-properties-common && \  
apt-get autoremove -y && \  
apt-get clean && \  
apt-get autoclean && \  
echo -n > /var/lib/apt/extended_states && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /usr/share/man/?? && \  
rm -rf /usr/share/man/??_*  
  
COPY . $APP_PATH  
WORKDIR $APP_PATH  
  
# build project  
RUN npm install -g @angular/cli  
RUN npm install  
RUN npm run pug-it  
RUN npm run ng build --prod  
  
WORKDIR $APP_PATH  
  
# expose ports  
EXPOSE 80  
# set container entrypoints  
VOLUME ["/var/www/html/app"]  
ENTRYPOINT ["/bin/bash","-c"]  
CMD ["./run.sh"]  

