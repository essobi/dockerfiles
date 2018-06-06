FROM tomcat:9-jre8  
MAINTAINER chaya  
  
#Install postgres client, to check database state  
RUN apt-get update && apt-get install -y postgresql-client  
  
COPY run.sh /usr/local/tomcat/bin/run.sh  
RUN chmod +x /usr/local/tomcat/bin/run.sh  
RUN echo "export JAVA_OPTS=\"\$JAVA_OPTS
-Djava.security.egd=file:/dev/./urandom\"" > /usr/local/tomcat/bin/setenv.sh  
  
CMD ["run.sh"]

