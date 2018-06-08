FROM centos:6  
  
COPY Tuleap.repo /etc/yum.repos.d/  
  
RUN yum -y install epel-release centos-release-scl && \  
yum -y install \  
tuleap \  
httpd24-httpd \  
mysql-server \  
&& \  
yum remove -y tuleap \  
tuleap-core-subversion \  
tuleap-core-subversion-modperl \  
tuleap-documentation && \  
yum clean all && \  
curl -k -sS https://getcomposer.org/installer | php && mv composer.phar
/usr/local/bin  
  
CMD /usr/share/tuleap/tests/soap/bin/run.sh  

