FROM tomcat:8.5.31-jre8-slim  
  
ENV CR_BASE=/var/local/cr  
ENV CR_HOME=${CR_BASE}/apphome  
ENV MAVEN_VERSION=3.3.9-4  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends git maven="$MAVEN_VERSION" \  
openjdk-8-jdk="$JAVA_DEBIAN_VERSION" \  
ca-certificates-java="$CA_CERTIFICATES_JAVA_VERSION" \  
&& mkdir -p $CR_BASE \  
$CR_BASE/build \  
$CR_HOME \  
$CR_HOME/acl \  
$CR_HOME/filestore \  
$CR_HOME/staging \  
$CR_HOME/tmp \  
&& git clone https://github.com/digital-agenda-data/scoreboard.contreg.git
$CR_BASE/build \  
&& cd $CR_BASE/build \  
&& git checkout 5089-docker-migration \  
&& cp docker.properties local.properties \  
&& sed -i "/^\s*application.homeDir/c\application.homeDir\=${CR_HOME}"
local.properties \  
&& mvn clean install -Dmaven.test.skip=true \  
&& cp -pr target/cr-das $CATALINA_HOME/webapps/data  
  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
  
VOLUME ${CR_HOME}  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["catalina.sh", "run"]  
  

