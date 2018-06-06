FROM coco/dropwizardbase:0.7.x-mvn333  
ADD .git/ /.git/  
ADD api-policy-component-service/ /api-policy-component-service/  
RUN apk --update add git \  
&& cd api-policy-component-service \  
&& HASH=$(git log -1 --pretty=format:%H) \  
&& TAG=$(git tag -l --points-at $HASH) \  
&& VERSION=${TAG:-untagged} \  
&& sed -i "s/<parent>//; s/<\/parent>//; s/<artifactId>api-policy-
component<\/artifactId>//" ./pom.xml \  
&& mvn versions:set -DnewVersion=$VERSION \  
&& mvn clean install -Dbuild.git.revision=$HASH
-Djava.net.preferIPv4Stack=true \  
&& rm target/api-policy-component-service-*-sources.jar \  
&& mv target/api-policy-component-service-*.jar /api-policy-component-
service.jar \  
&& mv config-local.yml /config.yml \  
&& apk del git \  
&& rm -rf /var/cache/apk/* \  
&& rm -rf /root/.m2/*  
  
EXPOSE 8080 8081  
  
CMD exec java $JAVA_OPTS \  
-Ddw.server.applicationConnectors[0].port=8080 \  
-Ddw.server.adminConnectors[0].port=8081 \  
-Dsun.net.http.allowRestrictedHeaders=true \  
-Ddw.varnish.primaryNodes=$READ_ENDPOINT \   
-Ddw.varnish.timeout=$JERSEY_TIMEOUT_DURATION \  
-Ddw.checkingVulcanHealth=$CHECKING_VULCAN_HEALTH \  
-Ddw.logging.appenders[0].logFormat="%-5p [%d{ISO8601, GMT}] %c: %X{transaction_id} %replace(%m%n[%thread]%xEx){'\n', '|'}%nopex%n" \  
-Ddw.metrics.reporters[0].host=$GRAPHITE_HOST \  
-Ddw.metrics.reporters[0].port=$GRAPHITE_PORT \  
-Ddw.metrics.reporters[0].prefix=$GRAPHITE_PREFIX \  
-jar api-policy-component-service.jar server config.yml  

