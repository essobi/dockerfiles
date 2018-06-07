FROM jenkins:1.651.3  
COPY install-plugins.sh /tmp/install-plugins.sh  
USER root  
RUN chmod +x /tmp/install-plugins.sh  
RUN /tmp/install-plugins.sh deployit-plugin xlrelease-plugin maven-plugin git
job-dsl chucknorris greenballs envinject gradle slack github view-job-filters
copyartifact cloudbees-folder sonar workflow-aggregator  
COPY plugins.txt /tmp/plugins.txt  
RUN /usr/local/bin/plugins.sh /tmp/plugins.txt  
#233 is the docker gid under CoreOS, has to be added in the container so
Jenkins can control the docker socket  
RUN groupadd -g 233 docker && adduser jenkins docker  
#Used for access on docker-machine  
RUN adduser jenkins users  
  
#To generate:  
#1) ssh-keyscan -t dsa github.com > githubKey  
#2) ssh-keygen -lf githubKey  
#3) Compare fingerprints against https://help.github.com/articles/what-are-
github-s-ssh-key-fingerprints/  
#4) If they match the content of the githubKey file is what you should echo
into known_hosts  
RUN echo 'github.com ssh-rsa
AAAAB3NzaC1yc2EAAAABIwAAAQEAq2A7hRGmdnm9tUDbO9IDSwBK6TbQa+PXYPCPy6rbTrTtw7PHkccKrpp0yVhp5HdEIcKr6pLlVDBfOLX9QUsyCOV0wzfjIJNlGEYsdlLJizHhbn2mUjvSAHQqZETYP81eFzLQNnPHt4EVVUh7VfDESU84KezmD5QlWpXLmvU31/yMf+Se8xhHTvKSCZIFImWwoG6mbUoWf9nzpIoaSjB+weqqUUmpaaasXVal72J+UX2B+2RPW3RcT0eOzQgqlJL3RKrTJvdsjE3JEAvGq3lGHSZXy28G3skua2SmVi/w4yCE6gbODqnTWlg7+wC604ydGXA8VJiS5ap43JXiUFFAaQ=='
>> /etc/ssh/ssh_known_hosts  
  
ADD jenkins_start.sh /usr/local/bin/jenkins_start.sh  
RUN chmod +x /usr/local/bin/jenkins_start.sh  
  
ADD *.xml /tmp/  
  
RUN apt-get update && apt-get install -y \  
jq \  
make \  
&& rm -rf /var/lib/apt/lists/*  
  
USER jenkins  
  
ENTRYPOINT ["/usr/local/bin/jenkins_start.sh"]  

