FROM cassandra:3.11  
RUN mv "${CASSANDRA_CONFIG}/cassandra.yaml"
"${CASSANDRA_CONFIG}/cassandra.yaml.template" && \  
rm -f "${CASSANDRA_CONFIG}/cassandra-topology.properties" && \  
rm -f "${CASSANDRA_CONFIG}/cassandra-rackdc.properties"  
  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["cassandra", "-f"]  

