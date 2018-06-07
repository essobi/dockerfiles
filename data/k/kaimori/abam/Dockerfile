FROM centos:latest  
MAINTAINER The maintainer  
#Install tools  
RUN yum install -y yum-utils python-setuptools inotify-tools unzip sendmail
tar mysql sudo wget telnet rsync git  
  
ADD nginx.repo /etc/yum.repos.d/  
RUN yum install -y nginx  
RUN yum -y install epel-release && \  
rpm -Uvh http://rpms.famillecollet.com/enterprise/remi-release-7.rpm && \  
yum-config-manager -q --enable remi && \  
yum-config-manager -q --enable remi-php56  
  
#Install nginx, php-fpm and php extensions  
RUN yum install -y php-fpm php-common memcached  
RUN yum install -y php-pecl-apc php-cli php-pear php-pdo php-mysql php-pecl-
memcache php-pecl-memcached php-gd php-mbstring php-mcrypt php-xml php-adodb
php-imap php-intl php-soap  
RUN yum install -y php-mysqli php-zip php-iconv php-curl php-simplexml php-dom
php-bcmath php-opcache php-pecl-redis  
  
#Clean up yum repos to save spaces  
RUN yum update -y && yum clean all  
  
#Install  
#Node.js configure error: No acceptable C compiler found  
RUN yum install -y sudo gcc-c++  
  
# Install Node.js  
RUN \  
cd /tmp && \  
wget http://nodejs.org/dist/v0.10.32/node-v0.10.32.tar.gz && \  
tar xvzf node-v0.10.32.tar.gz && \  
rm -f node-v0.10.32.tar.gz && \  
cd node-v* && \  
./configure && \  
CXX="g++ -Wno-unused-local-typedefs" make && \  
CXX="g++ -Wno-unused-local-typedefs" make install && \  
cd /tmp && \  
rm -rf /tmp/node-v* && \  
npm -y install -g npm && \  
echo -e '\n# Node.js\nexport PATH="node_modules/.bin:$PATH"' >> /root/.bashrc  
  
# Install Node modules  
RUN \  
npm -y install -g grunt-cli gulp webpack bower  
  
#Install supervisor  
RUN easy_install supervisor  
#Install composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
#Update nginx user group and name  
RUN groupmod --gid 80 --new-name www nginx && \  
usermod --uid 80 --home /data/www --gid 80 --login www --shell /bin/bash
--comment www nginx && \  
rm -rf /etc/nginx/*.d /etc/nginx/*_params && \  
chown -R www:www /var/www  
#lib/nginx  
#Add pre-configured files  
ADD container-files /  
RUN find /config |grep .sh |xargs chmod +x  
  
VOLUME ["/data"]  
  
EXPOSE 80 443  
ENTRYPOINT ["/config/bootstrap.sh"]  

