FROM java:8  
COPY src/ /usr/socket/src/  
COPY lib/ /usr/socket/lib/  
WORKDIR /usr/socket  
RUN find src -type f -name "*.java" -print | xargs javac -classpath
src:lib/json-20141113.jar:lib/postgresql-9.4-1201.jdbc4.jar  
WORKDIR /usr/socket/src/  
CMD java -classpath
/usr/socket/src:/usr/socket/lib/json-20141113.jar:/usr/socket/lib/postgresql-9.4-1201.jdbc4.jar
heyyou/sockets/LocationSocket  
EXPOSE 8489

