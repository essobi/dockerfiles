  
FROM tomcat  
ENV URL
http://repository.mygrid.org.uk/artifactory/ops/nl/nbic/conceptwiki/web/web-
ws/0.9.4-SNAPSHOT/web-ws-0.9.4-20150820.090514-1.war  
RUN rm -rf webapps/*  
WORKDIR temp  
RUN curl $URL.sha1 > ROOT.war.sha1  
RUN echo " ROOT.war" >> ROOT.war.sha1  
RUN curl -L $URL > ROOT.war && sha1sum -c ROOT.war.sha1  
WORKDIR ..  
RUN mv temp/ROOT.war webapps/ROOT.war  
  

