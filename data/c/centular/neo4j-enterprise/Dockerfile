  
FROM centular/java  
  
RUN yum install - y \  
bash \  
curl  
  
ENV
NEO4J_SHA256=7d90638e65798ef057f32742fb4f8c87d4d2f13d7c06d7a4c093320bd4df3191
\  
NEO4J_TARBALL=neo4j-enterprise-3.2.1-unix.tar.gz  
ARG NEO4J_URI=http://dist.neo4j.org/neo4j-enterprise-3.2.1-unix.tar.gz  
  
RUN curl --fail --silent --show-error --location --remote-name ${NEO4J_URI} \  
&& echo "${NEO4J_SHA256} ${NEO4J_TARBALL}" | sha256sum -cw - \  
&& tar --extract --file ${NEO4J_TARBALL} \--directory /var/lib \  
&& mv /var/lib/neo4j-* /var/lib/neo4j \  
&& rm ${NEO4J_TARBALL}  
  
WORKDIR /var/lib/neo4j  
RUN mv data /data \  
&& ln -s /data  
  
VOLUME /data  
  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
  
RUN chmod +x /docker-entrypoint.sh  
  
EXPOSE 7474 7473 7687  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["neo4j"]  

