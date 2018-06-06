  
# Build : sudo docker build -t splitified:jenkins-meteor-cypress  
# Run : sudo docker run -p 8080:8080 -p 50000:50000 -v
jenkins_home:/var/jenkins_home -v /var/run/docker.sock:/var/run/docker.sock -v
$(which docker):/bin/docker --net="host" IMAGE_ID_HERE  
FROM jenkins/jenkins:2.121-slim  
  
LABEL maintener "gallegoj@gmail.com"  
  
USER root  
  
# Install NodeJS (to get NPM)  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - \  
&& apt-get update && apt-get install -y curl nodejs  
  
# Set the locale (needed by Mongo)  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y locales \  
&& sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen \  
&& dpkg-reconfigure --frontend=noninteractive locales \  
&& update-locale LANG=en_US.UTF-8  
ENV LANG en_US.UTF-8  
# Allow jenkins user to run sudo commands  
RUN apt-get install -y sudo  
RUN usermod -a -G sudo jenkins  
RUN echo "jenkins ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers  
  
# Fix for allowing npm install -g to work  
RUN mkdir -p /home/node/.npm-global \  
&& chown -R jenkins /home/node/.npm-global  
ENV NPM_CONFIG_PREFIX=/home/node/.npm-global  
  
# Install Meteor  
RUN curl https://install.meteor.com/ | sh  
  
# Dependencies for Cypress & Meteor  
RUN apt-get install -y xvfb libgtk2.0-0 libxss1 libgconf-2-4 g++ build-
essential libnotify-dev libnss3 libasound2  
  
# Dependencies for Docker and Jenkins build tasks scripts  
RUN apt-get install -y libltdl-dev netcat  
  
# Some cleaning  
RUN apt-get clean && rm -Rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# drop back to the regular jenkins user - good practice  
USER jenkins  
  
# Install Cypress for acceptance tests  
RUN npm install cypress -g  

