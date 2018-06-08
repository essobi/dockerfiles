FROM coco/dropwizardbase:0.7.x-mvn333  
COPY . /hackathon-all-roads-service/  
RUN apk --update add git \  
&& cd hackathon-all-roads-service \  
&& HASH=$(git log -1 --pretty=format:%H) \  
&& mvn clean install -Dbuild.git.revision=$HASH
-Djava.net.preferIPv4Stack=true \  
&& rm target/all-roads-service-*-sources.jar \  
&& mv target/all-roads-service-*.jar /all-roads-service.jar \  
&& mv config.yaml /config.yaml \  
&& apk del git \  
&& rm -rf /var/cache/apk/* \  
&& rm -rf /root/.m2/*  
  
EXPOSE 8080 8081  
CMD exec java $JAVA_OPTS \  
-Ddw.server.applicationConnectors[0].port=8080 \  
-Ddw.server.adminConnectors[0].port=8081 \  
-Ddw.suggestorHost=$SUGGESTOR_HOST \  
-jar all-roads-service.jar server config.yaml  

