FROM openjdk:8-jre  
  
RUN curl -sL https://dl.bintray.com/sbt/native-
packages/sbt/0.13.12/sbt-0.13.12.zip > /tmp/sbt.zip && \  
unzip /tmp/sbt.zip -d /tmp && \  
cp -r /tmp/sbt/* /usr/local/ && \  
sbt about  
  
RUN apt-get update -y --fix-missing && \  
apt-get install -y \  
openssh-client \  
git  
  
RUN mkdir -p ~/.ssh && \  
echo 'Host *\n\  
StrictHostKeyChecking no\n\  
UserKnownHostsFile=/dev/null' >> ~/.ssh/config  
  
WORKDIR /usr/src/app  
  
CMD sbt  

