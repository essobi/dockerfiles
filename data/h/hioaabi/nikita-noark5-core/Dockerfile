FROM maven:3-jdk-8  
VOLUME /tmp  
  
ENV REPO "https://github.com/HiOA-ABI/nikita-noark5-core"  
ENV SRC_DIR "/srv/nikita-noark5-core"  
ENV BRANCH "master"  
# Get the source  
RUN git clone $REPO $SRC_DIR  
RUN git -C $SRC_DIR checkout $BRANCH  
  
# Build the application  
RUN mvn -f $SRC_DIR/pom.xml -Dmaven.test.skip=true clean install  
RUN mvn -f $SRC_DIR/pom.xml -Dmaven.test.skip=true package spring-
boot:repackage  
RUN cp $SRC_DIR/core-webapp/target/core-webapp-0.1.0-spring-boot.jar app.jar  
  
# Make the jar available  
RUN bash -c 'touch /app.jar'  
ENTRYPOINT ["java","-jar","/app.jar"]  
EXPOSE 8092 8082  

