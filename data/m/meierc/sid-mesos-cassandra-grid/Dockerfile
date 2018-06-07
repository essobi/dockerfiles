FROM webratio/groovy:latest  
MAINTAINER Christoph Meier  
  
RUN grape install com.google.guava guava 19.0 && \  
grape install ch.qos.logback logback-classic 1.1.5 && \  
grape install org.eclipse.jetty.aggregate jetty-all 7.6.19.v20160209 && \  
grape install com.datastax.cassandra cassandra-driver-core 3.0.0  
  
ADD grid.groovy /source/  
  
ENTRYPOINT ["groovy", "-Dgrape.root=/graperoot", "grid.groovy"]  

