# setup many of the prerequisites for node applications  
FROM iamclyde/centos_node  
MAINTAINER iamclyde@gmail.com  
  
RUN yum -y update; yum clean all  
RUN yum -y install make gcc gcc-c++ vim epel-release java-1.7.0-openjdk
java-1.7.0-openjdk-devel; yum clean all  
  
# install grunt globally  
RUN npm install grunt grunt-cli -g  
  

