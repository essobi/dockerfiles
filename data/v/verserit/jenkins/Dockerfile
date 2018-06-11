# Usa como base o CentOS com JDK  
FROM verserit/centos-jdk  
MAINTAINER Verser IT <verserit@verserit.com>  
  
RUN wget -O /etc/yum.repos.d/jenkins.repo http://pkg.jenkins-
ci.org/redhat/jenkins.repo  
RUN rpm --import http://pkg.jenkins-ci.org/redhat/jenkins-ci.org.key  
RUN yum install jenkins

