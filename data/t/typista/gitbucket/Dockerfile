FROM ubuntu:14.04  
RUN apt-get update && \  
apt-get install -q -y wget openjdk-7-jre-headless && \  
apt-get clean && \  
ln -s /gitbucket /root/.gitbucket && \  
wget
https://github.com/takezoe/gitbucket/releases/download/2.2.1/gitbucket.war -O
/opt/gitbucket.war  
#VOLUME /gitbucket  
#EXPOSE 8080  
CMD ["java", "-jar", "/opt/gitbucket.war"]  
  

