FROM dadez/jre:latest  
MAINTAINER dadez <dadez@protonmail.com>  
  
ARG BUILD_DATE  
ARG VCS_REF  
  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="tomcat8" \  
org.label-schema.description="tomcat8 based on oracle java8 and alpine linux"
\  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/dadez/tomcat-owasp" \  
org.label-schema.vendor="dadez" \  
org.label-schema.version=$VERSION \  
org.label-schema.schema-version="1.0"  
  
ADD ./configureWebXMLforDocker.groovy /tmp/  
ADD ./configureServerXMLforDocker.groovy /tmp/  
  
ENV CATALINA_HOME /opt/tomcat  
ENV PATH $CATALINA_HOME/bin:$PATH  
RUN mkdir -p "$CATALINA_HOME"  
WORKDIR $CATALINA_HOME  
  
ENV TIMEZONE Europe/Zurich  
ENV LANG en_US.UTF-8  
ENV LC_ALL ""  
ARG PROXY  
ENV http_proxy ${PROXY:-""}  
ENV https_proxy ${PROXY:-""}  
  
  
RUN apk add --no-cache gnupg  
# see https://www.apache.org/dist/tomcat/tomcat-$TOMCAT_MAJOR/KEYS  
# see also "update.sh" (https://github.com/docker-
library/tomcat/blob/master/update.sh)  
ENV GPG_KEYS 05AB33110949707C93A279E3D3EFE6B686867BA6
07E48665A34DCAFAE522E5E6266191C37C037D42
47309207D818FFD8DCD3F83F1931D684307A10A5
541FBE7D8F78B25E055DDEE13C370389288584E7
61B832AC2F1C5A90F0F9B00A1C506407564C17A3
79F7026C690BAA50B92CD8B66A3AD3F4F22C4FED
9BA44C2621385CB966EBA586F72C284D731FABEE
A27677289986DB50844682F8ACB77FC2E86E29AC
A9C5DF4D22E99998D9875A5110C01C5A2F6059E7
DCFD35E0BF8CA7344752DE8B6FB21E8933C60243
F3A04C595DB5B6A5F1ECA43E3B7BBB100D811BBE
F7DA48BB64BCB84ECBA7EE6935CD23C10D498E23  
RUN set -ex; \  
for key in $GPG_KEYS; do \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \  
done  
  
ARG TOMCAT_MAJOR  
ENV TOMCAT_MAJOR ${TOMCAT_MAJOR:-8}  
ARG TOMCAT_VERSION  
ENV TOMCAT_VERSION ${TOMCAT_VERSION:-8.5.9}  
  
ENV TOMCAT_TGZ_URL
http://archive.apache.org/dist/tomcat/tomcat-${TOMCAT_MAJOR}/v${TOMCAT_VERSION}/bin/apache-
tomcat-${TOMCAT_VERSION}.tar.gz  
ENV TOMCAT_ASC_URL
http://archive.apache.org/dist/tomcat/tomcat-${TOMCAT_MAJOR}/v${TOMCAT_VERSION}/bin/apache-
tomcat-${TOMCAT_VERSION}.tar.gz.asc  
  
RUN apk add --no-cache --virtual .fetch-deps \  
ca-certificates \  
tar \  
openssl \  
su-exec  
  
RUN apk add --update \  
unzip \  
bash \  
curl \  
tzdata  
  
#install tomcat  
RUN set -x \  
&& echo $TIMEZONE > /etc/timezone \  
&& cp /usr/share/zoneinfo/${TIMEZONE} /etc/localtime \  
  
&& wget -O tomcat.tar.gz "$TOMCAT_TGZ_URL" \  
&& wget -O tomcat.tar.gz.asc "$TOMCAT_ASC_URL" \  
&& gpg --batch --verify tomcat.tar.gz.asc tomcat.tar.gz \  
&& tar -xvf tomcat.tar.gz --strip-components=1 \  
&& rm bin/*.bat \  
&& rm tomcat.tar.gz*  
  
#configure tomcat  
#remove unneeded webapps  
RUN rm -rf $CATALINA_HOME/webapps/docs \  
$CATALINA_HOME/webapps/examples \  
$CATALINA_HOME/webapps/host-manager \  
$CATALINA_HOME/webapps/manager \  
  
#remove unneeded files  
&& rm -f $CATALINA_HOME/LICENSE \  
$CATALINA_HOME/NOTICE \  
$CATALINA_HOME/RELEASE-NOTES \  
$CATALINA_HOME/RUNNING.txt \  
  
#Overwrite Server Version  
&& mkdir -p $CATALINA_HOME/lib/org/apache/catalina/util \  
  
#empty ROOT webapp  
&& rm -rf $CATALINA_HOME/webapps/ROOT/*  
  
#workaround for allow groovy to run  
RUN ln -sf /bin/bash /bin/sh  
#install groovy  
WORKDIR /opt/  
ENV GROOVY_HOME /opt/groovy  
ENV PATH ${PATH}:${JAVA_HOME}/bin:${GROOVY_HOME}/bin  
ENV GROOVY_VERSION=2.4.8  
RUN curl -skLo /opt/groovy.zip https://dl.bintray.com/groovy/maven/apache-
groovy-binary-${GROOVY_VERSION}.zip \  
&& unzip /opt/groovy.zip \  
&& rm -f /opt/groovy.zip \  
&& ln -sf /opt/groovy-${GROOVY_VERSION} /opt/groovy  
  
#configure server.xml  
RUN groovy /tmp/configureServerXMLforDocker.groovy -path
$CATALINA_HOME/conf/server.xml \  
#configure web.xml  
&& groovy /tmp/configureWebXMLforDocker.groovy -path
$CATALINA_HOME/conf/web.xml \  
  
#restore default shell  
&& ln -sf /bin/busybox /bin/sh  
  
#overwrite some files  
ADD ./conf/logging.properties $CATALINA_HOME/conf/  
ADD ./conf/ServerInfo.properties $CATALINA_HOME/lib/org/apache/catalina/util/  
  
ADD ./webapps/ROOT/index.html $CATALINA_HOME/webapps/ROOT/  
ADD ./webapps/ROOT/error.jsp $CATALINA_HOME/webapps/ROOT/  
ADD ./webapps/ROOT/MemoryInfo.jsp $CATALINA_HOME/webapps/ROOT/  
ADD ./webapps/ROOT/SystemInfo.jsp $CATALINA_HOME/webapps/ROOT/  
  
#cleanup  
RUN apk del \  
bash \  
unzip \  
curl \  
tzdata \  
&& rm -rf /var/cache/apk/* /tmp/* /opt/groovy*  
  
VOLUME /opt/tomcat/logs  
WORKDIR /opt/tomcat  
  
ENV JAVA_OPTS -Duser.timezone=Europe/Zurich  
ENV CATALINA_OPTS -Dfile.encoding=UTF-8  
COPY docker-entrypoint.sh /usr/local/bin/  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
EXPOSE 8080  
CMD ["catalina.sh", "run"]  

