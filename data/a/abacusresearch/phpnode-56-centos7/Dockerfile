FROM centos/php-56-centos7  
  
USER root  
RUN INSTALL_PKGS="rh-nodejs4" && \  
yum install -y --setopt=tsflags=nodocs --enablerepo=centosplus $INSTALL_PKGS
&& \  
rpm -V $INSTALL_PKGS && \  
yum clean all -y  
  
ENV PATH=$PATH:/opt/rh/rh-php56/root/usr/bin:/opt/rh/rh-nodejs4/root/usr/bin \  
LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/rh/rh-
nodejs4/root/usr/lib64:/opt/rh/httpd24/root/usr/lib64:/opt/rh/rh-
php56/root/usr/lib64  
  
USER 1001  

