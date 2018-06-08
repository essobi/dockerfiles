#This docker file sets up Java, ant, and the ability to use the migration
toolkit from Salesforce.  
#Credit goes to Patrick Connelly (https://github.com/pcon) for providing the
versioned list of Migration Toolkit libraries.  
FROM webratio/ant  
MAINTAINER James Loghry <jwl007@gmail.com>  
ENV SALESFORCE_API_VERSION 38  
RUN cd /opt/ant/lib  
RUN wget https://github.com/dancinllama/ant-salesforce/raw/master/ant-
salesforce_${SALESFORCE_API_VERSION}.jar  
RUN wget https://github.com/dancinllama/DockerApexDoc/raw/master/apexdoc.jar  
  

