FROM dockerfile/java:oracle-java8  
  
RUN wget -qO - http://packages.confluent.io/deb/1.0/archive.key | sudo apt-key
add - && \  
add-apt-repository "deb [arch=all] http://packages.confluent.io/deb/1.0 stable
main" && \  
apt-get update && \  
apt-get install -y confluent-schema-registry  
  
EXPOSE 8081  
ADD schema-registry.properties /etc/schema-registry/schema-registry.properties  
  
CMD ["/usr/bin/schema-registry-start", "/etc/schema-registry/schema-
registry.properties"]

