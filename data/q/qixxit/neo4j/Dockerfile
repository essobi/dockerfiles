FROM neo4j:3.2.1  
MAINTAINER Leif Gensert <leif@leif.io>  
  
RUN apk add --no-cache ca-certificates openssl  
  
RUN cd /var/lib/neo4j/plugins \  
&& wget https://github.com/neo4j-contrib/neo4j-apoc-
procedures/releases/download/3.2.0.3/apoc-3.2.0.3-all.jar \  
&& wget
https://github.com/neo4j-contrib/spatial/releases/download/0.24-neo4j-3.1.1/neo4j-spatial-0.24-neo4j-3.1.1-server-
plugin.jar  
  
ENV NEO4J_dbms_security_procedures_unrestricted=apoc.\\\\\\*  
ENV NEO4J_apoc_import_file_enabled true  
ENV NEO4J_apoc_export_file_enabled true  

