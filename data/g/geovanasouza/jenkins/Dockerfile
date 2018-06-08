FROM jenkins:2.46.1  
ENV PATH $PATH:$JENKINS_HOME/workspace/scripts-ci  
  
USER root  
  
RUN apt-get update && apt-get install -y apt-transport-https ca-certificates
curl software-properties-common  
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -  
RUN add-apt-repository "deb [arch=amd64]
https://download.docker.com/linux/debian \  
$(lsb_release -cs) \  
stable"  
RUN apt-get update && apt-get install -y docker-ce jq gettext xmlstarlet
dos2unix

