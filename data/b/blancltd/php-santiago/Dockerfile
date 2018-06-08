FROM centos:centos6  
MAINTAINER Blanc Ltd <studio@blanc.ltd.uk>  
  
# Install packages needed  
RUN rpm -Uvh http://download.fedoraproject.org/pub/epel/6/i386/epel-
release-6-8.noarch.rpm  
RUN yum install -y php php-bcmath php-mcrypt php-gd php-mysql php-xml tar gcc
httpd-devel ssmtp && yum clean all  
  
# Custom RPAF  
RUN BUILDDIR=`mktemp --directory` && \  
cd $BUILDDIR && \  
curl -sL https://github.com/gnif/mod_rpaf/archive/v0.8.4.tar.gz | tar zx && \  
cd mod_rpaf-0.8.4 && \  
make install && \  
rm -rf $BUILDDIR  
  
# Disable defaults  
RUN sed -i \  
-e 's/^LoadModule/#LoadModule/g' \  
-e 's/^ServerAdmin/#ServerAdmin/g' \  
-e 's/^ServerSignature On/ServerSignature Off/g' \  
-e 's/^DocumentRoot/#DocumentRoot/g' /etc/httpd/conf/httpd.conf  
RUN rm /etc/httpd/conf.d/welcome.conf  
  
COPY conf.d /etc/httpd/conf.d/  
COPY php.d /etc/php.d/  
  
# Default run script  
COPY santiago-run /usr/local/bin/app-run  
CMD ["/usr/local/bin/app-run"]  

