# Builds a drupal distro builder  
#  
# VERSION 0.0.1  
FROM centos:centos7  
  
MAINTAINER Zach Seifts "zach.seifts@gmail.com"  
# Update packages and install dependencies  
RUN yum update -y  
RUN yum install http://dl.fedoraproject.org/pub/epel/beta/7/x86_64/epel-
release-7-1.noarch.rpm -y  
RUN yum install php-pear which tar nodejs npm -y  
  
# Install drush from pear  
RUN /usr/bin/pear install Console_Table  
RUN /usr/bin/pear channel-discover pear.drush.org  
RUN /usr/bin/pear install drush/drush  
  
# Install rvm and ruby from rvm  
RUN curl -L get.rvm.io | bash -s stable  
RUN source /etc/profile.d/rvm.sh  
RUN /bin/bash -l -c "rvm requirements"  
RUN /bin/bash -l -c "rvm install ruby"  
  

