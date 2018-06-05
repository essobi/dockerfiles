FROM coco/dropwizardbase:0.7.x-mvn333  
ADD .git/ /.git/  
ADD . /content-rw-aurora/  
RUN apk --update add git \  
&& cd content-rw-aurora \  
&& HASH=$(git log -1 --pretty=format:%H) \  
&& mvn clean install -Dbuild.git.revision=$HASH
-Djava.net.preferIPv4Stack=true \  
&& rm target/content-rw-aurora-*-sources.jar \  
&& mv target/content-rw-aurora-*.jar /content-rw-aurora.jar \  
&& mv config.yml /config.yml \  
&& apk del git \  
&& rm -rf /var/cache/apk/* \  
&& rm -rf /root/.m2/*  
  
EXPOSE 8080 8081  
CMD exec java $JAVA_OPTS \  
-Ddw.server.applicationConnectors[0].port=8080 \  
-Ddw.server.adminConnectors[0].port=8081 \  
-Ddw.db.url=$JDBC_URL \   
-Ddw.db.username=$JDBC_USERNAME \  
-Ddw.db.password=$JDBC_PASSWORD \  
-jar content-rw-aurora.jar server config.yml  

