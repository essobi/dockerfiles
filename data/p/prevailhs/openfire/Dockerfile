FROM ubuntu:14.04  
ENV OPENFIRE_VERSION=3.10.2 \  
OPENFIRE_USER=openfire \  
OPENFIRE_DATA_DIR=/data \  
OPENFIRE_LOG_DIR=/var/log/openfire  
  
RUN apt-get update \  
&& apt-get install -y wget openjdk-7-jre \  
&& wget
"http://www.igniterealtime.org/downloadServlet?filename=openfire/openfire_${OPENFIRE_VERSION}_all.deb"
\  
-O /tmp/openfire_${OPENFIRE_VERSION}_all.deb \  
&& dpkg -i /tmp/openfire_${OPENFIRE_VERSION}_all.deb \  
&& rm -rf openfire_${OPENFIRE_VERSION}_all.deb \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV JAVA_HOME=/usr/lib/jvm/java-7-openjdk-amd64/jre \  
DAEMON_DIR=/usr/share/openfire \  
DAEMON_LIB=/usr/share/openfire/lib  
  
# List port  
EXPOSE 5222/tcp  
EXPOSE 3478/tcp  
EXPOSE 3479/tcp  
EXPOSE 5223/tcp  
EXPOSE 5229/tcp  
EXPOSE 7070/tcp  
EXPOSE 7443/tcp  
EXPOSE 7777/tcp  
EXPOSE 9090/tcp  
EXPOSE 9091/tcp  
  
# For use by psql to initialize db  
VOLUME /usr/share/openfire/resources/database  
  
COPY entrypoint.sh /  
COPY openfire.xml /usr/share/openfire/conf/  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["sh", "-c", "${JAVA_HOME}/bin/java -server -DopenfireHome=${DAEMON_DIR}
-Dopenfire.lib.dir=${DAEMON_LIB} -classpath ${DAEMON_LIB}/startup.jar -jar
${DAEMON_LIB}/startup.jar"]  

