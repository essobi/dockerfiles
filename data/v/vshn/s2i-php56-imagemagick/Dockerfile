FROM centos/php-56-centos7  
  
# change to root to install ImageMagick  
USER root  
  
RUN INSTALL_PKGS="sclo-php56-php-pecl-imagick" && \  
yum install -y \--setopt=tsflags=nodocs $INSTALL_PKGS && \  
rpm -V $INSTALL_PKGS && \  
yum clean all -y  
  
# change back to unpriviledged user  
USER 1001  

