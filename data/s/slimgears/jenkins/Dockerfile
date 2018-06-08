FROM jenkins  
  
USER root  
RUN apt-get update && apt-get install -y lib32stdc++6 lib32z1 && rm -rf
/var/lib/apt/lists/*  
USER jenkins  
  
COPY plugins.txt "$JENKINS_HOME/plugins.txt"  
RUN /usr/local/bin/plugins.sh "$JENKINS_HOME/plugins.txt"  
  
ENV GRADLE_USER_HOME $JENKINS_HOME/.gradle  

