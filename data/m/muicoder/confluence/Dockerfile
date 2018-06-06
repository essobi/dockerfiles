FROM muicoder/glibc:server-jre  
  
ENV CONF_VERSION=6.9.0  
WORKDIR /opt  
  
RUN BASEURL="https://downloads.atlassian.com/software/confluence/downloads" &&
\  
wget -q ${BASEURL}/atlassian-confluence-${CONF_VERSION}.tar.gz && \  
tar -xf atlassian-confluence-${CONF_VERSION}.tar.gz && \  
mv atlassian-confluence-${CONF_VERSION} atlassian && \  
\  
mv atlassian/confluence/WEB-INF/classes/confluence-init.properties . && \  
echo "confluence.home=/var/atlassian/confluence" > atlassian/confluence/WEB-
INF/classes/confluence-init.properties && \  
\  
rm -rf /opt/atlassian-*  
  
EXPOSE 8090 8091  
VOLUME ["/opt/atlassian/logs", "/var/atlassian/confluence"]  
  
CMD ["/opt/atlassian/bin/start-confluence.sh", "-fg"]  

