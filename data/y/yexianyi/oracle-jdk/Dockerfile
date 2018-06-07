# This docker file is for creating CentOS7 + JDK1.8  
FROM centos:7.3.1611  
  
ARG MEGATOOLS_FILE_NAME=megatools-1.9.91-2.el7.nux.x86_64.rpm  
ARG MEGATOOLS_DOWNLOAD_LINK=https://raw.githubusercontent.com/yexianyi/docker-
assets/tools/$MEGATOOLS_FILE_NAME  
ARG JDK_PACKAGE_NAME=jdk-8u131-linux-x64.tar.gz  
ARG
JDK_PACKAGE_DOWNLOAD_LINK='https://mega.co.nz/#!dzI1GIyT!PXpVHJoEz9q1TbQRvhxNqYr2erGFtPLY_p3aWymCdrc'  
ARG JDK_INSTALL_PATH=/usr/lib/java  
  
ENV JAVA_HOME=$JDK_INSTALL_PATH/jdk1.8.0_131  
ENV PATH=$JAVA_HOME/bin:$PATH  
  
  
MAINTAINER Xianyi Ye <https://cn.linkedin.com/in/yexianyi>  
  
RUN yum update -y \  
&& yum install -y wget \  
&& yum install -y fuse-libs \  
&& yum install -y glib-networking \  
&& wget $MEGATOOLS_DOWNLOAD_LINK \  
&& rpm -Uvh $MEGATOOLS_FILE_NAME \  
&& rm -f $MEGATOOLS_FILE_NAME \  
# Install Oracle JDK  
&& mkdir $JDK_INSTALL_PATH \  
&& cd $JDK_INSTALL_PATH \  
&& megadl $JDK_PACKAGE_DOWNLOAD_LINK \  
&& tar -xzvf $JDK_PACKAGE_NAME \  
&& rm -f ./$JDK_PACKAGE_NAME \  
#Uninstall unecessary package  
&& rpm -e `rpm -q megatools` \  
&& yum -y remove glib-networking \  
&& yum -y remove fuse-libs \  
&& yum clean all \  
&& yum autoremove -y \  

