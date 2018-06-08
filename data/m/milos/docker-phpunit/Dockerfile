FROM milos/docker-composer  
  
  
WORKDIR /tmp  
  
RUN (\  
wget http://packages.sw.be/rpmforge-release/rpmforge-
release-0.5.2-2.el5.rf.x86_64.rpm; \  
rpm --import http://apt.sw.be/RPM-GPG-KEY.dag.txt \  
rpm -K rpmforge-release-0.5.2-2.el5.rf.x86_64.rpm; \  
rpm -i rpmforge-release-0.5.2-2.el5.rf.x86_64.rpm; \  
)  
  
RUN yum install -y git-gui  
  
RUN composer require "phpunit/phpunit:4.8.3" \--no-interaction && \  
ln -s /tmp/vendor/bin/phpunit /usr/local/bin/phpunit  
  
WORKDIR /var/www  
VOLUME ["/var/www"]  
  
RUN whereis phpunit  
ENTRYPOINT ["/usr/local/bin/phpunit"]  
  

