FROM java:8  
WORKDIR /opt/hsqldb  
  
EXPOSE 9001  
ENV HSQLDB_VERSION 2.3.4  
RUN wget
http://sourceforge.net/projects/hsqldb/files/hsqldb/hsqldb_2_3/hsqldb-$HSQLDB_VERSION.zip
&& unzip hsqldb-$HSQLDB_VERSION.zip && rm hsqldb-$HSQLDB_VERSION.zip  
ENTRYPOINT java -cp hsqldb-${HSQLDB_VERSION}/hsqldb/lib/sqltool.jar
org.hsqldb.Server -database.0 file:thedatabase -dbname.0 xdb  

