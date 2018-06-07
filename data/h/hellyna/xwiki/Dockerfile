FROM tomcat:8  
MAINTAINER Hellyna NG <hellyna@hellyna.com>  
  
RUN rm -rf webapps/* && \  
curl -L \  
'http://download.forge.ow2.org/xwiki/xwiki-enterprise-web-7.1.2.war' \  
-o xwiki.war && \  
unzip -d webapps/ROOT xwiki.war && \  
rm -f xwiki.war  
  
#RUN curl -L \  
# 'https://jdbc.postgresql.org/download/postgresql-9.4-1202.jdbc42.jar' \  
# -o 'webapps/xwiki/WEB-INF/lib/postgresql-9.4-1202.jdbc42.jar'  
RUN curl -L \  
'http://central.maven.org/maven2/org/hsqldb/hsqldb/2.3.3/hsqldb-2.3.3.jar' \  
-o 'webapps/ROOT/WEB-INF/lib/hsqldb-2.3.3.jar'  
  
COPY setenv.sh bin/  
COPY catalina.policy.append catalina.policy.append  
  
RUN cat catalina.policy.append >> conf/catalina.policy && \  
rm catalina.policy.append && \  
echo 'environment.permanentDirectory=/var/local/xwiki' >> \  
webapps/ROOT/WEB-INF/xwiki.properties  
  
VOLUME ["/usr/local/tomcat/webapps/ROOT/WEB-INF", "/var/local/xwiki"]  
#COPY scripts /scripts  
#RUN /scripts/build  

