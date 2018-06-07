#  
# ElasticSearch Dockerfile with Plugins used by Sutoiku:  
# http-auth, head, bigdesk and the native-script-updater.  
# Plugins in a mounted data volume are not appropriate for us.  
#  
# The auth plugin is disabled by default  
# To take advantage of the auth plugin:  
# docker run -e "ES_BASIC_AUTH_ENABLED=true" \  
# -e "ES_BASIC_AUTH_ENABLED=joe" \  
# -e "ES_BASIC_AUTH_PASSWORD=secret"  
#  
# Example of mounting the data volume on the host coreos directory  
# itself mounted on my macos machine  
# -v /home/core/share/data:/data  
#  
# https://github.com/hmalphettes/elasticsearch-stoic  
#  
  
# Pull base image with a bare elasticsearch installed  
FROM hmalphettes/elasticsearch  
  
# Use our own elasticsearch.yml config  
ADD config/elasticsearch.yml /elasticsearch/config/elasticsearch.yml  
  
# Install Sutoiku plugins  
RUN \  
export ES_BASIC_AUTH_ENABLED=false && export ES_BASIC_AUTH_USER=no && export
ES_BASIC_AUTH_PASSWORD=auth && \  
cd /elasticsearch && \  
bin/plugin -i native-script-updater --url
https://github.com/sutoiku/elasticsearch-native-script-
updater/releases/download/1.0.0/elasticsearch-native-script-updater-1.0.0.zip
&& \  
bin/plugin -i mobz/elasticsearch-head && \  
# Hawk support not quite ready:  
# bin/plugin -i http-auth-plugin --url
https://github.com/hmalphettes/elasticsearch-http-
basic/releases/download/1.3.2/elasticsearch-http-basic-1.3.2.zip && \  
bin/plugin -i http-auth-plugin --url https://github.com/Asquera/elasticsearch-
http-basic/releases/download/1.3.2/elasticsearch-http-basic-1.3.2.jar && \  
bin/plugin -i lukas-vlcek/bigdesk  
  
ENV ES_BASIC_AUTH_ENABLED false  
ENV ES_BASIC_AUTH_USER no  
ENV ES_BASIC_AUTH_PASSWORD auth  

