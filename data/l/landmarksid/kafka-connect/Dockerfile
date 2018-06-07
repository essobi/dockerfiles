FROM debian:jessie  
MAINTAINER Justin Soong <justinsoong@gmail.com>  
  
ENV CP_VERSION="4.0.0" KAFKA_VERSION="1.1.0" SCALA_VERSION="2.12"
CONFLUENT_DEB_VERSION="1" ZULU_OPENJDK_VERSION="8=8.17.0.3"  
  
RUN echo "===> Installing supervisor, schema registry" \  
&& apt-get -qq update \  
&& apt-get install -y supervisor \  
&& apt-get install -y wget \  
&& apt-get install -y openssl \  
&& apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 \--recv-keys
0x219BD9C9 \  
&& echo "deb http://repos.azulsystems.com/debian stable main" >>
/etc/apt/sources.list.d/zulu.list \  
&& apt-get -qq update \  
&& apt-get -y install zulu-${ZULU_OPENJDK_VERSION} \  
&& wget
https://gitlab.com/andmarios/checkport/uploads/3903dcaeae16cd2d6156213d22f23509/checkport
-O /usr/local/bin/checkport \  
&& chmod +x /usr/local/bin/checkport \  
&& mkdir /extra-connect-jars /connectors  
  
ARG CP_URL="https://packages.confluent.io/archive/4.0/confluent-
oss-${CP_VERSION}-2.11.tar.gz"  
RUN wget "$CP_URL" -O /opt/confluent.tar.gz \  
&& mkdir -p /opt/confluent \  
&& tar --no-same-owner --strip-components 1 -xzf /opt/confluent.tar.gz -C
/opt/confluent \  
&& mkdir /opt/confluent/logs && chmod 1777 /opt/confluent/logs \  
&& rm -rf /opt/confluent.tar.gz \  
&& cp /opt/confluent/share/java/confluent-common/common-config-4.0.0.jar
/opt/confluent/share/java/kafka-connect-s3 \  
&& ln -s /opt/confluent "/opt/confluent-${CP_VERSION}"  
  
ARG
KAFKA_URL="http://home.apache.org/~damianguy/kafka-1.1.0-rc3/kafka_2.12-1.1.0.tgz"  
RUN wget "$KAFKA_URL" -O /opt/kafka.tar.gz \  
&& mkdir -p /opt/kafka \  
&& tar --no-same-owner --strip-components 1 -xzf /opt/kafka.tar.gz -C
/opt/kafka \  
&& mkdir /opt/kafka/logs && chmod 1777 /opt/kafka/logs \  
&& rm -rf /opt/kafka.tar.gz  
  
# Add dumb init and quickcert  
RUN wget https://github.com/Yelp/dumb-init/releases/download/v1.2.0/dumb-
init_1.2.0_amd64 -O /usr/local/bin/dumb-init \  
&& chmod 0755 /usr/local/bin/dumb-init  
  
# Add ElasticSearch 6 And MongoDB Connectors, which have been built and hosted
manually  
RUN wget https://www.dropbox.com/s/74yyvlgft0zveoc/mongo-
elastic6-connectors.tar.gz -O mongo-elastic6-connectors.tar.gz \  
&& mkdir -p /opt/connectors \  
&& tar -xzf mongo-elastic6-connectors.tar.gz --no-same-owner --strip-
components=1 -C /opt/connectors \  
&& rm /mongo-elastic6-connectors.tar.gz \  
&& echo "plugin.path=/opt/confluent/share/java,/opt/connectors,/extra-connect-
jars,/connectors,/ext-jars" >> /opt/confluent/etc/schema-registry/connect-
avro-distributed.properties  
  
RUN wget http://central.maven.org/maven2/org/apache/calcite/calcite-
linq4j/1.14.0/calcite-linq4j-1.14.0-javadoc.jar -O calcite-
linq4j-1.14.0-javadoc.jar \  
&& mkdir -p /ext-jars/ \  
&& mv calcite-linq4j-1.14.0-javadoc.jar /ext-jars/  
  
ADD setup_run_kafka_connect.sh /usr/local/bin  
ADD supervisord.conf /etc/  
  
RUN chmod +x /usr/local/bin/setup_run_kafka_connect.sh  
  
EXPOSE 8083  
ENTRYPOINT ["/usr/local/bin/dumb-init", "--"]  
CMD ["/usr/local/bin/setup_run_kafka_connect.sh"]  

