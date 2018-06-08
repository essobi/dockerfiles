  
FROM alpine  
LABEL Name=wirsens-network-restarter Version=0.0.1  
RUN apk update && apk add bash sed net-tools  
ADD network-restarter.sh /network-restarter.sh  
  
CMD ["bin/bash", "network-restarter.sh"]  

