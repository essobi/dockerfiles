FROM java:8  
RUN mkdir /home/local/  
ADD http://repo.jenkins-ci.org/releases/org/jenkins-ci/plugins/swarm-
client/2.0/swarm-client-2.0-jar-with-dependencies.jar /home/local/  
ADD init.sh /home/local/  
RUN chmod +x /home/local/init.sh  
  
ENTRYPOINT ["/home/local/init.sh"]  

