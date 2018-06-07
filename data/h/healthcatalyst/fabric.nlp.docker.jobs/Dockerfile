FROM healthcatalyst/fabric.docker.centos.tomcat:latest  
  
LABEL maintainer="imran.qureshi@healthcatalyst.com"  
LABEL version="1.0.5"  
  
# install mariadb-client (i.e., mysql client) so we can wait for our tables to
become ready  
ADD mariadb.repo /etc/yum.repos.d/  
  
RUN yum -y install MariaDB-client; yum clean all  
  
# copy all the files  
RUN mv opt/apache-tomcat /opt/tomcat-nlp-nlp \  
&& cd /opt/tomcat-nlp-nlp/webapps/ \  
&& mkdir -p nlp \  
&& cd nlp \  
&& curl -O https://fabricnlpfiles.blob.core.windows.net/war/nlp.war \  
&& ls \  
&& jar xvf nlp.war \  
&& rm -fv nlp.war \  
&& ls -al /opt/tomcat-nlp-nlp/webapps/ \  
&& rm --force --verbose WEB-INF/lib/hibernate-validator-6.0.5.Final.jar \  
&& ls -al /opt/tomcat-nlp-nlp/webapps/nlp/WEB-INF/lib/hib* \  
&& cd  
  
ADD application.properties /etc/nlp/nlp/  
  
COPY indexes/ /opt/indexes/  
COPY models/ /opt/models/  
  
ADD server.xml /opt/tomcat-nlp-nlp/conf/server.xml  
ADD tomcat-users.xml /opt/tomcat-nlp-nlp/conf/  
  
ADD searchConfig.json /etc/nlp/  
ADD searchConfig.json /opt/nlp/  
  
ADD setenv.sh /opt/tomcat-nlp-nlp/bin/setenv.sh  
  
ADD docker-entrypoint.sh ./docker-entrypoint.sh  
ADD updateconfig.sh /etc/nlp/nlp/  
  
RUN dos2unix ./docker-entrypoint.sh &>/dev/null \  
&& chmod a+x ./docker-entrypoint.sh \  
&& dos2unix /etc/nlp/nlp/updateconfig.sh &>/dev/null \  
&& chmod a+x /etc/nlp/nlp/updateconfig.sh  
  
EXPOSE 8084  
ENTRYPOINT ["./docker-entrypoint.sh"]  

