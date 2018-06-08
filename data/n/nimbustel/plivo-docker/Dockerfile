FROM nimbustel/plivo-docker:base  
MAINTAINER Alex Recarey "alex@nimbustel.com"  
ADD conf/default.conf /usr/local/plivo/etc/plivo/default.conf  
  
ADD conf/cache.conf /usr/local/plivo/etc/plivo/cache/cache.conf  
  
ADD conf/start-plivo.sh /start-plivo.sh  
  
# Plivo Outbound server. (Freeswitch -> Plivo)  
EXPOSE 8084  
# Plivo REST server. (App -> Plivo)  
EXPOSE 8088  
# Plivo Cache server. (Plivo -> Plivo Cache). No expose required?  
# EXPOSE 8089  
CMD /bin/bash /start-plivo.sh && tail -F /usr/local/plivo/tmp/plivo-
outbound.log  

