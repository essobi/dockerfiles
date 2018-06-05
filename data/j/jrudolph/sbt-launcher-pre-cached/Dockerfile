FROM jrudolph/sbt-launcher:0.13.6  
MAINTAINER jrudolph  
  
RUN mkdir -p /tmp/test-project/project && echo -n "sbt.version=0.13.6" >
/tmp/test-project/project/build.properties  
  
WORKDIR /tmp/test-project  
  
RUN sbt  
  
CMD ["sbt"]  

