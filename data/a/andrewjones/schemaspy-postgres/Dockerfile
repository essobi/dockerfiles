FROM java:8-jre  
  
ENV VERSION 6.0.0-rc1  
  
RUN apt-get update && \  
apt-get install -y graphviz && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN wget
https://github.com/schemaspy/schemaspy/releases/download/v$VERSION/schemaspy-$VERSION.jar
-O schemaSpy.jar  
RUN wget https://jdbc.postgresql.org/download/postgresql-9.4.1212.jre6.jar -O
postgresql-jre6.jar  
  
VOLUME /output  
  
ENTRYPOINT [ "java", "-jar", "schemaSpy.jar", "-t", "pgsql", "-o", "/output",
"-dp", "postgresql-jre6.jar" ]  
  
CMD [ "-host", "database", "-port", "5432", "-db", "postgres", "-u",
"postgres", "-p", "postgres" ]  

