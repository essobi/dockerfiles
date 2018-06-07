FROM bde2020/hadoop-base:2.0.0-hadoop2.7.4-java8 as hadoop-base  
FROM bde2020/hbase-base:1.0.0-hbase1.2.6 as hbase-base  
  
FROM tomcat:9-jre8  
MAINTAINER Ivan Ermilov <ivan.s.ermilov@gmail.com>  
  
ENV HADOOP_VERSION=2.7.4  
COPY --from=hadoop-base /opt/hadoop-$HADOOP_VERSION
/opt/hadoop-$HADOOP_VERSION  
RUN ln -s /opt/hadoop-$HADOOP_VERSION/etc/hadoop /etc/hadoop  
ENV PATH /opt/hadoop-$HADOOP_VERSION/bin:$PATH  
  
ENV HBASE_VERSION=1.2.6  
COPY --from=hbase-base /opt/hbase-$HBASE_VERSION /opt/hbase-$HBASE_VERSION  
RUN ln -s /opt/hbase-$HBASE_VERSION/conf /etc/hbase  
ENV PATH /opt/hbase-$HBASE_VERSION/bin:$PATH  
  
ENV HALYARD_VERSION 1.2  
ENV HALYARD_URL
https://github.com/Merck/Halyard/releases/download/r$HALYARD_VERSION/halyard-
webapps-$HALYARD_VERSION.zip  
RUN set -x \  
&& curl -fSL "$HALYARD_URL" -o /tmp/halyard-webapps.zip \  
&& mkdir /opt/halyard-webapps-$HALYARD_VERSION \  
&& unzip /tmp/halyard-webapps.zip -d /opt/halyard-$HALYARD_VERSION/ \  
&& rm /tmp/halyard-webapps.zip*  
  
ENV HALYARD_PREFIX=/opt/halyard-$HALYARD_VERSION  
  
RUN cp $HALYARD_PREFIX/*.war $CATALINA_HOME/webapps  
RUN echo "export CLASSPATH=\"$CATALINA_HOME/lib/*:\"`hadoop classpath`:`hbase
classpath`" > /usr/local/tomcat/bin/setenv.sh  
  
RUN ln -s /opt/hbase-1.2.6/lib/jaxb-api-2.2.2.jar /opt/hbase-1.2.6/lib/jaxb-
api.jar  
RUN ln -s /opt/hbase-1.2.6/lib/jaxb-impl-2.2.3-1.jar
/opt/hbase-1.2.6/lib/jaxb1-impl.jar  
RUN ln -s /opt/hbase-1.2.6/lib/activation-1.1.jar
/opt/hbase-1.2.6/lib/activation.jar  
RUN wget
http://bits.netbeans.org/maven2/org/netbeans/external/jsr173_1.0_api/RELEASE731/jsr173_1.0_api-
RELEASE731.jar -O /opt/hbase-1.2.6/lib/jsr173_1.0_api.jar  
  
RUN ln -s /opt/hbase-1.2.6/lib/jaxb-api-2.2.2.jar
/opt/hadoop-2.7.4/share/hadoop/yarn/lib/jaxb-api.jar  
RUN ln -s /opt/hbase-1.2.6/lib/jaxb-impl-2.2.3-1.jar
/opt/hadoop-2.7.4/share/hadoop/yarn/lib/jaxb1-impl.jar  
RUN ln -s /opt/hbase-1.2.6/lib/activation-1.1.jar
/opt/hadoop-2.7.4/share/hadoop/yarn/lib/activation.jar  
RUN ln -s /opt/hbase-1.2.6/lib/jsr173_1.0_api.jar
/opt/hadoop-2.7.4/share/hadoop/yarn/lib/jsr173_1.0_api.jar  
  
RUN ln -s /opt/hbase-1.2.6/lib/jaxb-api-2.2.2.jar
/opt/hadoop-2.7.4/share/hadoop/common/lib/jaxb-api.jar  
RUN ln -s /opt/hbase-1.2.6/lib/jaxb-impl-2.2.3-1.jar
/opt/hadoop-2.7.4/share/hadoop/common/lib/jaxb1-impl.jar  
RUN ln -s /opt/hbase-1.2.6/lib/activation-1.1.jar
/opt/hadoop-2.7.4/share/hadoop/common/lib/activation.jar  
RUN ln -s /opt/hbase-1.2.6/lib/jsr173_1.0_api.jar
/opt/hadoop-2.7.4/share/hadoop/common/lib/jsr173_1.0_api.jar  
  
COPY --from=hbase-base /usr/lib/jvm/java-8-openjdk-amd64/
/usr/lib/jvm/java-8-openjdk-amd64/  
ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64  
ENV JRE_HOME=/usr/lib/jvm/java-8-openjdk-amd64  
  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-
install-recommends net-tools curl netcat  
  
ENV PATH=$PATH:$JAVA_HOME/bin  
  
ADD entrypoint.sh /entrypoint.sh  
RUN chmod a+x /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["catalina.sh", "run"]  

