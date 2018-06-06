from java:openjdk-9  
# Download compilation requisites  
RUN apt-get update && \  
apt-get -y install maven && \  
ln -s $JAVA_HOME/lib $JAVA_HOME/conf && \  
rm -rf /var/lib/apt/lists/*  
  
# Add source code  
ADD . /usr/src/jmx_exporter  
  
# Compile and the cleanup  
RUN mkdir -p /usr/share/jmx_exporter && \  
cd /usr/src/jmx_exporter && \  
mvn package && \  
cp jmx_prometheus_httpserver/target/jmx_prometheus_httpserver-*-jar-with-
dependencies.jar /usr/share/jmx_exporter.jar && \  
cd / && \  
rm -rf /root/.m2 && rm -rf /usr/src/jmx_exporter  
  
EXPOSE 5556  
USER nobody  
  
ENTRYPOINT [ "java" ]  
  
CMD [ "-jar", "/usr/share/jmx_exporter.jar", "5556",
"/etc/jmx_exporter/config.yml" ]  
  

