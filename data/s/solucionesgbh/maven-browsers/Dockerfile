FROM circleci/openjdk:8-jdk-browsers  
  
MAINTAINER Ignacio Canó <ignacio@helloalfred.com>  
  
RUN sudo apt-get purge -y google-chrome-stable  
  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo
apt-key add \- && \  
sudo sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google.list' && \  
sudo apt-get update && sudo apt-get install -y google-chrome-beta && google-
chrome --version  

