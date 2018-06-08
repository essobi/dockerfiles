# DOCKER-VERSION 1.0.1  
FROM sergeimuller/aem-base  
MAINTAINER sergeimuller  
  
#Copies required build media  
ONBUILD ADD cq-publish-4503.jar /aem/publish/cq-publish-4503.jar  
ONBUILD ADD license.properties /aem/publish/license.properties  
  
# Extracts AEM  
ONBUILD WORKDIR /aem/publish  
ONBUILD RUN java -XX:MaxPermSize=256m -Xmx1024M -jar cq-publish-4503.jar
-unpack -r publish -p 4503  
  
# Add customised log file, to print the logging to standard out.  
ONBUILD ADD https://raw.githubusercontent.com/sergeimuller/aem-
author/master/org.apache.sling.commons.log.LogManager.config /aem/publish/crx-
quickstart/install  
  
# Installs AEM  
ONBUILD RUN python /aem/publish/aemInstaller.py -i cq-publish-4503.jar -r
publisher -p 4503  
  
ONBUILD WORKDIR /aem/publish/crx-quickstart/bin  
#Replaces the port within the quickstart file with the standard publisher port  
ONBUILD RUN cp quickstart quickstart.original  
ONBUILD RUN cat quickstart.original | sed "s|4502|4503|g" > quickstart  
  
EXPOSE 4503 8000  
ENTRYPOINT ["/aem/publish/crx-quickstart/bin/quickstart"]  

