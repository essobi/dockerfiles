FROM gitlab/gitlab-runner:latest  
MAINTAINER andras.toth@chilisoft.org  
  
ENV GITLAB_CI_URL=yourgitlabci.com  
ENV GITLAB_CI_TOKEN=runners  
ENV GITLAB_CI_NAME=java-maven-sonar-1  
ENV GITLAB_CI_EXECUTOR=shell  
ENV SONAR_HOST_URL=myserver:9000  
ENV SONAR_JDBC_URL=  
ENV SONAR_JDBC_USER=  
ENV SONAR_JDBC_PWD=  
  
# Install Java, maven, sonar.  
RUN \  
apt-get install -q -y software-properties-common && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections && \  
apt-get install -q -y oracle-java8-installer && \  
apt-get install -q -y wget unzip  
  
RUN \  
wget http://repo1.maven.org/maven2/org/codehaus/sonar/runner/sonar-runner-
dist/2.4/sonar-runner-dist-2.4.zip && \  
unzip sonar-runner-dist-2.4.zip && \  
mv sonar-runner-2.4 /opt/sonar-runner  
  
COPY settings.xml /home/gitlab-runner/.m2/settings.xml  
  
# Install maven and git.  
RUN apt-get install -q -y maven git  
RUN apt-get clean  
  
COPY entrypoint.sh /  
RUN chmod +x /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]

