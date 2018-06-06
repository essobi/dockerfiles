FROM jeanblanchard/busybox-java:8  
MAINTAINER Christian Kroemer (christian.kroemer@comsysto.com)  
  
CMD /bin/sh -c 'java -Dport=${PORT} -Dhost=${HOST}
-Damq_host=${AMQ_PORT_5672_TCP_ADDR} -Damq_port=${AMQ_PORT_5672_TCP_PORT} -jar
/var/app/app.jar'  

