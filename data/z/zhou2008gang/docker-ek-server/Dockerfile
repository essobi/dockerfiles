FROM alpine:3.5  
ENV LANG C.UTF-8  
#ENV http_proxy http://87.254.212.121:8080/  
#ENV https_proxy http://87.254.212.121:8080/  
ENV ES_VERSION 5.2.1  
ENV KIBANA_VERSION 5.2.1  
RUN ["adduser","-D","es"]  
RUN { \  
echo '#!/bin/sh'; \  
echo 'set -e'; \  
echo; \  
echo 'dirname "$(dirname "$(readlink -f "$(which javac || which java)")")"'; \  
} > /usr/local/bin/docker-java-home \  
&& chmod +x /usr/local/bin/docker-java-home  
ENV JAVA_HOME /usr/lib/jvm/java-1.8-openjdk/jre  
ENV PATH
$PATH:/usr/lib/jvm/java-1.8-openjdk/jre/bin:/usr/lib/jvm/java-1.8-openjdk/bin  
RUN set -x \  
&& apk add --no-cache \  
openjdk8-jre \  
&& [ "$JAVA_HOME" = "$(docker-java-home)" ]  
  
RUN set -x \  
&& apk update \  
&& apk add --no-cache nodejs curl  
  
#RUN set -x \  
# && curl --proxy1.0 $http_proxy -sSL
https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-$ES_VERSION.tar.gz
> /elasticsearch-$ES_VERSION.tar.gz \  
# && tar -xzf /elasticsearch-$ES_VERSION.tar.gz \  
# && mv /elasticsearch-$ES_VERSION /elasticsearch \  
# && curl --proxy1.0 $http_proxy -sSL
https://artifacts.elastic.co/downloads/kibana/kibana-$KIBANA_VERSION-
linux-x86_64.tar.gz > /kibana-$KIBANA_VERSION.tar.gz \  
# && tar -xzf /kibana-$KIBANA_VERSION.tar.gz \  
# && mv /kibana-$KIBANA_VERSION-linux-x86_64 /kibana  
RUN set -x \  
&& curl -sSL
https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-$ES_VERSION.tar.gz
> /elasticsearch-$ES_VERSION.tar.gz \  
&& tar -xzf /elasticsearch-$ES_VERSION.tar.gz \  
&& mv /elasticsearch-$ES_VERSION /elasticsearch \  
&& curl -sSL
https://artifacts.elastic.co/downloads/kibana/kibana-$KIBANA_VERSION-
linux-x86_64.tar.gz > /kibana-$KIBANA_VERSION.tar.gz \  
&& tar -xzf /kibana-$KIBANA_VERSION.tar.gz \  
&& mv /kibana-$KIBANA_VERSION-linux-x86_64 /kibana  
  
#change configuration  
RUN set -x \  
&& sed -i 's/^#network\\.host:.*$/network.host: 0.0.0.0/'
/elasticsearch/config/elasticsearch.yml \  
&& grep -x "network.host: 0.0.0.0" /elasticsearch/config/elasticsearch.yml \  
&& sed -i 's/^#server\\.host:.*$/server.host: 0.0.0.0/'
/kibana/config/kibana.yml \  
&& grep -x "server.host: 0.0.0.0" /kibana/config/kibana.yml \  
&& sed -i 's/^#elasticsearch\\.url:.*$/elasticsearch.url:
"http:\/\/0.0.0.0:9200"/' /kibana/config/kibana.yml \  
&& grep -x "elasticsearch.url: \"http://0.0.0.0:9200\""
/kibana/config/kibana.yml \  
&& sed -i 's/^NODE=".*$/NODE="\/usr\/bin\/node"/' /kibana/bin/kibana* \  
&& grep -x "NODE=\"/usr/bin/node\"" /kibana/bin/kibana* \  
&& rm /kibana-$KIBANA_VERSION.tar.gz /elasticsearch-$ES_VERSION.tar.gz  
  
#initial startup.  
RUN { \  
echo '#!/bin/sh'; \  
echo 'sh /elasticsearch/bin/elasticsearch &'; \  
echo 'sleep 30'; \  
echo 'sh /kibana/bin/kibana'; \  
} > /startup.sh \  
&& chmod +x /startup.sh  
  
RUN ["chown","-R","es:es","/elasticsearch"]  
RUN ["chown","-R","es:es","/kibana"]  
RUN ["chown","-R","es:es","/startup.sh"]  
#USER root  
#RUN echo "vm.max_map_count=262144" >> /etc/sysctl.conf  
#RUN ["sysctl","-w","vm.max_map_count=262144"]  
USER es  
#EXPOSE 9200 9300  
CMD sh /startup.sh  

