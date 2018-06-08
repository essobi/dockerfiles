FROM virtualflybrain/docker-vfb-neo4j:2.3-enterprise  
  
MAINTAINER Robert Court "rcourt@ed.ac.uk"  
VOLUME /data  
VOLUME /backup  
  
RUN sed -i 's|=data\/graph\\.db|=\/data\/neo4j|' ${NEOSERCONF} && \  
sed -i 's|#dbms.directories.data=data|dbms.directories.data=\/data\/neo4j|'
${NEOSERCONF} && \  
sed -i 's|#dbms.active_database=graph\\.db|dbms.active_database=index\\.db|'
${NEOSERCONF} && \  
chmod -R 777 /data  

