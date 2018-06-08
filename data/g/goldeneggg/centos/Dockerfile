# using centos 7  
FROM centos:centos7  
  
MAINTAINER goldeneggg  
  
RUN mkdir /tmp/init  
WORKDIR /tmp/init  
  
# initial setup  
ADD https://raw.githubusercontent.com/goldeneggg/provisioning-
bash/master/facade.sh /tmp/init/facade.sh  
RUN sh facade.sh centos7 init_ja.sh goldeneggg jpshadowapps@gmail.com  

