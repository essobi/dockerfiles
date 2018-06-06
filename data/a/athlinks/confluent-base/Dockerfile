FROM athlinks/java-oracle:8  
RUN apk add --update unzip git jq gettext && \  
rm -rf /tmp/* /var/cache/apk/*  
  
ENV CONFLUENT_VERSION="2.0.1" \  
CONFLUENT_SUBVERSION="2.11.7" \  
MYSQL_CONNECTOR_VERSION="5.1.38"  
RUN cd /opt && \  
mirror="http://packages.confluent.io/archive/2.0/" && \  
url="${mirror}confluent-$CONFLUENT_VERSION-$CONFLUENT_SUBVERSION.tar.gz" && \  
curl "http://cdn.mysql.com/Downloads/Connector-J/mysql-connector-
java-$MYSQL_CONNECTOR_VERSION.tar.gz" | tar xzf - && \  
curl "$url" | tar xzf - && \  
mv /opt/confluent-$CONFLUENT_VERSION /opt/confluent && \  
mv ./mysql-connector-java-$MYSQL_CONNECTOR_VERSION/*.jar
./confluent/share/java/kafka-connect-jdbc/  
  
RUN ls /opt  
  
ENV PATH="/opt/confluent/bin:$PATH"  
ENV CONFLUENT_HOME="/opt/confluent"  
WORKDIR "/opt/confluent"  
  
ADD bin/* /usr/local/bin/  

