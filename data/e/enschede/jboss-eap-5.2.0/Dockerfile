FROM enschede/linux-core-jdk6  
  
RUN cd /opt && \  
wget http://www.xs4all.nl/~mensched/jboss-eap-5.2.0.zip && \  
unzip jboss-eap-5.2.0.zip && \  
rm jboss-eap-5.2.0.zip  
  
EXPOSE 8080 7402  
#CMD /bin/bash  
CMD java \  
-Dprogram.name=run.sh -server -Xms1303m -Xmx1303m -XX:MaxPermSize=256m \  
-Dorg.jboss.resolver.warning=true \  
-Dsun.rmi.dgc.client.gcInterval=3600000 \  
-Dsun.rmi.dgc.server.gcInterval=3600000 \  
-Dsun.lang.ClassLoader.allowArraySyntax=true \  
-Djava.net.preferIPv4Stack=true \  
-Djava.endorsed.dirs="/opt/jboss-eap-5.2/jboss-as/lib/endorsed" \  
-classpath "/opt/jboss-eap-5.2/jboss-as/bin/run.jar" org.jboss.Main -c default

