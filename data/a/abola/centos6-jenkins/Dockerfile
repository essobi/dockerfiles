#################################################################  
#  
# ## .  
# ## ## ## ==  
# ## ## ## ## ===  
# /""""""""""""""""\\___/ ===  
# ~~~ {~~ ~~~~ ~~~ ~~~~ ~~ ~ / ===- ~~~  
# \\______ o __/  
# \ \ __/  
# \\____\\______/  
#  
# Author: Abola Lee <abola921@gmail.com>  
# License: MIT  
#################################################################  
  
FROM centos  
  
MAINTAINER Abola Lee <abola921@gmail.com>  
  
RUN echo "export JAVA_HOME=/usr/lib/jvm/jre" >> /etc/profile  
RUN echo "export LANG=zh_TW.utf8" >> /etc/profile  
  
# add jenkins repo  
ADD http://pkg.jenkins-ci.org/redhat/jenkins.repo
/etc/yum.repos.d/jenkins.repo  
RUN rpm --import http://pkg.jenkins-ci.org/redhat/jenkins-ci.org.key  
  
# telnet is required by some fabric command. without it you have silent
failures  
RUN yum install -y java-1.7.0-openjdk-devel jenkins git  
  
EXPOSE 8080  
  
CMD service jenkins start ; bash  

