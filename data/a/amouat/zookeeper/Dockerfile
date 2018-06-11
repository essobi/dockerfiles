FROM java:8-jre  
  
RUN groupadd -r zookeeper && useradd -r -g zookeeper zookeeper  
RUN apt-get install -y ca-certificates curl  
  
ENV ZOOKEEPER_VERSION 3.4.8  
ENV ZOOKEEPER_URL
http://apache.mirrors.pair.com/zookeeper/zookeeper-$ZOOKEEPER_VERSION/zookeeper-$ZOOKEEPER_VERSION.tar.gz  
ENV ZOOKEEPER_KEY_URL
https://www.apache.org/dist/zookeeper/zookeeper-$ZOOKEEPER_VERSION/zookeeper-$ZOOKEEPER_VERSION.tar.gz.asc  
  
#Ideally we would not be downloading keys. But at least it's https :(  
RUN curl -SL https://www.apache.org/dist/zookeeper/KEYS -o KEYS && gpg
--import KEYS  
  
RUN curl -SL "$ZOOKEEPER_URL" -o zook.tar.gz \  
&& curl -SL "$ZOOKEEPER_KEY_URL" -o zook.tar.gz.asc \  
&& gpg --verify zook.tar.gz.asc \  
&& tar -xvf zook.tar.gz \  
&& mv /zookeeper-$ZOOKEEPER_VERSION /zookeeper \  
&& cp /zookeeper/conf/zoo_sample.cfg /zookeeper/conf/zoo.cfg  
  
WORKDIR /zookeeper  
  
ENTRYPOINT ["/zookeeper/bin/zkServer.sh"]  
CMD ["start-foreground"]  
  
EXPOSE 2181 2888 3888  

