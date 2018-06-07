FROM jenkins/jenkins:lts  
  
LABEL maintainer="jesus.peralesmr@uanl.edu.mx"  
  
USER root  
RUN apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -y sudo libltdl-dev \  
&& rm -rf /var/lib/apt/lists/*  
RUN echo "jenkins ALL=NOPASSWD: ALL" >> /etc/sudoers  
  
USER jenkins  

