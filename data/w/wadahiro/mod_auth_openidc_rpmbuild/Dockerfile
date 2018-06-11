FROM centos:centos6  
MAINTAINER Hiroyuki Wada <wadahiro@gmail.com>  
  
# setup base libraries  
RUN yum update -y  
RUN yum install -y rpm-build gcc tar git autoconf automake libtool  
  
# epel  
RUN rpm --import http://dl.fedoraproject.org/pub/epel/RPM-GPG-KEY-EPEL-6  
RUN rpm -ihv http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-
release-6-8.noarch.rpm  
  
# setup rpmbuild environment  
WORKDIR /opt/rpmbuild  
ENV HOME /opt/rpmbuild  
RUN mkdir -p $HOME/rpm/{BUILD,SRPMS,SPECS,SOURCES,RPMS}  
RUN echo "%_topdir $HOME/rpm" > ~/.rpmmacros  
  
# mod_auth_openidc depends  
RUN yum install --enablerepo=centosplus -y openssl-devel  
RUN yum install --enablerepo=epel -y jansson-devel  
RUN yum install -y httpd httpd-devel curl-devel hiredis-devel pcre-devel  
  
# build mod_auth_openidc rpm  
RUN curl -o $HOME/rpm/SOURCES/mod_auth_openidc-1.7.0.tar.gz
https://codeload.github.com/pingidentity/mod_auth_openidc/tar.gz/v1.7.0  
ADD mod_auth_openidc.spec $HOME/rpm/SPECS/mod_auth_openidc.spec  
ADD mod_auth_openidc-apxs2.patch $HOME/rpm/SOURCES/mod_auth_openidc-
apxs2.patch  
ENV HIREDIS_LIBS -lhiredis  
RUN rpmbuild -bb $HOME/rpm/SPECS/mod_auth_openidc.spec  
  

