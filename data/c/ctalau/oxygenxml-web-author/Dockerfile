FROM ctalau/web-author-platform  
  
USER root  
RUN cd /webauthor/webapps/ \  
&& curl -O https://oxygenxml.com/InstData/WebAuthor/war/oxygenxml-web-
author.war \  
&& unzip oxygenxml-web-author.war -d oxygenxml-web-author/ \  
&& rm -rf oxygenxml-web-author.war \  
&& chown -R oxygen.oxygen oxygenxml-web-author/  
  
USER oxygen  

