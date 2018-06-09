FROM tamboraorg/crejava  
#FROM openjdk:8-jre-alpine  
# https://github.com/docker-library/docs/tree/master/neo4j  
# https://github.com/neo4j/docker-
neo4j-publish/blob/master/3.3.3/enterprise/Dockerfile  
  
RUN apt-get update && \  
apt-get install -y bash  
  
ENV
NEO4J_SHA256=6901832c63bb3d9af150a1c3da3a88a4d15ad4b4a130611df138648d4c25f1a8
\  
NEO4J_TARBALL=neo4j-enterprise-3.3.3-unix.tar.gz \  
NEO4J_EDITION=enterprise  
ARG NEO4J_URI=http://dist.neo4j.org/neo4j-enterprise-3.3.3-unix.tar.gz  
  
COPY ./local-package/* /tmp/  
  
RUN curl --fail --silent --show-error --location --remote-name ${NEO4J_URI} \  
&& echo "${NEO4J_SHA256} ${NEO4J_TARBALL}" | sha256sum --status --check --warn
- \  
&& tar --extract --file ${NEO4J_TARBALL} --directory /var/lib \  
&& mv /var/lib/neo4j-* /var/lib/neo4j \  
&& rm ${NEO4J_TARBALL} \  
&& mv /var/lib/neo4j/data /data \  
&& ln -s /data /var/lib/neo4j/data  
  
  
ENV PATH /var/lib/neo4j/bin:$PATH  
  
WORKDIR /var/lib/neo4j  
  
VOLUME /data  
  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
  
EXPOSE 7474 7473 7687  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["neo4j"]  

