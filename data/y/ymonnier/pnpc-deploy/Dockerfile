FROM payara/server-full:173  
  
#Allows autodeploy  
RUN chown payara:payara /opt/payara41/glassfish/domains/domain1/autodeploy  
  
#installs postgresql jdbc driver  
#and adds a jdbc connection pool and ressource  
RUN wget https://jdbc.postgresql.org/download/postgresql-9.4.1212.jar \  
-O /opt/payara41/glassfish/domains/domain1/lib/postgresql.jar && \  
/opt/payara41/bin/asadmin start-domain && \  
/opt/payara41/bin/asadmin \--user admin \  
\--passwordfile=/opt/pwdfile \  
set-hazelcast-configuration \--enabled=true \--dynamic=true && \  
/opt/payara41/bin/asadmin \--user admin \  
\--passwordfile=/opt/pwdfile \  
create-jdbc-connection-pool \  
\--datasourceclassname org.postgresql.ds.PGConnectionPoolDataSource  \  
\--restype javax.sql.ConnectionPoolDataSource \  
\--property
portNumber=5432:password=pnpc_password:user=pnpc_app:serverName=db:databaseName=pnpc_app
\  
postgres-pool && \  
/opt/payara41/bin/asadmin \--user admin \  
\--passwordfile=/opt/pwdfile \  
create-jdbc-resource \--connectionpoolid postgres-pool jdbc/postgres-pool && \  
/opt/payara41/bin/asadmin stop-domain && \  
wget
https://bintray.com/ymonnier/pnpc/download_file?file_path=fr%2Fpnpc%2Fproject%2Fserver%2FPNPC-
Server%2F1.0.0-frozen-22%2FPNPC-Server-1.0.0-frozen-22.war -O
/opt/payara41/glassfish/domains/domain1/autodeploy/PNPC.war  

