FROM jboss/wildfly:10.1.0.Final  
MAINTAINER Leonardo Loures <luvres@hotmail.com>  
  
ENV PASS admin  
  
ENV URL_JDBC="https://github.com/luvres/jdbc/raw/master/"  
  
ENV MYSQL_CONN_J_VERSION 5.1.44  
ENV MYSQL_CONN_J mysql-connector-java-$MYSQL_CONN_J_VERSION-bin.jar  
ENV MYSQL_CONN_J_URL $URL_JDBC/$MYSQL_CONN_J  
  
ENV MARIADB_CONN_J_VERSION 2.2.0  
ENV MARIADB_CONN_J mariadb-java-client-$MARIADB_CONN_J_VERSION.jar  
ENV MARIADB_CONN_J_URL $URL_JDBC/$MARIADB_CONN_J  
  
ENV ORACLE_CONN_J ojdbc7.jar  
ENV ORACLE_CONN_J_URL $URL_JDBC/$ORACLE_CONN_J  
  
ENV POSTGRES_CONN_J postgresql-42.1.4.jar  
ENV POSTGRES_CONN_J_URL $URL_JDBC/$POSTGRES_CONN_J  
  
### Datasource  
RUN mkdir -p /opt/jboss/wildfly/modules/system/layers/base/com/mysql/main \  
&& curl -fSL $MYSQL_CONN_J_URL -o
/opt/jboss/wildfly/modules/system/layers/base/com/mysql/main/$MYSQL_CONN_J  
RUN mkdir -p /opt/jboss/wildfly/modules/system/layers/base/org/mariadb/main \  
&& curl -fSL $MARIADB_CONN_J_URL -o
/opt/jboss/wildfly/modules/system/layers/base/org/mariadb/main/$MARIADB_CONN_J  
RUN mkdir -p /opt/jboss/wildfly/modules/system/layers/base/com/oracle/main \  
&& curl -fSL $ORACLE_CONN_J_URL -o
/opt/jboss/wildfly/modules/system/layers/base/com/oracle/main/$ORACLE_CONN_J  
RUN mkdir -p /opt/jboss/wildfly/modules/system/layers/base/org/postgres/main \  
&& curl -fSL $POSTGRES_CONN_J_URL -o
/opt/jboss/wildfly/modules/system/layers/base/org/postgres/main/$POSTGRES_CONN_J  
  
