# Centos ha-bridge  
# Version 5.2.0  
FROM openjdk:8-alpine  
MAINTAINER Tobias Sgoff  
  
RUN apk add --no-cache curl  
RUN mkdir /bridge/ && cd /bridge && \  
UR="https://github.com/bwssytems/ha-bridge" ; \  
LV=`curl -s $UR/releases/latest |cut -d'v' -f2|cut -d'"' -f1` ; \  
wget $UR/releases/download/v${LV}/ha-bridge-${LV}.jar -Oha-bridge.jar  
RUN echo '#!/bin/ash' > /bridge/init.sh ; \  
echo java -jar \$PORT \$KEY \$CONFIG \$IP \$GARDEN /bridge/ha-bridge.jar >>
/bridge/init.sh  
RUN chmod +x /bridge/init.sh  
  
WORKDIR /bridge  
CMD ["/bridge/init.sh"]  

