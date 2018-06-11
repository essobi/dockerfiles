FROM utestfactory/doc  
  
MAINTAINER The U-TEST Team  
  
# following env variable should be define when running this image  
ENV JENKINS_PUBLIC_KEY="define" \  
GITLAB_SSH_PRIVATE_KEY="define"  
RUN yum install -y openssh-server \  
git \  
java-1.7.0-openjdk-devel  
  
RUN useradd -ms /bin/bash jenkins  
# Set password for the jenkins user (you may want to alter this).  
RUN echo -e "jenkins:jenkins\nroot:gc" | chpasswd  
  
# Standard SSH port  
EXPOSE 22  
# run.sh is in _/common_ directory  
COPY run.sh /run.sh  
  
ENTRYPOINT ["/run.sh"]  

