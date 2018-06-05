FROM coco/dropwizardbase:0.7.x-mvn333  
  
COPY . /  
  
RUN apk --update add git \  
&& HASH=$(git log -1 --pretty=format:%H) \  
&& mvn install -Dbuild.git.revision=$HASH -Djava.net.preferIPv4Stack=true \  
&& rm -f target/methode-article-internal-components-mapper-*sources.jar \  
&& mv target/methode-article-internal-components-mapper-*.jar /methode-
article-internal-components-mapper.jar \  
&& mv methode-article-internal-components-mapper.yaml /config.yaml \  
&& apk del git \  
&& rm -rf /var/cache/apk/* \  
&& rm -rf /root/.m2/*  
  
EXPOSE 8080 8081  
  
CMD exec java $JAVA_OPTS \  
-Ddw.server.applicationConnectors[0].port=8080 \  
-Ddw.server.adminConnectors[0].port=8081 \  
-Ddw.methodeArticleMapper.endpointConfiguration.primaryNodes=$METHODE_ARTICLE_MAPPER_URL \  
-Ddw.methodeContentPlaceholderMapper.endpointConfiguration.primaryNodes=$METHODE_CPH_MAPPER_URL \  
-Ddw.documentStoreApi.endpointConfiguration.primaryNodes=$DOC_STORE_API_URL \  
-Ddw.concordanceApi.endpointConfiguration.primaryNodes=$CONCORDANCE_API_URL \  
-Ddw.consumer.messageConsumer.queueProxyHost=http://$KAFKA_PROXY_URL \  
-Ddw.producer.messageProducer.proxyHostAndPort=$KAFKA_PROXY_URL \  
-Ddw.apiHost=$API_HOST \  
-Ddw.logging.appenders[0].logFormat="%-5p [%d{ISO8601, GMT}] %c: %X{transaction_id} %replace(%m%n[%thread]%xEx){'\n', '|'}%nopex%n" \  
-jar methode-article-internal-components-mapper.jar server config.yaml  

