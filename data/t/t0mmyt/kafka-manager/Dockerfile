FROM openjdk:8  
LABEL maintainer Tom Taylor <tom+dockerfiles@tomm.yt>  
  
ENV VERSION=1.3.3.14  
ENV ZK_HOSTS="127.0.0.1:2181"  
RUN curl -sLo km.tar.gz https://github.com/yahoo/kafka-
manager/archive/${VERSION}.tar.gz && \  
tar xf km.tar.gz && cd /kafka-manager-${VERSION} && \  
./sbt clean dist && \  
mv target/universal/kafka-manager-${VERSION}.zip / && cd / && \  
rm -rf /kafka-manager-${VERSION} /km.tar.gz /root/.sbt /root/.ivy2 && \  
unzip kafka-manager-${VERSION}.zip && ln -s /kafka-manager-${VERSION} /kafka-
manager && \  
rm /kafka-manager-${VERSION}.zip  
  
WORKDIR /kafka  
  
ENTRYPOINT [ "/kafka-manager/bin/kafka-manager" ]  

