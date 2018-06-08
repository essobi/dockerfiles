FROM java:8  
EXPOSE 80 443 8080  
RUN curl -sSL
http://apache.mirrors.spacedump.net/maven/maven-3/3.3.9/binaries/apache-
maven-3.3.9-bin.tar.gz | tar -xz  
COPY . /src  
RUN cd /src && \  
/apache-maven-3.3.9/bin/mvn clean package && \  
cp target/service-spy*.jar /service-spy.jar && \  
rm -rf /apache-maven-3.3.9 /src /root/.m2  
  
ENTRYPOINT ["java", "-jar", "service-spy.jar", "--proxy.servers.http.port=80",
"--proxy.servers.https.port=443", "--server.port=8080"]  

