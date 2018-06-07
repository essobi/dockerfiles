FROM centos:centos6  
MAINTAINER Dan Burke <dburke@addictmud.org>  
RUN yum update -y && yum clean all  
RUN yum install -y wget && yum clean all  
RUN yum install -y http://packages.erlang-solutions.com/erlang-
solutions-1.0-1.noarch.rpm && yum clean all  
RUN yum install -y erlang && yum clean all  
EXPOSE 4369  

