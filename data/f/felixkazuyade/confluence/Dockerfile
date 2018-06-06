FROM felixkazuyade/java-base  
MAINTAINER Felix Kazuya felix.kazuya@icloud.com  
  
# Umgebungsvariablen  
ENV HOME_DIR="/var/atlassian/application-data/confluence"  
ENV INSTALL_DIR="/opt/atlassian/confluence"  
ENV CONF_VERSION="6.3.1"  
ENV DOWNLOAD_URL
http://www.atlassian.com/software/confluence/downloads/binary/atlassian-
confluence-${CONF_VERSION}.tar.gz  
ENV MYSQL_VERSION 5.1.38  
ENV MYSQL_DRIVER_DOWNLOAD_URL
http://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-
java-${MYSQL_VERSION}.tar.gz  
  
#Date of Build  
RUN echo "Built at" $(date) > /etc/built_at  
  
# Portfreigaben  
EXPOSE 8090  
EXPOSE 8091  
# Dateien reinkopieren  
#COPY entrypoint /entrypoint  
#RUN chmod +x /entrypoint  
# Anwendungen  
RUN mkdir -p ${INSTALL_DIR}  
RUN curl -L --silent ${DOWNLOAD_URL} | tar -xz --strip=1 -C ${INSTALL_DIR}  
RUN mkdir -p ${INSTALL_DIR}/conf/Catalina  
RUN chmod -R 700 ${INSTALL_DIR}/conf/Catalina  
RUN chmod -R 700 ${INSTALL_DIR}/conf  
RUN chmod -R 700 ${INSTALL_DIR}/logs  
RUN chmod -R 700 ${INSTALL_DIR}/temp  
RUN chmod -R 700 ${INSTALL_DIR}/work  
RUN curl -Ls "${MYSQL_DRIVER_DOWNLOAD_URL}" | tar -xz --directory
"${INSTALL_DIR}/confluence/WEB-INF/lib" \--strip-components=1 --no-same-owner
"mysql-connector-java-${MYSQL_VERSION}/mysql-connector-
java-${MYSQL_VERSION}-bin.jar"  
RUN echo -e "\nconfluence.home=${HOME_DIR}" >> "${INSTALL_DIR}/confluence/WEB-
INF/classes/confluence-init.properties"  
RUN xmlstarlet ed --inplace \  
\--delete "Server/@debug" \  
\--delete "Server/Service/Connector/@debug" \  
\--delete "Server/Service/Connector/@useURIValidationHack" \  
\--delete "Server/Service/Connector/@minProcessors" \  
\--delete "Server/Service/Connector/@maxProcessors" \  
\--delete "Server/Service/Engine/@debug" \  
\--delete "Server/Service/Engine/Host/@debug" \  
\--delete "Server/Service/Engine/Host/Context/@debug" \  
"${INSTALL_DIR}/conf/server.xml" \  
&& touch -d "@0" "${INSTALL_DIR}/conf/server.xml"  
  
WORKDIR ${INSTALL_DIR}  
  
CMD ["./bin/catalina.sh", "run"]  

