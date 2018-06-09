#  
# TreasureBoat.org  
# by ishimoto  
#  
# CentOS 6.6 updated  
#  
# build : docker build -t treasureboat/centos6:0.3 .  
# run : docker run -d -P --name tbCentOS6 treasureboat/centos6:0.3  
FROM centos:6.6  
MAINTAINER treasureboat <office@treasureboat.org>  
  
# address any potential security concerns.  
RUN yum -y update && yum clean all  
  
# install basic packages  
RUN yum install -y wget tar gcc which  
  
# set timezone  
RUN rm -f /etc/localtime  
RUN ln -s /usr/share/zoneinfo/UTC /etc/localtime  
  
# install rsyslogd  
RUN yum install -y rsyslog  

