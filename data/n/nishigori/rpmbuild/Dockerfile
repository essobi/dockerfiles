# DOCKER-VERSION ~> 1.0.0  
# AUTHOR: Takuya Nishigori <nishigori.tak@gmail.com>  
# TO_BUILD: docker build -t my/app .  
FROM centos:latest  
MAINTAINER nishigori  
  
ENV HOME /root  
  
RUN yum update -y  
RUN yum install -y curl make gcc vim-enhanced  
RUN yum install -y rpmdev-setuptree rpmdevtools yum-utils  
  
RUN rpmdev-setuptree  
RUN rpmbuild --showrc

