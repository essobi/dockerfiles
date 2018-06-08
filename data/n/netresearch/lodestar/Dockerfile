FROM tomcat:8  
# Download openlink libs required for virtuoso  
# @todo Build lodestar with -P virtuoso  
RUN mkdir -p /opt/openlink \  
&& cd /opt/openlink \  
&& wget
http://opldownload.s3.amazonaws.com/uda/virtuoso/7.2/rdfproviders/jena/210/virt_jena2.jar
\  
&& wget
http://opldownload.s3.amazonaws.com/uda/virtuoso/7.2/jdbc/virtjdbc4.jar  
  
# Download lodestar  
RUN mkdir -p /opt/lodestar \  
&& cd /opt/lodestar \  
&& wget -O - https://github.com/EBISPOT/lodestar/tarball/master | tar -xz
--strip-components=1  
  
# Build lodestar  
RUN cd /opt/lodestar \  
&& nativeBuildDeps=" \  
openjdk-${JAVA_VERSION%%[-~bu]*}-jdk=$JAVA_DEBIAN_VERSION \  
maven \  
" \  
&& apt-get update && apt-get install -y --no-install-recommends
$nativeBuildDeps && rm -rf /var/lib/apt/lists/* \  
&& mvn install:install-file -Dfile=/opt/openlink/virt_jena2.jar
-DgroupId=openlinksw.com \  
-DartifactId=virt-jena -Dversion=1.8 -Dpackaging=jar \  
&& mvn install:install-file -Dfile=/opt/openlink/virt_jena2.jar
-DgroupId=openlinksw.com \  
-DartifactId=virt-jdbc -Dversion=4.0.1 -Dpackaging=jar \  
&& mvn clean package \  
&& apt-get purge -y --auto-remove $nativeBuildDeps  
  
# Deploy lodestar  
RUN cp /opt/lodestar/web-ui/target/lodestar.war "$CATALINA_HOME/webapps" \  
&& cp -r /opt/lodestar/web-ui/target/lodestar "$CATALINA_HOME/webapps"  
  
ENV SERVICE_BASE_URI http://localhost:8080/lodestar  
ENV ENDPOINT_URL http://dbpedia.org/sparql  
ENV MAX_LIMIT 1000  
ENV TOP_RELATIONSHIP
http://xmlns.com/foaf/0.1/page,http://purl.org/dc/terms/identifier  
ENV IGNORE_RELATIONSHIP http://www.w3.org/1999/02/22-rdf-syntax-ns#type  
ENV IGNORE_TYPES http://www.w3.org/2000/01/rdf-
schema#Resource,http://www.w3.org/2002/07/owl#Class,http://www.w3.org/2002/07/owl#Thing,http://www.w3.org/2002/07/owl#NamedIndividual  
ENV IGNORE_BLANKNODES true  
ENV LABEL http://www.w3.org/2000/01/rdf-
schema#label,http://www.w3.org/2004/02/skos/core#prefLabel  
ENV DESCRIPTION
http://purl.org/dc/terms/description,http://purl.org/dc/elements/1.1/description,http://www.w3.org/2004/02/skos/core#definition  
ENV DEPICT http://xmlns.com/foaf/0.1/depiction  
ENV MAX_OBJECTS 50  
ENV USE_INFERENCE false  
  
COPY ./entrypoint.sh /usr/local/bin/lodestar-entrypoint.sh  
RUN chmod +x /usr/local/bin/lodestar-entrypoint.sh  
ENTRYPOINT ["/usr/local/bin/lodestar-entrypoint.sh"]  
CMD ["catalina.sh", "run"]

