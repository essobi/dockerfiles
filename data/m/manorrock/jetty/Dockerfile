FROM manorrock/openjdk  
ENV JETTY_VERSION 9.4.9.v20180320  
ENV JETTY_BASE /var/lib/jetty  
ENV JETTY_HOME /usr/local/jetty/  
RUN zypper --non-interactive refresh && \  
zypper --non-interactive install curl unzip && \  
curl -O http://central.maven.org/maven2/org/eclipse/jetty/jetty-
distribution/${JETTY_VERSION}/jetty-distribution-${JETTY_VERSION}.zip && \  
unzip jetty-distribution-${JETTY_VERSION}.zip && \  
mv jetty-distribution-${JETTY_VERSION} /usr/local/jetty && \  
rm jetty-distribution-${JETTY_VERSION}.zip && \  
java -Djetty.base=${JETTY_BASE} -jar /usr/local/jetty/start.jar --create-
startd --add-to-start="server,http,deploy,jsp,jstl,ext,resources,websocket" &&
\  
zypper --non-interactive remove curl unzip && \  
zypper --non-interactive clean -a  
CMD java -Djetty.base=${JETTY_BASE} -jar ${JETTY_HOME}/start.jar  
WORKDIR /mnt  

