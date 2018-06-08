FROM jenkins/jenkins:lts  
  
USER root  
ENV DEBIAN_FRONTEND noninteractive  
ENV INITRD No  
  
COPY executors.groovy /usr/share/jenkins/ref/init.groovy.d/executors.groovy  
RUN echo 2.0 > /usr/share/jenkins/ref/jenkins.install.UpgradeWizard.state  
  
COPY entrypoint.sh /entrypoint.sh  
COPY .gitconfig /root/.gitconfig  
  
COPY plugins.txt /usr/share/jenkins/ref/plugins.txt  
RUN /usr/local/bin/install-plugins.sh < /usr/share/jenkins/ref/plugins.txt  
  
RUN apt-get update && apt-get install -qy python-pip groff-base  
RUN pip install awscli  
  
CMD /bin/bash /entrypoint.sh  

