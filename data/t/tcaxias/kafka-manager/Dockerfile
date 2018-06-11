FROM alpine  
  
WORKDIR /app  
  
ENV \  
DEPS="wget openjdk8" \  
PKGS="bash openjdk8-jre-base" \  
ZK_HOSTS="zk.zookeeper:2181" \  
APK="apk --update --no-cache" \  
VERSION="1.3.3.13"  
RUN \  
$APK add $DEPS $PKGS && \  
wget --quiet -O- \  
https://github.com/yahoo/kafka-manager/archive/${VERSION}.tar.gz | \  
tar -zx && \  
cd kafka-manager-${VERSION} && \  
./sbt clean dist && \  
rm -rf /root/.??* && \  
mv target/universal/kafka-manager-${VERSION}.zip /app && \  
cd .. && \  
rm -rf kafka-manager-${VERSION} && \  
unzip kafka-manager-${VERSION}.zip && \  
rm -f kafka-manager-${VERSION}.zip && \  
mv kafka-manager-${VERSION} kafka-manager && \  
apk del $DEPS  
  
EXPOSE "9000"  
CMD ["/app/kafka-manager/bin/kafka-manager"]  

