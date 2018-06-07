FROM streamsets/datacollector:2.7.1.0  
MAINTAINER Carlo Wouters <carlo.wouters@ae.be>  
  
ENV SDC_USER=sdc  
  
ENV SDC_VERSION ${SDC_VERSION:-2.7.1.0}  
ENV SDC_DIST="/opt/streamsets-datacollector-${SDC_VERSION}"  
ENV STREAMSETS_LIBRARIES_EXTRA_DIR="${SDC_DIST}/libs-common-lib"  
ENV MYSQL_CONNECTOR_VERSION="5.1.41"  
  
# Set permissions on shared libs folder  
USER root  
RUN chown -R "${SDC_USER}:${SDC_USER}" "${STREAMSETS_LIBRARIES_EXTRA_DIR}"  
USER ${SDC_USER}  
  
  
########################################  
# add specific drivers  
########################################  
  
# Move oracle driver and set the appropriate permissions  
COPY ojdbc7.jar "${STREAMSETS_LIBRARIES_EXTRA_DIR}"  
USER root  
RUN chown -R "${SDC_USER}:${SDC_USER}"
"${STREAMSETS_LIBRARIES_EXTRA_DIR}/ojdbc7.jar"  
  
# Move MSSQL JDBC driver and set the appropriate permissions  
COPY sqljdbc41.jar "${STREAMSETS_LIBRARIES_EXTRA_DIR}"  
USER root  
RUN chown -R "${SDC_USER}:${SDC_USER}"
"${STREAMSETS_LIBRARIES_EXTRA_DIR}/sqljdbc41.jar"  
  
# Move MySQL JDBC driver and set the appropriate permissions  
COPY mysql-connector-java-${MYSQL_CONNECTOR_VERSION}-bin.jar
"${STREAMSETS_LIBRARIES_EXTRA_DIR}"  
USER root  
RUN chown -R "${SDC_USER}:${SDC_USER}"
"${STREAMSETS_LIBRARIES_EXTRA_DIR}/mysql-connector-
java-${MYSQL_CONNECTOR_VERSION}-bin.jar"  
  
# Move Streamsets datacollector java sdk 2.2.0.0 and set the appropriate
permissions  
COPY streamsets-datacollector-sdk-${SDC_VERSION}.jar
"${STREAMSETS_LIBRARIES_EXTRA_DIR}"  
USER root  
RUN chown -R "${SDC_USER}:${SDC_USER}"
"${STREAMSETS_LIBRARIES_EXTRA_DIR}/streamsets-datacollector-
sdk-${SDC_VERSION}.jar"  
  
# USER ${SDC_USER}  
  
  
  
########################################  
# install specific packages  
########################################  
  
# comma separated names for packages to be installed  
# the names used should be the ones found in the package manager  
# e.g. streamsets-datacollector-apache-kafka_0_10-lib  
ARG INSTALLS=streamsets-datacollector-apache-kafka_0_10-lib\  
,streamsets-datacollector-jdbc-lib\  
,streamsets-datacollector-mongodb_3-lib\  
,streamsets-datacollector-mysql-binlog-lib\  
,streamsets-datacollector-cdh_5_9-lib  
  
RUN if [[ ! -z $INSTALLS ]]; then $SDC_DIST/bin/streamsets stagelibs
-install=$INSTALLS ; fi  

