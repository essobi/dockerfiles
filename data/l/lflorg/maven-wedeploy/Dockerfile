FROM maven:3.5-jdk-8-slim  
  
RUN apt update && \  
apt install gettext -y && \  
apt install build-essential -y && \  
apt install git -y  
  
RUN curl https://cdn.wedeploy.com/cli/latest/wedeploy.sh -sL | bash  

