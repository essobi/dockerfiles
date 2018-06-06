FROM jenkins/jenkins:lts  
COPY plugins.txt /usr/share/jenkins/ref/plugins.txt  
RUN /usr/local/bin/install-plugins.sh < /usr/share/jenkins/ref/plugins.txt  
  
USER root  
RUN groupadd -g 999 docker \  
&& adduser jenkins docker \  
&& apt-get update && apt-get install -y libltdl7 \  
&& rm -rf /var/lib/apt/lists/*  
  
USER jenkins  

