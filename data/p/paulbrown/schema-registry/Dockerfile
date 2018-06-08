FROM paulbrown/base:latest  
  
COPY confluent.repo /etc/yum.repos.d/confluent.repo  
  
RUN yum upgrade --quiet --assumeyes && yum clean all  
  
RUN yum install --quiet --assumeyes java-headless confluent-schema-registry &&
yum clean all  
  
EXPOSE 8081  
COPY schema-registry.properties /etc/schema-registry/schema-
registry.properties  
  
COPY onStart.sh /onStart.sh  
  
ENTRYPOINT ["/onStart.sh"]  

