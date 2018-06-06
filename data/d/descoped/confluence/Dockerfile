FROM descoped/atlassian-base  
MAINTAINER Ove Ranheim <oranheim@gmail.com>  
  
# Install Confluence  
ENV CONFLUENCE_VERSION 6.0.7  
ENV CONFLUENCE_INST /opt/confluence  
ENV CONFLUENCE_HOME /var/atlassian-home  
  
ENV UID confluence  
ENV GID atlassian  
  
ADD configure.bash /configure  
RUN chmod +x /configure  
  
RUN curl -Lk
http://www.atlassian.com/software/confluence/downloads/binary/atlassian-
confluence-$CONFLUENCE_VERSION.tar.gz -o /root/confluence.tar.gz \  
&& useradd -r --create-home --home-dir $CONFLUENCE_INST \--groups $GID
\--shell /bin/bash $UID \  
&& tar zxf /root/confluence.tar.gz --strip=1 -C $CONFLUENCE_INST \  
&& rm /root/confluence.tar.gz \  
&& echo "confluence.home=$CONFLUENCE_HOME" > $CONFLUENCE_INST/confluence/WEB-
INF/classes/confluence-init.properties \  
&& mv $CONFLUENCE_INST/conf/server.xml $CONFLUENCE_INST/conf/server-backup.xml  
  
# Launching Confluence  
WORKDIR $CONFLUENCE_INST  
VOLUME ["$CONFLUENCE_HOME"]  
  
COPY entrypoint.bash /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
EXPOSE 8090  
EXPOSE 8091  
CMD ["bin/start-confluence.sh", "-fg"]  

