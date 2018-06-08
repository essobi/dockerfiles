FROM java:8  
# create hsql user  
RUN groupadd -r hsqldb && useradd -m -g hsqldb hsqldb  
USER hsqldb  
WORKDIR /home/hsqldb  
  
# copy hsql distribution  
RUN mkdir lib db  
RUN wget -O lib/hsqldb.jar
http://central.maven.org/maven2/org/hsqldb/hsqldb/2.3.2/hsqldb-2.3.2.jar  
RUN wget -O lib/sqltool.jar
http://central.maven.org/maven2/org/hsqldb/sqltool/2.3.2/sqltool-2.3.2.jar  
COPY hsqldb.sh server.properties sqltool.rc ./  
  
# entry point is bash script; this allows us to do normal shutdown (SIGINT
does an abrupt shutdown)  
VOLUME db  
EXPOSE 9001  
ENTRYPOINT ["./hsqldb.sh"]  
  

