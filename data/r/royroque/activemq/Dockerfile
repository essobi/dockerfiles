FROM provlprr/java7:ubuntu1404  
  
RUN \  
apt-get update && \  
curl http://archive.apache.org/dist/activemq/apache-activemq/5.9.0/apache-
activemq-5.9.0-bin.tar.gz | tar -xz  
  
EXPOSE 61616 8161  
  
CMD java -Xms1024m -Xmx1024m -Dhawtio.realm=activemq -Dhawtio.role=admins
-Dhawtio.rolePrincipalClasses=org.apache.activemq.jaas.GroupPrincipal
-Djava.util.logging.config.file=logging.properties
-Dcom.sun.management.jmxremote -Dcom.sun.management.jmxremote
-Djava.security.auth.login.config=apache-activemq-5.9.0/conf/login.config
-Djava.io.tmpdir=apache-activemq-5.9.0/tmp -Dactivemq.classpath=apache-
activemq-5.9.0/conf -Dactivemq.home=apache-activemq-5.9.0
-Dactivemq.base=apache-activemq-5.9.0 -Dactivemq.conf=apache-
activemq-5.9.0/conf -Dactivemq.data=apache-activemq-5.9.0/data -jar apache-
activemq-5.9.0/bin/activemq.jar start  
  

