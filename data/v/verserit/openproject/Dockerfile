# Usa como base o CentOS padrão da Verser IT  
FROM verserit/centos-base  
MAINTAINER Verser IT <verserit@verserit.com>  
  
RUN sudo rpm --import https://rpm.packager.io/key  
  
RUN echo "[openproject] name=Repository for opf/openproject application.
baseurl=https://rpm.packager.io/gh/finnlabs/pkgr-openproject-
community/centos7/stable/4.2 enabled=1" | sudo tee /etc/yum.repos.d/pkgr-
openproject-community.repo  
  
RUN sudo yum install openproject-ce

