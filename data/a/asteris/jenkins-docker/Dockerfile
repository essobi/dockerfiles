FROM jenkins:latest  
  
ENV DEBIAN_FRONTEND noninteractive  
  
USER root  
RUN apt-get update && apt-get install -qqy apparmor iptables ca-certificates  
ADD https://get.docker.io/builds/Linux/x86_64/docker-latest
/usr/local/bin/docker  
RUN chmod +x /usr/local/bin/docker  
  
ADD https://github.com/docker/fig/releases/download/1.0.1/fig-Linux-x86_64
/usr/local/bin/fig  
RUN chmod +x /usr/local/bin/fig  
  
ADD https://raw.githubusercontent.com/jpetazzo/dind/master/wrapdocker
/usr/local/bin/wrapdocker  
RUN chmod +x /usr/local/bin/wrapdocker  
  
COPY plugins.txt /plugins.txt  
  
RUN /usr/local/bin/plugins.sh /plugins.txt  
  
VOLUME /var/lib/docker  
  
CMD wrapdocker && /usr/local/bin/jenkins.sh  

