FROM steigr/tomcat:latest  
  
ENV APPLICATION_USER=software \  
JIRA_SOFTWARE_VERSION=7.3.1  
  
RUN addgroup -S $APPLICATION_USER \  
&& adduser -h /app -G $APPLICATION_USER -g '' -S -D -H $APPLICATION_USER \  
&& apk add --no-cache --virtual .build-deps tar curl \  
&& install -D -d -o $APPLICATION_USER -g $APPLICATION_USER /app \  
&& curl -L https://www.atlassian.com/software/jira/downloads/binary/atlassian-
jira-software-$JIRA_SOFTWARE_VERSION.tar.gz \  
| su-exec $APPLICATION_USER tar -x -z -C /app --strip-components=1 \  
&& rm -rf /app/lib/hsqldb-*.jar \  
/app/lib/postgresql-*.jar \  
/app/README* \  
/app/NOTICE* \  
/app/licenses \  
/app/tomcat-docs \  
&& tomcat-install /app $APPLICATION_USER \  
&& xml c14n --without-comments /app/conf/server.xml | xml fo -s 2 >
/app/conf/server.xml.tmp \  
&& mv /app/conf/server.xml.tmp /app/conf/server.xml \  
&& curl -Lo /app/lib/hsqldb-2.3.4.jar
http://central.maven.org/maven2/org/hsqldb/hsqldb/2.3.4/hsqldb-2.3.4.jar \  
&& curl -Lo /app/lib/postgresql-42.0.0.jar
https://jdbc.postgresql.org/download/postgresql-42.0.0.jar \  
&& apk del .build-deps \  
&& rm -rf /var/cache/apk/*  
  
RUN export MIDANAUTHENTICATOR_VERSION=1.1.0 \  
&& apk add --no-cache --virtual .build-deps curl \  
&& curl -L https://github.com/MIDAN-
SOFTWARE/MIDANAuthenticator/releases/download/${MIDANAUTHENTICATOR_VERSION}/midan-
authenticator-${MIDANAUTHENTICATOR_VERSION:0:3}.jar \  
| install -D -o $APPLICATION_USER -g $APPLICATION_USER -m 0644 /dev/stdin
/app/atlassian-jira/WEB-INF/lib/midan-
authenticator-${MIDANAUTHENTICATOR_VERSION:0:3}.jar \  
&& apk del .build-deps \  
&& rm -rf /var/cache/apk/*  
  
HEALTHCHECK CMD nc -z 127.0.0.1 8080  
  
VOLUME /app/.oracle_jre_usage /app/work /app/logs /tmp  
ENTRYPOINT ["software"]  
ADD docker-entrypoint.sh /bin/software  
  
ADD scripts/main /main  
ADD scripts/vars /vars  
ADD scripts/crowd-sso-configurator /crowd-sso-configurator  
ADD scripts/jira-software-configurator /jira-software-configurator

