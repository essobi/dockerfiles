# Basics  
#  
FROM openjdk:8  
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64  
  
RUN export DEBIAN_FRONTEND=noninteractive && apt-get update && apt-get install
xmlstarlet -y  
  
# Setup volume handling  
RUN /usr/sbin/groupadd atlassian  
ADD own-volume.sh /usr/local/bin/own-volume  
RUN echo "%atlassian ALL=NOPASSWD: /usr/local/bin/own-volume" >> /etc/sudoers  
RUN mkdir -p /opt/atlassian-home  
  
# Add common script functions  
ADD common.bash /usr/local/share/atlassian/common.bash  
RUN chgrp atlassian /usr/local/share/atlassian/common.bash  
RUN chmod g+w /usr/local/share/atlassian/common.bash  
  
# Install Jira  
ENV JIRA_VERSION 7.3.1  
ENV CONTEXT_PATH ROOT  
ADD launch.bash /launch  
ADD provision.bash /provision  
  
RUN ["/provision"]  
  
# Launching Jira  
WORKDIR /opt/jira  
VOLUME ["/opt/atlassian-home"]  
EXPOSE 8080  
USER jira  
CMD ["/launch"]  

