# Basics  
#  
FROM wenzizone/atlassian-base  
MAINTAINER wenzizone <wenzizone@126.com>  
  
# Install Jira  
ENV JIRA_VERSION 7.0.5  
ENV CONTEXT_PATH jira  
#ENV DATABASE_URL mysql://jirauser:jIraUser@mysql:3306/jiradb  
#ENV DB_TYPE mysql  
ADD launch.bash /launch  
ADD provision.bash /provision  
  
RUN ["/provision"]  
  
# Launching Jira  
WORKDIR /opt/jira  
VOLUME ["/opt/atlassian-home"]  
EXPOSE 8080  
USER jira  
CMD ["/launch"]  

