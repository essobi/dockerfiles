FROM centos/httpd:latest  
MAINTAINER dayreiner  
  
# Update and install latest packages and prerequisites  
RUN yum makecache fast && yum -y --setopt=tsflags=nodocs update \  
&& yum -y --setopt=tsflags=nodocs install
https://mirror.webtatic.com/yum/el7/webtatic-release.rpm \  
&& yum -y --setopt=tsflags=nodocs install git php71w php71w-cli php71w-common
php71w-opcache php71w-mysql php71w-mbstring php71w-xml php71w-gd php71w-pdo \  
&& yum clean all && yum history new  
  
# Install php composer  
RUN curl -sS https://getcomposer.org/installer | php \  
&& mv /composer.phar /usr/bin/composer \  
&& chmod +x /usr/bin/composer  
  
COPY config/php.ini /etc/php.ini  
  
# Setup SSH for checking out code from github  
RUN echo "Setting up SSH for GitHub Checkouts..." && \  
mkdir -p /root/.ssh && chmod 700 /root/.ssh && \  
touch /root/.ssh/known_hosts && \  
ssh-keyscan -H github.com >> /root/.ssh/known_hosts && \  
chmod 600 /root/.ssh/known_hosts  
  
EXPOSE 80  
ENTRYPOINT ["/usr/sbin/httpd"]  
CMD ["-DFOREGROUND"]  

