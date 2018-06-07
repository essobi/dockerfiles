FROM ubuntu:latest  
  
LABEL maintainer "haobibo@gmail.com"  
  
USER root  
  
ENV APACHE_DIST="http://archive.apache.org/dist" \  
MAVEN_VERSION="3.5.3" \  
SOLR_VERSION="7.3.1" \  
SOLR_HOME="/data/solr" \  
SOLR_LIB_DIR="/data/solr/.lib" \  
SOLR_SERVER_LIB="/opt/solr/server/solr-webapp/webapp/WEB-INF/lib" \  
PATH="/opt/solr/bin:/opt/maven/bin:$PATH"  
RUN mkdir -p $SOLR_HOME $SOLR_LIB_DIR \  
&& apt-get -y update --fix-missing && apt-get -y upgrade \  
&& apt-get -qq install -y --no-install-recommends wget unzip lsof
openjdk-11-jdk-headless \  
&& apt-get autoremove && apt-get clean && rm -rf /var/lib/apt/lists/* \  
&& wget -nv "${APACHE_DIST}/maven/maven-3/${MAVEN_VERSION}/binaries/apache-
maven-${MAVEN_VERSION}-bin.zip" -O /tmp/maven.zip \  
&& wget -nv
"${APACHE_DIST}/lucene/solr/${SOLR_VERSION}/solr-${SOLR_VERSION}.zip" -O
/tmp/solr.zip \  
&& unzip -q /tmp/solr.zip -d /opt/ && mv /opt/solr-${SOLR_VERSION} /opt/solr \  
&& unzip -q /tmp/maven.zip -d /opt/ && mv /opt/apache-maven-${MAVEN_VERSION}
/opt/maven \  
&& sed -i -e '/-Dsolr.clustering.enabled=true/ a SOLR_OPTS="$SOLR_OPTS
-Denable.runtime.lib=true -Dsun.net.inetaddr.ttl=60
-Dsun.net.inetaddr.negative.ttl=60"' /opt/solr/bin/solr.in.sh \  
&& echo 'SOLR_HOME=${SOLR_HOME}' >> /opt/solr/bin/solr.in.sh \  
&& echo 'SOLR_PID_DIR=${SOLR_HOME}' >> /opt/solr/bin/solr.in.sh \  
&& echo 'SOLR_LOGS_DIR=${SOLR_HOME}/logs' >> /opt/solr/bin/solr.in.sh \  
&& echo 'SOLR_LOG_LEVEL=WARN' >> /opt/solr/bin/solr.in.sh \  
&& echo '#!/bin/bash' >> /opt/solr/bin/start-solr.sh \  
&& echo '[ -f "${SOLR_HOME}/solr.xml" ] || cp -R /opt/solr/server/solr/*
${SOLR_HOME}/' >> /opt/solr/bin/start-solr.sh \  
&& echo 'cp -R ${SOLR_LIB_DIR}/*.jar ${SOLR_SERVER_LIB}/' >>
/opt/solr/bin/start-solr.sh \  
&& echo '/opt/solr/bin/solr start -force -f -c' >> /opt/solr/bin/start-solr.sh
\  
&& chmod +x /opt/solr/bin/start-solr.sh  
  
RUN mvn_get() { mvn dependency:copy -DlocalRepositoryDirectory="/tmp/m2repo"
-DoutputDirectory="${SOLR_SERVER_LIB}"
-Djavax.net.ssl.trustStorePassword=changeit -Dartifact="$1"; } \  
&& mvn_get "com.janeluo:ikanalyzer:2012_u6" \  
&& mvn_get "com.hankcs:hanlp:portable-1.6.3" \  
&& mvn_get "com.huaban:jieba-analysis:1.0.2" \  
&& rm -Rf /tmp/* /opt/solr/docs/ \  
&& ls -alh ${SOLR_SERVER_LIB}  
  
EXPOSE 8983 9983  
WORKDIR /opt/solr  
  
ENTRYPOINT ["start-solr.sh"]  
CMD ["start-solr.sh]  

