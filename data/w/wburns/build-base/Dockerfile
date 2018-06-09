# Use default jboss java 7 image  
FROM jboss/base-jdk:7  
MAINTAINER William Burns <william.a.burns@gmail.com>  
  
USER root  
  
RUN yum install -y \  
maven \  
git \  
&& yum clean all  
  
USER jboss  
  
# We set some defaults for git, this way we can do merges etc.  
RUN git config \--global user.email jboss@redhat.com \  
&& git config \--global user.name "Jboss Docker"  

