FROM droid42/dind-java8  
  
RUN apt-get update  
RUN apt-get install -y git  
RUN apt-get install unzip  
  
RUN wget "http://maven.jenkins-
ci.org/content/repositories/releases/org/jenkins-ci/plugins/swarm-
client/1.16/swarm-client-1.16-jar-with-dependencies.jar"  
  
#Server periodically down, so we copy this in here!  
#RUN \  
# wget "http://opentox.ntua.gr/files/InstallCert.zip" && \  
# unzip InstallCert.zip  
ADD ./InstallCert.zip /data/  
RUN unzip InstallCert.zip  
  
RUN rm -rf /var/lib/apt/lists/*  
  
WORKDIR /data  
  
ADD ./cmd.sh /data/  
  
CMD ["./cmd.sh"]  

