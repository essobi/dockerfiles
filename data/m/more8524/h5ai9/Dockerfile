FROM ubuntu:14.04  
MAINTAINER Aleksandar Diklic "https://github.com/rastasheep"  
# install unzip openssh-server nginx php5 imagemagick ..  
RUN apt-get update && apt-get install -y \  
nginx php5-fpm supervisor \  
wget unzip patch acl \  
libav-tools imagemagick \  
openssh-server \  
software-properties-common \  
python-software-properties \  
graphicsmagick zip unzip php5-gd  
RUN add-apt-repository ppa:alessandro-strada/ppa  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV HTTPD_USER www-data  
  
# install h5ai and patch configuration  
ENV H5AI_VERSION 0.29.0+002~140eb30  
RUN wget -O h5ai.zip
https://github.com/CoRfr/h5ai/raw/build/build/h5ai-$H5AI_VERSION.zip  
RUN unzip h5ai.zip -d /usr/share/h5ai  
  
# patch h5ai because we want to deploy it ouside of the document root and use
/var/www as root for browsing  
COPY class-setup.php.patch class-setup.php.patch  
RUN patch -p1 -u -d /usr/share/h5ai/_h5ai/private/php/core/ -i /class-
setup.php.patch && rm class-setup.php.patch  
  
# add default configuration for nginx  
RUN rm /etc/nginx/sites-enabled/default  
ADD h5ai.nginx.conf /etc/nginx/sites-available/h5ai  
RUN ln -s /etc/nginx/sites-available/h5ai /etc/nginx/sites-enabled/h5ai  
  
# make the cache writable  
RUN chown ${HTTPD_USER} /usr/share/h5ai/_h5ai/public/cache/  
RUN chown ${HTTPD_USER} /usr/share/h5ai/_h5ai/private/cache/  
  
# use supervisor to monitor all services  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
CMD supervisord -c /etc/supervisor/conf.d/supervisord.conf  
  
# install openssh-sever rootpass  
RUN mkdir /var/run/sshd  
RUN echo 'root:root' |chpasswd  
  
RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/'
/etc/ssh/sshd_config  
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config  
  
# expose only nginx HTTP port  
EXPOSE 80 443 22  
# expose path  
VOLUME /var/www  
  
CMD ["/usr/sbin/sshd", "-D"]  

