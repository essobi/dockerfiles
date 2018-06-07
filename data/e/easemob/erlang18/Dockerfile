# VERSION v1  
# docker build -t="easemob/erlang18:v1" .  
FROM liulantao/fpm  
MAINTAINER Liu Lantao <liulantao@gmail.com>  
ENV REFRESHED_AT 2015-12-03  
RUN curl http://packages.erlang-solutions.com/rpm/centos/erlang_solutions.repo
-o /etc/yum.repos.d/erlang_solutions.repo  
RUN yum install -yq erlang-18.0-1.el6.x86_64 git expat-devel redhat-lsb-core  

