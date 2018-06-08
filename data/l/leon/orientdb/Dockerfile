FROM java:8  
MAINTAINER Leon Radley "leon@radley.se"  
# Set workdir for download and unpack  
WORKDIR /opt  
  
ENV ORIENTDB_VERSION orientdb-community-2.0.3  
ENV ORIENTDB_URL
http://www.orientechnologies.com/download.php?email=unknown@unknown.com&file=${ORIENTDB_VERSION}.tar.gz&os=linux  
ENV ORIENTDB_ROOT_PASSWORD orientdbmasterpassword  
ENV ORIENTDB_BACKUP false  
  
# Download orientdb  
ADD ${ORIENTDB_URL} orientdb-community.tar.gz  
  
# Unpack  
RUN tar -xzf orientdb-community.tar.gz  
RUN rm orientdb-community.tar.gz  
RUN mv ${ORIENTDB_VERSION} orientdb  
  
# Set workdir to newly unpacked orientdb  
WORKDIR /opt/orientdb  
  
# Move config to /etc/orientdb  
RUN mv config orientdb  
RUN mv orientdb /etc  
RUN ln -s /etc/orientdb config  
  
# Set logging path  
RUN mkdir /var/log/orientdb  
RUN sed -i -e "s/java.util.logging.FileHandler.pattern=..\/log\/orient-
server.log/java.util.logging.FileHandler.pattern=\/var\/log\/orientdb\/orientdb.log/g"
/etc/orientdb/orientdb-server-log.properties  
  
# Set data  
RUN mkdir -p /var/lib/orientdb/data  
RUN sed -i -e "s/<\/properties>/<entry name=\"server.database.path\"
value=\"\/var\/lib\/orientdb\/data\" \/><\/properties>/g"
/etc/orientdb/orientdb-server-config.xml  
  
# Set backup  
# Not working yet  
#RUN mkdir /var/lib/orientdb/backup  
#RUN sed -i -e
"s/<handler\sclass=\"com.orientechnologies.orient.server.handler.OAutomaticBackup\">*<parameters>*<parameter\sname=\"enabled\"\svalue=\"false\"/>/<handler
class=\"com.orientechnologies.orient.server.handler.OAutomaticBackup\"><parameters><parameter
name=\"enabled\" value=\"${ORIENTDB_BACKUP}\"/>/g" /etc/orientdb/orientdb-
server-config.xml  
# Create standard db  
# Not working yet  
#<storage name="mydb" path="local:C:/temp/databases/mydb" userName="admin"
userPassword="admin" loaded-at-startup="true" />  
# Expose volumes  
VOLUME ["/etc/orientdb", "/var/lib/orientdb/data", "/var/log/orientdb"]  
  
# Expose binary and http ports  
EXPOSE 2424 2480  
ENTRYPOINT ["bin/server.sh"]  

