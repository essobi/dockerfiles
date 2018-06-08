FROM openjdk:8-jdk-slim AS build  
  
MAINTAINER Matthias Nuessler <m.nuessler@web.de>  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get -y dist-upgrade && \  
DEBIAN_FRONTEND=noninteractive apt-get -y --fix-missing --no-install-
recommends install \  
maven \  
subversion && \  
svn checkout -r 662 svn://svn.code.sf.net/p/schemaspy/code/trunk
/usr/src/schemaspy && \  
perl -p -i -e 's/(driverPath=).*/\1\/usr\/share\/java\/mysql-connector-
java\\.jar/g' \  
/usr/src/schemaspy/src/main/resources/net/sourceforge/schemaspy/dbTypes/mysql.properties
&& \  
mvn -f /usr/src/schemaspy/pom.xml package && \  
mkdir /opt/schemaspy && \  
mv /usr/src/schemaspy/target/schemaspy-5.0.0.jar /opt/schemaspy/schemaspy.jar
&& \  
rm -Rf ~/.m2 /usr/src/schemaspy && \  
DEBIAN_FRONTEND=noninteractive apt-get -y remove subversion maven && \  
DEBIAN_FRONTEND=noninteractive apt-get -y autoremove && \  
apt-get clean  
  
  
FROM openjdk:8-jre-slim  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get -y dist-upgrade && \  
DEBIAN_FRONTEND=noninteractive apt-get -y --no-install-recommends install \  
graphviz \  
less \  
libhsqldb-java \  
libmysql-java \  
libpostgresql-jdbc-java  
  
COPY start.sh /  
COPY --from=build /opt/schemaspy/schemaspy.jar /opt/schemaspy/schemaspy.jar  
  
CMD ["--help"]  
ENTRYPOINT ["/start.sh"]  

