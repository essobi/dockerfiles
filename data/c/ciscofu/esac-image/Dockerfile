FROM openjdk:8-jre-alpine  
ADD bin/EsaSyslogService.jar /usr/local/bin  
EXPOSE 514/udp  
ENTRYPOINT
["java","-jar","/usr/local/bin/EsaSyslogService.jar","/usr/local/etc/esac/startup.txt"]

