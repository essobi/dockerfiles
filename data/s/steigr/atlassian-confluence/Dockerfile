FROM steigr/tomcat:latest  
  
ENV APPLICATION_USER=confluence \  
CONFLUENCE_VERSION=6.0.6  
  
RUN addgroup -S $APPLICATION_USER \  
&& adduser -h /app -G $APPLICATION_USER -g '' -S -D -H $APPLICATION_USER \  
&& apk add --no-cache --virtual .build-deps tar curl \  
&& install -D -d -o $APPLICATION_USER -g $APPLICATION_USER /app \  
&& curl -L
https://www.atlassian.com/software/confluence/downloads/binary/atlassian-
confluence-${CONFLUENCE_VERSION}.tar.gz \  
| su-exec $APPLICATION_USER tar -x -z -C /app --strip-components=1 \  
&& tomcat-install /app $APPLICATION_USER \  
&& rm -rf /app/lib/hsqldb-*.jar \  
/app/lib/postgresql-*.jar \  
/app/README* \  
/app/NOTICE* \  
/app/licenses \  
/app/tomcat-docs \  
&& xml c14n --without-comments /app/conf/server.xml | xml fo -s 2 >
/app/conf/server.xml.tmp \  
&& mv /app/conf/server.xml.tmp /app/conf/server.xml \  
&& hsqldb_version=$(curl -sL
http://central.maven.org/maven2/org/hsqldb/hsqldb/maven-metadata.xml | xml sel
--net --template --value-of '/metadata/versioning/latest' ) \  
&& curl -Lo /app/lib/hsqldb-$hsqldb_version.jar
http://central.maven.org/maven2/org/hsqldb/hsqldb/$hsqldb_version/hsqldb-$hsqldb_version.jar
\  
&& postgresql_version=$(curl -sL
https://repo1.maven.org/maven2/org/postgresql/postgresql/maven-metadata.xml |
xml sel --net --template --value-of '/metadata/versioning/latest' | sed -e
's@\\.jre.*@@') \  
&& curl -Lo /app/lib/postgresql-$postgresql_version.jar
https://jdbc.postgresql.org/download/postgresql-$postgresql_version.jar \  
&& apk del .build-deps \  
&& rm -rf /var/cache/apk/*  
  
RUN export MIDANAUTHENTICATOR_VERSION=1.1.0 \  
&& apk add --no-cache --virtual .build-deps curl \  
&& curl -L https://github.com/MIDAN-
SOFTWARE/MIDANAuthenticator/releases/download/${MIDANAUTHENTICATOR_VERSION}/midan-
authenticator-${MIDANAUTHENTICATOR_VERSION:0:3}.jar \  
| install -D -o $APPLICATION_USER -g $APPLICATION_USER -m 0644 /dev/stdin
/app/atlassian-confluence/WEB-INF/lib/midan-
authenticator-${MIDANAUTHENTICATOR_VERSION:0:3}.jar \  
&& apk del .build-deps \  
&& rm -rf /var/cache/apk/*  
  
VOLUME /app/.oracle_jre_usage /app/work /app/logs /tmp  
ENTRYPOINT ["confluence"]  
ADD docker-entrypoint.sh /bin/confluence  
  
ADD scripts/main /main  
ADD scripts/vars /vars  
ADD scripts/crowd-sso-configurator /crowd-sso-configurator  
ADD scripts/confluence-configurator /confluence-configurator

