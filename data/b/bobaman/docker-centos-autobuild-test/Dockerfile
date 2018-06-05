FROM centos:7.3.1611  
MAINTAINER bobaman <bobaman@nate.com>  
  
ENV JAVA_VERSION 7u80  
ENV JAVA_BUILD b15  
ENV OS_VERSION x64  
  
ENV DOWNLOAD_COOKIE Cookie: oraclelicense=accept-securebackup-cookie  
ENV DOWNLOAD_SITE http://download.oracle.com/otn-pub/java/jdk  
ENV DOWNLOAD_VERSION ${JAVA_VERSION}-${JAVA_BUILD}  
ENV DOWNLOAD_FILE jdk-${JAVA_VERSION}-linux-${OS_VERSION}.rpm  
  
# RUN yum -y update;yum clean all;  
WORKDIR /opt  
  
RUN curl -v -j -k -L -H "${DOWNLOAD_COOKIE}"
${DOWNLOAD_SITE}/${DOWNLOAD_VERSION}/${DOWNLOAD_FILE} > ${DOWNLOAD_FILE}  
  
RUN rpm -ivh ${DOWNLOAD_FILE}  
  
RUN rm -f ${DOWNLOAD_FILE}  
  
WORKDIR /  
  
CMD ["/bin/bash"]  

