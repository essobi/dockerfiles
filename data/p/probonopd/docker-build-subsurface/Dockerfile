############################################################  
# Dockerfile to build Subsurface AppImages  
# Based on CentOS 6  
############################################################  
FROM centos:6  
ADD
https://github.com/probonopd/AppImages/raw/master/recipes/subsurface.centos6.sh
/subsurface.centos6.sh  
RUN sed -i -e 's|sudo ||g' subsurface.centos6.sh && yum -y install wget && yum
clean all && bash -ex subsurface.centos6.sh && yum clean all && rm -rf
/Subsurface/Subsurface*  
CMD echo "bash -ex subsurface.centos6.sh"  

