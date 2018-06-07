FROM blacklabelops/jira:servicedesk  
  
MAINTAINER Graeme Gellatly "graemeg@roof.co.nz"  
ENV JIRA_INSTALL=/opt/jira  
  
RUN sed -i '/<\/Context>/ i \ <Resources cachingAllowed="true"
cacheMaxSize="100000" />' ${JIRA_INSTALL}/conf/context.xml  

