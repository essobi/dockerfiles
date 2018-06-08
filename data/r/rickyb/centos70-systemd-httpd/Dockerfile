FROM rickyb/centos70-systemd  
RUN yum -y install httpd php php-devel php-bcmath php-gd php-mysql php-pdo
php-mbstring php-cli php-pear curl; yum clean all; systemctl enable
httpd.service  
RUN yum -y install openssh openssh-server openssh-clients; yum clean all;
systemctl enable sshd.service  
RUN yum -y install cronie; yum clean all; systemctl enable crond.service  
RUN yum -y install https://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-
release-7-9.noarch.rpm; yum clean all  
RUN yum -y install php-PHPMailer php-pear-File php-pear-Math-Stats php-pear-
Net-Curl php-pear-OLE php-pecl-memcache php-pecl-memcached php-pecl-ssh2; yum
clean all  
RUN yum -y install ssmtp; yum clean all  
RUN yum -y install incron; yum clean all; systemctl enable incrond.service  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
RUN yum -y install screen; yum clean all  
COPY phpinfo.php /var/www/html/.  
EXPOSE 80 22  
CMD ["/usr/sbin/init"]  

