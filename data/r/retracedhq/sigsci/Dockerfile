# Dockerfile for running Sigsci in Docker  
# Adapted from
https://github.com/signalsciences/SigSciDockerExample/blob/master/Dockerfile  
FROM ubuntu:xenial  
  
COPY sigsci-release.list /etc/apt/sources.list.d/sigsci-release.list  
RUN apt-get update; \  
apt-get install -y apt-transport-https curl; \  
curl -slL https://apt.signalsciences.net/gpg.key | apt-key add -; \  
apt-get update; \  
apt-get install -y sigsci-agent=2.1.2~xenial; \  
apt-get clean  
  
CMD ["/usr/sbin/sigsci-agent"]  

