FROM codingame/maven3-builder:1.2  
# Copy files  
COPY target/java-maven3-junit4-runner-0.0.1-SNAPSHOT-jar-with-dependencies.jar
/usr/src/codingame/junit-runner/junit-runner.jar  
COPY docker/junit-runner /usr/src/codingame/junit-runner/  
  
COPY docker/build.sh /project/build  
  
ENV CG_RUN_DIR /project/answer  
  
ENTRYPOINT ["/usr/src/codingame/junit-runner/junit-runner"]  
  

