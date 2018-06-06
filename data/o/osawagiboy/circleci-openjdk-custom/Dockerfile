FROM circleci/openjdk:8  
MAINTAINER osawagiboy<osawagiboy@gmail.com>  
  
ENV SBT_VERSION 0.13.13  
RUN sudo apt-get update -y  
RUN sudo apt-get install -y mysql-client ruby ruby-dev python-pip  
  
RUN sudo pip install --upgrade pip  
RUN sudo pip install --upgrade awscli  
  
RUN sudo wget -q https://dl.bintray.com/sbt/debian/sbt-${SBT_VERSION}.deb  
RUN sudo dpkg -i sbt-${SBT_VERSION}.deb  
RUN sudo gem install --no-ri --no-rdoc bundler  
  
RUN sudo apt-get clean && \  
sudo rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

