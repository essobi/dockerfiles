FROM alpine:3.4  
  
ENV NEO4J_VERSION=3.1.0  
ENV
NEO4J_SHA256=1f289296c23004ace4d37e14f2af433d203dfb028977534429e766bc308d584a  
ENV NEO4J_TARBALL=neo4j-enterprise-${NEO4J_VERSION}-unix.tar.gz  
ARG
NEO4J_URI=https://neo4j.com/artifact.php?name=neo4j-enterprise-${NEO4J_VERSION}-unix.tar.gz  
  
COPY ./local-package/* /tmp/  
  
RUN apk update && apk add --no-cache openjdk8-jre curl bash ca-certificates  
  
RUN curl --fail --show-error --silent --location ${NEO4J_URI} -o
${NEO4J_TARBALL} \  
&& echo "${NEO4J_SHA256} ${NEO4J_TARBALL}" >/tmp/cs \  
&& sha256sum -c /tmp/cs \  
&& rm /tmp/cs \  
&& tar --extract --file ${NEO4J_TARBALL} --directory /var/lib \  
&& mv /var/lib/neo4j-* /var/lib/neo4j \  
&& rm ${NEO4J_TARBALL}  
  
WORKDIR /var/lib/neo4j  
  
RUN mv data /data \  
&& ln -s /data /var/lib/neo4j/  
  
VOLUME /data  
  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
COPY neo4j-http-logging.xml /neo4j-http-logging.xml  
  
EXPOSE 7474 7473  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["neo4j"]  

