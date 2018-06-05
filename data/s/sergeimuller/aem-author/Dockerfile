# DOCKER-VERSION 1.0.1  
FROM sergeimuller/aem-base  
MAINTAINER sergeimuller  
  
#Copies required build media  
ONBUILD ADD cq-author-4502.jar /aem/author/cq-author-4502.jar  
ONBUILD ADD license.properties /aem/author/license.properties  
ONBUILD ADD https://raw.githubusercontent.com/sergeimuller/aem-
author/master/postInstallHook.py /aem/postInstallHook.py  
  
# Extracts AEM  
ONBUILD WORKDIR /aem/author  
ONBUILD RUN java -XX:MaxPermSize=256m -Xmx1024M -jar cq-author-4502.jar
-unpack -r nosamplecontent  
  
# Add customised log file, to print the logging to standard out.  
ONBUILD ADD https://raw.githubusercontent.com/sergeimuller/aem-
author/master/org.apache.sling.commons.log.LogManager.config /aem/author/crx-
quickstart/install  
  
# Installs AEM  
ONBUILD RUN ["python","/aem/author/aemInstaller.py","-i","cq-
author-4502.jar","-r","author","-p","4502"]  
  
EXPOSE 4502 8000  
ENTRYPOINT ["/aem/author/crx-quickstart/bin/quickstart"]  

