FROM nearpod/alpine-jvm:3.7-jdk8  
  
ARG KEYCLOAK_VERSION="3.4.3.Final"  
ARG KEYCLOAK_HOME="/usr/local/keycloak-$KEYCLOAK_VERSION"  
ARG JDBC_POSTGRES_VERSION=42.1.4  
ARG JDBC_MYSQL_VERSION=5.1.44  
ARG MYSQL_MD5=526d4f3b2b127abcc25b575ece2c54d1  
ARG KEYCLOAK_USER=jboss  
  
# Enables signals getting passed from startup script to JVM  
# ensuring clean shutdown when container is stopped.  
ENV LAUNCH_JBOSS_IN_BACKGROUND 1  
ENV PROXY_ADDRESS_FORWARDING false  
ENV KEYCLOAK_HOME=$KEYCLOAK_HOME \  
JBOSS_HOME=$KEYCLOAK_HOME \  
JDBC_POSTGRES_VERSION=$JDBC_POSTGRES_VERSION \  
JDBC_MYSQL_VERSION=$JDBC_MYSQL_VERSION  
RUN set -ex; \  
WORKDIR="$PWD"; \  
curl -q -sSLO
"https://downloads.jboss.org/keycloak/$KEYCLOAK_VERSION/keycloak-$KEYCLOAK_VERSION.tar.gz";
\  
curl -q -sSLO
"https://downloads.jboss.org/keycloak/$KEYCLOAK_VERSION/keycloak-$KEYCLOAK_VERSION.tar.gz.md5";
\  
echo "$(cat keycloak-$KEYCLOAK_VERSION.tar.gz.md5)
keycloak-$KEYCLOAK_VERSION.tar.gz" | md5sum -c; \  
mkdir -p "$KEYCLOAK_HOME"; \  
tar -xzf "keycloak-$KEYCLOAK_VERSION.tar.gz" \--strip-components=1 -C
"$KEYCLOAK_HOME"; \  
rm -f "keycloak-$KEYCLOAK_VERSION.tar.gz"
"keycloak-$KEYCLOAK_VERSION.tar.gz.md5"; \  
curl -q -sSLO "http://central.maven.org/maven2/mysql/mysql-connector-
java/$JDBC_MYSQL_VERSION/mysql-connector-java-$JDBC_MYSQL_VERSION.jar"; \  
curl -q -sSLO "http://central.maven.org/maven2/mysql/mysql-connector-
java/$JDBC_MYSQL_VERSION/mysql-connector-java-$JDBC_MYSQL_VERSION.jar.md5"; \  
echo "$(cat mysql-connector-java-$JDBC_MYSQL_VERSION.jar.md5) mysql-connector-
java-$JDBC_MYSQL_VERSION.jar" | md5sum -c; \  
mkdir -p "$KEYCLOAK_HOME/modules/system/layers/base/com/mysql/jdbc/main/"; \  
mv "mysql-connector-java-$JDBC_MYSQL_VERSION.jar"
"$KEYCLOAK_HOME/modules/system/layers/base/com/mysql/jdbc/main/mysql-
jdbc.jar"; \  
curl -q -sSLO
"http://central.maven.org/maven2/org/postgresql/postgresql/$JDBC_POSTGRES_VERSION/postgresql-$JDBC_POSTGRES_VERSION.jar";
\  
curl -q -sSLO
"http://central.maven.org/maven2/org/postgresql/postgresql/$JDBC_POSTGRES_VERSION/postgresql-$JDBC_POSTGRES_VERSION.jar.md5";
\  
echo "$(cat postgresql-$JDBC_POSTGRES_VERSION.jar.md5)
postgresql-$JDBC_POSTGRES_VERSION.jar" | md5sum -c; \  
mkdir -p "$KEYCLOAK_HOME/modules/system/layers/base/org/postgresql/jdbc/main";
\  
mv "postgresql-$JDBC_POSTGRES_VERSION.jar"
"$KEYCLOAK_HOME/modules/system/layers/base/org/postgresql/jdbc/main/postgres-
jdbc.jar"; \  
rm -rf "$KEYCLOAK_HOME/standalone/configuration/standalone_xml_history"
"$KEYCLOAK_HOME/standalone_ha/configuration/standalone_xml_history"; \  
rm -f "mysql-connector-java-$JDBC_MYSQL_VERSION.jar.md5"
"postgresql-$JDBC_POSTGRES_VERSION.jar.md5"  
  
EXPOSE 8080  
  
WORKDIR $KEYCLOAK_HOME  
  
COPY files/docker-entrypoint.sh files/change-database.sh $KEYCLOAK_HOME/bin/  
COPY files/cli $KEYCLOAK_HOME/cli/  
COPY files/mysql-module.xml
$KEYCLOAK_HOME/modules/system/layers/base/org/mysql/jdbc/main/module.xml  
COPY files/postgres-module.xml
$KEYCLOAK_HOME/modules/system/layers/base/org/postgresql/jdbc/main/module.xml  
  
  
RUN set -ex; \  
WORKDIR="$PWD"; \  
addgroup -g 1000 "$KEYCLOAK_USER"; \  
adduser -D -h "$WORKDIR" -u 1000 -G "$KEYCLOAK_USER" "$KEYCLOAK_USER"; \  
[ `id -u "$KEYCLOAK_USER"` -eq 1000 ]; \  
[ `id -g "$KEYCLOAK_USER"` -eq 1000 ]; \  
chown -R "$KEYCLOAK_USER:$KEYCLOAK_USER" "$KEYCLOAK_HOME";  
  
USER jboss:jboss  
  
ENTRYPOINT [ "bin/docker-entrypoint.sh" ]  
  
CMD ["-b", "0.0.0.0"]  

