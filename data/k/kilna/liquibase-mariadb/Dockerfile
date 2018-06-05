FROM kilna/liquibase  
LABEL maintainer="Kilna kilna@kilna.com"  
  
ARG jdbc_driver_version  
ENV jdbc_driver_version=${jdbc_driver_version:-2.2.1}\  
jdbc_driver_download_url=https://downloads.mariadb.com/Connectors/java/connector-
java-${jdbc_driver_version}\  
LIQUIBASE_PORT=${LIQUIBASE_PORT:-3306}\  
LIQUIBASE_CLASSPATH=${LIQUIBASE_CLASSPATH:-/opt/jdbc/mariadb-jdbc.jar}\  
LIQUIBASE_DRIVER=${LIQUIBASE_DRIVER:-org.mariadb.jdbc.Driver}\  
LIQUIBASE_URL=${LIQUIBASE_URL:-'jdbc:mariadb://${HOST}:${PORT}/${DATABASE}'}  
  
COPY test/ /opt/test_liquibase_mariadb/  
RUN set -x -e -o pipefail;\  
echo "JDBC DRIVER VERSION: $jdbc_driver_version";\  
cd /opt/jdbc;\  
chmod +x /opt/test_liquibase_mariadb/run_test.sh;\  
jarfile=mariadb-java-client-${jdbc_driver_version}.jar;\  
curl -SOLs ${jdbc_driver_download_url}/${jarfile};\  
[[ -e ${jarfile} ]] || exit 190;\  
ln -s ${jarfile} mariadb-jdbc.jar  
  

