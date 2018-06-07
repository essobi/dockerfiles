#################################################################  
# Creates a base CentOS 6 image with Python 2.7 and Oracle Java 7  
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
# Author: Kale Franz <kale@franz.io>  
# License: MIT  
#################################################################  
  
FROM kalefranz/centos:latest  
MAINTAINER Kale Franz <kale@franz.io>  
  
# install Java7 from http://download.oracle.com/otn-
pub/java/jdk/7u51-b13/jdk-7u51-linux-x64.rpm  
RUN wget --no-check-certificate --no-cookies --header "Cookie:
gpw_e24=http%3A%2F%2Fwww.oracle.com" -O jdk-linux-x64.rpm
"http://download.oracle.com/otn-pub/java/jdk/7u51-b13/jdk-7u51-linux-x64.rpm"  
RUN rpm -Uvh jdk-linux-x64.rpm  
RUN rm jdk-linux-x64.rpm  
ENV JAVA_HOME /usr/java/default  

