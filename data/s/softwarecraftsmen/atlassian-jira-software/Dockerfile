FROM buildpack-deps:trusty  
MAINTAINER Software Craftsmen GmbH & Co KG <office@software-craftsmen.at>  
  
ENV JIRA_VERSION=7.1.0-jira-7.1.0-x64  
  
RUN wget --no-verbose
https://www.atlassian.com/software/jira/downloads/binary/atlassian-jira-
software-$JIRA_VERSION.bin -O atlassian-jira-$JIRA_VERSION.bin && \  
chmod a+x atlassian-jira-$JIRA_VERSION.bin  
  
# Run the installer  
# The response file is produced by an attended installation at
/opt/atlassian/jira/.install4j/response.varfile  
ADD response.varfile response.varfile  
# Run unattended installation with input from response.varfile  
RUN ./atlassian-jira-$JIRA_VERSION.bin -q -varfile response.varfile && \  
rm atlassian-jira-$JIRA_VERSION.bin  
  
EXPOSE 8080  
# Adjust this path if the installation location has been modified by the
response.varfile  
CMD ["./opt/atlassian/jira/bin/start-jira.sh", "-fg"]  

