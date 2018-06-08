FROM schwierd/atlassian-base:latest  
MAINTAINER Daniel Schwierzeck <daniel.schwierzeck@gmail.com>  
  
ENV JIRA_VERSION 7.1.0  
ENV JIRA_ROOT /opt/jira  
  
# Create system user  
RUN groupadd -r jira -g 666 && \  
useradd -r -g jira -u 666 -m -d $JIRA_ROOT -s /sbin/nologin jira && \  
mkdir -p $JIRA_ROOT/install $JIRA_ROOT/data  
  
# Install JIRA  
RUN curl -sSL
http://www.atlassian.com/software/jira/downloads/binary/atlassian-jira-
software-$JIRA_VERSION-jira-$JIRA_VERSION.tar.gz \  
| tar -xz --strip=1 -C $JIRA_ROOT/install/  
  
# Configure JIRA home directory  
RUN echo "jira.home = $JIRA_ROOT/data" > $JIRA_ROOT/install/atlassian-
jira/WEB-INF/classes/jira-application.properties  
  
# Enable APR based Apache Tomcat Native library and increase JVM memory  
RUN sed -i \  
-e 's,JVM_SUPPORT_RECOMMENDED_ARGS="",JVM_SUPPORT_RECOMMENDED_ARGS="-Djava.library.path=/usr/lib/x86_64-linux-gnu",g' \  
-e 's,JVM_MAXIMUM_MEMORY=.*,JVM_MAXIMUM_MEMORY="2048m",g' \  
$JIRA_ROOT/install/bin/setenv.sh  
  
# Fix permissions  
RUN chown -R jira:jira $JIRA_ROOT  
  
EXPOSE 8080  
VOLUME $JIRA_ROOT/data  
  
COPY docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
WORKDIR $JIRA_ROOT/install/bin  
USER jira  
CMD [ "run" ]  

