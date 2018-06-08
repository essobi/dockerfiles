############################################################  
# Dockerfile to build Buongiorno LocalDeploy container  
############################################################  
  
# Set the base image to Centos6  
FROM centos:centos6  
  
# File Author / Maintainer  
MAINTAINER FalchiT FalchiT  
  
# Enable SCL  
RUN yum install -y centos-release-SCL  
  
################## BEGIN INSTALLATION ######################  
  
RUN yum install -y java-1.7.0-openjdk \  
perl-TermReadKey \  
unzip \  
rsync \  
curl \  
wget \  
tar \  
sudo \  
screen \  
git  
  
## HACK penoso, centos fa vomitare  
RUN curl -o /tmp/epel-release-6-8.noarch.rpm
"http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm"  
RUN rpm -Uvh /tmp/epel-release-6-8.noarch.rpm  
RUN yum -y install perl-Net-SSH-Perl  
RUN yum -y install perl-DBI  
RUN yum -y install perl-Config-Properties  
RUN yum -y install perl-XML-XPath  
  
## middleware "default" core  
RUN yum -y install cronie  
RUN yum -y install nginx  
  
## Create the default user  
RUN useradd -m jmailer  
RUN useradd -m devel  
RUN usermod -a -G jmailer devel  
RUN groupadd www  
RUN usermod -a -G www devel  
  
## LocalDeploy  
COPY localDeploy.sh /usr/local/bin/localDeploy.sh  
RUN chmod +x /usr/local/bin/localDeploy.sh  
RUN mkdir -p /jhub/_prod/ && chown -R jmailer:jmailer /jhub/_prod/  
COPY functions /etc/init.d/functions  
  
## Python 2.7 da scl  
RUN sh -c 'wget -qO- http://people.redhat.com/bkabrda/scl_python27.repo >>
/etc/yum.repos.d/scl.repo'  
RUN yum install -y python27  
  
# Azucar!  
COPY bashrc /root/.bashrc  
RUN cat /root/.bashrc >> /home/jmailer/.bashrc  
RUN cat /root/.bashrc >> /home/devel/.bashrc  
  
##################### INSTALLATION END #####################  
  
# Porta da esporre fuori dal container  
#EXPOSE 8001  

