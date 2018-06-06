FROM cocoon/droyd  
MAINTAINER cocoon  
  
  
  
# install more python lib for droydjenkins  
ADD requirements.txt /tmp/  
RUN pip install -r /tmp/requirements.txt  
  
RUN apt-get update && apt-get clean  
RUN apt-get install -q -y git  
RUN apt-get install -q -y openjdk-7-jre-headless && apt-get clean  
ADD http://mirrors.jenkins-ci.org/war/1.578/jenkins.war /opt/jenkins.war  
RUN chmod 644 /opt/jenkins.war  
ENV JENKINS_HOME /jenkins  
  
  
# install pyjenkins  
RUN pip install PyYAML  
RUN pip install git+https://bitbucket.org/cocoon_bitbucket/pyjenkins.git  
  
# volumes: /jenkins for the state , /tests for the test sources /opt/python
for pyrun  
#VOLUME /tests  
#VOLUME /jenkins  
#VOLUME /opt/python  
# default values for volumes  
ADD sandbox/jenkins /jenkins/  
ADD sandbox/tests /tests/  
  
# expose http port  
EXPOSE 8080  
# expose ssh port: Started SSHD at port 8081  
# ssh -p 8081 localhost who-am-i  
EXPOSE 8081  
#ENTRYPOINT ["java", "-jar", "/opt/jenkins.war"]  
#CMD [""]  
CMD java -jar /opt/jenkins.war  
  

