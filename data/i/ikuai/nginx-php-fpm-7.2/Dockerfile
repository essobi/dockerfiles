FROM ubuntu:16.04  
  
MAINTAINER Dylan <bbcheng@ikuai8.com>  
  
#############################################################################################  
# Locale, Language  
ENV OS_LOCALE="en_US.UTF-8"  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get update \  
&& apt-get install -y locales \  
&& locale-gen ${OS_LOCALE}  
ENV LANG=${OS_LOCALE} \  
LC_ALL=${OS_LOCALE} \  
LANGUAGE=en_US:en  
  
#############################################################################################  
# Allow ssh login (only ssh-key, prohibit password)  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get install -y openssh-server tzdata \  
&& mkdir /var/run/sshd \  
&& ln -fs /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \  
&& dpkg-reconfigure -f noninteractive tzdata  
# RUN echo 'root:screencast' | chpasswd  
# RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
  
#############################################################################################  
# App Env  
ENV php_conf /etc/php/7.2/fpm/php.ini  
ENV fpm_conf /etc/php/7.2/fpm/pool.d/www.conf  
  
#############################################################################################  
# Install Basic Requirements  
RUN DEBIAN_FRONTEND=noninteractive \  
buildDeps='software-properties-common python-software-properties' \  
&& apt-get install --no-install-recommends --no-install-suggests -y $buildDeps
\  
&& add-apt-repository -y ppa:ondrej/php \  
&& add-apt-repository -y ppa:nginx/stable \  
&& apt-get update \  
&& apt-get install --no-install-recommends --no-install-suggests -q -y \  
cron \  
iputils-ping \  
net-tools \  
curl \  
vim \  
zip \  
unzip \  
python-pip \  
python-setuptools \  
nginx \  
php7.2-bcmath \  
php7.2-bz2 \  
php7.2-fpm \  
php7.2-cli \  
php7.2-dev \  
php7.2-common \  
php7.2-json \  
php7.2-opcache \  
php7.2-readline \  
php7.2-mbstring \  
php7.2-curl \  
php7.2-memcached \  
php7.2-imagick \  
php7.2-mysql \  
php7.2-zip \  
php7.2-pgsql \  
php7.2-intl \  
php7.2-xml \  
php7.2-redis \  
php7.2-gd \  
php-mongodb \  
&& mkdir -p /run/php \  
&& pip install wheel \  
&& pip install supervisor supervisor-stdout \  
&& echo "#!/bin/sh\nexit 0" > /usr/sbin/policy-rc.d \  
&& sed -i -e "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g" ${php_conf} \  
&& sed -i -e "s/memory_limit\s*=\s*.*/memory_limit = 256M/g" ${php_conf} \  
&& sed -i -e "s/upload_max_filesize\s*=\s*2M/upload_max_filesize = 100M/g"
${php_conf} \  
&& sed -i -e "s/post_max_size\s*=\s*8M/post_max_size = 100M/g" ${php_conf} \  
&& sed -i -e "s/variables_order = \"GPCS\"/variables_order = \"EGPCS\"/g"
${php_conf} \  
&& sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php/7.2/fpm/php-
fpm.conf \  
&& sed -i -e "s/;catch_workers_output\s*=\s*yes/catch_workers_output = yes/g"
${fpm_conf} \  
&& sed -i -e "s/pm.max_children = 5/pm.max_children = 4/g" ${fpm_conf} \  
&& sed -i -e "s/pm.start_servers = 2/pm.start_servers = 3/g" ${fpm_conf} \  
&& sed -i -e "s/pm.min_spare_servers = 1/pm.min_spare_servers = 2/g"
${fpm_conf} \  
&& sed -i -e "s/pm.max_spare_servers = 3/pm.max_spare_servers = 4/g"
${fpm_conf} \  
&& sed -i -e "s/pm.max_requests = 500/pm.max_requests = 200/g" ${fpm_conf} \  
&& sed -i -e "s/^;clear_env = no$/clear_env = no/" ${fpm_conf} \  
# Clean  
&& apt-get purge -y --auto-remove $buildDeps \  
&& apt-get autoremove -y \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# Nginx Upstream config  
ADD ./conf/upstream.conf /etc/nginx/upstream.conf  
  
# Add upstream config to nginx.conf  
COPY ./conf/nginx.conf /etc/nginx/nginx.conf  
  
# Supervisor config  
ADD ./conf/supervisord.conf /etc/supervisord.conf  
  
# Override default nginx welcome page  
COPY html /usr/share/nginx/html  
  
# Add Scripts  
ADD ./start.sh /start.sh  
  
EXPOSE 80 443  
  
CMD ["/start.sh"]  

