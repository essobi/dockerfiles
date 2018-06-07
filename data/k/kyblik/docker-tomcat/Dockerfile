FROM 511200753148.dkr.ecr.eu-west-1.amazonaws.com/oracle-jdk7-amazonlinux  
  
ENV CATALINA_HOME=/usr/local/tomcat \  
CATALINA_CUSTOM_OPTS=''  
ENV PATH=$CATALINA_HOME/bin:$PATH \  
SSL_HOME=$CATALINA_HOME/ssl \  
SECRETS_BUCKET_NAME= \  
SECRETS_BUCKET_SSL_KEY= \  
SSL_CERTIFICATE_FILE= \  
SSL_CERTIFICATE_KEY_FILE= \  
SSL_CA_CERTIFICATE_KEY_FILE= \  
SSL_CERTIFICATE_CHAIN_FILE= \  
SSL_PROTOCOL='TLSv1.2' \  
SSL_VERIFY_CLIENT='none' \  
NEW_RELIC_LICENSE_KEY= \  
NEW_RELIC_APP_NAME='Tomcat' \  
NEW_RELIC_ENABLE_AUTO_APP_NAMING=false \  
NEW_RELIC_LABELS='' \  
NEW_RELIC_AGENT_VERSION=current \  
LD_LIBRARY_PATH=$CATALINA_HOME/lib:/usr/lib  
  
RUN mkdir -p "$CATALINA_HOME"  
WORKDIR $CATALINA_HOME  
  
# Install aws-cli  
RUN yum install -y \  
bash \  
python \  
wget \  
ca-certificates \  
openssl-devel \  
openssl098e \  
&& yum clean all  
  
ENV TOMCAT_MAJOR 7  
ENV TOMCAT_VERSION 7.0.79  
#
https://issues.apache.org/jira/browse/INFRA-8753?focusedCommentId=14735394#comment-14735394  
ENV TOMCAT_TGZ_URL
https://www.apache.org/dyn/closer.cgi?action=download&filename=tomcat/tomcat-$TOMCAT_MAJOR/v$TOMCAT_VERSION/bin/apache-
tomcat-$TOMCAT_VERSION.tar.gz  
# not all the mirrors actually carry the .asc files :'(  
ENV TOMCAT_ASC_URL
https://www.apache.org/dist/tomcat/tomcat-$TOMCAT_MAJOR/v$TOMCAT_VERSION/bin/apache-
tomcat-$TOMCAT_VERSION.tar.gz.asc  
  
RUN set -x \  
\  
&& wget -O tomcat.tar.gz "$TOMCAT_TGZ_URL" \  
&& wget -O tomcat.tar.gz.asc "$TOMCAT_ASC_URL" \  
&& tar -xvf tomcat.tar.gz --strip-components=1 \  
&& rm bin/*.bat \  
&& rm tomcat.tar.gz*  
  
COPY lib* $CATALINA_HOME/lib/  
RUN ln -s $CATALINA_HOME/lib/libapr-1.so.0.5.2
$CATALINA_HOME/lib/libapr-1.so.0  
RUN ln -s $CATALINA_HOME/lib/libtcnative-1.so.0.1.34
$CATALINA_HOME/lib/libtcnative-1.so  
RUN ln -s /usr/lib64/libssl.so.0.9.8e /usr/lib64/libssl.so.1.0.0  
RUN ln -sf /usr/lib64/libcrypto.so.0.9.8e /usr/lib64/libcrypto.so.1.0.0  
  
# Create the certificate folder  
RUN mkdir $SSL_HOME  
  
# Remove standard tomcat webapps  
RUN rm -rf $CATALINA_HOME/webapps/*  
  
# Expose tomcat ports  
EXPOSE 8080 8443  
# Add customized tomcat conf files  
# Workaround for COPY as it does not work as expected  
# https://github.com/docker/docker/issues/15858#issuecomment-136541563  
COPY tomcat/ $CATALINA_HOME/  
  
COPY docker-entrypoint.sh /usr/local/bin/  
RUN chmod 744 /usr/local/bin/docker-entrypoint.sh  
  
# Add NewRelic java agent  
RUN wget http://download.newrelic.com/newrelic/java-agent/newrelic-
agent/current/newrelic-java.zip \  
&& unzip -n newrelic-java.zip -d $CATALINA_HOME \  
&& rm -f newrelic-java.zip  
  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
CMD ["catalina.sh", "run"]  

