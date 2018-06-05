FROM neo4j:enterprise  
  
RUN apk update && apk add openssh  
  
# Location of config files (separate in v2)  
ENV NEOCONF="/var/lib/neo4j/conf/neo4j.conf"  
ENV NEOSERCONF=${NEOCONF}  
# Read_only setting:  
ENV NEO4J_dbms_read__only=false  
# Default is open access (read_only) change bellow to require below
user/password:  
ENV NEO4J_dbms_security_auth__enabled=false  
ENV NEO4J_AUTH=neo4j/password  
# Enable upgrading of DB:  
ENV NEO4J_ALLOW_STORE_UPGRADE=true  
ENV NEO4J_dbms_allow__upgrade=true  
# Max memory size (typically half the default):  
ENV NEO4J_dbms_memory_heap_maxSize=10G  
ENV NEO4J_dbms_logs_query_enabled=true  
ENV NEO4J_dbms_logs_query_allocation__logging__enabled=true  
ENV NEO4J_dbms_logs_query_time__logging__enabled=true  
# Log all queries that take longer then (seconds):  
ENV NEO4J_dbms_logs_query_threshold=0  
# Accept Neo4j license:  
ENV NEO4J_ACCEPT_LICENSE_AGREEMENT=yes  
# Set import directory:  
ENV NEO4J_dbms_directories_import=/import  

