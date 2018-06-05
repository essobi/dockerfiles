FROM ubuntu:14.04  
MAINTAINER Kevin Chabreck <kchabreck@siteworx.com>  
MAINTAINER Justin McWhirter <jmcwhirter@siteworx.com>  
MAINTAINER Nick Noel <nnoel@siteworx.com>  
  
# Builds an image containing Ubuntu and an Oracle Java JDK  
# note: Java is installed to /opt/java_home  
ENV JAVA_DOWNLOAD_URL http://download.oracle.com/otn-pub/java/jdk/8u65-b17/  
ENV JAVA_ARCHIVE_FILENAME jdk-8u65-linux-x64.tar.gz  
  
#update package list  
RUN sudo apt-get update  
  
# install wget  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y wget  
  
# install Oracle Java JDK  
RUN DEBIAN_FRONTEND=noninteractive wget --no-check-certificate --no-cookies
--header "Cookie: oraclelicense=accept-securebackup-cookie"
${JAVA_DOWNLOAD_URL}${JAVA_ARCHIVE_FILENAME} && \  
mkdir /opt/java_home && \  
tar xf ${JAVA_ARCHIVE_FILENAME} -C /opt/java_home --strip-components 1  
  
# define commonly used JAVA_HOME variable  
ENV JAVA_HOME /opt/java_home  
ENV PATH ${PATH}:/opt/java_home/bin  
  
# delete gz file  
RUN rm jdk-8u65-linux-x64.tar.gz  

