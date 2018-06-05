FROM boky/java7  
  
# Jboss won't compile with a later maven version  
ENV MAVEN_VERSION=3.1.1  
ENV ANT_VERSION=1.9.6  
ENV MAVEN_OPTS="-Xmx512m -XX:MaxPermSize=256m"  
ENV MAX_FD="maximum"  
  
ENV M2_HOME=/usr/lib/maven/default  
ENV M2=$M2_HOME/bin  
ENV ANT_HOME=/usr/lib/ant/default  
ENV ANT=$ANT_HOME/bin  
ENV JAVA_HOME="/usr/lib/jvm/default-jvm"  
ENV JAVA=$JAVA_HOME/bin/java  
ENV PATH $PATH:$$JAVA_HOME:$JAVA:$M2_HOME:$M2:$ANT  
ENV JBOSS_HOME="/usr/lib/jboss/default"  
  
RUN \  
apk add --no-cache --virtual=build-dependencies --update curl ca-certificates
tar && \  
cd /tmp && \  
echo "Downloading Maven ${MAVEN_VERSION}..." && \  
curl -S -L
http://mirror.vorboss.net/apache/maven/maven-3/${MAVEN_VERSION}/binaries/apache-
maven-${MAVEN_VERSION}-bin.tar.gz | tar xfz - && \  
mkdir -p /usr/lib/maven && \  
mv /tmp/apache-maven* /usr/lib/maven/${MAVEN_VERSION} && \  
ln -s /usr/lib/maven/${MAVEN_VERSION} ${M2_HOME} && \  
cd /tmp && \  
echo "Downloading Ant ${ANT_VERSION}..." && \  
curl -S -O http://mirror.vorboss.net/apache/ant/binaries/apache-
ant-${ANT_VERSION}-bin.zip && \  
unzip -q apache*zip && \  
rm apache*zip && \  
mkdir -p /usr/lib/ant && \  
mv /tmp/apache-ant* /usr/lib/ant/${ANT_VERSION} && \  
ln -s /usr/lib/ant/${ANT_VERSION} ${ANT_HOME}  
  
  
RUN \  
cd /tmp && curl -L https://github.com/jbossas/jboss-
as/archive/7.1.2.Final.tar.gz | tar xfz - && \  
cd /tmp/jboss* && $M2/mvn -s tools/maven/conf/settings.xml install
-Djava.protocol.handler.pkgs=org.jboss.net.protocol -DskipTests && \  
mkdir -p /usr/lib/jboss && \  
cd /tmp/jboss* && mv build/target/jboss-as-7.1.2.Final /usr/lib/jboss/ && \  
ln -s /usr/lib/jboss/jboss-as-7.1.2.Final /usr/lib/jboss/default && \  
cd /tmp && rm -rf /tmp/jboss* && rm -rf /root/.m2/repository && \  
mkdir -p /var/log/jboss/standalone && \  
rm -rf /usr/lib/jboss/default/standalone/log && \  
ln -s /var/log/jboss/standalone /usr/lib/jboss/default/standalone/log && \  
mkdir -p /var/tmp/jboss/standalone && \  
rm -rf /usr/lib/jboss/default/standalone/tmp && \  
ln -s /var/tmp/jboss/standalone /usr/lib/jboss/default/standalone/tmp && \  
echo "admin=c22052286cd5d72239a90fe193737253" >
/usr/lib/jboss/default/standalone/configuration/mgmt-users.properties && \  
echo "root=18ddf90cbc83bed62ffe8199f21c5fe1" >>
/usr/lib/jboss/default/standalone/configuration/mgmt-users.properties && \  
mkdir -p /var/log/jboss/domain && \  
rm -rf /usr/lib/jboss/default/domain/log && \  
ln -s /var/log/jboss/domain /usr/lib/jboss/default/domain/log && \  
mkdir -p /var/tmp/jboss/domain && \  
rm -rf /usr/lib/jboss/default/domain/tmp && \  
ln -s /var/tmp/jboss/domain /usr/lib/jboss/default/domain/tmp && \  
echo "admin=c22052286cd5d72239a90fe193737253" >
/usr/lib/jboss/default/domain/configuration/mgmt-users.properties && \  
echo "root=18ddf90cbc83bed62ffe8199f21c5fe1" >>
/usr/lib/jboss/default/domain/configuration/mgmt-users.properties && \  
cd /tmp && \  
curl -O http://download.jboss.org/jbossws/jbossws-cxf-4.2.3.Final.zip && \  
unzip -q jboss*zip && \  
cd jbossws-cxf-bin-dist && \  
echo "jboss712.home=/usr/lib/jboss/default" > ant.properties && \  
echo "jbossws.integration.target=jboss712" >> ant.properties && \  
echo "jboss.bind.address=localhost" >> ant.properties && \  
echo "jbossws.deployer.authentication.username=admin" >> ant.properties && \  
echo "jbossws.deployer.authentication.password=admin" >> ant.properties && \  
echo "javac.debug=yes" >> ant.properties && \  
echo "javac.deprecation=no" >> ant.properties && \  
echo "javac.fail.onerror=yes" >> ant.properties && \  
echo "javac.verbose=no" >> ant.properties && \  
ant -Djboss.server.instance=default deploy-jboss712 && \  
rm -rf /tmp/jboss* && \  
rm -rf /usr/lib/jboss/default/docs && \  
rm -rf /usr/lib/jboss/default/welcome-content && \  
rm -rf /usr/lib/jboss/default/*.txt && \  
rm -rf /root/.m2  
  
RUN addgroup -S jbossas  
RUN adduser -S -D -H -s /sbin/nologin jbossas  
RUN addgroup jbossas jbossas  
#RUN curl -S -L https://github.com/Yelp/dumb-
init/releases/download/v1.0.0/dumb-init_1.0.0_amd64 > /usr/local/bin/dumb-init  
#RUN chmod +x /usr/local/bin/dumb-init  
#RUN apk add --update --repository
http://dl-1.alpinelinux.org/alpine/edge/community/ tini  
ENV TINI_VERSION v0.9.0  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini-
static /usr/local/bin/tini  
RUN chmod +x /usr/local/bin/tini  
  
RUN \  
chown -R jbossas:jbossas /var/tmp/jboss && \  
chown -R jbossas:jbossas /var/log/jboss && \  
mkdir -p /usr/lib/jboss/default/domain/data && chown -R jbossas:jbossas
/usr/lib/jboss/default/domain/data && \  
mkdir -p /usr/lib/jboss/default/standalone/data && chown -R jbossas:jbossas
/usr/lib/jboss/default/standalone/data && \  
mkdir -p /usr/lib/jboss/default/domain/deployments && chown -R jbossas:jbossas
/usr/lib/jboss/default/domain/deployments && \  
mkdir -p /usr/lib/jboss/default/standalone/deployments && chown -R
jbossas:jbossas /usr/lib/jboss/default/standalone/deployments && \  
chown -R jbossas:jbossas /usr/lib/jboss/default/domain/configuration && \  
chown -R jbossas:jbossas /usr/lib/jboss/default/standalone/configuration && \  
mkdir -p /usr/lib/jboss/default/welcome-content  
  
COPY ./start.sh /  
RUN chmod +x /start.sh  
  
USER jbossas  
EXPOSE 4447  
EXPOSE 8080  
EXPOSE 9990  
EXPOSE 9443  
EXPOSE 9999  
  
ENV FLUSH_ON_START=false  
ENV STARTUP_OPTS="-b 0.0.0.0 -Djboss.bind.address.management=0.0.0.0"  
ENV JAVA_OPTS="-XX:MaxPermSize=512m -Xmx2G -XX:+CMSClassUnloadingEnabled
-Djavax.faces.PROJECT_STAGE=Production"  
  
ENTRYPOINT [ "/usr/local/bin/tini, "-v", "\--" ]  
CMD [ "/bin/sh", "-c", "/start.sh" ]

