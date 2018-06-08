FROM razzek/lab.java:8  
COPY jenkins.xml /home/service/.jenkins/config.xml  
COPY applab.xml /home/service/.jenkins/jobs/applab/config.xml  
COPY hudson.tasks.Maven.xml /home/service/.jenkins/  
  
RUN curl -fSLs http://mirrors.jenkins-ci.org/war-stable/1.609.2/jenkins.war -o
/opt/jenkins.war \  
&& echo '59215da16f9f8a781d185dde683c05fcf11450ef /opt/jenkins.war' | sha1sum
-c - \  
&& mkdir /home/service/.jenkins/war \  
&& unzip -d /home/service/.jenkins/war /opt/jenkins.war -x \\*.class \  
&& chown -R service:service /home/service/.jenkins  
  
USER service  
WORKDIR /home/service  
EXPOSE 8080 50000  
CMD [ "java", "-jar", "/opt/jenkins.war" ]  

