FROM centos:7  
MAINTAINER Tatsuya Saito <twopackas@gmail.com>  
  
RUN yum -y clean all && \  
yum -y update && \  
yum -y install yum-plugin-ovl  
  
RUN yum install -y epel-release centos-release-scl-rh && \  
yum-config-manager --enable epel && \  
yum-config-manager --enable rhel-server-rhscl-7-rpms && \  
yum -y clean all && \  
yum -y update  
  
RUN rm -f /etc/rpm/macros.image-language-conf && \  
sed -i '/^override_install_langs=/d' /etc/yum.conf && \  
yum -y reinstall glibc-common  
  
RUN yum install -y which selinux-policy firewalld scl-utils  
  
RUN yum groups mark install "Development Tools" && \  
yum groups mark convert "Development Tools" && \  
yum group install -y "Development Tools"  
  
RUN yum install -y ansible git openssl-devel readline-devel zlib-devel \  
curl-devel libyaml-devel libffi-devel httpd httpd-devel \  
ImageMagick ImageMagick-devel ipa-pgothic-fonts \  
subversion ssmtp mariadb-server mariadb-devel MySQL-python  
  
RUN yum install -y rh-ruby24 rh-ruby24-ruby-devel  
RUN source scl_source enable rh-ruby24 && \  
echo -e '#!/bin/bash\nsource scl_source enable rh-ruby24' > /etc/profile.d/rh-
ruby24.sh  
RUN ln -s /opt/rh/rh-ruby24/root/usr/lib64/libruby.so.2.4 /usr/lib64  
ENV PATH $PATH:/opt/rh/rh-ruby24/root/usr/bin:/opt/rh/rh-
ruby24/root/usr/local/bin  
  
RUN gem install passenger --no-ri --no-rdoc -V  
RUN passenger-install-apache2-module --auto  
  
RUN echo '<Directory "/var/lib/redmine/public">' >
/etc/httpd/conf.d/redmine.conf  
RUN echo ' Require all granted' >> /etc/httpd/conf.d/redmine.conf  
RUN echo '</Directory>' >> /etc/httpd/conf.d/redmine.conf  
RUN echo '' >> /etc/httpd/conf.d/redmine.conf  
RUN passenger-install-apache2-module --snippet >>
/etc/httpd/conf.d/redmine.conf  
RUN echo '' >> /etc/httpd/conf.d/redmine.conf  
RUN echo 'Header always unset "X-Powered-By"' >>
/etc/httpd/conf.d/redmine.conf  
RUN echo 'Header always unset "X-Runtime"' >> /etc/httpd/conf.d/redmine.conf  
RUN echo '' >> /etc/httpd/conf.d/redmine.conf  
RUN echo 'PassengerMaxPoolSize 20' >> /etc/httpd/conf.d/redmine.conf  
RUN echo 'PassengerMaxInstancesPerApp 4' >> /etc/httpd/conf.d/redmine.conf  
RUN echo 'PassengerPoolIdleTime 864000' >> /etc/httpd/conf.d/redmine.conf  
RUN echo 'PassengerHighPerformance on' >> /etc/httpd/conf.d/redmine.conf  
RUN echo 'PassengerStatThrottleRate 10' >> /etc/httpd/conf.d/redmine.conf  
RUN echo 'PassengerSpawnMethod smart' >> /etc/httpd/conf.d/redmine.conf  
RUN echo 'PassengerFriendlyErrorPages off' >> /etc/httpd/conf.d/redmine.conf  
RUN echo '' >> /etc/httpd/conf.d/redmine.conf  
RUN echo 'RackBaseURI /redmine' >> /etc/httpd/conf.d/redmine.conf  
  
RUN ln -s /var/lib/redmine/public /var/www/html/redmine  
RUN httpd -k restart  

