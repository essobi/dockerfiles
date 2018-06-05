FROM amazonlinux:latest  
  
RUN yum install -y vi nano httpd24 php70  
RUN yum install -y php70-opcache php70-mcrypt php70-mhash php70-gd php70-xsl
php70-curl php70-xmlrpc php70-soap php70-mysqli php70-memcached php70-redis
php70-mbstring php70-pdo php70-intl  
RUN yum install -y zip mysql  
  
RUN yum install -y libjpeg-devel libpng-devel  
  
# RUN rpm -ivUh http://mirror-fpt-telecom.fpt.net/fedora/epel/6/i386/epel-
release-6-8.noarch.rpm  
RUN yum install -y epel-release  
RUN sed -i "6 s/enabled=0/enabled=1/" /etc/yum.repos.d/epel.repo  
RUN yum install -y gifsicle optipng  
  
RUN rpm -Uvh http://yum.newrelic.com/pub/newrelic/el5/x86_64/newrelic-
repo-5-3.noarch.rpm  
RUN yum install -y newrelic-php5  
  
RUN groupdel tape && userdel apache && \  
groupadd apache -g 33 && useradd -u 33 -g apache -s /sbin/nologin apache  
  
ENV DEFAULT_PHP_MODS=  
ENV DEFAULT_LIB_DEPENDENCIES=  
  
COPY conf_default /var/conf_default  
COPY conf /var/conf_tmp  
  
RUN rm -rf /var/conf && mkdir -p /var/conf  
ENV PHP_INI_SCAN_DIR=/etc/php-7.0.d:/var/conf  
  
RUN rm -rf /var/session && mkdir -p /var/session  
  
WORKDIR /var/www/html  
  
VOLUME /var/www/html  
VOLUME /var/conf  
VOLUME /var/session  
  
EXPOSE 80  
ADD install_and_run.sh /tmp/install_and_run.sh  
RUN chmod +x /tmp/install_and_run.sh  
ENTRYPOINT ["/tmp/install_and_run.sh"]  
  

