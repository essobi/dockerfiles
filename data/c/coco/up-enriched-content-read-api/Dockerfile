FROM coco/dropwizardbase  
  
ADD .git/ /.git/  
ADD . /enriched-content-read-api/  
  
RUN apk --update add git \  
&& cd enriched-content-read-api \  
&& HASH=$(git log -1 \--pretty=format:%H) \  
&& mvn install -Dbuild.git.revision=$HASH -Dbuild.number=0
-Dbuild.url=http://not-available.ft.com/ -Djava.net.preferIPv4Stack=true \  
&& mv target/enriched-content-read-api.jar /enriched-content-read-api.jar \  
&& mv config-local.yml /enriched-content-read-api.yaml \  
&& apk del git \  
&& rm -rf /var/cache/apk/* \  
&& rm -rf /root/.m2/*  
  
EXPOSE 8080 8081  
  
CMD exec java $JAVA_OPTS \  
-Ddw.server.applicationConnectors[0].port=8080 \  
-Ddw.server.adminConnectors[0].port=8081 \  
-Ddw.contentApi.endpointConfiguration.primaryNodes=$VULCAN_HOST \  
-Ddw.contentApi.hostHeader=content-public-read \  
-Ddw.contentApi.pingNodes=$VULCAN_HOST \  
-Ddw.annotationsApi.endpointConfiguration.primaryNodes=$VULCAN_HOST \  
-Ddw.annotationsApi.hostHeader=public-annotations-api \  
-Ddw.cacheControlMaxAge=$CACHE_TTL \  
-Ddw.logging.appenders[0].logFormat="%-5p [%d{ISO8601, GMT}] %c: %X{transaction_id} %replace(%m%n[%thread]%xEx){'\n', '|'}%nopex%n" \  
-jar enriched-content-read-api.jar server enriched-content-read-api.yaml  

