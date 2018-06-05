FROM caarlos0/alpine-oraclejdk7-mvn:latest  
  
ENV LANG C.UTF-8  
ENV JAVA_TOOL_OPTIONS -Dfile.encoding=UTF8  
  
ADD https://github.com/OSBI/saiku/archive/saiku-3.5.zip saiku-server.zip  
RUN unzip saiku-server.zip \  
&& mv saiku-saiku-3.5 saiku-build \  
&& rm saiku-server.zip  
  
WORKDIR /saiku-build  
RUN sed -i 's/failonerror="true"/failonerror="false"/g' saiku-ui/pom.xml  
RUN mvn clean -pl '!saiku-bi-platform-plugin-p5' install
-Dmaven.test.skip=true  
RUN cp saiku-ui/target/saiku-ui/saiku.min.js \  
saiku-server/target/dist/saiku-server/tomcat/webapps/ROOT/  
  
WORKDIR /saiku-build/saiku-server/target/dist/  
ADD start-saiku.sh saiku-server/start-saiku.sh  
ADD http://central.maven.org/maven2/org/apache/commons/commons-
math/2.2/commons-math-2.2.jar \  
./saiku-server/tomcat/webapps/saiku/WEB-INF/lib/commons-math-2.2.jar  
  
WORKDIR /  
RUN mv /saiku-build/saiku-server/target/dist/saiku-server /saiku \  
&& chmod +x /saiku/*.sh \  
&& chmod +x /saiku/tomcat/bin/*.sh \  
&& rm -fR saiku-build  
  
EXPOSE 8080  
VOLUME ["/saiku/data", "/saiku/repository/data"]  
ENTRYPOINT /saiku/start-saiku.sh  

