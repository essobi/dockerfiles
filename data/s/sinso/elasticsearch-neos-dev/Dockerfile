FROM sinso/elasticsearch-neos:latest  
MAINTAINER Aslam Idrisov <aslambek.idrisov1@swisscom.com>  
  
  
# Install Debugging plugins  
  
RUN /usr/share/elasticsearch/bin/plugin -i elastic/elasticsearch-migration \  
&& /usr/share/elasticsearch/bin/plugin -i mobz/elasticsearch-head \  
&& /usr/share/elasticsearch/bin/plugin -i lukas-vlcek/bigdesk \  
&& /usr/share/elasticsearch/bin/plugin -i lmenezes/elasticsearch-kopf \  
&& /usr/share/elasticsearch/bin/plugin -i royrusso/elasticsearch-HQ  
  

