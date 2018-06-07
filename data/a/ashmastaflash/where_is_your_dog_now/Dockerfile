FROM ubuntu:16.04  
MAINTAINER toolbox@cloudpassage.com  
  
ENV
REPO_KEY=https://production.packages.cloudpassage.com/cloudpassage.packages.key  
  
  
RUN apt-get update && \  
apt-get install -y \  
apt-transport-https \  
curl  
  
COPY cloudpassage.list /etc/apt/sources.list.d/  
RUN curl $REPO_KEY | apt-key add -  
RUN apt-get update && \  
apt-get install -y \  
cphalo  
  
COPY runner.sh /app/runner.sh  
  
RUN mkdir /export  
  
CMD /app/runner.sh  

