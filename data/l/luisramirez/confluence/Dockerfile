FROM debian:8.5  
COPY ./confluence /opt/atlassian/confluence  
  
RUN mkdir -p /var/atlassian/application-data/confluence && \  
groupadd confluence && \  
useradd -g confluence confluence && \  
chown -R confluence:confluence /opt/atlassian/confluence
/var/atlassian/application-data/confluence  
  
VOLUME ["/opt/atlassian/confluence", "/var/atlassian/application-
data/confluence"]  
  
EXPOSE 8090 8000  
USER confluence  
  
CMD ./opt/atlassian/confluence/bin/start-confluence.sh -fg  

