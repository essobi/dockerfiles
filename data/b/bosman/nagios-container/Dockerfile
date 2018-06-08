#
-----------------------------------------------------------------------------  
# nagios-container  
#  
# Builds a basic docker image that can run nagios  
#  
# Authors: Bosman  
# Updated: March 8th, 2018  
# Require: Docker (http://www.docker.io/)  
#
-----------------------------------------------------------------------------  
# Base system is CentOS 6.9  
FROM centos:centos6  
MAINTAINER "Bosman"  
ENV container=docker \  
NAGIOS_HOME="/etc/nagios" \  
NAGIOS_BIN="/usr/sbin/nagios" \  
NAGIOS_USER="nagios" \  
NAGIOS_GROUP="nagios" \  
NAGIOS_CMDUSER="nagios" \  
NAGIOS_CMDGROUP="nagios" \  
NAGIOSADMIN_USER="nagiosadmin" \  
NAGIOSADMIN_PASS="nagios" \  
APACHE_RUN_USER="nagios" \  
APACHE_RUN_GROUP="nagios" \  
NAGIOS_TIMEZONE="MST"  
# Environment paths  
ENV PATH /sbin:/bin:/usr/sbin:/usr/bin  
  
# Lets get the latest patches for CentOS  
RUN yum clean all \  
&& yum update -y  
  
# Install Nagios prereq's and some common stuff (we will get the epel release
for the nagios install).  
RUN yum install -y \  
httpd \  
mod_ssl \  
bash-completion \  
yum-utils \  
php \  
php-cli \  
mlocate \  
sendmail \  
crontabs \  
vim-common \  
vim-enhanced \  
mlocate \  
sysstat \  
wget \  
unzip \  
screen \  
ntp \  
man \  
elinks \  
cronie \  
mtr \  
traceroute \  
nmap \  
ipset \  
postfix \  
bridge-utils \  
perl \  
perl-CGI \  
perl-GD \  
perl-CPAN \  
perl-DBI \  
perl-DBD-Pg \  
epel-release  
  
# Add nagios and apache group and user info  
RUN useradd nagios \  
&& groupadd nagcmd \  
&& usermod -a -G nagcmd nagios \  
&& usermod -a -G nagcmd apache  
  
# Get the nagios rpm's  
RUN yum-config-manager --enable epel-testing \  
&& yum clean all \  
&& yum install -y nrpe \  
nagios \  
nagios-plugins-all \  
perl-Nagios-Plugin \  
bash-completion \  
pnp4nagios  
RUN yum-config-manager --disable epel-testing  
  
# Create and set the nagios login and password (change this for your custom
use - username first then password).  
RUN /usr/bin/htpasswd -c -b /etc/nagios/htpasswd nagiosadmin nagiosadmin  
  
# Start our services  
#RUN for startup in nrpe crond httpd nagios sendmail;do /sbin/service $startup
on;done  
# Config services startup  
#RUN for service in nrpe crond httpd nagios sendmail;do /sbin/service $service
start;done  
# Disable Nagios Notifications (comment this out if you want notifications out
of the box).  
RUN perl -pi -e 's/^enable_notifications=1/enable_notifications=0/'
/etc/nagios/nagios.cfg  
  
# Open ports for http/https/ntp  
# 443 is for https  
EXPOSE 443  
# 80 is for http  
EXPOSE 80  
# 123 for ntp  
EXPOSE 123/UDP  
# 5666 for nrpe  
EXPOSE 5666  

