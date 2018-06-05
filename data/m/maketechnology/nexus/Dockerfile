FROM maketechnology/nexus-p2-alpine:latest  
  
USER root  
  
RUN MAVEN_VERSION=3.3.9 \  
&& cd /usr/share \  
&& wget -q
http://apache.dattatec.com/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz -O - | tar xzf - \  
&& mv /usr/share/apache-maven-$MAVEN_VERSION /usr/share/maven \  
&& ln -s /usr/share/maven/bin/mvn /usr/bin/mvn  
  
COPY token /token  
  
RUN apk add --no-cache git nodejs  
  
RUN git clone https://github.com/maketechnology/target2nexus.git /target2nexus
\  
&& npm install -g /target2nexus  
  
USER $SERVICE_USER  
  
RUN git clone -b test_gitlab https://gitlab-ci-token:$(cat
/token)@gitlab.com/gzunino/dbt2.git src  
  
RUN /opt/sonatype/nexus/bin/nexus-service.sh start \  
&& sleep 120 \  
&& cd src \  
&& target2nexus com.querix.dbt.target/com.querix.dbt.target.target
http://0.0.0.0:8081/nexus \  
&& ./postToNexus.sh \  
&& mvn -fn -B -Dorg.eclipse.update.jarprocessor.pack200=/opt/jre1.8.0_74/bin
clean verify -s settings-nexus.xml -f pom.xml -Pmodules,products,envs,uiTests
\  
&& rm -rf ~/.m2 \  
&& rm -rf ~/tmp/ \  
&& cd .. \  
&& rm -rf src  
  
USER root  
  
RUN npm uninstall -g /target2nexus \  
&& apk del --purge git nodejs \  
&& rm -f /usr/bin/mvn && rm -rf /usr/share/maven \  
&& rm -rf /target2nexus \  
&& rm -f /token \  
&& rm -rf /opt/sonatype/nexus/tmp \  
&& rm -rf /opt/sonatype/nexus/logs \  
&& rm -rf /opt/sonatype-work/nexus/logs \  
&& rm -rf /opt/sonatype-work/nexus/timeline \  
&& rm -rf /tmp/* && rm -rf ~/tmp/  
  
USER $SERVICE_USER  
  
RUN /opt/sonatype/nexus/bin/nexus-service.sh stop

