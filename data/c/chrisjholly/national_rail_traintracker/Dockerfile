FROM frolvlad/alpine-oraclejdk8:slim  
  
  
ENTRYPOINT ["/usr/bin/java", "-Xmx768m", "-XX:MaxMetaspaceSize=128m", "-jar",
"/usr/share/app/app.jar"]  
  
ARG JAR_FILE  
ADD target/${JAR_FILE} /usr/share/app/app.jar

