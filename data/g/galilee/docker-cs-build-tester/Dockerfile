FROM centos:7.3.1611  
MAINTAINER Gabriel Malet <gmalet@galilee.fr>  
  
ENV NODE_VERSION 8  
RUN yum -y install wget curl git bash openssl openssh openssh-clients  
  
RUN curl --silent --location
https://rpm.nodesource.com/setup_${NODE_VERSION}.x | bash - \  
&& yum -y install nodejs  
  
RUN wget https://dl.yarnpkg.com/rpm/yarn.repo -O /etc/yum.repos.d/yarn.repo \  
&& yum -y install yarn  
  
RUN mkdir -p /root/.ssh  
COPY resources/ssh_config /root/.ssh/config  
  
COPY resources/.npmrc /root/.npmrc  
  
COPY resources/entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]

