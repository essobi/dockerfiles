FROM wyntau/atlassian-bamboo-agent-base:6.5.0  
  
RUN apk add \--no-cache nodejs shadow \  
&& mkdir -p /home/${RUN_USER} \  
&& chown ${RUN_USER}:${RUN_GROUP} /home/${RUN_USER} \  
&& usermod -d /home/${RUN_USER} ${RUN_USER}  

