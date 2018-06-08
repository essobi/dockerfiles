FROM tomcat:8.5.8-jre8  
  
MAINTAINER Martin Rumanek <martin@rumanek.cz>  
  
ENV REFRESHED_AT 2014-3-20  
ENV FCREPO_DOWNLOAD_URL http://downloads.sourceforge.net/fedora-
commons/fcrepo-installer-3.8.1.jar  
ENV JDBC_DRIVER_DOWNLOAD_URL
http://jdbc.postgresql.org/download/postgresql-9.3-1103.jdbc4.jar  
  
## install packages  
RUN apt-get -yqq update && apt-get -y install xmlstarlet && rm -rf
/var/lib/apt/lists/*  
  
WORKDIR $CATALINA_HOME  
RUN curl -sL "$JDBC_DRIVER_DOWNLOAD_URL" -o lib/postgresql-9.3-1103.jdbc4.jar  
  
ENV FEDORA_HOME /usr/local/fedora  
  
## install fedora  
ADD fedora-install.properties /tmp/fedora-install.properties  
RUN curl -sL "$FCREPO_DOWNLOAD_URL" -o fedora-install.jar && \  
java -jar fedora-install.jar /tmp/fedora-install.properties  
  
RUN xmlstarlet ed -L -N x="http://www.fedora.info/definitions/1/0/config/" \  
-s "//x:module[@role='org.fcrepo.server.resourceIndex.ResourceIndex']" -t elem -n "paramKrameriusTMP" -v "" \  
-s "//x:module[@role='org.fcrepo.server.resourceIndex.ResourceIndex']" -t elem -n "paramOAITMP" -v "" \  
-i "//paramKrameriusTMP" -t attr -n "name" -v "alias:kramerius" \  
-i "//paramKrameriusTMP" -t attr -n "value" -v "http://www.nsdl.org/ontologies/relationships#" \  
-s "//paramKrameriusTMP" -t elem -n "comment" -v "Alias for Kramerius" \  
-r "//paramKrameriusTMP" -v "param" \  
-i "//paramOAITMP" -t attr -n "name" -v "alias:oai" \  
-i "//paramOAITMP" -t attr -n "value" -v "http://www.openarchives.org/OAI/2.0/" \  
-s "//paramOAITMP" -t elem -n "comment" -v "Alias for OAI" \  
-r "//paramOAITMP" -v "param" \  
-u "//x:module[@role='org.fcrepo.server.resourceIndex.ResourceIndex']/x:param[@name='datastore']/@value" -v "localPostgresMPTTriplestore" \  
-u "//x:datastore[@id='localPostgresMPTTriplestore']/x:param[@name='jdbcURL']/@value" -v "jdbc:postgresql://riTriplesPostgres/riTriples" \  
$FEDORA_HOME/server/config/fedora.fcfg  
  
ADD logback.xml $FEDORA_HOME/server/config/logback.xml  
  
ENV JAAS_CONFIG $FEDORA_HOME/server/config/jaas.conf  
  
ENV TOMCAT_USER tomcat  
ENV TOMCAT_UID 8983  
RUN groupadd -r $TOMCAT_USER && \  
useradd -r -u $TOMCAT_UID -g $TOMCAT_USER $TOMCAT_USER  
ADD fedora-xacml-policies $FEDORA_HOME/data/fedora-xacml-policies  
RUN chown -R $TOMCAT_USER:$TOMCAT_USER $CATALINA_HOME  
RUN chmod -R ugo+rwx $CATALINA_HOME  
RUN chown -R $TOMCAT_USER:$TOMCAT_USER $FEDORA_HOME  
RUN chmod -R ug+rwX $FEDORA_HOME  
  
USER $TOMCAT_USER  
  
  
EXPOSE 8080  
ADD docker-entrypoint.sh /  
ADD context.xml $CATALINA_HOME/conf/context.xml  
ADD server.xml $CATALINA_HOME/conf/server.xml  
ADD objects-jaxrs.xml $FEDORA_HOME/server/config/spring/web/jaxrs/objects-
jaxrs.xml  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["catalina.sh", "run"]  
  

