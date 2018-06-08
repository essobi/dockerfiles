FROM ubuntu:14.04  
MAINTAINER Scandio GmbH <info@scandio.de>  
  
ENV ATL_HOME /opt/atlassian/home  
ENV TESTSYSTEM_WORK_DIR /opt/atlassian/testsystem  
ENV TESTSYSTEM_CONFIG_PATH ${TESTSYSTEM_WORK_DIR}/testsystem.conf  
ENV MYSQL_DUMP_CREATE false  
ENV MYSQL_DUMP_HOST db  
ENV MYSQL_DUMP_USER none  
ENV MYSQL_DUMP_PASS none  
ENV MYSQL_DUMP_DB none  
ENV MYSQL_DUMP_PATH ${TESTSYSTEM_WORK_DIR}/db.sql  
ENV MYSQL_IMPORT_HOST db  
ENV MYSQL_IMPORT_USER none  
ENV MYSQL_IMPORT_PASS none  
ENV MYSQL_IMPORT_DB none  
ENV RUN_USER root  
ENV ATL_USER daemon  
  
RUN apt-get update && \  
apt-get install -y \  
mysql-client \  
sed && \  
apt-get clean  
  
COPY configure-and-start.sh ${ATL_INSTALL}/bin/  
  
USER ${RUN_USER}  
  
RUN chown ${RUN_USER}: ${ATL_INSTALL}/bin/configure-and-start.sh  
RUN mkdir -p ${ATL_HOME} && \  
mkdir -p ${TESTSYSTEM_WORK_DIR}  
  
VOLUME ["${ATL_HOME}"]  
VOLUME ["${TESTSYSTEM_CONFIG_PATH}"]  
  
WORKDIR /  
  
ENTRYPOINT ["bin/configure-and-start.sh"]  
  

