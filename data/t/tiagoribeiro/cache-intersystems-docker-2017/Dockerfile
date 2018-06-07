FROM centos:latest  
MAINTAINER Tiago G. Ribeiro <tiago.sistema@yahoo.com>  
  
RUN yum -y update && yum -y install which tar hostname net-tools wget && yum
-y clean all  
  
ENV TMP_INSTALL_DIR=/tmp/distrib  
ENV TMP_FILE_INSTALL="cache-2017.1.1.111.0su-lnxrhx64.tar.gz"  
ENV TMP_DIRECTORY="cache-2017.1.1.111.0su-lnxrhx64"  
ENV ISC_PACKAGE_INSTANCENAME="CACHE" \  
ISC_PACKAGE_INSTALLDIR="/usr/cachesys" \  
ISC_PACKAGE_UNICODE="Y"  
RUN mkdir ${TMP_INSTALL_DIR}  
WORKDIR ${TMP_INSTALL_DIR}  
  
RUN wget -c --progress=bar
http://download2.intersystems.com/webcinst/201711/f65c/LINUX/${TMP_FILE_INSTALL}  
RUN tar -xzf ${TMP_FILE_INSTALL}  
  
RUN ./${TMP_DIRECTORY}/cinstall_silent && rm -rf ${TMP_INSTALL_DIR}  
  
RUN ccontrol stop ${ISC_PACKAGE_INSTANCENAME} quietly  
  
WORKDIR /  
ADD ccontainermain .  
RUN chmod +x ccontainermain  
  
EXPOSE 57772 1972 22  
ENTRYPOINT ["/ccontainermain","-cconsole","-i","CACHE"]  

