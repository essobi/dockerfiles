############################################################  
# Dockerfile to build Nginx Yum Service Base Container  
# Based on: appcontainers/centos:latest (6.8)  
# DATE: 08/03/2016  
# COPYRIGHT: Appcontainers.com  
############################################################  
  
# Set the base image in namespace/repo format.  
# To use repos that are not on the docker hub use the
example.com/namespace/repo format.  
FROM appcontainers/centos:latest  
  
# File Author / Maintainer  
MAINTAINER Rich Nason rnason@sciquest.com  
  
#####################################################################################################################  
#************************************************** APP VERSIONS
**************************************************  
#####################################################################################################################  
  
  
#####################################################################################################################  
#****************************************** OVERRIDE ENABLED ENV VARIABLES
****************************************  
#####################################################################################################################  
  
ENV TERMTAG Yum  
ENV ENV dev  
ENV APP_NAME yum.sciquest.com  
ENV APACHE_SVRALIAS www.yum.sciquest.com yum  
  
#####################################################################################################################  
#******************************************** ADD REQUIRED APP FILES
**********************************************  
#####################################################################################################################  
# Create the necessary file structure  
RUN mkdir -p
/opt/yum/sciquest/{dev,stage,prod}/{6,7}/{base,custom}/{x86_64,noarch}/RPMS &&
\  
mkdir -p /opt/yum/sciquest/scripts  
  
ADD yum_refresh.sh /opt/yum/sciquest/scripts/yum_refresh.sh  
  
RUN chmod +x /opt/yum/sciquest/scripts/yum_refresh.sh  
  
#####################################################################################################################  
#********************************************** UPDATES & PRE-REQS
************************************************  
#####################################################################################################################  
  
# Clean, Update, and Install... then clear non English local data.  
RUN yum clean all && \  
yum -y update && \  
  
# Install required packages  
yum -y install createrepo rpm-sign rng-tools nginx && \  
  
# Remove yum cache this bad boy can be 150MBish  
yum clean all && \  
rm -fr /var/cache/*  
  
# Remove locales other than english  
RUN for x in `ls /usr/share/locale | grep -v -i en | grep -v -i local`;do rm
-fr /usr/share/locale/$x; done && \  
for x in `ls /usr/share/i18n/locales/ | grep -v en_`; do rm -fr
/usr/share/i18n/locales/$x; done && \  
rm -fr ca* den men wen zen && \  
cd /usr/lib/locale && \  
localedef --list-archive | grep -v -i ^en | xargs localedef --delete-from-
archive && \  
mv -f locale-archive locale-archive.tmpl && \  
build-locale-archive  
  
  
#####################################################################################################################  
#********************************************** APPLICATION INSTALL
***********************************************  
#####################################################################################################################  
  
ADD nginx.conf /etc/nginx/  
ADD yum.sciquest.com.conf /etc/nginx/conf.d/  
  
RUN mkdir -p /var/www/html || exit 0 && \  
ln -s /opt/yum/sciquest/ /var/www/html/sciquest  
  
#####################################################################################################################  
#********************************************* POST DEPLOY CLEAN UP
***********************************************  
#####################################################################################################################  
  
# Add Jenkins User  
RUN useradd jenkins && \  
usermod -s /bin/bash jenkins && \  
mkdir -p /home/jenkins/.ssh || exit 0 && \  
chown -R jenkins:jenkins /home/jenkins && \  
chmod 0700 /home/jenkins/.ssh && \  
usermod -g nginx jenkins  
  
# Set permissions on the yum directory  
RUN chown -R jenkins:nginx /opt/yum  
  
#####################################################################################################################  
#********************************************* CONFIGURE START ITEMS
**********************************************  
#####################################################################################################################  
  
CMD /bin/bash  
  
#####################################################################################################################  
#******************************************** EXPOSE APPLICATION PORTS
********************************************  
#####################################################################################################################  
  
# Expose ports to other containers only  
EXPOSE 80  
EXPOSE 443  
  
#####################################################################################################################  
#*********************************************** OPTIONAL / LEGACY
************************************************  
#####################################################################################################################  
  
  
  
  
  
  
  
  
  
  
  
  
  

