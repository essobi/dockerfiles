FROM centos:7  
RUN yum -y install \  
make \  
gcc \  
gcc-c++ \  
zip \  
unzip \  
rsync \  
&& \  
yum -y clean all  
  
ENV NODE_VER 8.x  
  
RUN curl --silent --location https://rpm.nodesource.com/setup_$NODE_VER | bash
-  
RUN curl -o /etc/yum.repos.d/yarn.repo https://dl.yarnpkg.com/rpm/yarn.repo  
RUN yum -y install nodejs yarn  
  
CMD [ "node" ]  

