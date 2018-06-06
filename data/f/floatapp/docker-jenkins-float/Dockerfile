# docker build -t floatapp/docker-jenkins-float:{jenkins-ver} .  
FROM jenkins/jenkins:2.107.3  
  
# install via apt  
USER root  
RUN apt-get update && apt-get install -y rsync  
  
# if jenkins user needs sudo, uncomment below:  
# RUN apt-get install -y sudo && echo "jenkins ALL=(ALL) NOPASSWD: ALL" >>
/etc/sudoers  
RUN apt-get clean  
  
# drop back to the regular jenkins user - good practice  
USER jenkins  

