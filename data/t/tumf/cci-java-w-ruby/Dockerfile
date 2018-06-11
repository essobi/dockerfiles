FROM circleci/openjdk:8-jdk-browsers  
MAINTAINER tumf <y.takahara@gmail.com>  
  
RUN sudo apt-get update && \  
sudo apt-get install ruby &&\  
sudo rm -rf /var/lib/apt/lists/*  
  
RUN sudo gem install bundler  
  
# GHR  
ADD
https://github.com/tcnksm/ghr/releases/download/v0.5.4/ghr_v0.5.4_linux_amd64.zip
/tmp  
RUN sudo unzip /tmp/ghr_v0.5.4_linux_amd64.zip -d /usr/local/bin && sudo rm
/tmp/ghr_v0.5.4_linux_amd64.zip  

