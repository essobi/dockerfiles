FROM openjdk:8-alpine  
  
MAINTAINER Fabrizio Lungo <docker@flungo.me>  
  
# Matches home of official Jenkins image.  
ENV JENKINS_HOME=/var/jenkins_home  
  
RUN apk add --update wget ca-certificates  
  
RUN adduser -D -h $JENKINS_HOME jenkins  
  
USER jenkins  
  
WORKDIR $JENKINS_HOME  
COPY init.sh $JENKINS_HOME/bin/  
ENTRYPOINT ["./bin/init.sh"]  

