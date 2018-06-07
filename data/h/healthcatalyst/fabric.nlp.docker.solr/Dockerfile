FROM healthcatalyst/fabric.docker.centos.tomcat:latest  
LABEL maintainer="Health Catalyst"  
LABEL version="1.0"  
  
RUN mv opt/apache-tomcat /opt/tomcat-nlp-solr  
  
# copy all the files  
# ADD https://fabricnlpfiles.blob.core.windows.net/war/solr.war /opt/tomcat-
nlp-solr/webapps/  
RUN cd /opt/tomcat-nlp-solr/webapps/ \  
&& curl -O https://fabricnlpfiles.blob.core.windows.net/war/solr.war \  
&& ls \  
&& jar xvf solr.war  
  
#ADD solr/solr.xml /opt/tomcat-nlp-solr/conf/Catalina/localhost/solr.xml  
#ADD solr/context.xml /opt/tomcat-nlp-solr/conf/Catalina/localhost/context.xml  
COPY conf/ /opt/tomcat-nlp-solr/conf/  
ADD solr/log4j.xml /etc/nlp/solr/  
COPY solr/ /opt/nlp/solr/  
ADD server.xml /opt/tomcat-nlp-solr/conf/server.xml  
ADD tomcat-users.xml /opt/tomcat-nlp-solr/conf/  
  
# ADD opt/solr/collection1/core.properties
/opt/solr/collection1/core.properties  
ADD opt/solr/patient_cohort/core.properties
/opt/solr/patient_cohort/core.properties  
ADD opt/solr/regenconcept/core.properties
/opt/solr/regenconcept/core.properties  
ADD opt/solr/report_core/core.properties /opt/solr/report_core/core.properties  
ADD opt/solr/report_list/core.properties /opt/solr/report_list/core.properties  
  
ADD opt/solr/collection1/conf/* /opt/solr/collection1/conf/  
ADD opt/solr/patient_cohort/conf/* /opt/solr/patient_cohort/conf/  
ADD opt/solr/regenconcept/conf/* /opt/solr/regenconcept/conf/  
ADD opt/solr/report_core/conf/* /opt/solr/report_core/conf/  
ADD opt/solr/report_list/conf/* /opt/solr/report_list/conf/  
  
ADD setenv.sh /opt/tomcat-nlp-solr/bin/setenv.sh  
  
ADD docker-entrypoint.sh ./docker-entrypoint.sh  
ADD createcores.sh ./  
  
RUN dos2unix ./docker-entrypoint.sh \  
&& chmod a+x ./docker-entrypoint.sh \  
&& dos2unix ./createcores.sh \  
&& chmod a+x ./createcores.sh \  
&& mkdir -p /opt/healthcatalyst  
  
EXPOSE 8085  
ENTRYPOINT ["./docker-entrypoint.sh"]  
  

