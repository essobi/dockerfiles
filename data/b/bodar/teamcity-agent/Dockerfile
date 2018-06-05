# docker run --restart=on-failure:10 -e
TEAMCITY_SERVER_URL=http://teamcity:8111 -dt -p 9090:9090 bodar/teamcity-agent  
FROM bodar/teamcity-base  
  
ENV TEAMCITY_AGENT_DATA /data/BuildAgent  
VOLUME [$TEAMCITY_AGENT_DATA]  
  
EXPOSE 9090  
COPY buildAgent.properties.template run /opt/BuildAgent/  
  
CMD bash /opt/BuildAgent/run  

