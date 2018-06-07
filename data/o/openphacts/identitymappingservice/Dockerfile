FROM tomcat:7-jre7  
  
## source  
ENV WAR_URL
https://github.com/openphacts/queryExpander/releases/download/2.0.5/query.expander.ws.server-2.0.5.war  
#ENV WAR_URL
http://repository.mygrid.org.uk/artifactory/ops/uk/ac/manchester/cs/openphacts/queryexpander/query.expander.ws.server/2.0.4-SNAPSHOT/query.expander.ws.server-2.0.4-20160418.153025-76.war  
ENV WAR_SHA1 2acadf67149d2e2145e6aaf03821e8cd1c7c6176  
  
  
ENV LOADER_URL
https://github.com/openphacts/IdentityMappingService/releases/download/2.0.4/loader-2.0.4-onejar.jar  
#ENV LOADER_URL
http://repository.mygrid.org.uk/artifactory/ops/uk/ac/manchester/cs/openphacts/ims/loader/2.0.3-SNAPSHOT/loader-2.0.3-20160418.152936-48-onejar.jar  
ENV LOADER_SHA1 24c97b42c507692f0f03e24bfdfd1f4e35616628  
  
# clean  
RUN rm -rf webapps/*  
  
# download  
ADD $WAR_URL webapps/QueryExpander.war  
ADD $LOADER_URL /usr/local/lib/ims-loader.jar  
  
# checksums  
RUN echo $WAR_SHA1 webapps/QueryExpander.war >> /tmp/checksums  
RUN echo $LOADER_SHA1 /usr/local/lib/ims-loader.jar >> /tmp/checksums  
RUN sha1sum -c /tmp/checksums  
  
# permissions  
RUN chmod 755 webapps/QueryExpander.war  
  
# scripts and properties  
ADD loader /usr/local/bin/loader  
RUN chmod 755 /usr/local/bin/loader  
RUN mkdir -p /usr/local/tomcat/conf/BridgeDb  
ADD local.properties /usr/local/tomcat/conf/BridgeDb/  
  

