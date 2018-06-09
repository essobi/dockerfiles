#Create a jenkins image with android from one with nodejs npm and meteor
available  
FROM ocasta/android-jenkins:latest  
MAINTAINER Jack Kavanagh (http://jackkav.github.io)  
  
#install meteor  
RUN curl https://install.meteor.com/ | sh && export PATH=$PATH:$HOME/.meteor  
  
#install android platform  
RUN echo y | android update sdk --no-ui --all --filter platform-tools,build-
tools-23.0.2,build-tools-23.0.3,android-23  
  
#install node 4  
RUN curl -sL https://deb.nodesource.com/setup_4.x | bash && apt-get install -y
nodejs  

