FROM debian:jessie  
  
# Let the container know that there is no tty  
ENV DEBIAN_FRONTEND noninteractive  
ENV NGINX_VERSION 1.11.7-1~jessie  
ENV php_conf /etc/php/7.1/fpm/php.ini  
ENV fpm_conf /etc/php/7.1/fpm/pool.d/www.conf  
  
# Install Basic Requirements  
RUN apt-get update && apt-get install --no-install-recommends -y wget curl
nano zip unzip python-pip git  
  
# Supervisor config  
RUN pip install supervisor supervisor-stdout  
ADD ./supervisord.conf /etc/supervisord.conf  
  
# Avoid ERROR: invoke-rc.d: policy-rc.d denied execution of start.  
RUN echo "#!/bin/sh\nexit 0" > /usr/sbin/policy-rc.d  
  
# Add sources for latest nginx and php  
RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys
573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62 \  
&& echo "deb http://nginx.org/packages/mainline/debian/ jessie nginx" >>
/etc/apt/sources.list \  
&& echo "deb http://packages.dotdeb.org jessie all" >> /etc/apt/sources.list \  
&& echo "deb-src http://packages.dotdeb.org jessie all" >>
/etc/apt/sources.list \  
&& wget https://www.dotdeb.org/dotdeb.gpg \  
&& apt-key add dotdeb.gpg \  
&& apt-get update  
  
RUN apt-get -y install apt-transport-https lsb-release ca-certificates \  
&& wget -O /etc/apt/trusted.gpg.d/php.gpg
https://packages.sury.org/php/apt.gpg \  
&& echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" >
/etc/apt/sources.list.d/php.list \  
&& apt-get update  
  
# Install nginx  
RUN apt-get install --no-install-recommends --no-install-suggests -y \  
ca-certificates \  
nginx=${NGINX_VERSION}  
  
# Override nginx's default config  
RUN rm -rf /etc/nginx/conf.d/default.conf  
ADD ./default.conf /etc/nginx/conf.d/default.conf  
  
# Override default nginx welcome page  
COPY html /usr/share/nginx/html  
  
# Install PHP  
RUN apt-get -y install php7.1-fpm php7.1-cli php7.1-dev php7.1-common \  
php7.1-json php7.1-opcache php7.1-readline php7.1-mbstring php7.1-curl \  
php7.1-imagick php7.1-mcrypt php7.1-mysql php7.1-xml php7.1-redis \  
php7.1-zip php7.1-pgsql php7.1-gmp  
  
# Override php-fpm config  
RUN sed -i -e "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g" ${php_conf} && \  
sed -i -e "s/memory_limit\s*=\s*128M/memory_limit = 256M/g" ${php_conf} && \  
sed -i -e "s/upload_max_filesize\s*=\s*2M/upload_max_filesize = 100M/g"
${php_conf} && \  
sed -i -e "s/post_max_size\s*=\s*8M/post_max_size = 100M/g" ${php_conf} && \  
sed -i -e "s/;\smax_input_vars\s*=\s*1000/max_input_vars = 5000/g" ${php_conf}
&& \  
sed -i -e "s/variables_order = \"GPCS\"/variables_order = \"EGPCS\"/g"
${php_conf} && \  
sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php/7.1/fpm/php-
fpm.conf && \  
sed -i -e "s/;catch_workers_output\s*=\s*yes/catch_workers_output = yes/g"
${fpm_conf} && \  
sed -i -e "s/pm.max_children = 5/pm.max_children = 4/g" ${fpm_conf} && \  
sed -i -e "s/pm.start_servers = 2/pm.start_servers = 3/g" ${fpm_conf} && \  
sed -i -e "s/pm.min_spare_servers = 1/pm.min_spare_servers = 2/g" ${fpm_conf}
&& \  
sed -i -e "s/pm.max_spare_servers = 3/pm.max_spare_servers = 4/g" ${fpm_conf}
&& \  
sed -i -e "s/pm.max_requests = 500/pm.max_requests = 200/g" ${fpm_conf} && \  
sed -i -e "s/www-data/nginx/g" ${fpm_conf} && \  
sed -i -e "s/^;clear_env = no$/clear_env = no/" ${fpm_conf}  
  
# Clean up  
RUN apt-get clean && rm -rf /var/lib/apt/lists/*  
  
# Add Scripts  
ADD ./start.sh /start.sh  
RUN chmod 755 /start.sh  
  
EXPOSE 80  
CMD ["/start.sh"]  

