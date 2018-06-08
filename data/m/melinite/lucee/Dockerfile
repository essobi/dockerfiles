# use with docker 1.4.1+ recommended  
# lucee server jetty 9 java 8  
FROM melinite/jetty_base:latest  
MAINTAINER David Seong <melinite@gmail.com>  
  
# As always, define userspace; security is going to be an ongoing issue with
popularity of Docker.  
# Beware of privilege escalation and do not trust arbitrary docker files
blindly.  
USER  root  
  
ENV JETTY_PORT=8080 \  
JETTY_USER=lucee \  
JETTY_BASE=/opt/lucee \  
JETTY_LUCEE_CONTEXT=/ \  
JETTY_LUCEE_APPNAME=luceeimhome \  
LUCEE_VERSION=4.5.1.000 \  
LUCEE_URL=https://bitbucket.org/lucee/lucee/downloads \  
TMPDIR=${JETTY_HOME}/temp \  
JAVA_OPTIONS="-server -XX:+UseConcMarkSweepGC -XX:+CMSParallelRemarkEnabled
-XX:+UseCMSInitiatingOccupancyOnly -XX:CMSInitiatingOccupancyFraction=70
-XX:+ScavengeBeforeFullGC -XX:+CMSScavengeBeforeRemark -Xms512m -Xmx512m
-XX:MaxMetaspaceSize=256M"  
RUN mkdir -p ${JETTY_BASE}/lib/lucee ${JETTY_BASE}/etc ${JETTY_BASE}/webapps
&& \  
useradd -rUM -s /bin/false -c "system user jetty" ${JETTY_USER} && \  
chown -RH ${JETTY_USER}:${JETTY_USER} ${JETTY_HOME} ${JETTY_BASE}  
# seperate run for efficient caching when jetty user changes frequently.  
RUN wget ${LUCEE_URL}/lucee-${LUCEE_VERSION}-jars.zip -O /tmp/luceejars.zip &&
\  
cd ${JETTY_BASE}/lib/lucee && \  
jar xf /tmp/luceejars.zip && \  
rm /tmp/luceejars.zip  
  
# Had to comment the user privilege out which reduces functionality of host to
container mount volumes permissions.  
# Uncomment the line below for production use and make sure your ACL is
aligned.  
# USER ${JETTY_USER}  
  
COPY webdefault.xml ${JETTY_BASE}/etc/  
COPY lucee.mod ${JETTY_HOME}/modules/  
  
WORKDIR ${JETTY_BASE}  
VOLUME ["$JETTY_BASE/webapps"]  
  
RUN java -jar ${JETTY_HOME}/start.jar \--add-to-start=lucee  
  
EXPOSE 8080  
  
CMD java ${JAVA_OPTIONS} -jar ${JETTY_HOME}/start.jar
-Djetty.lucee.context=${JETTY_LUCEE_CONTEXT}
-Djetty.lucee.appname=${JETTY_LUCEE_APPNAME}

