FROM java:8  
MAINTAINER Ahmed Soliman <me@ahmedsoliman.com>  
  
  
WORKDIR /data  
  
RUN \  
apt-get update && \  
apt-get install -y git  
  
RUN wget "http://maven.jenkins-
ci.org/content/repositories/releases/org/jenkins-ci/plugins/swarm-
client/1.22/swarm-client-1.22-jar-with-dependencies.jar"  
  
RUN \  
wget "http://opentox.ntua.gr/files/InstallCert.zip" && \  
unzip InstallCert.zip  
  
RUN wget -qO- https://get.docker.com/ | sh  
  
RUN rm -rf /var/lib/apt/lists/*  
  
ADD ./cmd.sh /data/  
  
CMD ["./cmd.sh"]  

