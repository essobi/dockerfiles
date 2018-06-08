FROM debian  
MAINTAINER christopher.hoskin@gmail.com  
  
RUN apt-get update && apt-get install -y default-jre-headless  
RUN apt-get install -y unzip wget  
RUN wget http://repo1.maven.org/maven2/net/tirasa/connid/connector-server-
zip/1.4.3.0/connector-server-zip-1.4.3.0.zip  
RUN unzip connector-server-zip-1.4.3.0.zip -d /opt/  
RUN rm connector-server-zip-1.4.3.0.zip  
  
RUN mkdir /etc/connector-server  
RUN mkdir -p /opt/connid-connector-server/bundles  
RUN mkdir -p /opt/connid-connector-server/bundles-lib  
  
ENV cmd_version 0.2  
ENV ad_version 1.3.4  
ENV rest_version 1.0.1  
ENV csvdir_version 0.8.7  
ENV ldap_version 1.5.2  
ENV googleapps_version 1.4.1  
RUN wget
http://repo1.maven.org/maven2/net/tirasa/connid/bundles/net.tirasa.connid.bundles.cmd/${cmd_version}/net.tirasa.connid.bundles.cmd-${cmd_version}.jar
-O /opt/connid-connector-
server/bundles/net.tirasa.connid.bundles.cmd-${cmd_version}.jar  
RUN wget
http://repo1.maven.org/maven2/net/tirasa/connid/bundles/net.tirasa.connid.bundles.ad/${ad_version}/net.tirasa.connid.bundles.ad-${ad_version}.jar
-O /opt/connid-connector-
server/bundles/net.tirasa.connid.bundles.ad-${ad_version}.jar  
RUN wget
http://repo1.maven.org/maven2/net/tirasa/connid/bundles/net.tirasa.connid.bundles.rest/${rest_version}/net.tirasa.connid.bundles.rest-${rest_version}.jar
-O /opt/connid-connector-
server/bundles/net.tirasa.connid.bundles.rest-${rest_version}.jar  
RUN wget
http://repo1.maven.org/maven2/net/tirasa/connid/bundles/net.tirasa.connid.bundles.csvdir/${csvdir_version}/net.tirasa.connid.bundles.csvdir-${csvdir_version}.jar
-O /opt/connid-connector-
server/bundles/net.tirasa.connid.bundles.csvdir-${csvdir_version}.jar  
RUN wget
http://repo1.maven.org/maven2/net/tirasa/connid/bundles/net.tirasa.connid.bundles.ldap/${ldap_version}/net.tirasa.connid.bundles.ldap-${ldap_version}.jar
-O /opt/connid-connector-
server/bundles/net.tirasa.connid.bundles.ldap-${ldap_version}.jar  
RUN wget
http://repo1.maven.org/maven2/net/tirasa/connid/bundles/net.tirasa.connid.bundles.googleapps/${googleapps_version}/net.tirasa.connid.bundles.googleapps-${googleapps_version}.jar
-O /opt/connid-connector-
server/bundles/net.tirasa.connid.bundles.googleapps-${googleapps_version}.jar  
  
ENV polygon_databasetable_version 1.4.2.0  
ENV polygon_csv_version 2.1  
ENV polygon_ldap 1.5.1  
RUN wget
http://nexus.evolveum.com/nexus/service/local/repositories/releases/content/com/evolveum/polygon/connector-
databasetable/${polygon_databasetable_version}/connector-
databasetable-${polygon_databasetable_version}.jar -O /opt/connid-connector-
server/bundles/connector-databasetable-${polygon_databasetable_version}.jar  
RUN wget
http://nexus.evolveum.com/nexus/content/groups/public/com/evolveum/polygon/connector-
csv/${polygon_csv_version}/connector-csv-${polygon_csv_version}.jar -O
/opt/connid-connector-server/bundles/connector-csv-${polygon_csv_version}.jar  
RUN wget
http://nexus.evolveum.com/nexus/content/repositories/releases/com/evolveum/polygon/connector-
ldap/${polygon_ldap}/connector-ldap-${polygon_ldap}.jar -O /opt/connid-
connector-server/bundles/connector-ldap-${polygon_ldap}.jar  
  
ENV oracle_version 1.1.0.0  
ENV scriptedsql_version 1.1.2.0.em3  
  
RUN wget http://nexus.evolveum.com/nexus/service/local/repositories/openicf-
releases/content/org/forgerock/openicf/connectors/oracle-
connector/${oracle_version}/oracle-connector-${oracle_version}.jar -O
/opt/connid-connector-server/oracle-connector-${oracle_version}.jar  
RUN wget http://nexus.evolveum.com/nexus/content/repositories/openicf-
releases/org/forgerock/openicf/connectors/scriptedsql-
connector/${scriptedsql_version}/scriptedsql-
connector-${scriptedsql_version}.jar -O /opt/connid-connector-
server/bundles/scriptedsql-connector-${scriptedsql_version}.jar  
  
COPY connector-server.properties /etc/connector-server/connector-
server.properties  
  
RUN java -cp "/opt/connid-connector-server/lib/framework/*"
org.identityconnectors.framework.server.Main -setKey -key fibble -properties
/etc/connector-server/connector-server.properties  
  
RUN mkdir -p /opt/connid-connector-server/test-files/  
  
COPY test-file1.csv /opt/connid-connector-server/test-files/test-file1.csv  
COPY test-file2.csv /opt/connid-connector-server/test-files/test-file2.csv  
  
EXPOSE 8759  
CMD [ "java", "-cp", "/opt/connid-connector-server/lib/framework/*",
"org.identityconnectors.framework.server.Main", "-run", "-properties",
"/etc/connector-server/connector-server.properties" ]  

