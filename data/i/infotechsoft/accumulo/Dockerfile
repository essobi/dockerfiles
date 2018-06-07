FROM uhopper/hadoop:2.8.1  
  
RUN gpg --keyserver pgpkeys.mit.edu --recv-keys \  
2BFF0BA7 \  
352ACF76 \  
ABBA8A49 \  
00B6899D \  
EF362B9E \  
4677D66C \  
5969A43B \  
7DB33653 \  
AB471AE9 \  
B8C3D406 \  
68E327C1 \  
6E1CC7A4 \  
8EE2F25C \  
D2C80E32 \  
820F225C \  
92BC2F2B \  
ADAFD097 \  
B5E9BD2D  
  
ENV ACCUMULO_VERSION 1.8.1  
ENV ACCUMULO_URL
https://www.apache.org/dist/accumulo/$ACCUMULO_VERSION/accumulo-$ACCUMULO_VERSION-
bin.tar.gz  
  
RUN set -x \  
&& curl -fSL "$ACCUMULO_URL" -o /tmp/accumulo.tar.gz \  
&& curl -fSL "$ACCUMULO_URL.asc" -o /tmp/accumulo.tar.gz.asc \  
&& gpg \--verify /tmp/accumulo.tar.gz.asc /tmp/accumulo.tar.gz \  
&& tar -xvf /tmp/accumulo.tar.gz -C /opt/ \  
&& rm /tmp/accumulo.tar.gz* \  
&& ln -s /opt/accumulo-$ACCUMULO_VERSION /opt/accumulo  
  
ENV ZOOKEEPER_VERSION 3.4.10  
ENV ZOOKEEPER_URL
http://apache.org/dist/zookeeper/zookeeper-$ZOOKEEPER_VERSION/zookeeper-$ZOOKEEPER_VERSION.tar.gz  
  
RUN set -x \  
&& curl -fSL "$ZOOKEEPER_URL" -o /tmp/zookeeper.tar.gz \  
&& curl -fSL "$ZOOKEEPER_URL.asc" -o /tmp/zookeeper.tar.gz.asc \  
&& gpg \--verify /tmp/zookeeper.tar.gz.asc /tmp/zookeeper.tar.gz \  
&& tar -xvf /tmp/zookeeper.tar.gz -C /opt/ \  
&& rm /tmp/zookeeper.tar.gz*  
  
ADD accumulo-entrypoint.sh /accumulo-entrypoint.sh  
RUN chmod a+x /accumulo-entrypoint.sh  
  
ENV ACCUMULO_HOME /opt/accumulo-$ACCUMULO_VERSION  
ENV ZOOKEEPER_HOME /opt/zookeeper-$ZOOKEEPER_VERSION  
  
ENTRYPOINT ["/accumulo-entrypoint.sh"]  

