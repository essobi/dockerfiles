FROM jeanblanchard/busybox-java:8  
MAINTAINER Christian Kroemer (christian.kroemer@comsysto.com)  
  
CMD /bin/sh -c 'java -Xdebug
-Xrunjdwp:transport=dt_socket,address=10000,server=y,suspend=n -Dport=${PORT}
-Dhost=${HOST} -Damq_host=${AMQ_PORT_5672_TCP_ADDR}
-Damq_port=${AMQ_PORT_5672_TCP_PORT} -jar /var/app/app.jar'

