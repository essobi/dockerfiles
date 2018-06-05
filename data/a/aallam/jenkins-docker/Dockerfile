FROM aallam/jenkins  
  
USER root  
  
RUN apt-get update \  
&& apt-get -y install unzip sudo mysql-client libltdl7 \  
&& rm -rf /var/lib/apt/lists/*  
RUN echo "jenkins ALL=NOPASSWD: ALL" >> /etc/sudoers  
  
USER jenkins  
  
RUN /usr/local/bin/install-plugins.sh scm-api git-client git github junit
greenballs jclouds-jenkins token-macro durable-task docker-plugin:0.16.1  

