FROM coco/dropwizardbase:0.7.x-mvn333  
  
COPY . /document-store-api  
  
RUN apk \--update add git libstdc++ wget \  
&& cd /tmp \  
&& wget -q https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/2.21-r2/glibc-2.21-r2.apk \  
&& wget -q https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/2.21-r2/glibc-bin-2.21-r2.apk \  
&& apk add \--allow-untrusted glibc-2.21-r2.apk glibc-bin-2.21-r2.apk \  
&& /usr/glibc/usr/bin/ldconfig /lib /usr/glibc/usr/lib \  
&& cd /document-store-api \  
&& HASH=$(git log -1 \--pretty=format:%H) \  
&& TAG=$(git tag -l --points-at $HASH) \  
&& VERSION=${TAG:-untagged} \  
&& mvn clean versions:set -DnewVersion=$VERSION \  
&& mvn clean package -Dbuild.git.revision=$HASH
-Djava.net.preferIPv4Stack=true \  
&& rm target/document-store-api-*-sources.jar \  
&& mv target/document-store-api-*.jar /document-store-api.jar \  
&& mv config.yaml /config.yaml \  
&& mv data-migration-scripts* /data-migration-scripts \  
&& mv scripts* /scripts \  
&& apk del go git \  
&& rm -rf /var/cache/apk/* /document-store-api/target* /root/.m2/* /tmp/*.apk  
  
EXPOSE 8080 8081  
  
CMD exec java $JAVA_OPTS \  
-Ddw.server.applicationConnectors[0].port=8080 \  
-Ddw.server.adminConnectors[0].port=8081 \  
-Ddw.mongo.addresses=$MONGO_ADDRESSES \  
-Ddw.cacheTtl=$CACHE_TTL \  
-Ddw.apiHost=$API_HOST \  
-Ddw.logging.appenders[0].logFormat="%-5p [%d{ISO8601, GMT}] %c: %X{transaction_id} %replace(%m%n[%thread]%xEx){'\n', '|'}%nopex%n" \  
-jar document-store-api.jar server config.yaml  

