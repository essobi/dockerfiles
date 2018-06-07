FROM openjdk:8-jdk-alpine  
  
ENV DB_URL=dbhost \  
DB_USER=lavagna \  
DB_PASS=lavagna  
  
RUN set -x && \  
apk \--no-cache add ca-certificates && \  
update-ca-certificates && \  
apk \--no-cache add bash git maven openssl && \  
\  
mkdir -p /opt/lavagna && cd /opt/lavagna && \  
git clone --depth 1 -b lavagna-1.1-M5
https://github.com/digitalfondue/lavagna.git src && \  
cd src && \  
mvn clean install -Dmaven.test.skip=true && \  
mv target/lavagna-jetty-console.war ../ && \  
\  
apk del git maven openssl && \  
cd /opt/lavagna && rm -rf src && \  
rm -rf /root/.m2  
  
EXPOSE 8080  
  
CMD java -Xms64m -Xmx128m -Ddatasource.dialect=MYSQL \  
-Ddatasource.url=jdbc:mysql://${DB_URL}/lavagna?useSSL=false\&useUnicode=true\&characterEncoding=UTF-8 \  
-Ddatasource.username=${DB_USER} \  
-Ddatasource.password=${DB_PASS} \  
-Dspring.profiles.active=prod \  
-jar /opt/lavagna/lavagna-jetty-console.war --contextPath /lavagna --headless  

