#FROM buildpack-deps:yakkety  
#FROM buildpack-deps:jessie-scm  
FROM ubuntu:16.04  
MAINTAINER Chris Geymo "chris.geymo@gmail.com"  
  
##############SOFTWARE BLOCK########################  
  
# Install required dependencies if needed  
####################################################  
  
RUN apt-get update && apt-get install -y apt-transport-https software-
properties-common wget sudo zip  
RUN apt-get install -y evolution evolution-ews && rm -rf /var/lib/apt/lists/*  
  
  
RUN mkdir -p /home/developer && \  
echo "developer:x:1000:1000:Developer,,,:/home/developer:/bin/bash" >>
/etc/passwd && \  
echo "developer:x:1000:" >> /etc/group && \  
echo "developer ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/developer && \  
chmod 0440 /etc/sudoers.d/developer && \  
chown developer:developer -R /home/developer && \  
chown root:root /usr/bin/sudo && chmod 4755 /usr/bin/sudo  
  
#COPY lombok.jar /opt/eclipse  
#RUN echo '-javaagent:/opt/eclipse/lombok.jar' >> /opt/eclipse/eclipse.ini  
  
USER developer  
ENV HOME /home/developer  
WORKDIR /home/developer  
CMD evolution  