# module.xml (MySQL)  
RUN echo '<?xml version="1.0" encoding="UTF-8"?>'
>>/opt/jboss/wildfly/modules/system/layers/base/com/mysql/main/module.xml \  
&& echo '<module xmlns="urn:jboss:module:1.1" name="com.mysql">'
>>/opt/jboss/wildfly/modules/system/layers/base/com/mysql/main/module.xml \  
&& echo '<resources>'
>>/opt/jboss/wildfly/modules/system/layers/base/com/mysql/main/module.xml \  
&& echo ' <resource-root path="mysql-connector-java-5.1.44-bin.jar"/>'
>>/opt/jboss/wildfly/modules/system/layers/base/com/mysql/main/module.xml \  
&& echo '</resources>'
>>/opt/jboss/wildfly/modules/system/layers/base/com/mysql/main/module.xml \  
&& echo '<dependencies>'
>>/opt/jboss/wildfly/modules/system/layers/base/com/mysql/main/module.xml \  
&& echo ' <module name="javax.api"/>'
>>/opt/jboss/wildfly/modules/system/layers/base/com/mysql/main/module.xml \  
&& echo ' <module name="javax.transaction.api"/>'
>>/opt/jboss/wildfly/modules/system/layers/base/com/mysql/main/module.xml \  
&& echo '</dependencies>'
>>/opt/jboss/wildfly/modules/system/layers/base/com/mysql/main/module.xml \  
&& echo '</module>'
>>/opt/jboss/wildfly/modules/system/layers/base/com/mysql/main/module.xml  
# module.xml (MariaDB)  
RUN echo '<?xml version="1.0" encoding="UTF-8"?>'
>>/opt/jboss/wildfly/modules/system/layers/base/org/mariadb/main/module.xml \  
&& echo '<module xmlns="urn:jboss:module:1.1" name="org.mariadb">'
>>/opt/jboss/wildfly/modules/system/layers/base/org/mariadb/main/module.xml \  
&& echo '<resources>'
>>/opt/jboss/wildfly/modules/system/layers/base/org/mariadb/main/module.xml \  
&& echo ' <resource-root path="mariadb-java-client-2.2.0.jar"/>'
>>/opt/jboss/wildfly/modules/system/layers/base/org/mariadb/main/module.xml \  
&& echo '</resources>'
>>/opt/jboss/wildfly/modules/system/layers/base/org/mariadb/main/module.xml \  
&& echo '<dependencies>'
>>/opt/jboss/wildfly/modules/system/layers/base/org/mariadb/main/module.xml \  
&& echo ' <module name="javax.api"/>'
>>/opt/jboss/wildfly/modules/system/layers/base/org/mariadb/main/module.xml \  
&& echo ' <module name="javax.transaction.api"/>'
>>/opt/jboss/wildfly/modules/system/layers/base/org/mariadb/main/module.xml \  
&& echo '</dependencies>'
>>/opt/jboss/wildfly/modules/system/layers/base/org/mariadb/main/module.xml \  
&& echo '</module>'
>>/opt/jboss/wildfly/modules/system/layers/base/org/mariadb/main/module.xml  
# module.xml (OracleXE)  
RUN echo '<?xml version="1.0" encoding="UTF-8"?>'
>>/opt/jboss/wildfly/modules/system/layers/base/com/oracle/main/module.xml \  
&& echo '<module xmlns="urn:jboss:module:1.1" name="com.oracle">'
>>/opt/jboss/wildfly/modules/system/layers/base/com/oracle/main/module.xml \  
&& echo '<resources>'
>>/opt/jboss/wildfly/modules/system/layers/base/com/oracle/main/module.xml \  
&& echo ' <resource-root path="ojdbc7.jar"/>'
>>/opt/jboss/wildfly/modules/system/layers/base/com/oracle/main/module.xml \  
&& echo '</resources>'
>>/opt/jboss/wildfly/modules/system/layers/base/com/oracle/main/module.xml \  
&& echo '<dependencies>'
>>/opt/jboss/wildfly/modules/system/layers/base/com/oracle/main/module.xml \  
&& echo ' <module name="javax.api"/>'
>>/opt/jboss/wildfly/modules/system/layers/base/com/oracle/main/module.xml \  
&& echo ' <module name="javax.transaction.api"/>'
>>/opt/jboss/wildfly/modules/system/layers/base/com/oracle/main/module.xml \  
&& echo '</dependencies>'
>>/opt/jboss/wildfly/modules/system/layers/base/com/oracle/main/module.xml \  
&& echo '</module>'
>>/opt/jboss/wildfly/modules/system/layers/base/com/oracle/main/module.xml  
# module.xml (PostgreSQL)  
RUN echo '<?xml version="1.0" encoding="UTF-8"?>'
>>/opt/jboss/wildfly/modules/system/layers/base/org/postgres/main/module.xml \  
&& echo '<module xmlns="urn:jboss:module:1.1" name="org.postgres">'
>>/opt/jboss/wildfly/modules/system/layers/base/org/postgres/main/module.xml \  
&& echo '<resources>'
>>/opt/jboss/wildfly/modules/system/layers/base/org/postgres/main/module.xml \  
&& echo ' <resource-root path="postgresql-42.1.4.jar"/>'
>>/opt/jboss/wildfly/modules/system/layers/base/org/postgres/main/module.xml \  
&& echo '</resources>'
>>/opt/jboss/wildfly/modules/system/layers/base/org/postgres/main/module.xml \  
&& echo '<dependencies>'
>>/opt/jboss/wildfly/modules/system/layers/base/org/postgres/main/module.xml \  
&& echo ' <module name="javax.api"/>'
>>/opt/jboss/wildfly/modules/system/layers/base/org/postgres/main/module.xml \  
&& echo ' <module name="javax.transaction.api"/>'
>>/opt/jboss/wildfly/modules/system/layers/base/org/postgres/main/module.xml \  
&& echo '</dependencies>'
>>/opt/jboss/wildfly/modules/system/layers/base/org/postgres/main/module.xml \  
&& echo '</module>'
>>/opt/jboss/wildfly/modules/system/layers/base/org/postgres/main/module.xml  
### standalone.xml  
# (MySQL)  
RUN sed -i 's/<\/drivers>/ <driver name="MySQL"
module="com.mysql">\n\t\t\t<xa-datasource-
class>com.mysql.jdbc.jdbc2.optional.MysqlXADataSource<\/xa-datasource-
class>\n\t\t <\/driver>\n\t\t<\/drivers>/'
/opt/jboss/wildfly/standalone/configuration/standalone.xml  
  
# (MariaDB)  
RUN sed -i 's/<\/drivers>/ <driver name="MariaDB"
module="org.mariadb">\n\t\t\t<xa-datasource-
class>org.mariadb.jdbc.MySQLDataSource<\/xa-datasource-class>\n\t\t
<\/driver>\n\t\t<\/drivers>/'
/opt/jboss/wildfly/standalone/configuration/standalone.xml  
  
# (OracleXE)  
RUN sed -i 's/<\/drivers>/ <driver name="OracleXE"
module="com.oracle">\n\t\t\t<xa-datasource-
class>oracle.jdbc.xa.client.OracleXADataSource<\/xa-datasource-class>\n\t\t
<\/driver>\n\t\t<\/drivers>/'
/opt/jboss/wildfly/standalone/configuration/standalone.xml  
  
# (PostgreSQL)  
RUN sed -i 's/<\/drivers>/ <driver name="PostgreSQL"
module="org.postgres">\n\t\t\t<xa-datasource-
class>org.postgresql.xa.PGXADataSource<\/xa-datasource-class>\n\t\t
<\/driver>\n\t\t<\/drivers>/'
/opt/jboss/wildfly/standalone/configuration/standalone.xml  
  
  
ADD start.sh /etc/start.sh  
ENTRYPOINT ["bash", "/etc/start.sh"]  
  

