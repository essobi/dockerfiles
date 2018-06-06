FROM coco/dropwizardbase:0.7.x-mvn333  
  
COPY . /methode-image-model-mapper  
  
RUN apk --update add git \  
&& cd methode-image-model-mapper \  
&& HASH=$(git log -1 --pretty=format:%H) \  
&& TAG=$(git tag -l --points-at $HASH) \  
&& VERSION=${TAG:-untagged} \  
&& mvn versions:set -DnewVersion=$VERSION \  
&& mvn install -Dbuild.git.revision=$HASH -Djava.net.preferIPv4Stack=true \  
&& rm -f target/methode-image-model-mapper-*sources.jar \  
&& mv target/methode-image-model-mapper-*.jar /methode-image-model-mapper.jar
\  
&& mv methode-image-model-mapper.yaml /config.yaml \  
&& apk del git \  
&& rm -rf /var/cache/apk/* \  
&& rm -rf /root/.m2/*  
  
EXPOSE 8080 8081  
CMD exec java $JAVA_OPTS \  
-Ddw.server.applicationConnectors[0].port=8080 \  
-Ddw.server.adminConnectors[0].port=8081 \  
-Ddw.consumer.messageConsumer.queueProxyHost=http://$KAFKA_PROXY \  
-Ddw.producer.messageProducer.proxyHostAndPort=$KAFKA_PROXY \  
-Ddw.externalBinaryUrlBasePath=$S3_URL \  
-Ddw.logging.appenders[0].logFormat="%-5p [%d{ISO8601, GMT}] %c: %X{transaction_id} %replace(%m%n[%thread]%xEx){'\n', '|'}%nopex%n" \  
-jar methode-image-model-mapper.jar server config.yaml  

