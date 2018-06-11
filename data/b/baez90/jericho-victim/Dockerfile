FROM gradle:4.3.1-jdk-alpine as build  
WORKDIR jericho  
ADD . ./  
USER root  
RUN chown -R gradle:gradle /home/gradle/jericho && \  
gradle --no-daemon -Pkotlin.incremental=false
-Dkotlin.compiler.execution.strategy=in-proces distTar  
  
FROM java:openjdk-8-jre-alpine  
EXPOSE 8080  
COPY \--from=build /home/gradle/jericho/build/distributions/*.tar
/tmp/JerichoICNDB.tar  
WORKDIR /usr/src/JerichoICNDB  
RUN tar -xf /tmp/JerichoICNDB.tar -C ./ && \  
mv JerichoICNDB-1.0-SNAPSHOT/* ./ && \  
rmdir JerichoICNDB-1.0-SNAPSHOT  
ENTRYPOINT ["bin/JerichoICNDB", "run",
"de.fhro.inf.sa.jerichoDemo.MainApiVerticle"]

