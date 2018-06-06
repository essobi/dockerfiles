# Jenkins latest image  
FROM jenkins:latest  
  
MAINTAINER Andre Nascimento <andreluiznsilva@gmail.com>  
  
ENV JENKINS_PLUGINS="job-dsl parameterized-trigger envinject copyartifact
delivery-pipeline-plugin build-pipeline-plugin nested-view"  
  
USER root  
  
EXPOSE 8080 50000  
  
COPY entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]

