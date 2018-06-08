# This Dockerfile is used to build an image containing basic stuff to be used
as a Jenkins slave build node. based on evarga/jenkins-slave  
# This Dockerfile is based on stevenhorsman-ibm's.  
FROM evarga/jenkins-slave  
  
ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64  
  
# Install curl, maven,  
RUN apt-get update && apt-get install -y \  
curl \  
git \  
openjdk-8-jdk \  
sshpass \  
zip \  
gzip \  
tar \  
rsync \  
&& rm -rf /var/lib/apt/lists/*  
  
# Add node version 8 which should bring in npm, add maven and required ssl
certificates to contact maven central  
RUN curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -  
RUN apt-get install -y nodejs build-essential maven ca-certificates-java &&
update-ca-certificates -f  
  
CMD ["/usr/sbin/sshd", "-D"]  

